"""Tests for cex_feedback.py -- artifact scanning and analysis."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_feedback import (analyze, calc_density, parse_frontmatter,
                          scan_artifacts)

ROOT = Path(__file__).resolve().parent.parent.parent


class TestParseFrontmatter:
    def test_valid_file(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("---\nid: test_1\nkind: knowledge_card\nquality: 8.5\n---\n# Body\nContent here.", encoding="utf-8")
        fm = parse_frontmatter(f)
        assert fm is not None
        assert fm["id"] == "test_1"
        assert fm["quality"] == 8.5

    def test_no_frontmatter(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("# Just markdown\nNo frontmatter here.", encoding="utf-8")
        fm = parse_frontmatter(f)
        assert fm is None

    def test_quality_null(self, tmp_path):
        f = tmp_path / "test.md"
        f.write_text("---\nid: test_2\nkind: agent\nquality: null\n---\n# Body", encoding="utf-8")
        fm = parse_frontmatter(f)
        assert fm is not None
        assert fm["quality"] is None


class TestCalcDensity:
    def test_short_file(self, tmp_path):
        f = tmp_path / "short.md"
        f.write_text("---\nid: x\n---\n# Title\nOne line.", encoding="utf-8")
        d = calc_density(f)
        assert 0 <= d <= 1.0

    def test_dense_file(self, tmp_path):
        f = tmp_path / "dense.md"
        body = "\n".join([f"## Section {i}\nContent paragraph {i} with details." for i in range(20)])
        f.write_text(f"---\nid: y\n---\n{body}", encoding="utf-8")
        d = calc_density(f)
        assert d > 0.5


class TestScanArtifacts:
    def test_returns_list(self):
        arts = scan_artifacts()
        assert isinstance(arts, list)
        assert len(arts) > 50  # we have 100+ scored artifacts

    def test_artifact_info_fields(self):
        arts = scan_artifacts()
        if arts:
            a = arts[0]
            assert hasattr(a, "path")
            assert hasattr(a, "kind")
            assert hasattr(a, "quality")


class TestAnalyze:
    def test_returns_dict(self):
        arts = scan_artifacts()
        results = analyze(arts)
        assert isinstance(results, dict)
        assert "total" in results or "count" in results or len(results) > 0
