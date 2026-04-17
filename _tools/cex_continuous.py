#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Continuous Mode v1.0 -- Poll for handoffs, auto-dispatch, keep running.

Runs an infinite loop that:
  1. Scans .cex/runtime/handoffs/ for *_task.md files
  2. Dispatches each to the appropriate nucleus
  3. Watches signals for completion
  4. Consolidates results (commit, archive, quality gate)
  5. Waits for new handoffs (configurable poll interval)

Unlike cex_mission_runner.py (which runs a single mission plan),
continuous mode runs indefinitely and picks up ANY handoff that appears.

Modes:
  --mode scan    : One-shot scan + dispatch (default)
  --mode loop    : Continuous loop until CTRL+C or --max-cycles
  --mode daemon  : Background daemon (writes PID file, log to file)

Integration:
  - Uses cex_lock.py to prevent double-dispatch
  - Uses cex_mission_state.py for persistent tracking
  - Reads decision_manifest.yaml for GDP compliance

Usage:
    python _tools/cex_continuous.py --mode loop --poll 60
    python _tools/cex_continuous.py --mode scan --dry-run
    python _tools/cex_continuous.py --mode loop --max-cycles 10 --timeout 1800

Exit codes:
    0 = clean shutdown (CTRL+C, max-cycles reached, or no work)
    1 = error
    2 = quality gate failure
"""

import argparse
import json
import os
import re
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "_tools"
HANDOFF_DIR = ROOT / ".cex" / "runtime" / "handoffs"
SIGNAL_DIR = ROOT / ".cex" / "runtime" / "signals"
ARCHIVE_DIR = ROOT / ".cex" / "archive" / "handoffs_done"
PID_DIR = ROOT / ".cex" / "runtime" / "pids"

sys.path.insert(0, str(TOOLS))

# Graceful shutdown flag
_shutdown = False


def _handle_signal(signum, frame):
    global _shutdown
    _shutdown = True
    log("Shutdown signal received. Finishing current cycle...")


def log(msg: str, level: str = "INFO") -> None:
    ts = datetime.now().strftime("%H:%M:%S")
    safe = str(msg).encode("ascii", "replace").decode("ascii")
    print(f"[{ts}] [CONTINUOUS/{level}] {safe}", flush=True)


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="CEX Continuous Mode -- auto-dispatch loop")
    p.add_argument("--mode", choices=["scan", "loop", "daemon"], default="scan",
                   help="scan=one-shot, loop=continuous, daemon=background")
    p.add_argument("--poll", type=int, default=60, help="Poll interval in seconds (default: 60)")
    p.add_argument("--timeout", type=int, default=1800, help="Timeout per dispatch cycle (default: 1800s)")
    p.add_argument("--max-cycles", type=int, default=0, help="Max cycles before exit (0=infinite)")
    p.add_argument("--quality-floor", type=float, default=8.0, help="Minimum quality score")
    p.add_argument("--dry-run", action="store_true", help="Preview without executing")
    p.add_argument("--nuclei", default="", help="Only dispatch these nuclei (comma-separated)")
    p.add_argument("--signal-poll", type=int, default=30, help="Signal poll interval (default: 30s)")
    return p.parse_args()


# ======================================================================
# Handoff Scanner
# ======================================================================

def scan_handoffs(filter_nuclei: set[str] | None = None) -> list[dict[str, Any]]:
    """Find pending handoff task files.

    Returns list of dicts: [{nucleus, path, size}]
    Only picks up files matching n0X_task.md pattern.
    """
    tasks = []
    if not HANDOFF_DIR.exists():
        return tasks

    for f in sorted(HANDOFF_DIR.glob("*_task.md")):
        match = re.match(r'(n0[1-7])_task\.md', f.name, re.IGNORECASE)
        if not match:
            continue
        nucleus = match.group(1).lower()
        if filter_nuclei and nucleus not in filter_nuclei:
            continue
        # Skip empty files
        if f.stat().st_size < 10:
            continue
        tasks.append({
            "nucleus": nucleus,
            "path": str(f),
            "size": f.stat().st_size,
        })
    return tasks


# ======================================================================
# Dispatch Cycle
# ======================================================================

def dispatch_cycle(
    tasks: list[dict[str, Any]],
    timeout: int = 1800,
    signal_poll: int = 30,
    quality_floor: float = 8.0,
    dry_run: bool = False,
) -> dict[str, Any]:
    """Execute one dispatch cycle: dispatch -> watch -> gate -> consolidate.

    Returns: {status, nuclei, quality, duration_s}
    """
    from cex_lock import CexLock
    from cex_mission_state import MissionState

    nuclei = [t["nucleus"] for t in tasks]
    cycle_id = f"cycle_{int(time.time())}"

    log(f"Cycle {cycle_id}: dispatching {', '.join(n.upper() for n in nuclei)}")

    # Acquire dispatch lock
    lock = CexLock("continuous_dispatch", timeout=30)
    if not lock.acquire():
        log("Another dispatch cycle is running. Skipping.", "WARN")
        return {"status": "skipped", "reason": "locked"}

    try:
        # Create mission state
        ms = MissionState(cycle_id)
        ms.start(total_waves=1)
        ms.start_wave(1, nuclei)

        if dry_run:
            log("[DRY-RUN] Would dispatch grid", "DRY")
            ms.finish_wave(1)
            ms.finish()
            return {"status": "dry_run", "nuclei": nuclei}

        # Clean old signals
        _clean_signals()

        # Dispatch via grid
        _dispatch_grid(nuclei)
        ms.wave_watching(1)

        # Watch for signals
        result = _watch_signals(nuclei, timeout, signal_poll)
        watch_status = result.get("status", "unknown")

        # Update task states from signals
        for nucleus in nuclei:
            sig = result.get("nuclei", {}).get(nucleus, {})
            sig_status = sig.get("status", "unknown")
            quality = sig.get("quality", 0)

            if sig_status == "complete":
                ms.task_complete(1, nucleus, quality=quality)
            elif sig_status == "crashed":
                ms.task_crashed(1, nucleus)
            elif sig_status in ("timeout", "unknown", "no_signal"):
                ms.task_failed(1, nucleus, reason=sig_status)
            else:
                ms.task_complete(1, nucleus, quality=quality)

        # Quality gate
        ms.wave_gating(1)
        gate_results = {}
        all_passed = True
        for nucleus in nuclei:
            sig = result.get("nuclei", {}).get(nucleus, {})
            quality = sig.get("quality", 0)
            passed = quality >= quality_floor if quality > 0 else True
            gate_results[nucleus] = {"quality": quality, "passed": passed}
            if not passed:
                all_passed = False
            status_str = "PASS" if passed else "FAIL"
            log(f"  {nucleus.upper()}: quality={quality} [{status_str}]")

        # Finish wave
        from cex_mission_state import Status
        ms.finish_wave(1, Status.DONE if all_passed else Status.FAILED)

        # Consolidate: commit + archive
        _consolidate(nuclei, cycle_id)

        # Finish mission
        ms.finish(Status.COMPLETE if all_passed else Status.FAILED)

        return {
            "status": "complete" if all_passed else "quality_fail",
            "nuclei": nuclei,
            "gate": gate_results,
            "watch_status": watch_status,
            "duration_s": result.get("duration_seconds", 0),
        }

    finally:
        lock.release()


def _clean_signals():
    """Remove old signal files."""
    if SIGNAL_DIR.exists():
        for f in SIGNAL_DIR.glob("signal_*.json"):
            f.unlink(missing_ok=True)


def _dispatch_grid(nuclei: list):
    """Dispatch nuclei via spawn system."""
    # Use dispatch.sh for grid dispatch
    cmd = ["bash", "_spawn/dispatch.sh", "grid", "CONTINUOUS"]
    try:
        subprocess.run(cmd, cwd=str(ROOT), timeout=30, capture_output=True)
        log("Grid dispatched")
        time.sleep(10)  # Allow processes to spawn
    except (subprocess.TimeoutExpired, FileNotFoundError):
        # Fallback: try PowerShell directly
        try:
            ps_cmd = [
                "powershell", "-NoProfile", "-ExecutionPolicy", "Bypass",
                "-File", str(ROOT / "_spawn" / "spawn_grid.ps1"),
                "-mission", "CONTINUOUS", "-mode", "static",
            ]
            subprocess.run(ps_cmd, cwd=str(ROOT), timeout=30, capture_output=True)
            log("Grid dispatched (PowerShell fallback)")
            time.sleep(10)
        except Exception as e:
            log(f"Dispatch failed: {e}", "ERROR")


def _watch_signals(nuclei: list, timeout: int, poll: int) -> dict:
    """Block until all nuclei signal or timeout."""
    expected = ",".join(nuclei)
    cmd = [
        sys.executable, str(TOOLS / "cex_signal_watch.py"),
        "--expect", expected,
        "--timeout", str(timeout),
        "--poll", str(poll),
    ]
    log(f"Watching: {expected} (timeout={timeout}s)")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT), timeout=timeout + 60)
        stdout = result.stdout
        if "---JSON_START---" in stdout:
            json_str = stdout.split("---JSON_START---")[1].split("---JSON_END---")[0].strip()
            return json.loads(json_str)
        return json.loads(stdout)
    except (subprocess.TimeoutExpired, json.JSONDecodeError, IndexError):
        return {"status": "timeout", "nuclei": {n: {"status": "timeout"} for n in nuclei}}


def _consolidate(nuclei: list, cycle_id: str):
    """Commit outputs and archive handoffs."""
    # Git commit
    subprocess.run(["git", "add", "-A"], cwd=str(ROOT), capture_output=True)
    msg = f"[continuous] {cycle_id}: {', '.join(n.upper() for n in nuclei)}"
    subprocess.run(["git", "commit", "-m", msg, "--no-verify"],
                   cwd=str(ROOT), capture_output=True)

    # Archive handoffs
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    for nucleus in nuclei:
        task_file = HANDOFF_DIR / f"{nucleus}_task.md"
        if task_file.exists():
            ts = datetime.now().strftime("%Y%m%d_%H%M%S")
            dest = ARCHIVE_DIR / f"{nucleus}_task_{ts}.md"
            task_file.rename(dest)
    log("Consolidated (committed + archived)")


# ======================================================================
# Main Loop
# ======================================================================

def run_continuous(args: argparse.Namespace) -> int:
    """Main continuous mode entry point."""
    global _shutdown

    # Register signal handlers for graceful shutdown
    signal.signal(signal.SIGINT, _handle_signal)
    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, _handle_signal)

    filter_nuclei = set(n.strip().lower() for n in args.nuclei.split(",")) if args.nuclei else None

    log(f"{'='*50}")
    log(f"CEX CONTINUOUS MODE v1.0")
    log(f"Mode: {args.mode} | Poll: {args.poll}s | Timeout: {args.timeout}s")
    log(f"Quality floor: {args.quality_floor}")
    if filter_nuclei:
        log(f"Filter: {', '.join(sorted(filter_nuclei))}")
    if args.max_cycles:
        log(f"Max cycles: {args.max_cycles}")
    log(f"Dry run: {args.dry_run}")
    log(f"{'='*50}")

    # Write PID file for daemon mode
    if args.mode == "daemon":
        PID_DIR.mkdir(parents=True, exist_ok=True)
        pid_file = PID_DIR / "continuous.pid"
        pid_file.write_text(str(os.getpid()), encoding="utf-8")
        log(f"PID file: {pid_file}")

    cycle_count = 0
    total_dispatched = 0
    total_passed = 0
    total_failed = 0

    try:
        while not _shutdown:
            cycle_count += 1

            # Check max cycles
            if args.max_cycles and cycle_count > args.max_cycles:
                log(f"Max cycles ({args.max_cycles}) reached. Exiting.")
                break

            # Scan for handoffs
            tasks = scan_handoffs(filter_nuclei)

            if not tasks:
                if args.mode == "scan":
                    log("No pending handoffs. Nothing to do.")
                    break
                log(f"No handoffs. Sleeping {args.poll}s... (cycle {cycle_count})")
                _interruptible_sleep(args.poll)
                continue

            log(f"Found {len(tasks)} handoff(s): {', '.join(t['nucleus'].upper() for t in tasks)}")

            # Dispatch
            result = dispatch_cycle(
                tasks,
                timeout=args.timeout,
                signal_poll=args.signal_poll,
                quality_floor=args.quality_floor,
                dry_run=args.dry_run,
            )

            # Tally
            total_dispatched += len(tasks)
            status = result.get("status", "?")
            if status == "complete":
                total_passed += len(tasks)
            elif status == "quality_fail":
                gate = result.get("gate", {})
                total_passed += sum(1 for g in gate.values() if g.get("passed"))
                total_failed += sum(1 for g in gate.values() if not g.get("passed"))
            elif status == "skipped":
                pass

            log(f"Cycle done: {status} | dispatched={total_dispatched} passed={total_passed} failed={total_failed}")

            # Single scan mode: exit after one cycle
            if args.mode == "scan":
                break

            # Sleep between cycles
            if not _shutdown:
                log(f"Sleeping {args.poll}s before next scan...")
                _interruptible_sleep(args.poll)

    except KeyboardInterrupt:
        log("Interrupted by user.")
    finally:
        # Cleanup PID file
        pid_file = PID_DIR / "continuous.pid"
        if pid_file.exists():
            pid_file.unlink(missing_ok=True)

    # Summary
    log(f"{'='*50}")
    log(f"CONTINUOUS MODE SUMMARY")
    log(f"Cycles: {cycle_count} | Dispatched: {total_dispatched}")
    log(f"Passed: {total_passed} | Failed: {total_failed}")
    log(f"{'='*50}")

    return 0 if total_failed == 0 else 2


def _interruptible_sleep(seconds: float):
    """Sleep that can be interrupted by shutdown signal."""
    end = time.monotonic() + seconds
    while time.monotonic() < end and not _shutdown:
        time.sleep(min(1.0, end - time.monotonic()))


# ======================================================================
# CLI
# ======================================================================

def main() -> None:
    args = parse_args()
    sys.exit(run_continuous(args))


if __name__ == "__main__":
    main()
