"""Tests for brand_inject.py, brand_validate.py, brand_propagate.py, brand_audit.py."""
import sys
from pathlib import Path
import pytest

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from brand_inject import (
    flatten, inject_brand, count_unresolved, load_brand_config,
    load_instance_config, compute_derived, INSTANCE_VARS, INSTANCE_CONFIG,
)
from brand_validate import validate, is_placeholder, validate_section
from brand_propagate import extract_vars, format_brand_context, NUCLEUS_VARS
from brand_audit import (
    score_config_completeness, score_archetype_alignment,
    score_voice_consistency, score_visual_coherence,
    score_positioning_clarity, score_narrative_integrity,
)

ROOT = Path(__file__).resolve().parent.parent.parent
TEMPLATE_PATH = ROOT / ".cex" / "brand" / "brand_config_template.yaml"


# -- brand_inject.py --

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
        template = "{{BRAND_NAME}} -- {{BRAND_TAGLINE}}"
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


# -- Instance Config (new: 23 variables from kc_instance_variable_registry) --

class TestLoadInstanceConfig:
    def test_loads_template(self):
        tpl = INSTANCE_CONFIG.parent / "instance_config_template.yaml"
        if tpl.exists():
            config = load_instance_config(tpl)
            assert isinstance(config, dict)
            assert "crm_pipeline" in config
            assert "dashboard" in config
            assert "infrastructure" in config
            assert "research" in config

    def test_nonexistent(self):
        config = load_instance_config(Path("nonexistent.yaml"))
        assert config == {}

    def test_template_has_23_vars(self):
        tpl = INSTANCE_CONFIG.parent / "instance_config_template.yaml"
        if tpl.exists():
            config = load_instance_config(tpl)
            flat = flatten(config)
            # Filter to actual variable keys (not section prefixes)
            var_keys = {k for k in flat.keys() if k.isupper() and "." not in k}
            assert len(var_keys) >= 23, f"Expected >=23 vars, got {len(var_keys)}: {var_keys}"


class TestInstanceInjection:
    """Test that instance variables get injected alongside brand variables."""

    def test_instance_vars_injected(self):
        brand = {"identity": {"BRAND_NAME": "TestCorp"}}
        instance = {"crm_pipeline": {"INDUSTRY": "pet", "TARGET_COUNT": "500"}}
        template = "{{BRAND_NAME}} targets {{TARGET_COUNT}} leads in {{INDUSTRY}}"
        result = inject_brand(template, brand, instance)
        assert result == "TestCorp targets 500 leads in pet"

    def test_brand_takes_precedence(self):
        """If both configs define the same key, brand wins."""
        brand = {"identity": {"BRAND_NAME": "BrandVal"}}
        instance = {"crm_pipeline": {"BRAND_NAME": "InstanceVal"}}
        template = "Hello {{BRAND_NAME}}"
        result = inject_brand(template, brand, instance)
        assert result == "Hello BrandVal"

    def test_instance_only(self):
        """Instance vars work even with empty brand config."""
        instance = {
            "dashboard": {"MAP_CENTER_LAT": "-23.6235", "MAP_CENTER_LNG": "-46.5519"},
        }
        template = "Center: {{MAP_CENTER_LAT}}, {{MAP_CENTER_LNG}}"
        result = inject_brand(template, {}, instance)
        assert result == "Center: -23.6235, -46.5519"

    def test_instance_none_loads_from_disk(self):
        """When instance_config=None, it attempts disk load (returns {} if missing)."""
        brand = {"identity": {"BRAND_NAME": "X"}}
        result = inject_brand("Hello {{BRAND_NAME}}", brand, None)
        assert "X" in result

    def test_all_23_instance_vars_registered(self):
        """Verify INSTANCE_VARS set has exactly 23 known variables."""
        assert len(INSTANCE_VARS) == 23
        # Spot-check critical vars
        for var in ("INDUSTRY", "MAP_CENTER_LAT", "DB_PROVIDER", "SEARCH_PROVIDERS"):
            assert var in INSTANCE_VARS

    def test_full_crm_pipeline(self):
        """All 12 CRM pipeline vars inject correctly."""
        instance = {"crm_pipeline": {
            "INDUSTRY": "pet", "TARGET_COUNT": "500",
            "BATCH_SOURCES": "directories, google_maps",
            "DIRECTORY_SOURCES": "guialocal, ifood",
            "SEARCH_QUERIES": "pet shop {cidade}",
            "CATEGORIES": "pet_shop, clinica_vet",
            "CITIES": "Sao Caetano, Santo Andre",
            "RADIUS_KM": "50",
            "HASHTAGS": "#petshop, #gatosdobrasil",
            "MARKETPLACES": "iFood, Rappi",
            "CNAE_CODES": "4789-0/04, 7500-1/00",
            "LEGAL_SOURCES": "Casa dos Dados, ReceitaWS",
        }}
        template = "{{INDUSTRY}} {{TARGET_COUNT}} {{RADIUS_KM}} {{CNAE_CODES}}"
        result = inject_brand(template, {}, instance)
        assert "pet" in result
        assert "500" in result
        assert "50" in result
        assert "4789-0/04" in result

    def test_dashboard_vars(self):
        instance = {"dashboard": {
            "MAP_CENTER_LAT": "-23.6235", "MAP_CENTER_LNG": "-46.5519",
            "MAP_ZOOM": "12", "CRM_DATA_SOURCE": "inline",
        }}
        template = "lat={{MAP_CENTER_LAT}} lng={{MAP_CENTER_LNG}} zoom={{MAP_ZOOM}} src={{CRM_DATA_SOURCE}}"
        result = inject_brand(template, {}, instance)
        assert "-23.6235" in result
        assert "12" in result
        assert "inline" in result

    def test_infrastructure_vars(self):
        instance = {"infrastructure": {
            "DB_PROVIDER": "supabase", "TABLES": "contatos, interacoes",
            "MAP_PROVIDER": "leaflet_osm", "AUTH_METHOD": "supabase_auth",
        }}
        template = "db={{DB_PROVIDER}} auth={{AUTH_METHOD}}"
        result = inject_brand(template, {}, instance)
        assert result == "db=supabase auth=supabase_auth"

    def test_research_vars(self):
        instance = {"research": {
            "SEARCH_PROVIDERS": "SERPER, FIRECRAWL",
            "MERGE_STRATEGY": "dedup_by_cnpj",
            "DEDUP_FIELDS": "cnpj, phone, name",
        }}
        template = "providers={{SEARCH_PROVIDERS}} merge={{MERGE_STRATEGY}}"
        result = inject_brand(template, {}, instance)
        assert "SERPER" in result
        assert "dedup_by_cnpj" in result


class TestDerivedVariables:
    """Test derived variables including new BRAND_DOMAIN."""

    def test_brand_domain_from_logo_url(self):
        flat = {"BRAND_LOGO_URL": "https://brand.example/logo.png"}
        derived = compute_derived(flat)
        assert derived.get("BRAND_DOMAIN") == "brand.example"

    def test_brand_domain_from_favicon_url(self):
        flat = {"BRAND_FAVICON_URL": "https://example.com/favicon.ico"}
        derived = compute_derived(flat)
        assert derived.get("BRAND_DOMAIN") == "example.com"

    def test_brand_domain_logo_takes_priority(self):
        flat = {
            "BRAND_LOGO_URL": "https://primary.com/logo.png",
            "BRAND_FAVICON_URL": "https://fallback.com/fav.ico",
        }
        derived = compute_derived(flat)
        assert derived["BRAND_DOMAIN"] == "primary.com"

    def test_brand_domain_placeholder_skipped(self):
        flat = {"BRAND_LOGO_URL": "{{LOGO_URL}}"}
        derived = compute_derived(flat)
        assert "BRAND_DOMAIN" not in derived

    def test_brand_domain_no_url_no_derive(self):
        flat = {"BRAND_NAME": "TestCo"}
        derived = compute_derived(flat)
        assert "BRAND_DOMAIN" not in derived

    def test_region_alias(self):
        flat = {"BRAND_REGION": "ABC Paulista"}
        derived = compute_derived(flat)
        assert derived.get("REGION") == "ABC Paulista"

    def test_platforms_alias(self):
        flat = {"BRAND_CHANNELS": "Instagram, TikTok, YouTube"}
        derived = compute_derived(flat)
        assert derived.get("PLATFORMS") == "Instagram, TikTok, YouTube"


class TestCountUnresolvedExtended:
    """Verify count_unresolved catches instance vars too."""

    def test_catches_instance_vars(self):
        text = "Industry: {{INDUSTRY}}, Brand: {{BRAND_NAME}}"
        unresolved = count_unresolved(text)
        assert "INDUSTRY" in unresolved
        assert "BRAND_NAME" in unresolved

    def test_catches_map_vars(self):
        text = "{{MAP_CENTER_LAT}} {{MAP_CENTER_LNG}}"
        unresolved = count_unresolved(text)
        assert "MAP_CENTER_LAT" in unresolved

    def test_ignores_lowercase(self):
        """Lowercase vars like {{name}} are not CEX variables."""
        text = "Hello {{name}}, your {{BRAND_NAME}} is ready"
        unresolved = count_unresolved(text)
        assert "name" not in unresolved
        assert "BRAND_NAME" in unresolved


# -- brand_validate.py --

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


# -- brand_propagate.py --

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


# -- brand_audit.py --

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
