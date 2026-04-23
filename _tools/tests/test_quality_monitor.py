"""Tests for cex_quality_monitor.py -- quality tracking + regression detection."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_quality_monitor import (find_regressions, load_history, load_snapshot,
                                 quality_report, save_snapshot)

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def quality_dir(tmp_path, monkeypatch):
    """Isolated quality directory."""
    qdir = tmp_path / ".cex" / "quality"
    qdir.mkdir(parents=True)
    monkeypatch.setattr("cex_quality_monitor.QUALITY_DIR", qdir)
    monkeypatch.setattr("cex_quality_monitor.SNAPSHOT_PATH", qdir / "latest_snapshot.json")
    monkeypatch.setattr("cex_quality_monitor.HISTORY_PATH", qdir / "history.json")
    return qdir


SAMPLE_ARTIFACTS = [
    {"path": "N03/agents/agent_a.md", "kind": "agent", "pillar": "P02", "score": 9.0, "title": "Agent A", "id": "a1"},
    {"path": "N03/agents/agent_b.md", "kind": "agent", "pillar": "P02", "score": 8.5, "title": "Agent B", "id": "a2"},
    {"path": "N01/knowledge/kc_test.md", "kind": "knowledge_card", "pillar": "P01", "score": 7.5, "title": "KC Test", "id": "k1"},
]


# =============================================================================
# save_snapshot / load_snapshot
# =============================================================================


class TestSnapshotPersistence:
    @pytest.mark.unit
    def test_save_and_load(self, quality_dir):
        save_snapshot(SAMPLE_ARTIFACTS)
        snap = load_snapshot()
        assert snap is not None
        assert snap["total"] == 3
        assert snap["avg_score"] > 0

    @pytest.mark.unit
    def test_load_empty(self, quality_dir):
        snap = load_snapshot()
        assert snap is None

    @pytest.mark.unit
    def test_snapshot_has_timestamp(self, quality_dir):
        save_snapshot(SAMPLE_ARTIFACTS)
        snap = load_snapshot()
        assert "timestamp" in snap

    @pytest.mark.unit
    def test_snapshot_updates_history(self, quality_dir):
        save_snapshot(SAMPLE_ARTIFACTS)
        save_snapshot(SAMPLE_ARTIFACTS)
        history = load_history()
        assert len(history) == 2


# =============================================================================
# load_history
# =============================================================================


class TestLoadHistory:
    @pytest.mark.unit
    def test_empty(self, quality_dir):
        history = load_history()
        assert history == []

    @pytest.mark.unit
    def test_after_saves(self, quality_dir):
        save_snapshot(SAMPLE_ARTIFACTS[:1])
        save_snapshot(SAMPLE_ARTIFACTS[:2])
        history = load_history()
        assert len(history) == 2


# =============================================================================
# find_regressions
# =============================================================================


class TestFindRegressions:
    @pytest.mark.unit
    def test_no_regression(self):
        current = [{"path": "a.md", "score": 9.0}]
        previous = [{"path": "a.md", "score": 8.5}]
        regs = find_regressions(current, previous)
        assert len(regs) == 0  # score went up, no regression

    @pytest.mark.unit
    def test_regression_detected(self):
        current = [{"path": "a.md", "score": 7.0}]
        previous = [{"path": "a.md", "score": 9.0}]
        regs = find_regressions(current, previous)
        assert len(regs) == 1
        assert regs[0]["delta"] < 0

    @pytest.mark.unit
    def test_new_artifact_no_regression(self):
        current = [{"path": "new.md", "score": 8.0}]
        previous = [{"path": "old.md", "score": 9.0}]
        regs = find_regressions(current, previous)
        assert len(regs) == 0

    @pytest.mark.unit
    def test_multiple_regressions_sorted(self):
        current = [
            {"path": "a.md", "score": 5.0},
            {"path": "b.md", "score": 7.0},
        ]
        previous = [
            {"path": "a.md", "score": 9.0},
            {"path": "b.md", "score": 9.0},
        ]
        regs = find_regressions(current, previous)
        assert len(regs) == 2
        assert regs[0]["delta"] <= regs[1]["delta"]  # worst first


# =============================================================================
# quality_report
# =============================================================================


class TestQualityReport:
    @pytest.mark.unit
    def test_empty(self):
        report = quality_report([])
        assert report["total"] == 0

    @pytest.mark.unit
    def test_basic_report(self):
        report = quality_report(SAMPLE_ARTIFACTS)
        assert report["total"] == 3
        assert "avg_score" in report
        assert report["avg_score"] > 0

    @pytest.mark.unit
    def test_distribution(self):
        report = quality_report(SAMPLE_ARTIFACTS)
        dist = report.get("distribution", {})
        assert isinstance(dist, dict)

    @pytest.mark.unit
    def test_report_with_single_artifact(self):
        report = quality_report([SAMPLE_ARTIFACTS[0]])
        assert report["total"] == 1
        assert report["avg_score"] == 9.0
