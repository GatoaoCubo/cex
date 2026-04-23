"""Tests for cex_bootstrap.py -- first-run brand setup."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from cex_bootstrap import (count_filled, count_placeholders,
                           inject_brand_header, is_bootstrapped)

ROOT = Path(__file__).resolve().parent.parent.parent


class TestIsBootstrapped:
    def test_no_config_file(self, tmp_path):
        """No brand_config.yaml = not bootstrapped."""
        import cex_bootstrap as cb
        original = cb.BRAND_CONFIG
        cb.BRAND_CONFIG = tmp_path / "nonexistent.yaml"
        try:
            assert is_bootstrapped() is False
        finally:
            cb.BRAND_CONFIG = original

    def test_lock_file_means_bootstrapped(self, tmp_path):
        """Lock file exists = bootstrapped."""
        import cex_bootstrap as cb

        config = tmp_path / "brand_config.yaml"
        lock = tmp_path / ".bootstrapped"
        config.write_text("identity:\n  BRAND_NAME: Test\n", encoding="utf-8")
        lock.write_text("bootstrapped: true\n", encoding="utf-8")

        orig_config = cb.BRAND_CONFIG
        orig_lock = cb.BRAND_LOCK
        cb.BRAND_CONFIG = config
        cb.BRAND_LOCK = lock
        try:
            assert is_bootstrapped() is True
        finally:
            cb.BRAND_CONFIG = orig_config
            cb.BRAND_LOCK = orig_lock


class TestCountPlaceholders:
    def test_template_has_placeholders(self):
        config = {
            "identity": {"BRAND_NAME": "{{BRAND_NAME}}", "BRAND_TAGLINE": "{{BRAND_TAGLINE}}"},
            "archetype": {"BRAND_ARCHETYPE": "{{BRAND_ARCHETYPE}}"},
        }
        assert count_placeholders(config) >= 3

    def test_filled_has_none(self):
        config = {
            "identity": {"BRAND_NAME": "Codexa", "BRAND_TAGLINE": "Build AI"},
            "archetype": {"BRAND_ARCHETYPE": "sage"},
        }
        assert count_placeholders(config) == 0


class TestCountFilled:
    def test_counts_real_values(self):
        config = {
            "identity": {"BRAND_NAME": "Codexa", "BRAND_TAGLINE": "Build AI"},
            "archetype": {"BRAND_ARCHETYPE": "sage"},
        }
        filled = count_filled(config)
        assert filled >= 3

    def test_template_has_low_filled(self):
        config = {
            "identity": {"BRAND_NAME": "{{BRAND_NAME}}"},
        }
        # Placeholders count as values but are subtracted
        assert count_filled(config) <= 1


class TestInjectBrandHeader:
    def test_injects_into_claude_md(self, tmp_path):
        """Brand header gets injected into CLAUDE.md."""
        import cex_bootstrap as cb

        claude_md = tmp_path / "CLAUDE.md"
        claude_md.write_text(
            "# CEX\n\n## Who Am I?\n\nSome content here.\n",
            encoding="utf-8",
        )

        orig = cb.CLAUDE_MD
        cb.CLAUDE_MD = claude_md
        try:
            config = {
                "identity": {"BRAND_NAME": "TestBrand", "BRAND_TAGLINE": "Test tag"},
                "archetype": {"BRAND_ARCHETYPE": "sage"},
            }
            inject_brand_header(config)

            content = claude_md.read_text(encoding="utf-8")
            assert "Brand Identity (bootstrapped)" in content
            assert "TestBrand" in content
            assert "sage" in content
            assert "## Who Am I?" in content  # preserved
        finally:
            cb.CLAUDE_MD = orig

    def test_idempotent(self, tmp_path):
        """Running twice doesn't duplicate the block."""
        import cex_bootstrap as cb

        claude_md = tmp_path / "CLAUDE.md"
        claude_md.write_text("# CEX\n\n## Who Am I?\n\nContent.\n", encoding="utf-8")

        orig = cb.CLAUDE_MD
        cb.CLAUDE_MD = claude_md
        try:
            config = {
                "identity": {"BRAND_NAME": "Test", "BRAND_TAGLINE": "Tag"},
                "archetype": {"BRAND_ARCHETYPE": "hero"},
            }
            inject_brand_header(config)
            inject_brand_header(config)  # second run

            content = claude_md.read_text(encoding="utf-8")
            count = content.count("Brand Identity (bootstrapped)")
            assert count == 1, f"Found {count} brand blocks (expected 1)"
        finally:
            cb.CLAUDE_MD = orig
