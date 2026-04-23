#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for cex_mission_state.py -- persistent mission state tracking."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from cex_mission_state import MissionState, Status, list_missions

# ======================================================================
# Basic lifecycle
# ======================================================================

class TestMissionLifecycle:
    def test_create_new(self, tmp_path):
        ms = MissionState("TEST_001", state_dir=tmp_path)
        assert ms.status == "pending"
        assert ms.current_wave == 0

    def test_start_and_finish(self, tmp_path):
        ms = MissionState("TEST_002", state_dir=tmp_path)
        ms.start(total_waves=3)
        assert ms.status == "running"
        ms.finish(Status.COMPLETE)
        assert ms.status == "complete"
        assert ms._state["total_duration_s"] > 0 or ms._state["total_duration_s"] == 0

    def test_persists_to_disk(self, tmp_path):
        ms = MissionState("PERSIST", state_dir=tmp_path)
        ms.start(total_waves=2)
        # Verify file exists
        assert (tmp_path / "PERSIST.json").exists()
        # Load fresh instance
        ms2 = MissionState("PERSIST", state_dir=tmp_path)
        assert ms2.status == "running"

    def test_finish_failed(self, tmp_path):
        ms = MissionState("FAIL_TEST", state_dir=tmp_path)
        ms.start()
        ms.finish(Status.FAILED)
        assert ms.status == "failed"


# ======================================================================
# Wave lifecycle
# ======================================================================

class TestWaveLifecycle:
    def test_start_wave(self, tmp_path):
        ms = MissionState("WAVE_001", state_dir=tmp_path)
        ms.start(total_waves=2)
        ms.start_wave(1, ["n01", "n03", "n05"])
        assert ms.current_wave == 1
        wave = ms.get_wave(1)
        assert wave["status"] == "dispatched"
        assert "n01" in wave["nuclei"]
        assert "n03" in wave["nuclei"]
        assert "n05" in wave["nuclei"]

    def test_wave_transitions(self, tmp_path):
        ms = MissionState("WAVE_TRANS", state_dir=tmp_path)
        ms.start(total_waves=1)
        ms.start_wave(1, ["n01"])
        assert ms.get_wave(1)["status"] == "dispatched"
        ms.wave_watching(1)
        assert ms.get_wave(1)["status"] == "watching"
        ms.wave_gating(1)
        assert ms.get_wave(1)["status"] == "gating"
        ms.finish_wave(1)
        assert ms.get_wave(1)["status"] == "done"

    def test_wave_failure(self, tmp_path):
        ms = MissionState("WAVE_FAIL", state_dir=tmp_path)
        ms.start()
        ms.start_wave(1, ["n01"])
        ms.finish_wave(1, Status.FAILED)
        assert ms.get_wave(1)["status"] == "failed"

    def test_get_nonexistent_wave(self, tmp_path):
        ms = MissionState("NO_WAVE", state_dir=tmp_path)
        assert ms.get_wave(99) == {}

    def test_multiple_waves(self, tmp_path):
        ms = MissionState("MULTI_WAVE", state_dir=tmp_path)
        ms.start(total_waves=3)
        ms.start_wave(1, ["n01"])
        ms.finish_wave(1)
        ms.start_wave(2, ["n03", "n05"])
        ms.finish_wave(2)
        ms.start_wave(3, ["n02"])
        ms.finish_wave(3)
        assert ms.current_wave == 3
        assert len(ms._state["waves"]) == 3


# ======================================================================
# Task lifecycle
# ======================================================================

class TestTaskLifecycle:
    def test_task_complete(self, tmp_path):
        ms = MissionState("TASK_OK", state_dir=tmp_path)
        ms.start()
        ms.start_wave(1, ["n01", "n03"])
        ms.task_running(1, "n01")
        ms.task_complete(1, "n01", quality=9.5, output="output.md")
        task = ms.get_wave(1)["nuclei"]["n01"]
        assert task["status"] == "complete"
        assert task["quality"] == 9.5
        assert task["output"] == "output.md"

    def test_task_failed(self, tmp_path):
        ms = MissionState("TASK_FAIL", state_dir=tmp_path)
        ms.start()
        ms.start_wave(1, ["n03"])
        ms.task_failed(1, "n03", reason="timeout")
        task = ms.get_wave(1)["nuclei"]["n03"]
        assert task["status"] == "failed"
        assert task["reason"] == "timeout"

    def test_task_crashed(self, tmp_path):
        ms = MissionState("TASK_CRASH", state_dir=tmp_path)
        ms.start()
        ms.start_wave(1, ["n05"])
        ms.task_crashed(1, "n05")
        task = ms.get_wave(1)["nuclei"]["n05"]
        assert task["status"] == "crashed"

    def test_task_for_nonexistent_nucleus_ignored(self, tmp_path):
        ms = MissionState("TASK_GHOST", state_dir=tmp_path)
        ms.start()
        ms.start_wave(1, ["n01"])
        # Should not raise
        ms.task_complete(1, "n99", quality=9.0)
        assert "n99" not in ms.get_wave(1)["nuclei"]


# ======================================================================
# Recovery
# ======================================================================

class TestRecovery:
    def test_recoverable_dispatched(self, tmp_path):
        ms = MissionState("RECOVER_DISP", state_dir=tmp_path)
        ms.start(total_waves=2)
        ms.start_wave(1, ["n01", "n03"])
        ms.task_complete(1, "n01", quality=9.0)
        # n03 still pending, wave still dispatched
        assert ms.is_recoverable
        rp = ms.get_recovery_point()
        assert rp is not None
        assert rp["wave_num"] == 1
        assert "n03" in rp["pending_nuclei"]
        assert "n01" in rp["completed_nuclei"]
        assert rp["phase"] == "dispatch"

    def test_recoverable_watching(self, tmp_path):
        ms = MissionState("RECOVER_WATCH", state_dir=tmp_path)
        ms.start()
        ms.start_wave(1, ["n01", "n05"])
        ms.wave_watching(1)
        rp = ms.get_recovery_point()
        assert rp["phase"] == "watch"
        assert set(rp["pending_nuclei"]) == {"n01", "n05"}

    def test_not_recoverable_complete(self, tmp_path):
        ms = MissionState("NOT_RECOVER", state_dir=tmp_path)
        ms.start()
        ms.start_wave(1, ["n01"])
        ms.task_complete(1, "n01", quality=9.0)
        ms.finish_wave(1)
        ms.finish()
        assert not ms.is_recoverable
        assert ms.get_recovery_point() is None

    def test_not_recoverable_failed(self, tmp_path):
        ms = MissionState("FAILED_DONE", state_dir=tmp_path)
        ms.start()
        ms.finish(Status.FAILED)
        assert not ms.is_recoverable


# ======================================================================
# Events
# ======================================================================

class TestEvents:
    def test_events_recorded(self, tmp_path):
        ms = MissionState("EVENTS", state_dir=tmp_path)
        ms.start(total_waves=1)
        ms.start_wave(1, ["n01"])
        ms.task_complete(1, "n01", quality=9.0)
        ms.finish_wave(1)
        ms.finish()
        events = ms._state["events"]
        types = [e["type"] for e in events]
        assert "mission_start" in types
        assert "wave_start" in types
        assert "task_complete" in types
        assert "wave_finish" in types
        assert "mission_finish" in types

    def test_events_capped(self, tmp_path):
        ms = MissionState("CAP_EVENTS", state_dir=tmp_path)
        ms.start()
        for i in range(600):
            ms._event("spam", f"event_{i}")
        ms._flush()
        assert len(ms._state["events"]) <= 500


# ======================================================================
# Quality summary
# ======================================================================

class TestQualitySummary:
    def test_quality_computed(self, tmp_path):
        ms = MissionState("QUALITY", state_dir=tmp_path)
        ms.start()
        ms.start_wave(1, ["n01", "n03", "n05"])
        ms.task_complete(1, "n01", quality=9.0)
        ms.task_complete(1, "n03", quality=8.5)
        ms.task_complete(1, "n05", quality=7.0)
        ms.finish_wave(1)
        ms.finish()
        qs = ms._state["quality_summary"]
        assert qs["count"] == 3
        assert qs["mean"] == pytest.approx(8.17, abs=0.1)
        assert qs["min"] == 7.0
        assert qs["max"] == 9.0
        assert qs["below_8"] == 1


# ======================================================================
# Summary / dict
# ======================================================================

class TestAccessors:
    def test_summary(self, tmp_path):
        ms = MissionState("SUMMARY", state_dir=tmp_path)
        ms.start(total_waves=2)
        s = ms.summary()
        assert s["mission"] == "SUMMARY"
        assert s["status"] == "running"
        assert "0/2" in s["waves"]

    def test_to_dict(self, tmp_path):
        ms = MissionState("DICT", state_dir=tmp_path)
        d = ms.to_dict()
        assert isinstance(d, dict)
        assert d["mission_id"] == "DICT"

    def test_explicit_save(self, tmp_path):
        ms = MissionState("SAVE", state_dir=tmp_path)
        ms._state["status"] = "custom"
        ms.save()
        ms2 = MissionState("SAVE", state_dir=tmp_path)
        assert ms2.status == "custom"


# ======================================================================
# list_missions
# ======================================================================

class TestListMissions:
    def test_list_empty(self, tmp_path):
        assert list_missions(tmp_path) == []

    def test_list_multiple(self, tmp_path):
        MissionState("A", state_dir=tmp_path).start()
        MissionState("B", state_dir=tmp_path).start()
        missions = list_missions(tmp_path)
        assert len(missions) == 2
        ids = {m["mission_id"] for m in missions}
        assert ids == {"A", "B"}

    def test_list_handles_corrupt(self, tmp_path):
        (tmp_path / "corrupt.json").write_text("not json", encoding="utf-8")
        missions = list_missions(tmp_path)
        assert len(missions) == 1
        assert missions[0]["status"] == "corrupt"


# ======================================================================
# Atomic write (crash safety)
# ======================================================================

class TestAtomicWrite:
    def test_no_tmp_files_left(self, tmp_path):
        ms = MissionState("ATOMIC", state_dir=tmp_path)
        ms.start()
        ms.start_wave(1, ["n01"])
        ms.task_complete(1, "n01", quality=9.0)
        ms.finish_wave(1)
        ms.finish()
        tmp_files = list(tmp_path.glob("*.tmp"))
        assert len(tmp_files) == 0

    def test_file_valid_after_many_writes(self, tmp_path):
        ms = MissionState("MULTI_WRITE", state_dir=tmp_path)
        ms.start(total_waves=5)
        for i in range(1, 6):
            ms.start_wave(i, [f"n0{min(i,6)}"])
            ms.task_complete(i, f"n0{min(i,6)}", quality=8.0 + i * 0.2)
            ms.finish_wave(i)
        ms.finish()
        # Reload and verify
        ms2 = MissionState("MULTI_WRITE", state_dir=tmp_path)
        assert ms2.status == "complete"
        assert len(ms2._state["waves"]) == 5
