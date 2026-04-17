#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Mission State v1.0 -- Persistent, crash-recoverable mission state tracking.

Tracks mission lifecycle: waves, tasks, quality gates, timing.
State persists to disk after every mutation (crash-safe).
Integrates with cex_lock.py for atomic writes.

States:
  PENDING -> RUNNING -> COMPLETE | FAILED | TIMED_OUT
  Wave: PENDING -> DISPATCHED -> WATCHING -> GATING -> DONE | FAILED
  Task: PENDING -> RUNNING -> COMPLETE | FAILED | CRASHED

Recovery:
  On startup, reads state file. If a wave was DISPATCHED/WATCHING,
  it resumes from that wave (re-polls signals, doesn't re-dispatch).

Usage:
    from cex_mission_state import MissionState

    ms = MissionState("FULLGRID_20260406")
    ms.start_wave(1, ["n01", "n03", "n05"])
    ms.task_complete("n01", quality=9.2)
    ms.task_failed("n03", reason="timeout")
    ms.finish_wave(1)
    ms.save()  # also called automatically on every mutation

CLI:
    python _tools/cex_mission_state.py --mission FULLGRID --status
    python _tools/cex_mission_state.py --mission FULLGRID --history
    python _tools/cex_mission_state.py --list
    python _tools/cex_mission_state.py --mission FULLGRID --recover
"""

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from enum import Enum
from pathlib import Path
from typing import Any, Optional

ROOT = Path(__file__).resolve().parent.parent
STATE_DIR = ROOT / ".cex" / "runtime" / "mission_state"

sys.path.insert(0, str(ROOT / "_tools"))


class Status(str, Enum):
    PENDING = "pending"
    RUNNING = "running"
    DISPATCHED = "dispatched"
    WATCHING = "watching"
    GATING = "gating"
    COMPLETE = "complete"
    FAILED = "failed"
    CRASHED = "crashed"
    TIMED_OUT = "timed_out"
    DONE = "done"


class MissionState:
    """Persistent mission state with automatic disk flush.

    State file: .cex/runtime/mission_state/{mission_id}.json
    Every mutating method calls _flush() to persist immediately.
    """

    def __init__(self, mission_id: str, state_dir: Path = STATE_DIR):
        self.mission_id = mission_id
        self.state_dir = Path(state_dir)
        self.state_file = self.state_dir / f"{mission_id}.json"
        self._state = self._load_or_create()

    def _load_or_create(self) -> dict:
        """Load existing state or create fresh."""
        if self.state_file.exists():
            try:
                data = json.loads(self.state_file.read_text(encoding="utf-8"))
                return data
            except (json.JSONDecodeError, OSError):
                pass
        return {
            "mission_id": self.mission_id,
            "status": Status.PENDING.value,
            "created_at": _now(),
            "updated_at": _now(),
            "started_at": None,
            "finished_at": None,
            "total_duration_s": 0,
            "current_wave": 0,
            "total_waves": 0,
            "waves": {},
            "events": [],
            "retries": 0,
            "quality_summary": {},
        }

    def _flush(self):
        """Persist state to disk atomically (write-to-temp + rename)."""
        self._state["updated_at"] = _now()
        self.state_dir.mkdir(parents=True, exist_ok=True)
        tmp = self.state_file.with_suffix(".tmp")
        tmp.write_text(json.dumps(self._state, indent=2, default=str), encoding="utf-8")
        # Atomic rename (on Windows, need to remove dst first)
        if sys.platform == "win32" and self.state_file.exists():
            self.state_file.unlink()
        tmp.rename(self.state_file)

    def _event(self, event_type: str, detail: str = "", **extra):
        """Append an event to the log."""
        ev = {"type": event_type, "at": _now(), "detail": detail, **extra}
        self._state["events"].append(ev)
        # Cap events at 500 to prevent unbounded growth
        if len(self._state["events"]) > 500:
            self._state["events"] = self._state["events"][-500:]

    # ------------------------------------------------------------------
    # Mission lifecycle
    # ------------------------------------------------------------------

    def start(self, total_waves: int = 0) -> None:
        """Mark mission as running."""
        self._state["status"] = Status.RUNNING.value
        self._state["started_at"] = _now()
        self._state["total_waves"] = total_waves
        self._event("mission_start", f"total_waves={total_waves}")
        self._flush()

    def finish(self, status: Status = Status.COMPLETE) -> None:
        """Mark mission as finished (COMPLETE, FAILED, TIMED_OUT)."""
        self._state["status"] = status.value
        self._state["finished_at"] = _now()
        if self._state["started_at"]:
            started = datetime.fromisoformat(self._state["started_at"])
            finished = datetime.fromisoformat(self._state["finished_at"])
            self._state["total_duration_s"] = round((finished - started).total_seconds(), 1)
        self._compute_quality_summary()
        self._event("mission_finish", f"status={status.value}")
        self._flush()

    @property
    def status(self) -> str:
        return self._state["status"]

    @property
    def current_wave(self) -> int:
        return self._state["current_wave"]

    @property
    def is_recoverable(self) -> bool:
        """True if mission was interrupted mid-wave and can be resumed."""
        s = self._state["status"]
        if s in (Status.COMPLETE.value, Status.FAILED.value):
            return False
        # Check if any wave is in a mid-state
        for wid, wave in self._state["waves"].items():
            if wave["status"] in (Status.DISPATCHED.value, Status.WATCHING.value, Status.RUNNING.value):
                return True
        return s == Status.RUNNING.value

    # ------------------------------------------------------------------
    # Wave lifecycle
    # ------------------------------------------------------------------

    def start_wave(self, wave_num: int, nuclei: list[str]) -> None:
        """Mark a wave as started with its nucleus assignments."""
        wid = str(wave_num)
        self._state["waves"][wid] = {
            "wave": wave_num,
            "status": Status.DISPATCHED.value,
            "nuclei": {n: {"status": Status.PENDING.value, "quality": None, "duration_s": 0} for n in nuclei},
            "started_at": _now(),
            "finished_at": None,
            "duration_s": 0,
        }
        self._state["current_wave"] = wave_num
        self._event("wave_start", f"wave={wave_num}, nuclei={nuclei}")
        self._flush()

    def wave_watching(self, wave_num: int) -> None:
        """Mark wave as in signal-watching state."""
        wid = str(wave_num)
        if wid in self._state["waves"]:
            self._state["waves"][wid]["status"] = Status.WATCHING.value
            self._event("wave_watching", f"wave={wave_num}")
            self._flush()

    def wave_gating(self, wave_num: int) -> None:
        """Mark wave as in quality-gate state."""
        wid = str(wave_num)
        if wid in self._state["waves"]:
            self._state["waves"][wid]["status"] = Status.GATING.value
            self._event("wave_gating", f"wave={wave_num}")
            self._flush()

    def finish_wave(self, wave_num: int, status: Status = Status.DONE) -> None:
        """Mark wave as finished."""
        wid = str(wave_num)
        if wid in self._state["waves"]:
            wave = self._state["waves"][wid]
            wave["status"] = status.value
            wave["finished_at"] = _now()
            if wave.get("started_at"):
                started = datetime.fromisoformat(wave["started_at"])
                finished = datetime.fromisoformat(wave["finished_at"])
                wave["duration_s"] = round((finished - started).total_seconds(), 1)
            self._event("wave_finish", f"wave={wave_num}, status={status.value}")
            self._flush()

    def get_wave(self, wave_num: int) -> dict[str, Any]:
        """Get wave state. Empty dict if not found."""
        return self._state["waves"].get(str(wave_num), {})

    # ------------------------------------------------------------------
    # Task (nucleus within a wave) lifecycle
    # ------------------------------------------------------------------

    def task_running(self, wave_num: int, nucleus: str) -> None:
        """Mark a task within a wave as running."""
        wid = str(wave_num)
        wave = self._state["waves"].get(wid)
        if wave and nucleus in wave["nuclei"]:
            wave["nuclei"][nucleus]["status"] = Status.RUNNING.value
            wave["nuclei"][nucleus]["started_at"] = _now()
            self._flush()

    def task_complete(
        self,
        wave_num: int,
        nucleus: str,
        quality: float = 0.0,
        output: str = "",
    ) -> None:
        """Mark a task as complete with quality score."""
        wid = str(wave_num)
        wave = self._state["waves"].get(wid)
        if wave and nucleus in wave["nuclei"]:
            task = wave["nuclei"][nucleus]
            task["status"] = Status.COMPLETE.value
            task["quality"] = quality
            task["output"] = output
            task["finished_at"] = _now()
            if task.get("started_at"):
                started = datetime.fromisoformat(task["started_at"])
                finished = datetime.fromisoformat(task["finished_at"])
                task["duration_s"] = round((finished - started).total_seconds(), 1)
            self._event("task_complete", f"wave={wave_num}, nucleus={nucleus}, quality={quality}")
            self._flush()

    def task_failed(self, wave_num: int, nucleus: str, reason: str = "") -> None:
        """Mark a task as failed."""
        wid = str(wave_num)
        wave = self._state["waves"].get(wid)
        if wave and nucleus in wave["nuclei"]:
            task = wave["nuclei"][nucleus]
            task["status"] = Status.FAILED.value
            task["reason"] = reason
            task["finished_at"] = _now()
            self._event("task_failed", f"wave={wave_num}, nucleus={nucleus}, reason={reason}")
            self._flush()

    def task_crashed(self, wave_num: int, nucleus: str) -> None:
        """Mark a task as crashed (process died without signaling)."""
        wid = str(wave_num)
        wave = self._state["waves"].get(wid)
        if wave and nucleus in wave["nuclei"]:
            task = wave["nuclei"][nucleus]
            task["status"] = Status.CRASHED.value
            task["finished_at"] = _now()
            self._event("task_crashed", f"wave={wave_num}, nucleus={nucleus}")
            self._flush()

    # ------------------------------------------------------------------
    # Recovery
    # ------------------------------------------------------------------

    def get_recovery_point(self) -> Optional[dict[str, Any]]:
        """Find where to resume after a crash.

        Returns dict with:
          wave_num: wave to resume
          pending_nuclei: nuclei that didn't complete
          phase: 'dispatch' or 'watch' (what to resume doing)
        """
        if not self.is_recoverable:
            return None

        for wid in sorted(self._state["waves"].keys(), key=int):
            wave = self._state["waves"][wid]
            if wave["status"] in (Status.DISPATCHED.value, Status.WATCHING.value, Status.RUNNING.value):
                pending = [
                    n for n, t in wave["nuclei"].items()
                    if t["status"] not in (Status.COMPLETE.value, Status.DONE.value)
                ]
                phase = "watch" if wave["status"] == Status.WATCHING.value else "dispatch"
                return {
                    "wave_num": int(wid),
                    "pending_nuclei": pending,
                    "completed_nuclei": [
                        n for n, t in wave["nuclei"].items()
                        if t["status"] in (Status.COMPLETE.value, Status.DONE.value)
                    ],
                    "phase": phase,
                }
        return None

    # ------------------------------------------------------------------
    # Quality summary
    # ------------------------------------------------------------------

    def _compute_quality_summary(self):
        """Compute aggregate quality metrics."""
        scores = []
        for wave in self._state["waves"].values():
            for nucleus, task in wave.get("nuclei", {}).items():
                q = task.get("quality")
                if q is not None and q > 0:
                    scores.append(q)
        if scores:
            self._state["quality_summary"] = {
                "count": len(scores),
                "mean": round(sum(scores) / len(scores), 2),
                "min": round(min(scores), 2),
                "max": round(max(scores), 2),
                "below_8": sum(1 for s in scores if s < 8.0),
            }

    # ------------------------------------------------------------------
    # Accessors
    # ------------------------------------------------------------------

    def to_dict(self) -> dict[str, Any]:
        """Full state as dict."""
        return dict(self._state)

    def summary(self) -> dict[str, Any]:
        """Compact summary for logging / display."""
        waves_done = sum(
            1 for w in self._state["waves"].values()
            if w["status"] in (Status.DONE.value, Status.COMPLETE.value)
        )
        total = self._state["total_waves"] or len(self._state["waves"])
        return {
            "mission": self.mission_id,
            "status": self.status,
            "waves": f"{waves_done}/{total}",
            "current_wave": self.current_wave,
            "duration_s": self._state["total_duration_s"],
            "recoverable": self.is_recoverable,
            "quality": self._state.get("quality_summary", {}),
        }

    def save(self) -> None:
        """Explicit save (also called automatically on every mutation)."""
        self._flush()


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


# ======================================================================
# Multi-mission listing
# ======================================================================

def list_missions(state_dir: Path = STATE_DIR) -> list[dict[str, Any]]:
    """List all known mission states."""
    results = []
    if not state_dir.exists():
        return results
    for f in sorted(state_dir.glob("*.json")):
        if f.suffix == ".tmp":
            continue
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            results.append({
                "mission_id": data.get("mission_id", f.stem),
                "status": data.get("status", "?"),
                "waves": f"{len(data.get('waves', {}))}",
                "updated_at": data.get("updated_at", "?"),
                "duration_s": data.get("total_duration_s", 0),
            })
        except (json.JSONDecodeError, OSError):
            results.append({"mission_id": f.stem, "status": "corrupt"})
    return results


# ======================================================================
# CLI
# ======================================================================

def main() -> None:
    p = argparse.ArgumentParser(description="CEX Mission State Manager")
    p.add_argument("--mission", metavar="ID", help="Mission ID")
    p.add_argument("--status", action="store_true", help="Show mission status")
    p.add_argument("--history", action="store_true", help="Show event history")
    p.add_argument("--list", action="store_true", help="List all missions")
    p.add_argument("--recover", action="store_true", help="Show recovery point")
    p.add_argument("--json", action="store_true", help="JSON output")
    args = p.parse_args()

    if args.list:
        missions = list_missions()
        if not missions:
            print("No mission states found.")
        else:
            print(f"{len(missions)} mission(s):")
            for m in missions:
                print(f"  {m['mission_id']:<30} {m['status']:<12} waves={m['waves']} duration={m['duration_s']}s")
        return

    if not args.mission:
        p.print_help()
        return

    ms = MissionState(args.mission)

    if args.recover:
        rp = ms.get_recovery_point()
        if rp:
            print(f"RECOVERABLE: wave={rp['wave_num']}, phase={rp['phase']}")
            print(f"  Pending: {rp['pending_nuclei']}")
            print(f"  Done:    {rp['completed_nuclei']}")
        else:
            print(f"NOT RECOVERABLE: status={ms.status}")
        return

    if args.history:
        events = ms._state.get("events", [])
        if not events:
            print("No events recorded.")
        else:
            for ev in events[-50:]:  # Last 50
                print(f"  [{ev.get('at', '?')[:19]}] {ev.get('type', '?')}: {ev.get('detail', '')}")
        return

    # Default: status
    if args.json:
        print(json.dumps(ms.to_dict(), indent=2, default=str))
    else:
        s = ms.summary()
        print(f"Mission: {s['mission']}")
        print(f"Status:  {s['status']}")
        print(f"Waves:   {s['waves']} (current: {s['current_wave']})")
        print(f"Duration: {s['duration_s']}s")
        print(f"Recoverable: {s['recoverable']}")
        if s.get("quality"):
            q = s["quality"]
            print(f"Quality: mean={q.get('mean', '?')} min={q.get('min', '?')} max={q.get('max', '?')} below_8={q.get('below_8', 0)}")


if __name__ == "__main__":
    main()
