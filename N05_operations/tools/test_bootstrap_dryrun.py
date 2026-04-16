#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Bootstrap Pre-Flight Dry-Run v1.0

Automated validation of all overnight bootstrap infrastructure.
Run before any overnight session to verify components work end-to-end.

Usage:
    python N05_operations/scripts/test_bootstrap_dryrun.py
    python N05_operations/scripts/test_bootstrap_dryrun.py --verbose
    python N05_operations/scripts/test_bootstrap_dryrun.py --json

Exit codes:
    0 = all checks passed (GO)
    1 = blockers found (NO-GO)
    2 = warnings only (GO with caution)
"""

import argparse
import json
import os
import re
import shutil
import sys
import tempfile
import threading
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / "_tools"))


class PreFlightRunner:
    """Runs all 6 pre-flight checks and collects results."""

    def __init__(self, verbose: bool = False):
        self.verbose = verbose
        self.results = []
        self.blockers = 0
        self.warnings = 0
        self.passed = 0

    def _record(self, check_id: str, name: str, status: str, detail: str = ""):
        """Record a check result."""
        entry = {"id": check_id, "name": name, "status": status, "detail": detail}
        self.results.append(entry)
        if status == "PASS":
            self.passed += 1
        elif status == "FAIL":
            self.blockers += 1
        elif status == "WARN":
            self.warnings += 1
        if self.verbose or status != "PASS":
            tag = "[PASS]" if status == "PASS" else ("[FAIL]" if status == "FAIL" else "[WARN]")
            print(f"  {tag} {check_id}: {detail or name}")

    def check_mission_state(self):
        """Check 1: mission_state.py checkpoint/resume."""
        print("\n[1/6] mission_state.py -- checkpoint/resume")
        test_dir = Path(tempfile.mkdtemp())
        try:
            from cex_mission_state import MissionState, Status

            # Create, start, checkpoint
            ms = MissionState("DRYRUN_TEST", state_dir=test_dir)
            ms.start(total_waves=2)
            ms.start_wave(1, ["n01", "n03"])
            ms.task_running(1, "n01")
            ms.task_complete(1, "n01", quality=9.0)
            ms.task_running(1, "n03")
            ms.task_complete(1, "n03", quality=8.5)
            ms.finish_wave(1)
            self._record("1a", "Create and checkpoint", "PASS", "Mission created, wave 1 done")

            # Simulate crash mid-wave-2
            ms.start_wave(2, ["n02", "n04"])
            ms.task_running(2, "n02")
            ms.wave_watching(2)

            # Reload from disk
            ms2 = MissionState("DRYRUN_TEST", state_dir=test_dir)
            if ms2.status != "running":
                self._record("1b", "Persist to disk", "FAIL", f"Status={ms2.status}, expected running")
                return
            self._record("1b", "Persist to disk", "PASS", "State survives reload")

            # Recovery point
            rp = ms2.get_recovery_point()
            if not rp or rp["wave_num"] != 2:
                self._record("1c", "Recovery point", "FAIL", f"Recovery={rp}")
                return
            if "n02" not in rp["pending_nuclei"] and "n04" not in rp["pending_nuclei"]:
                self._record("1c", "Recovery point", "FAIL", f"Pending={rp['pending_nuclei']}")
                return
            self._record("1c", "Recovery point", "PASS",
                         f"wave={rp['wave_num']}, pending={rp['pending_nuclei']}")

            # Resume and complete
            ms2.task_complete(2, "n02", quality=9.1)
            ms2.task_complete(2, "n04", quality=8.8)
            ms2.finish_wave(2)
            ms2.finish()
            if ms2.status != "complete":
                self._record("1d", "Resume and complete", "FAIL", f"Status={ms2.status}")
                return
            self._record("1d", "Resume and complete", "PASS",
                         f"Mean quality={ms2.summary()['quality']['mean']}")

        except Exception as e:
            self._record("1x", "mission_state.py", "FAIL", str(e))
        finally:
            shutil.rmtree(test_dir, ignore_errors=True)

    def check_continuous(self):
        """Check 2: cex_continuous.py scanning."""
        print("\n[2/6] cex_continuous.py -- handoff scanning")
        try:
            from cex_continuous import scan_handoffs, HANDOFF_DIR

            if not HANDOFF_DIR.exists():
                self._record("2a", "Handoff dir exists", "WARN", "No handoff dir")
                return

            tasks = scan_handoffs()
            self._record("2a", "Scanner runs", "PASS", f"Found {len(tasks)} handoff(s)")

            # Filter test
            filtered = scan_handoffs(filter_nuclei={"n99_nonexistent"})
            if len(filtered) == 0:
                self._record("2b", "Filter works", "PASS", "Non-matching filter returns 0")
            else:
                self._record("2b", "Filter works", "FAIL", f"Filter returned {len(filtered)}")

        except Exception as e:
            self._record("2x", "cex_continuous.py", "FAIL", str(e))

    def check_overnight_cmd(self):
        """Check 3: overnight_infinite.cmd validation."""
        print("\n[3/6] overnight_infinite.cmd -- syntax and paths")
        cmd_file = ROOT / "boot" / "overnight_infinite.cmd"

        if not cmd_file.exists():
            self._record("3a", "File exists", "FAIL", "overnight_infinite.cmd not found")
            return

        content = cmd_file.read_text(encoding="utf-8")
        self._record("3a", "File exists", "PASS", f"{len(content)} chars")

        # Loop structure
        has_loop = ":loop" in content and "goto loop" in content
        self._record("3b", "Loop structure", "PASS" if has_loop else "FAIL",
                     "label + goto present" if has_loop else "Missing loop")

        # Claude CLI
        has_claude = "claude" in content
        self._record("3c", "Claude CLI", "PASS" if has_claude else "FAIL",
                     "claude command found" if has_claude else "No claude command")

        # Session continuity
        has_continue = "--continue" in content or "--fork-session" in content
        self._record("3d", "Session continuity", "PASS" if has_continue else "WARN",
                     "Has --continue/--fork-session" if has_continue else "No session resume flag")

        # Referenced file paths
        ref_paths = ["N07_admin/agent_card_n07.md", ".cex/config/context_self_select.md"]
        missing = [p for p in ref_paths if not (ROOT / p).exists()]
        if missing:
            self._record("3e", "Referenced paths", "FAIL", f"Missing: {missing}")
        else:
            self._record("3e", "Referenced paths", "PASS", f"All {len(ref_paths)} paths exist")

    def check_signal_watch(self):
        """Check 4: signal_watch.py detection."""
        print("\n[4/6] signal_watch.py -- signal detection")
        test_dir = Path(tempfile.mkdtemp())
        signal_dir = test_dir / "signals"
        signal_dir.mkdir()

        try:
            import cex_signal_watch as sw
            original_dir = sw.SIGNAL_DIR
            sw.SIGNAL_DIR = signal_dir

            # Empty scan
            result = sw.find_signals({"n01"}, "")
            self._record("4a", "Empty scan", "PASS" if len(result) == 0 else "FAIL",
                         "No signals = empty result")

            # Create and detect signals
            now = datetime.now(timezone.utc)
            for nuc, q in [("n01", 9.2), ("n03", 8.8)]:
                sig = {"nucleus": nuc, "status": "complete",
                       "quality_score": q, "timestamp": now.isoformat()}
                sf = signal_dir / f"signal_{nuc}_test.json"
                sf.write_text(json.dumps(sig), encoding="utf-8")

            result = sw.find_signals({"n01", "n03"}, "")
            if len(result) == 2:
                self._record("4b", "Signal detection", "PASS", "2/2 signals found")
            else:
                self._record("4b", "Signal detection", "FAIL", f"Found {len(result)}/2")

            # Timestamp filter
            future = (now + timedelta(hours=1)).isoformat()
            filtered = sw.find_signals({"n01"}, future)
            self._record("4c", "Timestamp filter", "PASS" if len(filtered) == 0 else "FAIL",
                         "Future baseline correctly filters")

            # PID alive check
            alive = sw.is_pid_alive(os.getpid())
            self._record("4d", "PID alive check", "PASS" if alive else "FAIL",
                         f"Own PID alive={alive}")

            sw.SIGNAL_DIR = original_dir

        except Exception as e:
            self._record("4x", "signal_watch.py", "FAIL", str(e))
        finally:
            shutil.rmtree(test_dir, ignore_errors=True)

    def check_dispatch(self):
        """Check 5: dispatch.sh + PID format."""
        print("\n[5/6] dispatch.sh -- PID format and session awareness")
        dispatch = ROOT / "_spawn" / "dispatch.sh"
        grid_ps1 = ROOT / "_spawn" / "spawn_grid.ps1"
        stop_ps1 = ROOT / "_spawn" / "spawn_stop.ps1"

        if not dispatch.exists():
            self._record("5a", "dispatch.sh exists", "FAIL", "Not found")
            return
        self._record("5a", "dispatch.sh exists", "PASS")

        content = dispatch.read_text(encoding="utf-8")
        has_session = "CEX_SESSION_ID" in content
        self._record("5b", "Session ID mgmt", "PASS" if has_session else "FAIL",
                     "CEX_SESSION_ID handling present" if has_session else "Missing")

        if grid_ps1.exists():
            grid_content = grid_ps1.read_text(encoding="utf-8")
            has_pid_write = "spawn_pids.txt" in grid_content
            self._record("5c", "PID file write", "PASS" if has_pid_write else "FAIL")
        else:
            self._record("5c", "spawn_grid.ps1", "FAIL", "Not found")

        self._record("5d", "spawn_stop.ps1", "PASS" if stop_ps1.exists() else "FAIL",
                     "Exists" if stop_ps1.exists() else "Not found")

        # PID path consistency
        try:
            from cex_signal_watch import PID_FILE
            pid_path = str(PID_FILE).replace("\\", "/")
            if "spawn_pids.txt" in pid_path:
                self._record("5e", "PID path consistency", "PASS",
                             "signal_watch + spawn_grid use same path")
            else:
                self._record("5e", "PID path consistency", "WARN", f"Path: {pid_path}")
        except ImportError:
            self._record("5e", "PID path consistency", "WARN", "Could not import signal_watch")

    def check_lock(self):
        """Check 6: cex_lock.py concurrent access."""
        print("\n[6/6] cex_lock.py -- file locking")
        test_dir = Path(tempfile.mkdtemp())

        try:
            from cex_lock import CexLock, clean_stale

            # Basic acquire/release
            lk = CexLock("dryrun_lock", owner="n05", lock_dir=test_dir)
            acquired = lk.acquire()
            if not acquired:
                self._record("6a", "Basic acquire", "FAIL", "Could not acquire")
                return
            lk.release()
            self._record("6a", "Acquire/release", "PASS")

            # Double acquire blocks
            lk1 = CexLock("dryrun_double", owner="n01", timeout=1, lock_dir=test_dir)
            lk2 = CexLock("dryrun_double", owner="n03", timeout=1, lock_dir=test_dir)
            lk1.acquire()
            blocked = not lk2.acquire()
            lk1.release()
            self._record("6b", "Double acquire blocked",
                         "PASS" if blocked else "FAIL",
                         "Second acquire correctly timed out" if blocked else "RACE CONDITION")

            # Context manager
            try:
                with CexLock("dryrun_ctx", owner="n05", lock_dir=test_dir):
                    pass
                self._record("6c", "Context manager", "PASS")
            except TimeoutError:
                self._record("6c", "Context manager", "FAIL", "Could not acquire in context")

            # Stale detection
            stale = CexLock("dryrun_stale", owner="old", ttl=1, lock_dir=test_dir)
            stale.acquire()
            data = json.loads(stale.lock_file.read_text(encoding="utf-8"))
            data["acquired_at"] = "2020-01-01T00:00:00+00:00"
            data["pid"] = 99999
            stale.lock_file.write_text(json.dumps(data), encoding="utf-8")
            fresh = CexLock("dryrun_stale", owner="new", ttl=1, lock_dir=test_dir)
            if fresh._is_stale():
                got = fresh.acquire()
                self._record("6d", "Stale detection", "PASS" if got else "FAIL",
                             "Stale lock cleared and re-acquired")
                fresh.release()
            else:
                self._record("6d", "Stale detection", "FAIL", "Did not detect stale lock")

        except Exception as e:
            self._record("6x", "cex_lock.py", "FAIL", str(e))
        finally:
            shutil.rmtree(test_dir, ignore_errors=True)

    def run_all(self) -> dict:
        """Run all 6 checks."""
        print("=" * 60)
        print("CEX BOOTSTRAP PRE-FLIGHT VALIDATION")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("=" * 60)

        self.check_mission_state()
        self.check_continuous()
        self.check_overnight_cmd()
        self.check_signal_watch()
        self.check_dispatch()
        self.check_lock()

        # Summary
        total = self.passed + self.blockers + self.warnings
        print("\n" + "=" * 60)
        print(f"RESULTS: {self.passed}/{total} PASS | {self.blockers} FAIL | {self.warnings} WARN")

        if self.blockers > 0:
            verdict = "NO-GO"
            code = 1
        elif self.warnings > 0:
            verdict = "GO (with caution)"
            code = 2
        else:
            verdict = "GO"
            code = 0

        print(f"VERDICT: {verdict}")
        print("=" * 60)

        return {
            "verdict": verdict,
            "exit_code": code,
            "passed": self.passed,
            "failed": self.blockers,
            "warnings": self.warnings,
            "total": total,
            "checks": self.results,
            "timestamp": datetime.now(timezone.utc).isoformat(),
        }


def main():
    p = argparse.ArgumentParser(description="CEX Bootstrap Pre-Flight Dry-Run")
    p.add_argument("--verbose", "-v", action="store_true", help="Show all results including PASS")
    p.add_argument("--json", action="store_true", help="Output JSON summary")
    args = p.parse_args()

    runner = PreFlightRunner(verbose=args.verbose)
    summary = runner.run_all()

    if args.json:
        print(json.dumps(summary, indent=2))

    sys.exit(summary["exit_code"])


if __name__ == "__main__":
    main()
