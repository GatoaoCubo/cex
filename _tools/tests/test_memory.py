"""Tests for cex_memory.py -- persistent build context + entity memory."""

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_memory import (build_entity_memory, build_summary,
                        get_injection_context, load_entity_memory,
                        load_learning_records, prune_records,
                        save_entity_memory)

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def learning_dir(tmp_path, monkeypatch):
    """Create isolated learning records directory."""
    lr_dir = tmp_path / ".cex" / "learning_records"
    lr_dir.mkdir(parents=True)
    monkeypatch.setattr("cex_memory.LEARNING_DIR", lr_dir)
    return lr_dir


@pytest.fixture
def memory_dir(tmp_path, monkeypatch):
    """Create isolated memory directory."""
    mem_dir = tmp_path / ".cex" / "memory"
    mem_dir.mkdir(parents=True)
    monkeypatch.setattr("cex_memory.MEMORY_DIR", mem_dir)
    monkeypatch.setattr("cex_memory.ENTITY_DB", mem_dir / "entity_memory.json")
    monkeypatch.setattr("cex_memory.SUMMARY_DB", mem_dir / "build_summary.json")
    return mem_dir


def _write_lr(lr_dir, kind, passed, retries=0, suffix="001"):
    """Helper to write a learning record JSON."""
    rec = {
        "kind": kind,
        "intent": f"create {kind}",
        "timestamp": f"2026-03-31T12:00:{suffix}",
        "passed": passed,
        "retries": retries,
        "time_ms": 1500.0,
        "gates": {"H01": True, "H02": True},
        "issues": [] if passed else ["H01: frontmatter missing"],
    }
    path = lr_dir / f"lr_{kind}_{suffix}.json"
    path.write_text(json.dumps(rec), encoding="utf-8")
    return rec


# =============================================================================
# load_learning_records
# =============================================================================


class TestLoadLearningRecords:
    @pytest.mark.unit
    def test_empty_dir(self, learning_dir):
        assert load_learning_records() == []

    @pytest.mark.unit
    def test_loads_json_files(self, learning_dir):
        _write_lr(learning_dir, "agent", True)
        _write_lr(learning_dir, "knowledge_card", False, suffix="002")
        records = load_learning_records()
        assert len(records) == 2

    @pytest.mark.unit
    def test_skips_invalid_json(self, learning_dir):
        (learning_dir / "bad.json").write_text("not json", encoding="utf-8")
        _write_lr(learning_dir, "agent", True)
        records = load_learning_records()
        assert len(records) == 1

    @pytest.mark.unit
    def test_no_dir(self, tmp_path, monkeypatch):
        monkeypatch.setattr("cex_memory.LEARNING_DIR", tmp_path / "nonexistent")
        assert load_learning_records() == []


# =============================================================================
# build_entity_memory
# =============================================================================


class TestBuildEntityMemory:
    @pytest.mark.unit
    def test_empty_records(self):
        entities = build_entity_memory([])
        assert entities == {}

    @pytest.mark.unit
    def test_single_kind(self):
        records = [
            {"kind": "agent", "verdict": {"passed": True, "retries": 0}, "timings": {"F1": 500, "F2": 500}},
            {"kind": "agent", "verdict": {"passed": True, "retries": 1}, "timings": {"F1": 1000, "F2": 1000}},
            {"kind": "agent", "verdict": {"passed": False, "retries": 2, "issues": ["H01: bad"]}, "timings": {"F1": 1500, "F2": 1500}},
        ]
        entities = build_entity_memory(records)
        assert "agent" in entities
        e = entities["agent"]
        assert e["builds"] == 3
        assert e["pass_rate"] > 0.5

    @pytest.mark.unit
    def test_multiple_kinds(self):
        records = [
            {"kind": "agent", "verdict": {"passed": True, "retries": 0}, "timings": {}},
            {"kind": "knowledge_card", "verdict": {"passed": False, "retries": 1, "issues": ["H03"]}, "timings": {}},
        ]
        entities = build_entity_memory(records)
        assert len(entities) == 2
        assert "agent" in entities
        assert "knowledge_card" in entities


# =============================================================================
# save / load entity memory
# =============================================================================


class TestEntityMemoryPersistence:
    @pytest.mark.unit
    def test_save_and_load(self, memory_dir):
        data = {"agent": {"total": 5, "passed": 4}}
        save_entity_memory(data)
        loaded = load_entity_memory()
        assert loaded == data

    @pytest.mark.unit
    def test_load_empty(self, memory_dir):
        loaded = load_entity_memory()
        assert loaded == {}


# =============================================================================
# build_summary
# =============================================================================


class TestBuildSummary:
    @pytest.mark.unit
    def test_empty_records(self):
        summary = build_summary([])
        assert summary["total"] == 0

    @pytest.mark.unit
    def test_summary_counts(self):
        records = [
            {"kind": "agent", "verdict": {"passed": True, "retries": 0}, "timings": {"F1": 500}},
            {"kind": "agent", "verdict": {"passed": False, "retries": 2, "issues": ["H01"]}, "timings": {"F1": 1500}},
        ]
        summary = build_summary(records)
        assert summary["total"] == 2
        assert summary["passed"] == 1
        assert summary["failed"] == 1


# =============================================================================
# get_injection_context
# =============================================================================


class TestGetInjectionContext:
    @pytest.mark.unit
    def test_no_records(self, learning_dir, memory_dir):
        ctx = get_injection_context("agent")
        assert isinstance(ctx, str)

    @pytest.mark.unit
    def test_with_records(self, learning_dir, memory_dir):
        _write_lr(learning_dir, "agent", True, suffix="001")
        _write_lr(learning_dir, "agent", False, retries=2, suffix="002")
        ctx = get_injection_context("agent")
        assert isinstance(ctx, str)


# =============================================================================
# prune_records
# =============================================================================


class TestPruneRecords:
    @pytest.mark.unit
    def test_prune_dry_run(self, learning_dir):
        _write_lr(learning_dir, "agent", True)
        count = prune_records("2099-01", dry_run=True)
        assert count >= 0
        # Files should still exist in dry run
        assert len(list(learning_dir.glob("*.json"))) == 1

    @pytest.mark.unit
    def test_prune_no_match(self, learning_dir):
        _write_lr(learning_dir, "agent", True)
        count = prune_records("2020-01", dry_run=False)
        assert count == 0
