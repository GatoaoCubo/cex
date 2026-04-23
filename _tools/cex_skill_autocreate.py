# -*- coding: ascii -*-
"""
CEX Skill Auto-Creator -- HERMES W4.1

Watches task traces (JSONL) and auto-generates skill artifacts when
a task completes with >= 5 successful tool calls.

CLI:
    python _tools/cex_skill_autocreate.py --trace .cex/runtime/traces/trace_xxx.jsonl [--force] [--dry-run]
    python _tools/cex_skill_autocreate.py --scan-recent --since 1h
    python _tools/cex_skill_autocreate.py --help
"""
from __future__ import annotations

import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
_REPO_ROOT = Path(__file__).resolve().parent.parent
_TRACES_DIR = _REPO_ROOT / ".cex" / "runtime" / "traces"
_SKILLS_DIR = _REPO_ROOT / ".cex" / "skills" / "autocreated"
_INDEX_PATH = _REPO_ROOT / ".cex" / "skills" / "index.json"
_SIGNALS_DIR = _REPO_ROOT / ".cex" / "runtime" / "signals"

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------
MIN_TOOL_CALLS = 5
MIN_UNIQUE_TOOLS = 3        # must use >= 3 distinct tool types
MAX_STEPS_IN_BODY = 30      # collapse beyond this (no 105-line "Edit" lists)
MIN_GOAL_QUALITY = 0.4      # reject if goal is just a tool name
SKILL_PILLAR = "P04"
SKILL_KIND = "skill"


# ---------------------------------------------------------------------------
# Trace parsing
# ---------------------------------------------------------------------------

def load_trace(path: Path) -> list[dict[str, Any]]:
    """Load JSONL trace file; return list of event dicts."""
    events: list[dict[str, Any]] = []
    with open(path, "r", encoding="ascii", errors="replace") as fh:
        for lineno, raw in enumerate(fh, 1):
            raw = raw.strip()
            if not raw:
                continue
            try:
                events.append(json.loads(raw))
            except json.JSONDecodeError as exc:
                print(f"[WARN] trace line {lineno} skipped: {exc}", file=sys.stderr)
    return events


def compute_trace_hash(path: Path) -> str:
    """SHA-256 of file content, first 16 hex chars."""
    digest = hashlib.sha256(path.read_bytes()).hexdigest()
    return digest[:16]


def extract_successful_calls(events: list[dict[str, Any]]) -> list[dict[str, Any]]:
    """Return tool-call events whose status is 'success' (or absent)."""
    calls: list[dict[str, Any]] = []
    for ev in events:
        if ev.get("type") not in (None, "tool_call", "tool_result"):
            # Accept events that have a 'tool' key regardless of type field
            pass
        tool = ev.get("tool") or ev.get("tool_name")
        if not tool:
            continue
        status = ev.get("status", "success")
        if status in ("success", "ok", "completed", ""):
            calls.append(ev)
    return calls


def detect_task_error(events: list[dict[str, Any]]) -> bool:
    """Return True if any event signals a terminal error."""
    error_statuses = {"error", "failed", "fatal", "exception"}
    for ev in events:
        if ev.get("status", "").lower() in error_statuses:
            return True
        # Also check explicit error keys
        if ev.get("error") and ev.get("terminal", False):
            return True
    return False


def derive_task_goal(events: list[dict[str, Any]]) -> tuple[str, float]:
    """Extract task goal from trace metadata. Returns (goal, confidence 0-1)."""
    for ev in events:
        goal = ev.get("goal") or ev.get("task") or ev.get("intent")
        if goal and isinstance(goal, str) and len(goal.strip()) > 10:
            return goal[:120], 1.0
    # Try user_message or prompt fields
    for ev in events:
        msg = ev.get("user_message") or ev.get("prompt") or ev.get("message")
        if msg and isinstance(msg, str) and len(msg.strip()) > 10:
            return msg[:120], 0.8
    # Fall back to file paths touched (more useful than tool names)
    paths = set()
    for ev in events:
        args = ev.get("args") or ev.get("input") or {}
        if isinstance(args, dict):
            for key in ("file_path", "path", "file"):
                val = args.get(key)
                if val and isinstance(val, str):
                    paths.add(Path(val).name)
    if paths:
        sample = ", ".join(sorted(paths)[:5])
        return f"Multi-file operation on: {sample}", 0.5
    # Last resort -- tool name (low quality, will be rejected by gate)
    from collections import Counter
    tools = [
        ev.get("tool") or ev.get("tool_name", "")
        for ev in events
        if ev.get("tool") or ev.get("tool_name")
    ]
    if tools:
        top = Counter(tools).most_common(1)[0][0]
        return f"Procedure involving {top} and related tools", 0.2
    return "Automated procedure from trace", 0.0


def derive_auto_name(goal: str, trace_hash: str) -> str:
    """Produce a slug name for the skill from the goal string."""
    slug = re.sub(r"[^a-z0-9]+", "_", goal.lower())[:40].strip("_")
    return f"{slug}_{trace_hash[:6]}"


def summarize_calls(calls: list[dict[str, Any]]) -> list[dict[str, str]]:
    """Produce a COMPRESSED summary -- groups consecutive same-tool runs."""
    raw: list[dict[str, str]] = []
    for call in calls:
        tool = call.get("tool") or call.get("tool_name", "unknown")
        args = call.get("args") or call.get("input") or {}
        if isinstance(args, dict):
            fp = args.get("file_path") or args.get("path") or ""
            if fp:
                arg_str = Path(fp).name if isinstance(fp, str) else str(fp)[:40]
            else:
                arg_str = ", ".join(
                    f"{k}={str(v)[:40]}" for k, v in list(args.items())[:3]
                )
        else:
            arg_str = str(args)[:80]
        result = call.get("result") or call.get("output") or ""
        result_str = str(result)[:80] if result else ""
        raw.append({"tool": tool, "args": arg_str, "result": result_str})

    # Compress consecutive same-tool runs into "Edit x15 (file1, file2, ...)"
    compressed: list[dict[str, str]] = []
    i = 0
    while i < len(raw):
        tool = raw[i]["tool"]
        run_start = i
        files: list[str] = []
        while i < len(raw) and raw[i]["tool"] == tool:
            if raw[i]["args"]:
                files.append(raw[i]["args"])
            i += 1
        count = i - run_start
        unique_files = sorted(set(files))[:5]
        if count > 1:
            file_hint = f" ({', '.join(unique_files)})" if unique_files else ""
            compressed.append({
                "tool": tool,
                "args": f"x{count}{file_hint}",
                "result": "",
            })
        else:
            compressed.append(raw[run_start])
    return compressed[:MAX_STEPS_IN_BODY]


def count_unique_tools(calls: list[dict[str, Any]]) -> int:
    """Count distinct tool types used in calls."""
    return len({
        c.get("tool") or c.get("tool_name", "unknown") for c in calls
    })


def derive_prerequisites(calls: list[dict[str, Any]]) -> list[str]:
    """Infer prerequisites from tool names."""
    tool_names = {c.get("tool") or c.get("tool_name", "") for c in calls}
    prereqs: list[str] = []
    if any("git" in t.lower() for t in tool_names):
        prereqs.append("git repository initialized")
    if any("python" in t.lower() or "bash" in t.lower() for t in tool_names):
        prereqs.append("Python 3.10+ available")
    if any("compile" in t.lower() for t in tool_names):
        prereqs.append("cex_compile.py accessible")
    if not prereqs:
        prereqs.append("CEX repo context")
    return prereqs


# ---------------------------------------------------------------------------
# Skill generation
# ---------------------------------------------------------------------------

def build_skill_markdown(
    auto_name: str,
    trace_hash: str,
    goal: str,
    call_summary: list[dict[str, str]],
    prerequisites: list[str],
) -> str:
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    # Build steps block
    steps_lines = ["## Procedure\n"]
    for i, step in enumerate(call_summary, 1):
        line = f"{i}. **{step['tool']}**"
        if step["args"]:
            line += f"  args: `{step['args']}`"
        if step["result"]:
            line += f"  -> `{step['result']}`"
        steps_lines.append(line)

    # Build prereqs block
    prereq_block = "\n".join(f"- {p}" for p in prerequisites)

    steps_block = "\n".join(steps_lines)

    return """---
id: p04_skill_{auto_name}
kind: skill
pillar: {SKILL_PILLAR}
title: "Auto-Skill: {auto_name}"
auto_generated_from: {trace_hash}
self_improves: true
agentskills_catalog_category: auto
trigger_tool_call_count_min: {MIN_TOOL_CALLS}
improvement_count: 0
created: "{today}"
quality: null
tags: [skill, auto_generated, hermes_origin]
---

## Goal

{goal}

## When to Apply

Use this skill when facing a task that matches the following trigger pattern:
- At least {MIN_TOOL_CALLS} tool calls are expected
- Task involves: {', '.join(set(s['tool'] for s in call_summary[:5]))}

## Prerequisites

{prereq_block}

{steps_block}

## Notes

Auto-generated by `cex_skill_autocreate.py` from trace `{trace_hash}`.
Review and improve via `cex_skill_improve.py`.
"""


# ---------------------------------------------------------------------------
# Index management
# ---------------------------------------------------------------------------

def load_index() -> dict[str, Any]:
    if _INDEX_PATH.exists():
        try:
            return json.loads(_INDEX_PATH.read_text(encoding="ascii", errors="replace"))
        except json.JSONDecodeError:
            pass
    return {"skills": {}}


def save_index(index: dict[str, Any]) -> None:
    _INDEX_PATH.parent.mkdir(parents=True, exist_ok=True)
    _INDEX_PATH.write_text(json.dumps(index, indent=2), encoding="ascii")


def is_registered(trace_hash: str, index: dict[str, Any]) -> bool:
    return trace_hash in index.get("skills", {})


def register_skill(trace_hash: str, skill_path: Path, auto_name: str, index: dict[str, Any]) -> None:
    # _INDEX_PATH is .cex/skills/index.json -> parent.parent.parent = repo root
    repo_root = _INDEX_PATH.parent.parent.parent
    try:
        rel = str(skill_path.relative_to(repo_root))
    except ValueError:
        rel = str(skill_path)
    index.setdefault("skills", {})[trace_hash] = {
        "path": rel,
        "name": auto_name,
        "created": datetime.now(timezone.utc).isoformat(),
    }


# ---------------------------------------------------------------------------
# Core pipeline
# ---------------------------------------------------------------------------

def process_trace(
    trace_path: Path,
    *,
    force: bool = False,
    dry_run: bool = False,
) -> bool:
    """
    Process a single trace file.
    Returns True if a skill was (or would be) written.
    """
    if not trace_path.exists():
        print(f"[FAIL] Trace not found: {trace_path}", file=sys.stderr)
        return False

    trace_hash = compute_trace_hash(trace_path)
    index = load_index()

    if not force and is_registered(trace_hash, index):
        print(f"[SKIP] trace {trace_hash} already has a skill (use --force to overwrite)")
        return False

    events = load_trace(trace_path)

    if detect_task_error(events):
        print(f"[SKIP] trace {trace_hash}: task ended in terminal error")
        return False

    successful_calls = extract_successful_calls(events)

    if len(successful_calls) < MIN_TOOL_CALLS:
        print(
            f"[SKIP] trace {trace_hash}: only {len(successful_calls)} successful tool calls "
            f"(threshold={MIN_TOOL_CALLS})"
        )
        return False

    # Gate: require tool diversity (reject pure Edit-only traces)
    unique_tools = count_unique_tools(successful_calls)
    if unique_tools < MIN_UNIQUE_TOOLS:
        print(
            f"[SKIP] trace {trace_hash}: only {unique_tools} unique tool types "
            f"(threshold={MIN_UNIQUE_TOOLS}) -- too monotonic for a useful skill"
        )
        return False

    goal, goal_confidence = derive_task_goal(events)

    # Gate: reject low-quality goals (just tool names, no semantics)
    if goal_confidence < MIN_GOAL_QUALITY:
        print(
            f"[SKIP] trace {trace_hash}: goal quality {goal_confidence:.1f} < "
            f"{MIN_GOAL_QUALITY} -- cannot derive meaningful skill name"
        )
        return False

    auto_name = derive_auto_name(goal, trace_hash)
    call_summary = summarize_calls(successful_calls)
    prerequisites = derive_prerequisites(successful_calls)

    markdown = build_skill_markdown(auto_name, trace_hash, goal, call_summary, prerequisites)

    skill_file = _SKILLS_DIR / f"skill_{auto_name}.md"

    if dry_run:
        print(f"[DRY-RUN] Would write: {skill_file}")
        print(f"[DRY-RUN] Skill name : {auto_name}")
        print(f"[DRY-RUN] Tool calls : {len(successful_calls)}")
        print(f"[DRY-RUN] Preview    :\n{markdown[:400]}...")
        return True

    _SKILLS_DIR.mkdir(parents=True, exist_ok=True)
    skill_file.write_text(markdown, encoding="ascii")
    register_skill(trace_hash, skill_file, auto_name, index)
    save_index(index)

    print(f"[OK] Skill written: {skill_file}")
    print(f"[OK] Registered in: {_INDEX_PATH}")
    return True


def parse_since(since_str: str) -> datetime:
    """Parse '1h', '30m', '2d' into a UTC cutoff datetime."""
    match = re.fullmatch(r"(\d+)([hmd])", since_str.strip().lower())
    if not match:
        raise ValueError(f"Invalid --since format: '{since_str}'. Use e.g. 1h, 30m, 2d")
    value, unit = int(match.group(1)), match.group(2)
    delta_map = {"h": timedelta(hours=value), "m": timedelta(minutes=value), "d": timedelta(days=value)}
    return datetime.now(timezone.utc) - delta_map[unit]


def scan_recent(since_str: str, *, force: bool = False, dry_run: bool = False) -> int:
    """Scan _TRACES_DIR for JSONL files modified after `since`. Returns count processed."""
    cutoff = parse_since(since_str)
    if not _TRACES_DIR.exists():
        print(f"[WARN] Traces directory does not exist: {_TRACES_DIR}", file=sys.stderr)
        return 0

    written = 0
    for trace_path in sorted(_TRACES_DIR.glob("*.jsonl")):
        mtime = datetime.fromtimestamp(trace_path.stat().st_mtime, tz=timezone.utc)
        if mtime < cutoff:
            continue
        if process_trace(trace_path, force=force, dry_run=dry_run):
            written += 1

    print(f"[OK] Scan complete: {written} skill(s) generated")
    return written


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="cex_skill_autocreate",
        description="Auto-generate CEX skill artifacts from task traces (HERMES W4.1).",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python _tools/cex_skill_autocreate.py --trace .cex/runtime/traces/trace_abc.jsonl
  python _tools/cex_skill_autocreate.py --trace ... --force --dry-run
  python _tools/cex_skill_autocreate.py --scan-recent --since 1h
""",
    )
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument(
        "--trace",
        metavar="PATH",
        help="Path to a single JSONL trace file to process",
    )
    mode.add_argument(
        "--scan-recent",
        action="store_true",
        help="Scan all recent traces in the traces directory",
    )
    parser.add_argument(
        "--since",
        default="1h",
        metavar="DURATION",
        help="Used with --scan-recent: how far back to look (e.g. 1h, 30m, 2d). Default: 1h",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing skill if trace_hash already registered",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print what would be written without touching any files",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)

    if args.trace:
        success = process_trace(Path(args.trace), force=args.force, dry_run=args.dry_run)
        return 0 if success else 1

    if args.scan_recent:
        count = scan_recent(args.since, force=args.force, dry_run=args.dry_run)
        return 0 if count >= 0 else 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
