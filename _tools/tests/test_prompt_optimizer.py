"""Tests for cex_prompt_optimizer.py -- builder instruction analysis."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_prompt_optimizer import (aggregate_by_kind, load_learning_records,
                                  scan_builders, suggest_improvements)

CEX_ROOT = Path(__file__).resolve().parent.parent.parent


# =============================================================================
# scan_builders
# =============================================================================


class TestScanBuilders:
    @pytest.mark.unit
    def test_returns_list(self):
        builders = scan_builders()
        assert isinstance(builders, list)

    @pytest.mark.unit
    def test_has_builders(self):
        builders = scan_builders()
        assert len(builders) >= 90  # we have 103 builders

    @pytest.mark.unit
    def test_builder_structure(self):
        builders = scan_builders()
        if builders:
            b = builders[0]
            assert "kind" in b
            assert "iso_count" in b
            assert "completeness" in b or "avg_score" in b

    @pytest.mark.unit
    def test_all_have_kind(self):
        builders = scan_builders()
        for b in builders:
            assert b.get("kind"), f"Builder missing kind: {b}"


# =============================================================================
# load_learning_records (optimizer's version)
# =============================================================================


class TestLoadRecords:
    @pytest.mark.unit
    def test_returns_list(self):
        records = load_learning_records()
        assert isinstance(records, list)


# =============================================================================
# aggregate_by_kind
# =============================================================================


class TestAggregateByKind:
    @pytest.mark.unit
    def test_empty(self):
        result = aggregate_by_kind([])
        assert result == {}

    @pytest.mark.unit
    def test_single_record(self):
        records = [
            {"kind": "agent", "verdict": {"passed": True, "retries": 0, "issues": []}, "timings": {}},
        ]
        agg = aggregate_by_kind(records)
        assert "agent" in agg
        assert agg["agent"]["total"] == 1
        assert agg["agent"]["passed"] == 1

    @pytest.mark.unit
    def test_multiple_kinds(self):
        records = [
            {"kind": "agent", "verdict": {"passed": True, "retries": 0, "issues": []}, "timings": {}},
            {"kind": "agent", "verdict": {"passed": False, "retries": 2, "issues": ["H01"]}, "timings": {}},
            {"kind": "workflow", "verdict": {"passed": True, "retries": 1, "issues": []}, "timings": {}},
        ]
        agg = aggregate_by_kind(records)
        assert agg["agent"]["total"] == 2
        assert agg["agent"]["failed"] == 1
        assert agg["workflow"]["total"] == 1

    @pytest.mark.unit
    def test_failure_tracking(self):
        records = [
            {"kind": "agent", "verdict": {"passed": False, "retries": 2, "issues": ["H01: bad"]}, "timings": {}},
            {"kind": "agent", "verdict": {"passed": False, "retries": 1, "issues": ["H01: bad"]}, "timings": {}},
        ]
        agg = aggregate_by_kind(records)
        assert agg["agent"]["failed"] == 2


# =============================================================================
# suggest_improvements
# =============================================================================


class TestSuggestImprovements:
    @pytest.mark.unit
    def test_known_kind(self):
        suggestions = suggest_improvements("agent")
        assert isinstance(suggestions, list)

    @pytest.mark.unit
    def test_unknown_kind(self):
        suggestions = suggest_improvements("nonexistent_kind_xyz_12345")
        assert isinstance(suggestions, list)
        assert len(suggestions) >= 1  # should report "builder not found"

    @pytest.mark.unit
    def test_suggestions_are_strings(self):
        suggestions = suggest_improvements("knowledge_card")
        for s in suggestions:
            assert isinstance(s, str)
