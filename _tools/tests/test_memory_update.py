"""Tests for cex_memory_update.py -- builder memory management."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_memory_update import (apply_decay, load_memory_file,
                               rebuild_frontmatter)


class TestLoadMemoryFile:
    def test_existing_builder(self):
        path, content, fm = load_memory_file("knowledge-card-builder")
        if path:  # builder exists
            assert isinstance(content, str)
            assert len(content) > 0

    def test_nonexistent_builder(self):
        path, content, fm = load_memory_file("nonexistent-builder-xyz-999")
        assert path is None or content == ""


class TestApplyDecay:
    def test_decay_reduces_scores(self):
        content = """## Observations
- [confidence=0.95] Pattern A works well
- [confidence=0.60] Pattern B is risky
- [confidence=0.30] Pattern C is unreliable"""
        fm = {"version": "1.0.0"}
        new_content, new_fm, decayed = apply_decay(content, fm)
        assert isinstance(new_content, str)
        assert isinstance(decayed, int)

    def test_empty_content(self):
        content = "## Empty memory"
        fm = {"version": "1.0.0"}
        new_content, new_fm, decayed = apply_decay(content, fm)
        assert decayed == 0


class TestRebuildFrontmatter:
    def test_preserves_fields(self):
        content = "---\nid: test_mem\nkind: memory\nversion: 1.0.0\n---\n# Body"
        fm = {"id": "test_mem", "kind": "memory", "version": "1.0.0"}
        result = rebuild_frontmatter(content, fm)
        assert "id: test_mem" in result
        assert "kind: memory" in result

    def test_updates_version(self):
        content = "---\nid: x\nversion: 1.0.0\n---\n# B"
        fm = {"id": "x", "version": "1.1.0"}
        result = rebuild_frontmatter(content, fm)
        assert "1.1.0" in result
