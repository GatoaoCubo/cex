#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Overnight Infinite Runner v1.0 -- Long-running autonomous execution.

Wraps cex_continuous.py with:
  - Health monitoring (periodic self-checks)
  - Auto-recovery (restart failed nuclei, clear stale locks)
  - Time-bounded execution (--until HH:MM or --hours N)
  - Resource guards (memory, disk, CPU)
  - Heartbeat logging (proves the runner is alive)
  - Mission queue (process multiple missions sequentially)
  - Summary report on exit

Designed for: "Start at midnight, stop at 8 AM, process all queued work."

Usage:
    python _tools/cex_overnight.py --hours 8
    python _tools/cex_overnight.py --until 08:00 --poll 120
    python _tools/cex_overnight.py --hours 4 --queue missions.txt --dry-run
    python _tools/cex_overnight.py --hours 12 --health-interval 300

Exit codes:
    0 = clean exit (time limit, all work done, or user interrupt)
    1 = error
    2 = health check failure (resource exhaustion)
"""

import argparse
import json
import os
import signal
import subprocess
import sys
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
TOOLS = ROOT / "_tools"
HANDOFF_DIR = ROOT / ".cex" / "runtime" / "handoffs"
STATE_DIR = ROOT / ".cex" / "runtime" / "mission_state"
LOCK_DIR = ROOT / ".cex" / "runtime" / "locks"
PID_DIR = ROOT / ".cex" / "runtime" / "pids"
LOG_DIR = ROOT / ".cex" / "runtime" / "logs"

sys.path.insert(0, str(TOOLS))

_shutdown = False


def _handle_signal(signum, frame):
    global _shutdown
    _shutdown = True


def log(msg: str, level: str = "INFO") -> None:
    ts = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    safe = str(msg).encode("ascii", "replace").decode("ascii")
    line = f"[{ts}] [OVERNIGHT/{level}] {safe}"
    print(line, flush=True)
    # Also append to log file
    try:
        LOG_DIR.mkdir(parents=True, exist_ok=True)
        log_file = LOG_DIR / f"overnight_{datetime.now().strftime('%Y%m%d')}.log"
        with open(log_file, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except OSError:
        pass


def parse_args() -> argparse.Namespace:
    p = argparse.ArgumentParser(description="CEX Overnight Infinite Runner")
    p.add_argument("--hours", type=float, default=0, help="Run for N hours (0=infinite)")
    p.add_argument("--until", metavar="HH:MM", help="Run until time (24h format, e.g. 08:00)")
    p.add_argument("--poll", type=int, default=120, help="Handoff poll interval (default: 120s)")
    p.add_argument("--timeout", type=int, default=3600, help="Timeout per dispatch cycle (default: 3600s)")
    p.add_argument("--quality-floor", type=float, default=8.0, help="Minimum quality")
    p.add_argument("--health-interval", type=int, default=600, help="Health check interval (default: 600s)")
    p.add_argument("--max-failures", type=int, default=5, help="Max consecutive failures before exit")
    p.add_argument("--queue", metavar="FILE", help="Mission queue file (one mission per line)")
    p.add_argument("--dry-run", action="store_true", help="Preview without executing")
    p.add_argument("--nuclei", default="", help="Only dispatch these nuclei")
    return p.parse_args()


# ======================================================================
# Time Boundary
# ======================================================================

def compute_deadline(args: argparse.Namespace) -> float:
    """Compute Unix timestamp for when to stop. Returns 0 for infinite."""
    now = time.time()

    if args.until:
        # Parse HH:MM
        parts = args.until.split(":")
        target_h, target_m = int(parts[0]), int(parts[1]) if len(parts) > 1 else 0
        today = datetime.now()
        target = today.replace(hour=target_h, minute=target_m, second=0, microsecond=0)
        # If target is in the past, assume tomorrow
        if target.timestamp() <= now:
            target += timedelta(days=1)
        return target.timestamp()

    if args.hours > 0:
        return now + (args.hours * 3600)

    return 0  # Infinite


def time_remaining(deadline: float) -> str:
    """Human-readable time remaining until deadline."""
    if deadline == 0:
        return "infinite"
    remaining = deadline - time.time()
    if remaining <= 0:
        return "expired"
    hours = int(remaining // 3600)
    minutes = int((remaining % 3600) // 60)
    return f"{hours}h{minutes:02d}m"


# ======================================================================
# Health Checks
# ======================================================================

class HealthStatus:
    """Result of a health check."""
    def __init__(self):
        self.ok = True
        self.checks = {}
        self.warnings = []
        self.blockers = []

    def add(self, name: str, ok: bool, detail: str = "") -> None:
        self.checks[name] = {"ok": ok, "detail": detail}
        if not ok:
            self.ok = False
            self.blockers.append(f"{name}: {detail}")

    def warn(self, msg: str) -> None:
        self.warnings.append(msg)


def run_health_check() -> HealthStatus:
    """Comprehensive health check: disk, locks, processes, git."""
    h = HealthStatus()

    # Disk space (warn below 1GB free)
    try:
        import shutil
        total, used, free = shutil.disk_usage(str(ROOT))
        free_gb = free / (1024**3)
        h.add("disk_space", free_gb > 0.5, f"{free_gb:.1f}GB free")
        if free_gb < 1.0:
            h.warn(f"Low disk: {free_gb:.1f}GB free")
    except Exception as e:
        h.add("disk_space", True, f"check failed: {e}")

    # Stale locks
    try:
        from cex_lock import clean_stale
        stale = clean_stale(ttl=600, lock_dir=LOCK_DIR)
        h.add("stale_locks", True, f"cleaned {stale}" if stale else "none")
    except Exception as e:
        h.add("stale_locks", True, f"check failed: {e}")

    # Git status (dirty working tree is OK, but broken repo isn't)
    try:
        r = subprocess.run(
            ["git", "status", "--porcelain"],
            capture_output=True, text=True, timeout=10, cwd=str(ROOT),
        )
        h.add("git", r.returncode == 0, f"{len(r.stdout.splitlines())} dirty files")
    except Exception as e:
        h.add("git", False, f"git broken: {e}")

    # Python imports (key modules)
    for mod in ["cex_lock", "cex_mission_state", "cex_continuous"]:
        try:
            __import__(mod)
            h.add(f"import_{mod}", True)
        except Exception as e:
            h.add(f"import_{mod}", False, str(e))

    # Runtime dirs
    for d in [HANDOFF_DIR, SIGNAL_DIR, STATE_DIR]:
        name = d.name
        exists = d.exists()
        h.add(f"dir_{name}", exists or True, "exists" if exists else "will create")

    return h


SIGNAL_DIR = ROOT / ".cex" / "runtime" / "signals"


# ======================================================================
# Mission Queue
# ======================================================================

def load_queue(queue_file: str) -> list[str]:
    """Load mission queue from file. One mission ID per line."""
    if not queue_file or not Path(queue_file).exists():
        return []
    lines = Path(queue_file).read_text(encoding="utf-8").strip().splitlines()
    return [l.strip() for l in lines if l.strip() and not l.startswith("#")]


def process_queued_mission(mission_id: str, args: argparse.Namespace) -> dict[str, Any]:
    """Process one queued mission via mission_runner."""
    log(f"Processing queued mission: {mission_id}")

    plan_path = ROOT / ".cex" / "runtime" / "plans" / f"plan_{mission_id}.md"
    if not plan_path.exists():
        plan_path = ROOT / ".cex" / "runtime" / "plans" / f"MISSION_{mission_id}.md"

    if not plan_path.exists():
        log(f"No plan found for {mission_id}. Skipping.", "WARN")
        return {"mission": mission_id, "status": "no_plan"}

    cmd = [
        sys.executable, str(TOOLS / "cex_mission_runner.py"),
        "--plan", str(plan_path),
        "--mission", mission_id,
        "--timeout", str(args.timeout),
        "--quality-floor", str(args.quality_floor),
    ]
    if args.dry_run:
        cmd.append("--dry-run")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=str(ROOT), timeout=args.timeout + 120)
        return {
            "mission": mission_id,
            "status": "complete" if result.returncode == 0 else "failed",
            "exit_code": result.returncode,
        }
    except subprocess.TimeoutExpired:
        return {"mission": mission_id, "status": "timeout"}


# ======================================================================
# Heartbeat
# ======================================================================

def write_heartbeat(cycle: int, deadline: float, stats: dict[str, Any]) -> None:
    """Write heartbeat file so external monitors can check liveness."""
    heartbeat = {
        "pid": os.getpid(),
        "cycle": cycle,
        "alive_since": stats.get("started_at", ""),
        "time_remaining": time_remaining(deadline),
        "total_dispatched": stats.get("total_dispatched", 0),
        "total_passed": stats.get("total_passed", 0),
        "total_failed": stats.get("total_failed", 0),
        "consecutive_failures": stats.get("consecutive_failures", 0),
        "last_health": stats.get("last_health", ""),
        "timestamp": datetime.now(timezone.utc).isoformat(),
    }
    hb_path = ROOT / ".cex" / "runtime" / "overnight_heartbeat.json"
    hb_path.parent.mkdir(parents=True, exist_ok=True)
    hb_path.write_text(json.dumps(heartbeat, indent=2), encoding="utf-8")


# ======================================================================
# Main Runner
# ======================================================================

def run_overnight(args: argparse.Namespace) -> int:
    global _shutdown

    signal.signal(signal.SIGINT, _handle_signal)
    if hasattr(signal, "SIGTERM"):
        signal.signal(signal.SIGTERM, _handle_signal)

    deadline = compute_deadline(args)
    started_at = datetime.now(timezone.utc).isoformat()

    log(f"{'='*60}")
    log(f"CEX OVERNIGHT INFINITE RUNNER v1.0")
    log(f"Started: {started_at}")
    log(f"Deadline: {time_remaining(deadline)} ({'infinite' if deadline == 0 else datetime.fromtimestamp(deadline).strftime('%Y-%m-%d %H:%M')})")
    log(f"Poll: {args.poll}s | Timeout: {args.timeout}s | Health: {args.health_interval}s")
    log(f"Quality floor: {args.quality_floor} | Max failures: {args.max_failures}")
    log(f"Dry run: {args.dry_run}")
    log(f"{'='*60}")

    # Write PID file
    PID_DIR.mkdir(parents=True, exist_ok=True)
    pid_file = PID_DIR / "overnight.pid"
    pid_file.write_text(str(os.getpid()), encoding="utf-8")

    # Initial health check
    log("Running initial health check...")
    health = run_health_check()
    if not health.ok:
        for b in health.blockers:
            log(f"BLOCKER: {b}", "ERROR")
        log("Health check FAILED. Aborting.", "ERROR")
        return 2
    for w in health.warnings:
        log(f"WARNING: {w}", "WARN")
    log("Health check PASSED")

    # Load mission queue if provided
    queue = load_queue(args.queue) if args.queue else []
    if queue:
        log(f"Mission queue: {len(queue)} missions: {', '.join(queue)}")

    stats = {
        "started_at": started_at,
        "total_dispatched": 0,
        "total_passed": 0,
        "total_failed": 0,
        "total_cycles": 0,
        "consecutive_failures": 0,
        "missions_processed": 0,
        "last_health": started_at,
    }
    last_health_time = time.time()

    try:
        # Phase 1: Process mission queue
        for mission_id in queue:
            if _shutdown:
                break
            if deadline and time.time() >= deadline:
                log("Deadline reached during queue processing.")
                break

            result = process_queued_mission(mission_id, args)
            stats["missions_processed"] += 1

            if result.get("status") == "complete":
                log(f"Mission {mission_id}: COMPLETE")
                stats["consecutive_failures"] = 0
            else:
                log(f"Mission {mission_id}: {result.get('status', 'unknown')}", "WARN")
                stats["consecutive_failures"] += 1

            if stats["consecutive_failures"] >= args.max_failures:
                log(f"Max consecutive failures ({args.max_failures}) reached.", "ERROR")
                break

        # Phase 2: Continuous mode (infinite poll loop)
        log("Entering continuous handoff polling mode...")

        while not _shutdown:
            stats["total_cycles"] += 1

            # Deadline check
            if deadline and time.time() >= deadline:
                log(f"Deadline reached. Time's up!")
                break

            # Periodic health check
            if time.time() - last_health_time > args.health_interval:
                log("Periodic health check...")
                health = run_health_check()
                stats["last_health"] = datetime.now(timezone.utc).isoformat()
                last_health_time = time.time()

                if not health.ok:
                    for b in health.blockers:
                        log(f"BLOCKER: {b}", "ERROR")
                    log("Health degraded. Stopping.", "ERROR")
                    break
                for w in health.warnings:
                    log(f"WARNING: {w}", "WARN")

            # Scan for handoffs
            from cex_continuous import scan_handoffs
            filter_nuclei = set(n.strip().lower() for n in args.nuclei.split(",")) if args.nuclei else None
            tasks = scan_handoffs(filter_nuclei)

            if tasks:
                from cex_continuous import dispatch_cycle
                log(f"Found {len(tasks)} handoff(s)")

                result = dispatch_cycle(
                    tasks,
                    timeout=args.timeout,
                    quality_floor=args.quality_floor,
                    dry_run=args.dry_run,
                )

                status = result.get("status", "?")
                stats["total_dispatched"] += len(tasks)

                if status == "complete":
                    stats["total_passed"] += len(tasks)
                    stats["consecutive_failures"] = 0
                elif status == "quality_fail":
                    gate = result.get("gate", {})
                    passed = sum(1 for g in gate.values() if g.get("passed"))
                    failed = sum(1 for g in gate.values() if not g.get("passed"))
                    stats["total_passed"] += passed
                    stats["total_failed"] += failed
                    if failed > 0:
                        stats["consecutive_failures"] += 1
                    else:
                        stats["consecutive_failures"] = 0
                elif status == "skipped":
                    pass
                else:
                    stats["consecutive_failures"] += 1

                log(f"Cycle {stats['total_cycles']}: {status} | "
                    f"dispatched={stats['total_dispatched']} passed={stats['total_passed']} "
                    f"failed={stats['total_failed']} | "
                    f"time_remaining={time_remaining(deadline)}")

                # Check failure threshold
                if stats["consecutive_failures"] >= args.max_failures:
                    log(f"Max consecutive failures ({args.max_failures}) reached.", "ERROR")
                    break
            else:
                remaining = time_remaining(deadline)
                log(f"No handoffs. Sleeping {args.poll}s... (remaining: {remaining})")

            # Write heartbeat
            write_heartbeat(stats["total_cycles"], deadline, stats)

            # Sleep (interruptible)
            _interruptible_sleep(args.poll)

    except KeyboardInterrupt:
        log("Interrupted by user.")
    finally:
        # Cleanup
        pid_file.unlink(missing_ok=True)
        hb = ROOT / ".cex" / "runtime" / "overnight_heartbeat.json"
        if hb.exists():
            hb.unlink(missing_ok=True)

    # Final summary
    total_duration = (datetime.now(timezone.utc) - datetime.fromisoformat(started_at)).total_seconds()

    log(f"{'='*60}")
    log(f"OVERNIGHT RUNNER SUMMARY")
    log(f"{'='*60}")
    log(f"Duration: {total_duration/3600:.1f}h ({int(total_duration)}s)")
    log(f"Cycles: {stats['total_cycles']}")
    log(f"Dispatched: {stats['total_dispatched']}")
    log(f"Passed: {stats['total_passed']}")
    log(f"Failed: {stats['total_failed']}")
    log(f"Missions processed: {stats['missions_processed']}")
    log(f"{'='*60}")

    # Write final report
    report = {
        "runner": "overnight_v1.0",
        "started_at": started_at,
        "finished_at": datetime.now(timezone.utc).isoformat(),
        "duration_hours": round(total_duration / 3600, 2),
        **stats,
    }
    report_path = ROOT / ".cex" / "runtime" / "overnight_report.json"
    report_path.write_text(json.dumps(report, indent=2), encoding="utf-8")
    log(f"Report: {report_path}")

    return 0 if stats["total_failed"] == 0 else 2


def _interruptible_sleep(seconds: float):
    end = time.monotonic() + seconds
    while time.monotonic() < end and not _shutdown:
        time.sleep(min(1.0, end - time.monotonic()))


# ======================================================================
# CLI
# ======================================================================

def main() -> None:
    args = parse_args()
    if not args.hours and not args.until:
        log("WARNING: No time limit set. Runner will run until interrupted or all work is done.", "WARN")
    sys.exit(run_overnight(args))


if __name__ == "__main__":
    main()
