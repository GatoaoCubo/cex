#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Tests for cex_continuous.py -- continuous mode handoff polling."""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from cex_continuous import scan_handoffs

# ======================================================================
# scan_handoffs
# ======================================================================

class TestScanHandoffs:
    def test_empty_dir(self, tmp_path):
        """No handoffs returns empty list."""
        import cex_continuous
        orig = cex_continuous.HANDOFF_DIR
        cex_continuous.HANDOFF_DIR = tmp_path
        try:
            tasks = scan_handoffs()
            assert tasks == []
        finally:
            cex_continuous.HANDOFF_DIR = orig

    def test_finds_task_files(self, tmp_path):
        """Detects n0X_task.md files."""
        (tmp_path / "n01_task.md").write_text("---\ntask: research\n---\nDo stuf", encoding="utf-8")
        (tmp_path / "n03_task.md").write_text("---\ntask: build\n---\nBuild stuf", encoding="utf-8")
        (tmp_path / "n05_task.md").write_text("---\ntask: test\n---\nTest stuf", encoding="utf-8")

        import cex_continuous
        orig = cex_continuous.HANDOFF_DIR
        cex_continuous.HANDOFF_DIR = tmp_path
        try:
            tasks = scan_handoffs()
            assert len(tasks) == 3
            nuclei = {t["nucleus"] for t in tasks}
            assert nuclei == {"n01", "n03", "n05"}
        finally:
            cex_continuous.HANDOFF_DIR = orig

    def test_ignores_non_task_files(self, tmp_path):
        """Ignores files that don't match n0X_task.md pattern."""
        (tmp_path / "n01_task.md").write_text("---\ntask: ok\n---\nContent", encoding="utf-8")
        (tmp_path / "MISSION_n01.md").write_text("not a task", encoding="utf-8")
        (tmp_path / "random.md").write_text("nope", encoding="utf-8")
        (tmp_path / "n08_task.md").write_text("invalid nucleus", encoding="utf-8")

        import cex_continuous
        orig = cex_continuous.HANDOFF_DIR
        cex_continuous.HANDOFF_DIR = tmp_path
        try:
            tasks = scan_handoffs()
            assert len(tasks) == 1
            assert tasks[0]["nucleus"] == "n01"
        finally:
            cex_continuous.HANDOFF_DIR = orig

    def test_ignores_empty_files(self, tmp_path):
        """Skips files smaller than 10 bytes."""
        (tmp_path / "n01_task.md").write_text("tiny", encoding="utf-8")  # 4 bytes
        (tmp_path / "n03_task.md").write_text("---\ntask: build\n---\nBuild it", encoding="utf-8")

        import cex_continuous
        orig = cex_continuous.HANDOFF_DIR
        cex_continuous.HANDOFF_DIR = tmp_path
        try:
            tasks = scan_handoffs()
            assert len(tasks) == 1
            assert tasks[0]["nucleus"] == "n03"
        finally:
            cex_continuous.HANDOFF_DIR = orig

    def test_filter_nuclei(self, tmp_path):
        """Filter to specific nuclei."""
        (tmp_path / "n01_task.md").write_text("---\ntask: research\n---\nResearch", encoding="utf-8")
        (tmp_path / "n03_task.md").write_text("---\ntask: build\n---\nBuild", encoding="utf-8")
        (tmp_path / "n05_task.md").write_text("---\ntask: test\n---\nTest", encoding="utf-8")

        import cex_continuous
        orig = cex_continuous.HANDOFF_DIR
        cex_continuous.HANDOFF_DIR = tmp_path
        try:
            tasks = scan_handoffs(filter_nuclei={"n01", "n05"})
            assert len(tasks) == 2
            nuclei = {t["nucleus"] for t in tasks}
            assert nuclei == {"n01", "n05"}
        finally:
            cex_continuous.HANDOFF_DIR = orig

    def test_nonexistent_dir(self):
        """Nonexistent directory returns empty."""
        import cex_continuous
        orig = cex_continuous.HANDOFF_DIR
        cex_continuous.HANDOFF_DIR = Path("/nonexistent/path/that/wont/exist")
        try:
            tasks = scan_handoffs()
            assert tasks == []
        finally:
            cex_continuous.HANDOFF_DIR = orig

    def test_n07_task_detected(self, tmp_path):
        """N07 tasks are also detected."""
        (tmp_path / "n07_task.md").write_text("---\ntask: orchestrate\n---\nOrchestrate", encoding="utf-8")

        import cex_continuous
        orig = cex_continuous.HANDOFF_DIR
        cex_continuous.HANDOFF_DIR = tmp_path
        try:
            tasks = scan_handoffs()
            assert len(tasks) == 1
            assert tasks[0]["nucleus"] == "n07"
        finally:
            cex_continuous.HANDOFF_DIR = orig

    def test_task_has_path_and_size(self, tmp_path):
        """Each task dict has path and size fields."""
        content = "---\ntask: build\n---\nBuild something"
        (tmp_path / "n03_task.md").write_text(content, encoding="utf-8")

        import cex_continuous
        orig = cex_continuous.HANDOFF_DIR
        cex_continuous.HANDOFF_DIR = tmp_path
        try:
            tasks = scan_handoffs()
            assert len(tasks) == 1
            assert "path" in tasks[0]
            assert tasks[0]["size"] > 0
        finally:
            cex_continuous.HANDOFF_DIR = orig
