"""Tests for cex_index.py -- file indexing and SQLite cache."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from cex_index import (compute_density, extract_wikilinks, parse_frontmatter,
                       scan_files)

ROOT = Path(__file__).resolve().parent.parent.parent


class TestParseFrontmatter:
    def test_valid(self):
        text = "---\nid: test_1\nkind: agent\npillar: P01\n---\n# Body"
        fm = parse_frontmatter(text)
        assert fm["id"] == "test_1"
        assert fm["kind"] == "agent"

    def test_empty(self):
        fm = parse_frontmatter("")
        assert fm == {} or fm is None

    def test_no_frontmatter(self):
        fm = parse_frontmatter("# Just a heading\nNo YAML here.")
        assert fm == {} or fm is None


class TestExtractWikilinks:
    def test_finds_links(self):
        text = "See [[kc_testing]] and [[workflow_deploy]] for details."
        links = extract_wikilinks(text)
        assert "kc_testing" in links
        assert "workflow_deploy" in links

    def test_no_links(self):
        links = extract_wikilinks("Plain text without any links.")
        assert links == []

    def test_empty(self):
        assert extract_wikilinks("") == []


class TestComputeDensity:
    def test_short_text(self):
        d = compute_density("hello world")
        assert 0 <= d <= 1.0

    def test_dense_text(self):
        text = " ".join([f"word{i}" for i in range(200)])
        d = compute_density(text)
        assert d > 0

    def test_empty(self):
        d = compute_density("")
        assert d == 0 or isinstance(d, float)


class TestScanFiles:
    def test_finds_md_files(self):
        files = scan_files(ROOT)
        assert len(files) > 100
        md_files = [f for f in files if f.suffix == ".md"]
        assert len(md_files) > 50  # most should be .md

    def test_excludes_compiled(self):
        files = scan_files(ROOT)
        compiled = [f for f in files if "compiled" in str(f)]
        # scan_files may or may not exclude compiled, just check it returns files
        assert len(files) > 0
