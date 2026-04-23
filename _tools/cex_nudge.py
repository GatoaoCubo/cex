#!/usr/bin/env python3
# -*- coding: ascii -*-
"""
cex_nudge.py -- Curation nudge runtime (HERMES W4.5)

Evaluates active nudge policies and emits in-session memory-persistence prompts.
Implements the `curation_nudge` kind (P11) at runtime.

Storage: .cex/nudges/nudge_state.db  (SQLite, also readable by cex_user_model.py)

Usage:
    python _tools/cex_nudge.py check --session s1
    python _tools/cex_nudge.py fire --session s1 --observation "user prefers tables" --target MEMORY.md
    python _tools/cex_nudge.py stats
"""
from __future__ import annotations

import argparse
import json
import os
import sqlite3
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Dict, List, Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
CEX_ROOT = Path(__file__).resolve().parent.parent
NUDGE_DB_PATH = CEX_ROOT / ".cex" / "nudges" / "nudge_state.db"
POLICY_DIR = CEX_ROOT / ".cex" / "curation_nudge_policies"

_MEMORY_CANDIDATES = [
    Path(os.path.expanduser("~")) / ".claude" / "projects" /
    "C--Users-CEX-Documents-GitHub-cex" / "memory" / "MEMORY.md",
    CEX_ROOT / "MEMORY.md",
]
DEFAULT_MEMORY_TARGET = _MEMORY_CANDIDATES[0]


def _default_memory_path() -> Path:
    for p in _MEMORY_CANDIDATES:
        if p.parent.exists():
            return p
    return _MEMORY_CANDIDATES[0]


# ---------------------------------------------------------------------------
# Minimal YAML loader (stdlib-only, handles simple nested YAML)
# ---------------------------------------------------------------------------

def _try_yaml(text: str) -> Dict[str, Any]:
    """Try PyYAML first; fall back to homegrown simple parser."""
    try:
        import yaml  # type: ignore
        return yaml.safe_load(text) or {}
    except ImportError:
        return _simple_yaml(text)


def _simple_yaml(text: str) -> Dict[str, Any]:
    """Parse two-level nested YAML (sufficient for nudge policies)."""
    result: Dict[str, Any] = {}
    current_parent: Optional[str] = None
    for raw in text.splitlines():
        line = raw.rstrip()
        if not line or line.lstrip().startswith("#"):
            continue
        indent = len(line) - len(line.lstrip())
        stripped = line.strip()
        if ":" not in stripped:
            continue
        key_raw, _, val_raw = stripped.partition(":")
        key = key_raw.strip()
        val_str = val_raw.strip()
        if indent == 0:
            current_parent = key
            if val_str:
                result[key] = _cast(val_str)
            else:
                result[key] = {}
        elif indent > 0 and current_parent:
            if not isinstance(result.get(current_parent), dict):
                result[current_parent] = {}
            result[current_parent][key] = _cast(val_str) if val_str else None
    return result


def _cast(v: str) -> Any:
    v = v.strip().strip('"').strip("'")
    if v.lower() == "true":
        return True
    if v.lower() == "false":
        return False
    try:
        return int(v)
    except ValueError:
        pass
    try:
        return float(v)
    except ValueError:
        pass
    return v


# ---------------------------------------------------------------------------
# Policy model
# ---------------------------------------------------------------------------

class NudgePolicy:
    """Loaded from a .cex/curation_nudge_policies/*.yaml file."""

    def __init__(self, data: Dict[str, Any], path: Path) -> None:
        self.policy_id: str = str(data.get("id", path.stem))
        trigger = data.get("trigger", {}) or {}
        self.trigger_type: str = str(trigger.get("type", "turn_count"))
        self.threshold: int = int(trigger.get("threshold", 10))
        cadence = data.get("cadence", {}) or {}
        self.min_interval_turns: int = int(cadence.get("min_interval_turns", 5))
        self.max_per_session: int = int(cadence.get("max_per_session", 3))
        self.prompt_template: str = str(
            data.get("prompt_template", "Notei {{observation}}. Persistir em MEMORY.md?")
        )
        target_mem = data.get("target_memory", {}) or {}
        self.destination: str = str(target_mem.get("destination", "MEMORY.md"))
        self.auto_write: bool = bool(target_mem.get("auto_write_if_confirmed", False))

    def render(self, observation: str) -> str:
        return self.prompt_template.replace("{{observation}}", observation)

    def should_fire(
        self,
        turn_count: int,
        tool_call_count: int,
        last_nudge_turn: int,
        nudge_count: int,
    ) -> bool:
        if nudge_count >= self.max_per_session:
            return False
        gap = turn_count - last_nudge_turn
        if gap < self.min_interval_turns:
            return False
        if self.trigger_type == "turn_count":
            return turn_count > 0 and turn_count % self.threshold == 0
        if self.trigger_type == "tool_call_count":
            return tool_call_count > 0 and tool_call_count % self.threshold == 0
        if self.trigger_type == "density_threshold":
            return turn_count >= self.threshold
        return False


def load_policies() -> List[NudgePolicy]:
    """Load all active nudge policies from the policy directory."""
    if not POLICY_DIR.exists():
        POLICY_DIR.mkdir(parents=True, exist_ok=True)
        _write_default_policies()
    policies: List[NudgePolicy] = []
    for p in sorted(POLICY_DIR.glob("*.yaml")):
        try:
            data = _try_yaml(p.read_text(encoding="utf-8"))
            if data.get("enabled", True) is not False:
                policies.append(NudgePolicy(data, p))
        except Exception as exc:  # noqa: BLE001
            print(f"[WARN] skipping {p.name}: {exc}", file=sys.stderr)
    return policies


def _write_default_policies() -> None:
    """Seed the policy directory with a sensible default."""
    default = POLICY_DIR / "p11_cn_turn_count.yaml"
    default.write_text(
        "id: p11_cn_turn_count\n"
        "enabled: true\n"
        "trigger:\n"
        "  type: turn_count\n"
        "  threshold: 10\n"
        "cadence:\n"
        "  min_interval_turns: 8\n"
        "  max_per_session: 3\n"
        "prompt_template: \"Notei {{observation}}. Persistir em MEMORY.md?\"\n"
        "target_memory:\n"
        "  destination: MEMORY.md\n"
        "  auto_write_if_confirmed: false\n",
        encoding="utf-8",
    )


# ---------------------------------------------------------------------------
# SQLite state
# ---------------------------------------------------------------------------

_SCHEMA = """
PRAGMA journal_mode=WAL;

CREATE TABLE IF NOT EXISTS nudge_sessions (
    session_id       TEXT PRIMARY KEY,
    turn_count       INTEGER NOT NULL DEFAULT 0,
    tool_call_count  INTEGER NOT NULL DEFAULT 0,
    last_nudge_turn  INTEGER NOT NULL DEFAULT 0,
    nudge_count      INTEGER NOT NULL DEFAULT 0,
    created          TEXT    NOT NULL,
    updated          TEXT    NOT NULL
);

CREATE TABLE IF NOT EXISTS nudge_log (
    log_id      INTEGER PRIMARY KEY AUTOINCREMENT,
    session_id  TEXT    NOT NULL,
    policy_id   TEXT    NOT NULL,
    turn_count  INTEGER NOT NULL,
    observation TEXT    NOT NULL DEFAULT '',
    target      TEXT    NOT NULL DEFAULT 'MEMORY.md',
    fired_at    TEXT    NOT NULL
);
"""


def _now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def _open_db(db_path: Optional[Path] = None) -> sqlite3.Connection:
    p = db_path or NUDGE_DB_PATH
    p.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(p))
    conn.row_factory = sqlite3.Row
    conn.executescript(_SCHEMA)
    conn.commit()
    return conn


def _get_or_create_session(
    conn: sqlite3.Connection, session_id: str
) -> sqlite3.Row:
    row = conn.execute(
        "SELECT * FROM nudge_sessions WHERE session_id=?", (session_id,)
    ).fetchone()
    if row is None:
        now = _now_iso()
        conn.execute(
            "INSERT INTO nudge_sessions(session_id,created,updated) VALUES(?,?,?)",
            (session_id, now, now),
        )
        conn.commit()
        row = conn.execute(
            "SELECT * FROM nudge_sessions WHERE session_id=?", (session_id,)
        ).fetchone()
    return row  # type: ignore[return-value]


def _update_session(
    conn: sqlite3.Connection,
    session_id: str,
    *,
    increment_turn: bool = False,
    increment_tool: bool = False,
    set_last_nudge_turn: Optional[int] = None,
    increment_nudge: bool = False,
) -> None:
    parts = ["updated=?"]
    vals: List[Any] = [_now_iso()]
    if increment_turn:
        parts.append("turn_count=turn_count+1")
    if increment_tool:
        parts.append("tool_call_count=tool_call_count+1")
    if set_last_nudge_turn is not None:
        parts.append("last_nudge_turn=?")
        vals.append(set_last_nudge_turn)
    if increment_nudge:
        parts.append("nudge_count=nudge_count+1")
    vals.append(session_id)
    conn.execute(
        f"UPDATE nudge_sessions SET {', '.join(parts)} WHERE session_id=?",
        tuple(vals),
    )
    conn.commit()


# ---------------------------------------------------------------------------
# Commands
# ---------------------------------------------------------------------------

def cmd_check(session_id: str, db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Return list of policies that should fire for this session."""
    conn = _open_db(db_path)
    row = _get_or_create_session(conn, session_id)
    policies = load_policies()
    results: List[Dict[str, Any]] = []
    for pol in policies:
        if pol.should_fire(
            turn_count=row["turn_count"],
            tool_call_count=row["tool_call_count"],
            last_nudge_turn=row["last_nudge_turn"],
            nudge_count=row["nudge_count"],
        ):
            results.append(
                {
                    "policy_id": pol.policy_id,
                    "trigger_type": pol.trigger_type,
                    "prompt_template": pol.prompt_template,
                    "destination": pol.destination,
                }
            )
    conn.close()
    return results


def cmd_fire(
    session_id: str,
    observation: str,
    target: Optional[str] = None,
    write: bool = False,
    db_path: Optional[Path] = None,
) -> str:
    """Emit nudge text; persist to target if write=True."""
    conn = _open_db(db_path)
    row = _get_or_create_session(conn, session_id)
    policies = load_policies()

    fired: List[str] = []
    for pol in policies:
        if not pol.should_fire(
            turn_count=row["turn_count"],
            tool_call_count=row["tool_call_count"],
            last_nudge_turn=row["last_nudge_turn"],
            nudge_count=row["nudge_count"],
        ):
            continue
        nudge_text = pol.render(observation)
        dest = target or pol.destination
        fired.append(nudge_text)
        conn.execute(
            "INSERT INTO nudge_log(session_id,policy_id,turn_count,observation,target,fired_at)"
            " VALUES(?,?,?,?,?,?)",
            (session_id, pol.policy_id, row["turn_count"], observation, dest, _now_iso()),
        )
        _update_session(
            conn, session_id,
            set_last_nudge_turn=row["turn_count"],
            increment_nudge=True,
        )
        row = _get_or_create_session(conn, session_id)  # refresh after update
        if write or pol.auto_write:
            _write_to_target(dest, observation)
    conn.commit()
    conn.close()

    if not fired:
        return "[nudge] No policies triggered for this session state."
    output = "\n".join(fired)
    if write:
        output += "\n[nudge] Written to " + (target or "MEMORY.md")
    return output


def cmd_tick(
    session_id: str,
    increment_turn: bool = True,
    increment_tool: bool = False,
    db_path: Optional[Path] = None,
) -> None:
    """Advance session counters. Called from PostToolUse hook."""
    conn = _open_db(db_path)
    _get_or_create_session(conn, session_id)
    _update_session(
        conn, session_id,
        increment_turn=increment_turn,
        increment_tool=increment_tool,
    )
    conn.close()


def cmd_stats(db_path: Optional[Path] = None) -> List[Dict[str, Any]]:
    """Return per-session nudge counts."""
    conn = _open_db(db_path)
    rows = conn.execute(
        "SELECT s.session_id, s.turn_count, s.tool_call_count, s.nudge_count,"
        " s.last_nudge_turn, COUNT(l.log_id) AS log_entries"
        " FROM nudge_sessions s"
        " LEFT JOIN nudge_log l ON l.session_id=s.session_id"
        " GROUP BY s.session_id"
        " ORDER BY s.updated DESC"
    ).fetchall()
    conn.close()
    return [dict(r) for r in rows]


def _write_to_target(destination: str, observation: str) -> None:
    """Append observation to the named destination."""
    if destination in ("MEMORY.md",):
        target_path = _default_memory_path()
    else:
        target_path = Path(destination)
    try:
        with open(target_path, "a", encoding="utf-8") as fh:
            fh.write(f"\n- [nudge] {observation}\n")
    except OSError as exc:
        print(f"[WARN] could not write to {destination}: {exc}", file=sys.stderr)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def _build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cex_nudge",
        description="Curation nudge runtime -- curation_nudge kind (P11)",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    chk = sub.add_parser("check", help="Decide if a nudge should fire")
    chk.add_argument("--session", required=True, help="Session identifier")
    chk.add_argument("--json", action="store_true", dest="as_json",
                     help="Output as JSON")

    fire = sub.add_parser("fire", help="Fire a nudge and optionally persist")
    fire.add_argument("--session", required=True)
    fire.add_argument("--observation", required=True,
                      help="What was observed (injected into prompt)")
    fire.add_argument("--target", default=None,
                      help="Destination (MEMORY.md or file path)")
    fire.add_argument("--write", action="store_true",
                      help="Persist observation to target immediately")

    tick = sub.add_parser("tick", help="Advance session counters (hook use)")
    tick.add_argument("--session", required=True)
    tick.add_argument("--tool", action="store_true", help="Increment tool_call_count")

    sub.add_parser("stats", help="Per-session nudge counts")

    return parser


def main(argv: Optional[List[str]] = None) -> int:
    parser = _build_parser()
    args = parser.parse_args(argv)

    if args.command == "check":
        results = cmd_check(args.session)
        if args.as_json:
            print(json.dumps(results, indent=2))
        elif results:
            for r in results:
                print(f"[nudge-ready] {r['policy_id']}: {r['prompt_template']}")
        else:
            print("[nudge] No policies ready.")
        return 0

    if args.command == "fire":
        text = cmd_fire(
            args.session,
            args.observation,
            target=args.target,
            write=args.write,
        )
        print(text)
        return 0

    if args.command == "tick":
        cmd_tick(args.session, increment_tool=args.tool)
        return 0

    if args.command == "stats":
        rows = cmd_stats()
        if not rows:
            print("[nudge] No sessions recorded.")
            return 0
        header = f"{'SESSION':<30} {'TURNS':>6} {'TOOLS':>6} {'NUDGES':>7} {'LAST':>6}"
        print(header)
        print("-" * len(header))
        for r in rows:
            print(
                f"{r['session_id']:<30} {r['turn_count']:>6} "
                f"{r['tool_call_count']:>6} {r['nudge_count']:>7} "
                f"{r['last_nudge_turn']:>6}"
            )
        return 0

    return 1


if __name__ == "__main__":
    sys.exit(main())
