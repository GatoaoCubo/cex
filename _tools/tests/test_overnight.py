#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for cex_overnight.py -- overnight infinite runner."""

import json
import os
import sys
import time
from datetime import datetime, timedelta
from pathlib import Path
from types import SimpleNamespace

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from cex_overnight import (HealthStatus, compute_deadline, load_queue,
                           run_health_check, time_remaining, write_heartbeat)

# ======================================================================
# Time Boundary
# ======================================================================

class TestComputeDeadline:
    def test_hours(self):
        args = SimpleNamespace(hours=2, until=None)
        dl = compute_deadline(args)
        # Should be ~2 hours from now
        assert dl > time.time()
        assert dl < time.time() + 7201

    def test_until_future(self):
        # Pick a time 1 hour from now
        future = datetime.now() + timedelta(hours=1)
        hhmm = future.strftime("%H:%M")
        args = SimpleNamespace(hours=0, until=hhmm)
        dl = compute_deadline(args)
        assert dl > time.time()

    def test_infinite(self):
        args = SimpleNamespace(hours=0, until=None)
        dl = compute_deadline(args)
        assert dl == 0

    def test_zero_hours(self):
        args = SimpleNamespace(hours=0, until=None)
        dl = compute_deadline(args)
        assert dl == 0


class TestTimeRemaining:
    def test_infinite(self):
        assert time_remaining(0) == "infinite"

    def test_expired(self):
        assert time_remaining(time.time() - 100) == "expired"

    def test_format(self):
        dl = time.time() + 3700  # ~1h1m
        s = time_remaining(dl)
        assert "h" in s
        assert "m" in s


# ======================================================================
# Health Check
# ======================================================================

class TestHealthStatus:
    def test_healthy(self):
        h = HealthStatus()
        h.add("disk", True, "10GB free")
        h.add("git", True)
        assert h.ok
        assert len(h.blockers) == 0

    def test_blocker(self):
        h = HealthStatus()
        h.add("disk", False, "0.1GB free")
        assert not h.ok
        assert len(h.blockers) == 1

    def test_warning(self):
        h = HealthStatus()
        h.warn("Low memory")
        assert h.ok  # Warnings don't block
        assert len(h.warnings) == 1


class TestRunHealthCheck:
    def test_runs_without_crash(self):
        """Health check should complete without exceptions."""
        health = run_health_check()
        assert isinstance(health, HealthStatus)
        assert "disk_space" in health.checks


# ======================================================================
# Mission Queue
# ======================================================================

class TestLoadQueue:
    def test_load_from_file(self, tmp_path):
        qf = tmp_path / "queue.txt"
        qf.write_text("MISSION_A\nMISSION_B\n# comment\n\nMISSION_C\n", encoding="utf-8")
        q = load_queue(str(qf))
        assert q == ["MISSION_A", "MISSION_B", "MISSION_C"]

    def test_empty_file(self, tmp_path):
        qf = tmp_path / "empty.txt"
        qf.write_text("", encoding="utf-8")
        assert load_queue(str(qf)) == []

    def test_nonexistent_file(self):
        assert load_queue("/nonexistent/queue.txt") == []

    def test_none_path(self):
        assert load_queue(None) == []

    def test_comments_ignored(self, tmp_path):
        qf = tmp_path / "commented.txt"
        qf.write_text("# header\nMISSION_A\n# skip\nMISSION_B\n", encoding="utf-8")
        q = load_queue(str(qf))
        assert q == ["MISSION_A", "MISSION_B"]


# ======================================================================
# Heartbeat
# ======================================================================

class TestHeartbeat:
    def test_write_heartbeat(self, tmp_path):
        import cex_overnight
        orig_root = cex_overnight.ROOT
        cex_overnight.ROOT = tmp_path

        (tmp_path / ".cex" / "runtime").mkdir(parents=True)

        stats = {
            "started_at": "2026-04-07T00:00:00Z",
            "total_dispatched": 5,
            "total_passed": 4,
            "total_failed": 1,
            "consecutive_failures": 0,
            "last_health": "2026-04-07T01:00:00Z",
        }
        write_heartbeat(10, time.time() + 3600, stats)

        hb_path = tmp_path / ".cex" / "runtime" / "overnight_heartbeat.json"
        assert hb_path.exists()
        data = json.loads(hb_path.read_text(encoding="utf-8"))
        assert data["cycle"] == 10
        assert data["total_dispatched"] == 5
        assert data["pid"] == os.getpid()

        cex_overnight.ROOT = orig_root
