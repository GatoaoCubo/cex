#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CEX Native Hooks -- single entry point for Claude Code (and runtime-agnostic) hooks.

Wired by .claude/settings.json. Detects CEX_NUCLEUS env to scope behavior.
Runtime-agnostic: gemini/codex/ollama boot wrappers call the same entry via
`python _tools/cex_hooks_native.py <event>` so every runtime gets identical side effects.

Events:
  post-tool-use   -- after Write|Edit: compile .md -> .yaml, sanitize code files
                     also appends to HERMES skill trace JSONL
  post-compact    -- after context compaction: decay memory ages
  session-start   -- on session boot: preflight quick-check + nudge check
  stop            -- on session stop: auto-emit signal + skill autocreate scan

Exit codes:
  0 = OK (always; hooks must never break the session)
  non-zero reserved for hard aborts (not used today)
"""

from __future__ import annotations

import argparse
import json
import os
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOOK_LOG = ROOT / ".cex" / "runtime" / "hook_log.jsonl"
HOOK_LOG.parent.mkdir(parents=True, exist_ok=True)
_TRACES_DIR = ROOT / ".cex" / "runtime" / "traces"
_SESSION_ID = os.environ.get("CEX_SESSION_ID") or os.environ.get("CEX_NUCLEUS", "n07")


def _rotate_hook_log(max_bytes: int = 512_000, keep_lines: int = 200) -> None:
    """Rotate hook log if it exceeds max_bytes, keeping the last keep_lines."""
    try:
        if not HOOK_LOG.exists():
            return
        if HOOK_LOG.stat().st_size <= max_bytes:
            return
        lines = HOOK_LOG.read_text(encoding="utf-8").splitlines()
        tail = lines[-keep_lines:] if len(lines) > keep_lines else lines
        HOOK_LOG.write_text("\n".join(tail) + "\n", encoding="utf-8")
    except Exception:
        pass


def _log(event: str, payload: dict) -> None:
    try:
        _rotate_hook_log()
        line = {
            "event": event,
            "nucleus": os.environ.get("CEX_NUCLEUS", "unknown"),
            "runtime": os.environ.get("CEX_RUNTIME", "claude"),
            "payload": payload,
        }
        with HOOK_LOG.open("a", encoding="utf-8") as f:
            f.write(json.dumps(line, ensure_ascii=False) + "\n")
    except Exception:
        pass


def _run(cmd: list[str], timeout: int = 20) -> tuple[int, str]:
    try:
        r = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, timeout=timeout)
        return r.returncode, (r.stdout or "") + (r.stderr or "")
    except Exception as e:
        return 1, str(e)


def _stdin_payload() -> dict:
    if sys.stdin.isatty():
        return {}
    try:
        raw = sys.stdin.read()
        return json.loads(raw) if raw.strip() else {}
    except Exception:
        return {}


def post_tool_use() -> int:
    payload = _stdin_payload()
    tool_name = payload.get("tool_name") or ""
    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("path") or ""

    # HERMES skill trace: append tool call to session JSONL
    try:
        import time as _time
        _TRACES_DIR.mkdir(parents=True, exist_ok=True)
        trace_path = _TRACES_DIR / f"trace_{_SESSION_ID}.jsonl"
        entry = {
            "ts": _time.time(),
            "tool": tool_name,
            "path": path,
            "nucleus": os.environ.get("CEX_NUCLEUS", "n07"),
        }
        with trace_path.open("a", encoding="ascii", errors="replace") as tf:
            tf.write(json.dumps(entry) + "\n")
    except Exception:
        pass

    if not path:
        _log("post-tool-use", {"skipped": "no_path"})
        return 0
    p = Path(path)
    if p.suffix == ".md":
        rc, out = _run(["python", "_tools/cex_compile.py", str(p)], timeout=30)
        _log("post-tool-use", {"action": "compile", "path": str(p), "rc": rc})
        # F3b: check for entity references in compiled .md
        try:
            if p.exists():
                head = p.read_text(encoding="utf-8", errors="replace")[:1500]
                if "## Entities" in head or "entity:" in head or "entities:" in head:
                    kind_val = "unknown"
                    for ln in head.splitlines()[:20]:
                        if ln.strip().startswith("kind:"):
                            kind_val = ln.split(":", 1)[1].strip()
                            break
                    _run(
                        [
                            "python", "_tools/cex_memory_update.py",
                            "--builder", kind_val + "-builder",
                            "--type", "reference",
                            "--observation", "F3b inline: entity refs in " + str(p),
                            "--pattern", "entity-bearing artifact",
                            "--confidence", "0.6",
                            "--outcome", "SUCCESS",
                        ],
                        timeout=10,
                    )
                    _log("post-tool-use", {"action": "f3b_persist", "path": str(p)})
        except Exception:
            pass
    elif p.suffix in {".py", ".ps1", ".sh"}:
        rc, out = _run(["python", "_tools/cex_sanitize.py", "--check", "--scope", str(p)], timeout=15)
        _log("post-tool-use", {"action": "sanitize-check", "path": str(p), "rc": rc})
    else:
        _log("post-tool-use", {"skipped": "unsupported_suffix", "path": str(p)})
    return 0


def post_compact() -> int:
    rc, out = _run(["python", "_tools/cex_memory_age.py", "--decay"], timeout=30)
    _log("post-compact", {"rc": rc})
    return 0


def session_start() -> int:
    rc, out = _run(["python", "_tools/cex_preflight.py", "--quick"], timeout=30)
    _log("session-start", {"rc": rc})
    # HERMES nudge: check if any curation nudge should fire at session start
    nucleus = os.environ.get("CEX_NUCLEUS", "n07")
    session_id = _SESSION_ID
    _run(["python", "_tools/cex_nudge.py", "check", "--session", session_id], timeout=10)
    return 0


def _persist_from_signal(signal_path: str) -> None:
    """F3b PERSIST: extract artifact from last commit, persist entities/learnings."""
    try:
        pass

        rc, last_files = _run(
            ["git", "dif", "--name-only", "HEAD~1", "HEAD", "--diff-filter=AM"],
            timeout=10,
        )
        if rc != 0 or not last_files.strip():
            _log("f3b_persist", {"skipped": "no_recent_artifacts"})
            return

        artifacts = [
            f for f in last_files.strip().splitlines()
            if f.strip().endswith(".md") and not f.strip().startswith(".")
        ]
        if not artifacts:
            _log("f3b_persist", {"skipped": "no_md_artifacts_in_commit"})
            return

        persisted = 0
        for art_path in artifacts[:5]:
            art_file = ROOT / art_path.strip()
            if not art_file.exists():
                continue
            try:
                content = art_file.read_text(encoding="utf-8", errors="replace")[:2000]
            except Exception:
                continue

            has_entities = (
                "## Entities" in content
                or "entity:" in content
                or "entities:" in content
            )
            if not has_entities:
                continue

            kind_line = ""
            for line in content.splitlines()[:20]:
                if line.strip().startswith("kind:"):
                    kind_line = line.split(":", 1)[1].strip()
                    break
            if not kind_line:
                kind_line = "unknown"

            nucleus = os.environ.get("CEX_NUCLEUS", "unknown")
            rc2, _ = _run(
                [
                    "python", "_tools/cex_memory_update.py",
                    "--builder", kind_line + "-builder",
                    "--type", "reference",
                    "--observation", "F3b auto-persist: entity references in " + art_path.strip(),
                    "--pattern", "entity-bearing artifact at " + art_path.strip(),
                    "--confidence", "0.7",
                    "--outcome", "SUCCESS",
                ],
                timeout=15,
            )
            if rc2 == 0:
                persisted += 1

        _log("f3b_persist", {
            "action": "f3b_persist",
            "artifacts_scanned": len(artifacts),
            "persisted": persisted,
            "signal": signal_path,
        })
    except Exception as e:
        _log("f3b_persist", {"error": str(e)})


def stop() -> int:
    nucleus = os.environ.get("CEX_NUCLEUS", "").lower()
    if not nucleus or nucleus == "n07":
        _log("stop", {"skipped": "no_nucleus_or_n07"})
    else:
        try:
            sys.path.insert(0, str(ROOT))
            from _tools.signal_writer import write_signal  # noqa: WPS433
            write_signal(nucleus, "complete", float(os.environ.get("CEX_QUALITY", "9.0")))
            _log("stop", {"signaled": nucleus})
            # F3b PERSIST: auto-persist entities/learnings after signal
            _persist_from_signal(nucleus)
        except Exception as e:
            _log("stop", {"error": str(e)})
    # HERMES skill autocreate: scan recent traces for skill candidates
    _run(
        ["python", "_tools/cex_skill_autocreate.py", "--scan-recent", "--since", "8h"],
        timeout=30,
    )
    return 0


EVENTS = {
    "post-tool-use": post_tool_use,
    "post-compact": post_compact,
    "session-start": session_start,
    "stop": stop,
}


def main(argv: list[str]) -> int:
    if len(argv) < 2:
        sys.stderr.write("usage: cex_hooks_native.py {post-tool-use|post-compact|session-start|stop}\n")
        return 0
    if not argv[1].startswith("-") and argv[1] not in EVENTS:
        sys.stderr.write("usage: cex_hooks_native.py {post-tool-use|post-compact|session-start|stop}\n")
        return 0

    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "event",
        nargs="?",
        help="Hook event to execute.",
    )
    parsed, _ = parser.parse_known_args(argv[1:])
    try:
        return EVENTS[parsed.event]()
    except Exception as e:
        _log(parsed.event, {"fatal": str(e)})
        return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
