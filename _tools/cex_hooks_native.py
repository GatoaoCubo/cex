#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Native Hooks -- single entry point for Claude Code (and runtime-agnostic) hooks.

Wired by .claude/settings.json. Detects CEX_NUCLEUS env to scope behavior.
Runtime-agnostic: gemini/codex/ollama boot wrappers call the same entry via
`python _tools/cex_hooks_native.py <event>` so every runtime gets identical side effects.

Events:
  post-tool-use   -- after Write|Edit: compile .md -> .yaml, sanitize code files
  post-compact    -- after context compaction: decay memory ages
  session-start   -- on session boot: preflight quick-check
  stop            -- on session stop: auto-emit completion signal

Exit codes:
  0 = OK (always; hooks must never break the session)
  non-zero reserved for hard aborts (not used today)
"""

from __future__ import annotations

import json
import os
import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
HOOK_LOG = ROOT / ".cex" / "runtime" / "hook_log.jsonl"
HOOK_LOG.parent.mkdir(parents=True, exist_ok=True)


def _log(event: str, payload: dict) -> None:
    try:
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
    tool_input = payload.get("tool_input") or {}
    path = tool_input.get("file_path") or tool_input.get("path") or ""
    if not path:
        _log("post-tool-use", {"skipped": "no_path"})
        return 0
    p = Path(path)
    if p.suffix == ".md":
        rc, out = _run(["python", "_tools/cex_compile.py", str(p)], timeout=30)
        _log("post-tool-use", {"action": "compile", "path": str(p), "rc": rc})
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
    return 0


def stop() -> int:
    nucleus = os.environ.get("CEX_NUCLEUS", "").lower()
    if not nucleus or nucleus == "n07":
        _log("stop", {"skipped": "no_nucleus_or_n07"})
        return 0
    try:
        sys.path.insert(0, str(ROOT))
        from _tools.signal_writer import write_signal  # noqa: WPS433
        write_signal(nucleus, "complete", float(os.environ.get("CEX_QUALITY", "9.0")))
        _log("stop", {"signaled": nucleus})
    except Exception as e:
        _log("stop", {"error": str(e)})
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
