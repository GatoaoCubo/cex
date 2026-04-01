"""Tests for brand_inject.py, brand_validate.py, brand_propagate.py, brand_audit.py."""
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from brand_inject import flatten, inject_brand, count_unresolved, load_brand_config
from brand_validate import validate, is_placeholder, validate_section
from brand_propagate import extract_vars, format_brand_context, NUCLEUS_VARS
from brand_audit import (
    score_config_completeness, score_archetype_alignment,
    score_voice_consistency, score_visual_coherence,
    score_positioning_clarity, score_narrative_integrity,
)

ROOT = Path(__file__).resolve().parent.parent.parent
TEMPLATE_PATH = ROOT / ".cex" / "brand" / "brand_config_template.yaml"


# ── brand_inject.py ──

class TestFlatten:
    def test_flat_dict(self):
        d = {"BRAND_NAME": "Codexa", "BRAND_TAGLINE": "Build with AI"}
        result = flatten(d)
        assert "BRAND_NAME" in result
        assert result["BRAND_NAME"] == "Codexa"

    def test_nested_dict(self):
        d = {"identity": {"BRAND_NAME": "Codexa"}, "voice": {"BRAND_VOICE_TONE": "direct"}}
        result = flatten(d)
        assert "BRAND_NAME" in result
        assert "BRAND_VOICE_TONE" in result

    def test_list_values(self):
        d = {"BRAND_VALUES": ["innovation", "speed", "quality"]}
        result = flatten(d)
        assert "innovation" in result["BRAND_VALUES"]

    def test_empty(self):
        assert flatten({}) == {}


class TestInjectBrand:
    def test_replaces_variables(self):
        config = {"identity": {"BRAND_NAME": "Codexa"}}
        template = "Welcome to {{BRAND_NAME}}!"
        result = inject_brand(template, config)
        assert result == "Welcome to Codexa!"

    def test_no_config(self):
        result = inject_brand("Hello {{BRAND_NAME}}", {})
        assert "{{BRAND_NAME}}" in result  # unreplaced

    def test_multiple_vars(self):
        config = {
            "identity": {"BRAND_NAME": "Codexa", "BRAND_TAGLINE": "Build with AI"},
        }
        template = "{{BRAND_NAME}} — {{BRAND_TAGLINE}}"
        result = inject_brand(template, config)
        assert "Codexa" in result
        assert "Build with AI" in result


class TestCountUnresolved:
    def test_finds_unresolved(self):
        text = "Hello {{BRAND_NAME}}, your color is {{PRIMARY_HEX}}"
        unresolved = count_unresolved(text)
        assert "BRAND_NAME" in unresolved
        assert "PRIMARY_HEX" in unresolved

    def test_no_unresolved(self):
        assert count_unresolved("Hello world") == []


class TestLoadBrandConfig:
    def test_loads_template(self):
        if TEMPLATE_PATH.exists():
            config = load_brand_config(TEMPLATE_PATH)
            assert isinstance(config, dict)
            assert "identity" in config

    def test_nonexistent(self):
        config = load_brand_config(Path("nonexistent.yaml"))
        assert config == {}


# ── brand_validate.py ──

class TestIsPlaceholder:
    def test_mustache_var(self):
        assert is_placeholder("{{BRAND_NAME}}") is True

    def test_real_value(self):
        assert is_placeholder("Codexa") is False

    def test_none(self):
        assert is_placeholder(None) is True

    def test_number(self):
        assert is_placeholder(3) is False


class TestValidate:
    def test_valid_config(self):
        config = {
            "identity": {"BRAND_NAME": "Test", "BRAND_TAGLINE": "Test tagline here", "BRAND_MISSION": "We exist to test software quality", "BRAND_VALUES": ["a", "b", "c"]},
            "archetype": {"BRAND_ARCHETYPE": "sage"},
            "voice": {"BRAND_VOICE_TONE": "direct", "BRAND_VOICE_FORMALITY": 3},
            "audience": {"BRAND_ICP": "Software developers who need testing", "BRAND_TRANSFORMATION": "From untested to fully covered through automation"},
            "visual": {"BRAND_COLORS": {"primary": "#000000", "secondary": "#111111", "accent": "#50C878"}},
            "positioning": {"BRAND_CATEGORY": "testing", "BRAND_UVP": "The only testing tool that writes itself"},
            "monetization": {"BRAND_PRICING_MODEL": "subscription", "BRAND_CURRENCY": "USD"},
        }
        result = validate(config)
        assert result["valid"] is True
        assert len(result["errors"]) == 0

    def test_invalid_archetype(self):
        config = {
            "identity": {"BRAND_NAME": "X", "BRAND_TAGLINE": "tag tag tag", "BRAND_MISSION": "We exist to do something good", "BRAND_VALUES": ["a", "b", "c"]},
            "archetype": {"BRAND_ARCHETYPE": "invalid_type"},
            "voice": {"BRAND_VOICE_TONE": "x", "BRAND_VOICE_FORMALITY": 3},
            "audience": {"BRAND_ICP": "someone who needs something", "BRAND_TRANSFORMATION": "From A to B through C"},
            "visual": {"BRAND_COLORS": {"primary": "#000", "secondary": "#111", "accent": "#222"}},
            "positioning": {"BRAND_CATEGORY": "x", "BRAND_UVP": "unique value proposition text"},
            "monetization": {"BRAND_PRICING_MODEL": "subscription", "BRAND_CURRENCY": "USD"},
        }
        result = validate(config)
        has_arch_error = any("archetype" in e.lower() for e in result["errors"])
        assert has_arch_error

    def test_missing_section(self):
        config = {"identity": {"BRAND_NAME": "X"}}
        result = validate(config)
        assert not result["valid"]

    def test_template_has_placeholders(self):
        if TEMPLATE_PATH.exists():
            import yaml
            with open(TEMPLATE_PATH, "r") as f:
                config = yaml.safe_load(f)
            result = validate(config)
            # Template should have warnings about placeholders
            assert len(result["warnings"]) > 0 or len(result["errors"]) > 0


# ── brand_propagate.py ──

class TestExtractVars:
    def test_extracts_from_nested(self):
        config = {
            "identity": {"BRAND_NAME": "Codexa", "BRAND_TAGLINE": "Build"},
            "voice": {"BRAND_VOICE_TONE": "direct"},
        }
        result = extract_vars(config, ["BRAND_NAME", "BRAND_VOICE_TONE"])
        assert "BRAND_NAME" in result
        assert "BRAND_VOICE_TONE" in result

    def test_missing_var(self):
        config = {"identity": {"BRAND_NAME": "X"}}
        result = extract_vars(config, ["BRAND_NONEXISTENT"])
        assert "BRAND_NONEXISTENT" not in result


class TestFormatBrandContext:
    def test_formats_output(self):
        result = format_brand_context("N02", {"BRAND_NAME": "Codexa", "BRAND_VOICE_TONE": "direct"})
        assert "Brand Context" in result
        assert "BRAND_NAME" in result

    def test_empty_vars(self):
        result = format_brand_context("N01", {})
        assert "Brand Context" in result


class TestNucleusVars:
    def test_all_nuclei_defined(self):
        for n in ["N01", "N02", "N03", "N04", "N05", "N07"]:
            assert n in NUCLEUS_VARS
            assert len(NUCLEUS_VARS[n]) > 0


# ── brand_audit.py ──

class TestScoreConfigCompleteness:
    def test_full_config(self):
        config = {
            "identity": {"BRAND_NAME": "X", "BRAND_TAGLINE": "tagline text", "BRAND_MISSION": "We exist to do something", "BRAND_VALUES": ["a", "b", "c"]},
            "archetype": {"BRAND_ARCHETYPE": "sage"},
            "voice": {"BRAND_VOICE_TONE": "direct", "BRAND_VOICE_FORMALITY": 3},
            "audience": {"BRAND_ICP": "developers who test", "BRAND_TRANSFORMATION": "From A to B through C"},
            "visual": {"BRAND_COLORS": {"primary": "#000", "secondary": "#111", "accent": "#222"}},
            "positioning": {"BRAND_CATEGORY": "testing", "BRAND_UVP": "unique value proposition"},
            "monetization": {"BRAND_PRICING_MODEL": "subscription"},
        }
        score, issues = score_config_completeness(config)
        assert score > 0.8
        assert len(issues) < 3

    def test_empty_config(self):
        score, issues = score_config_completeness({})
        assert score == 0
        assert len(issues) == 13


class TestScoreArchetypeAlignment:
    def test_valid_archetype(self):
        config = {"archetype": {"BRAND_ARCHETYPE": "sage", "BRAND_PERSONALITY": ["wise", "analytical", "calm"], "BRAND_ARCHETYPE_SHADOW": "trickster"}}
        score, issues = score_archetype_alignment(config)
        assert score == 1.0

    def test_no_archetype(self):
        score, issues = score_archetype_alignment({})
        assert score == 0


class TestScoreVoiceConsistency:
    def test_full_voice(self):
        config = {"voice": {"BRAND_VOICE_FORMALITY": 3, "BRAND_VOICE_ENTHUSIASM": 3, "BRAND_VOICE_HUMOR": 2, "BRAND_VOICE_WARMTH": 4, "BRAND_VOICE_AUTHORITY": 4, "BRAND_VOICE_DO": ["be direct", "use examples", "show data"]}}
        score, issues = score_voice_consistency(config)
        assert score >= 0.9

    def test_no_voice(self):
        score, issues = score_voice_consistency({})
        assert score == 0


class TestScoreVisualCoherence:
    def test_full_visual(self):
        config = {"visual": {"BRAND_COLORS": {"primary": "#000000", "secondary": "#111111", "accent": "#50C878"}, "BRAND_FONTS": {"heading": "Geist"}, "BRAND_STYLE": "minimal-dark"}}
        score, issues = score_visual_coherence(config)
        assert score >= 0.8


class TestScorePositioningClarity:
    def test_full_positioning(self):
        config = {"positioning": {"BRAND_CATEGORY": "testing", "BRAND_UVP": "The only testing framework that writes itself", "BRAND_DIFFERENTIATOR": "self-generating tests"}}
        score, issues = score_positioning_clarity(config)
        assert score == 1.0


class TestScoreNarrativeIntegrity:
    def test_full_narrative(self):
        config = {
            "identity": {"BRAND_STORY": "A" * 200, "BRAND_MISSION": "We test everything"},
            "audience": {"BRAND_TRANSFORMATION": "From untested to fully covered through automation"},
        }
        score, issues = score_narrative_integrity(config)
        assert score == 1.0
