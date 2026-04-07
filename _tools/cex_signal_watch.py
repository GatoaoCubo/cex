#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Signal Watcher v1.0 -- Blocks until all expected nuclei signal or timeout.

Usage:
    python _tools/cex_signal_watch.py --expect n01,n02,n03,n04,n05,n06 --timeout 3600
    python _tools/cex_signal_watch.py --expect n01,n03 --mission MONETIZE_CEX --poll 15
    python _tools/cex_signal_watch.py --expect n01,n02,n03,n04,n05,n06 --pid-file .cex/runtime/pids/spawn_pids.txt

Returns JSON summary when all signals received, any crash detected, or timeout.

Exit codes:
    0 = all expected nuclei signaled complete
    1 = timeout (some nuclei didn't signal)
    2 = crash detected (nucleus died without signaling)
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SIGNAL_DIR = ROOT / ".cex" / "runtime" / "signals"
PID_FILE = ROOT / ".cex" / "runtime" / "pids" / "spawn_pids.txt"


def parse_args():
    p = argparse.ArgumentParser(description="Watch for nucleus completion signals")
    p.add_argument("--expect", required=True, help="Comma-separated nuclei: n01,n02,n03")
    p.add_argument("--mission", default="", help="Mission name filter for signals")
    p.add_argument("--timeout", type=int, default=3600, help="Max seconds to wait (default: 3600)")
    p.add_argument("--poll", type=int, default=30, help="Poll interval seconds (default: 30)")
    p.add_argument("--pid-file", default=str(PID_FILE), help="PID tracking file")
    p.add_argument("--since", default="", help="Only count signals after this ISO timestamp")
    p.add_argument("--quiet", action="store_true", help="Suppress progress output")
    return p.parse_args()


def load_pids(pid_file: str) -> dict:
    """Load nucleus->PID mapping from spawn_pids.txt."""
    pids = {}
    path = Path(pid_file)
    if not path.exists():
        return pids
    for line in path.read_text(encoding="utf-8").strip().splitlines():
        parts = line.strip().split()
        if len(parts) >= 2:
            pid, nucleus = int(parts[0]), parts[1].lower()
            pids[nucleus] = pid
    return pids


def is_pid_alive(pid: int) -> bool:
    """Check if a process is still running (cross-platform)."""
    if sys.platform == "win32":
        import subprocess
        try:
            result = subprocess.run(
                ["tasklist", "/FI", f"PID eq {pid}", "/NH"],
                capture_output=True, text=True, timeout=5
            )
            return str(pid) in result.stdout
        except Exception:
            return False
    else:
        try:
            os.kill(pid, 0)
            return True
        except OSError:
            return False


def find_signals(expected: set, since: str) -> dict:
    """Scan signal directory for matching signals."""
    found = {}
    if not SIGNAL_DIR.exists():
        return found

    since_dt = None
    if since:
        try:
            since_dt = datetime.fromisoformat(since)
        except ValueError:
            pass

    for f in sorted(SIGNAL_DIR.glob("signal_*.json")):
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            nucleus = data.get("nucleus", "").lower()
            if nucleus not in expected:
                continue

            # Check timestamp filter
            if since_dt:
                sig_time = datetime.fromisoformat(data.get("timestamp", ""))
                if sig_time < since_dt:
                    continue

            # Keep latest signal per nucleus
            if nucleus not in found or f.stat().st_mtime > found[nucleus]["_mtime"]:
                found[nucleus] = {**data, "_file": str(f), "_mtime": f.stat().st_mtime}
        except (json.JSONDecodeError, KeyError, ValueError):
            continue

    return found


def log(msg: str, quiet: bool = False):
    if not quiet:
        ts = datetime.now().strftime("%H:%M:%S")
        safe = str(msg).encode("ascii", "replace").decode("ascii")
        # Progress goes to stderr so stdout stays clean for JSON
        print(f"[{ts}] [WATCH] {safe}", file=sys.stderr, flush=True)


def main():
    args = parse_args()
    expected = set(n.strip().lower() for n in args.expect.split(","))
    start_time = time.time()
    dispatch_ts = args.since or datetime.now(timezone.utc).isoformat()

    # If no --since, use NOW as the baseline (signals before dispatch don't count)
    # But give 5 seconds grace for signals written just before watch started
    if not args.since:
        grace = datetime.fromtimestamp(start_time - 5, tz=timezone.utc).isoformat()
        dispatch_ts = grace

    pids = load_pids(args.pid_file)

    log(f"Watching for: {', '.join(sorted(expected))}", args.quiet)
    log(f"Timeout: {args.timeout}s | Poll: {args.poll}s", args.quiet)
    if pids:
        log(f"PIDs: {pids}", args.quiet)

    result = {
        "mission": args.mission,
        "expected": sorted(expected),
        "status": "watching",
        "nuclei": {},
        "start_time": datetime.now(timezone.utc).isoformat(),
    }

    while True:
        elapsed = time.time() - start_time

        # Check timeout
        if elapsed > args.timeout:
            result["status"] = "timeout"
            log(f"TIMEOUT after {int(elapsed)}s", args.quiet)
            break

        # Scan signals
        signals = find_signals(expected, dispatch_ts)
        received = set(signals.keys())
        pending = expected - received

        # Update result
        for nucleus in expected:
            if nucleus in signals:
                sig = signals[nucleus]
                result["nuclei"][nucleus] = {
                    "status": sig.get("status", "complete"),
                    "quality": sig.get("quality_score", 0),
                    "timestamp": sig.get("timestamp", ""),
                }
            else:
                # Check if process is alive
                pid = pids.get(nucleus)
                alive = is_pid_alive(pid) if pid else None
                result["nuclei"][nucleus] = {
                    "status": "working" if alive else ("crashed" if alive is False else "unknown"),
                    "pid": pid,
                    "alive": alive,
                }

        # Report progress
        log(
            f"{len(received)}/{len(expected)} signals | "
            f"Done: {', '.join(sorted(received)) or '--'} | "
            f"Pending: {', '.join(sorted(pending)) or '--'} | "
            f"{int(elapsed)}s elapsed",
            args.quiet
        )

        # Check for crashes (process dead + no signal)
        for nucleus in pending:
            pid = pids.get(nucleus)
            if pid and not is_pid_alive(pid):
                log(f"WARN: {nucleus.upper()} CRASHED (PID:{pid} dead, no signal)", args.quiet)
                result["nuclei"][nucleus] = {"status": "crashed", "pid": pid, "alive": False}

        # All received?
        if received >= expected:
            result["status"] = "complete"
            log(f"ALL DONE: {len(expected)} nuclei signaled complete!", args.quiet)
            break

        # All pending are crashed?
        crashed = {n for n in pending if result.get("nuclei", {}).get(n, {}).get("status") == "crashed"}
        if crashed and crashed == pending:
            result["status"] = "all_pending_crashed"
            log(f"FATAL: All pending nuclei crashed: {crashed}", args.quiet)
            break

        # Sleep
        time.sleep(args.poll)

    # Final summary
    result["end_time"] = datetime.now(timezone.utc).isoformat()
    result["duration_seconds"] = int(time.time() - start_time)

    # Write summary to file
    summary_path = ROOT / ".cex" / "runtime" / "grid_status.json"
    summary_path.parent.mkdir(parents=True, exist_ok=True)
    summary_path.write_text(json.dumps(result, indent=2), encoding="utf-8")

    # Output JSON to stdout (logs went to stderr via log())
    # Marker so mission_runner can find the JSON block
    print("---JSON_START---")
    print(json.dumps(result, indent=2))
    print("---JSON_END---")

    # Exit code
    if result["status"] == "complete":
        sys.exit(0)
    elif result["status"] == "timeout":
        sys.exit(1)
    else:
        sys.exit(2)


if __name__ == "__main__":
    main()
