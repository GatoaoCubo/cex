"""Tests for cex_score.py -- Artifact quality scoring."""

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_score import score_artifact


class TestScoreArtifact:
    @pytest.mark.unit
    def test_score_valid_artifact(self, valid_artifact):
        score, notes = score_artifact(str(valid_artifact))
        assert isinstance(score, float)
        assert 7.0 <= score <= 10.0
        assert isinstance(notes, str)

    @pytest.mark.unit
    def test_score_missing_file(self, tmp_path):
        score, notes = score_artifact(str(tmp_path / "nonexistent.md"))
        assert score == 0.0
        assert "MISSING" in notes

    @pytest.mark.unit
    def test_score_no_frontmatter(self, invalid_artifact_no_fm):
        score, _notes = score_artifact(str(invalid_artifact_no_fm))
        assert score < 8.0  # Should score low without frontmatter

    @pytest.mark.unit
    def test_score_null_quality_artifact(self, valid_artifact_null_quality):
        score, _notes = score_artifact(str(valid_artifact_null_quality))
        assert isinstance(score, float)
        assert score >= 7.0

    @pytest.mark.unit
    def test_score_empty_file(self, tmp_path):
        f = tmp_path / "empty.md"
        f.write_text("", encoding="utf-8")
        score, _notes = score_artifact(str(f))
        assert score < 7.0

    @pytest.mark.unit
    def test_score_range(self, valid_artifact):
        """Scores should be in the documented 8.0-9.3 range for valid artifacts."""
        score, _ = score_artifact(str(valid_artifact))
        assert 8.0 <= score <= 9.5

    @pytest.mark.unit
    def test_score_returns_tuple(self, valid_artifact):
        result = score_artifact(str(valid_artifact))
        assert isinstance(result, tuple)
        assert len(result) == 2

    @pytest.mark.unit
    def test_larger_artifact_scores_higher(self, tmp_path):
        """A richer artifact should score higher than a minimal one."""
        small = tmp_path / "small.md"
        small.write_text(
            "---\nid: s\nkind: knowledge_card\npillar: P01\nquality: null\n---\n# Small\nOne line.",
            encoding="utf-8",
        )
        large = tmp_path / "large.md"
        large.write_text(
            "---\nid: l\nkind: knowledge_card\npillar: P01\nquality: null\n"
            "tags: [a,b,c]\ntldr: 'Rich content'\ndensity_score: 0.9\n---\n"
            "# Large\n\n## Section 1\n\nContent here.\n\n"
            "| A | B |\n|---|---|\n| 1 | 2 |\n\n"
            "## Section 2\n\n```python\ndef example(): pass\n```\n\n"
            "## Section 3\n\nMore content.\n",
            encoding="utf-8",
        )
        score_s, _ = score_artifact(str(small))
        score_l, _ = score_artifact(str(large))
        assert score_l > score_s
