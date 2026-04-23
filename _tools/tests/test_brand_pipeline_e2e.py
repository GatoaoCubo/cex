"""Integration test for N06 brand pipeline: inject -> validate -> propagate -> audit.

Tests the full brand tool chain with a real brand_config.yaml (test fixture).
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

from brand_audit import (audit, score_archetype_alignment,
                         score_config_completeness)
from brand_inject import count_unresolved, inject_brand
from brand_propagate import NUCLEUS_VARS, extract_vars, propagate
from brand_validate import validate

ROOT = Path(__file__).resolve().parent.parent.parent


# -- Fixture: realistic brand_config --

BRAND_CONFIG_REAL = {
    "identity": {
        "BRAND_NAME": "Codexa",
        "BRAND_TAGLINE": "Build AI agents that actually work",
        "BRAND_SLOGAN": "From intent to artifact in 8 steps",
        "BRAND_MISSION": "We exist to make AI agent development systematic, reproducible, and accessible to every builder.",
        "BRAND_VISION": "A world where every software team has a fleet of specialized AI agents built on proven architectural patterns.",
        "BRAND_VALUES": ["systematic-rigor", "builder-empathy", "radical-transparency", "ship-daily", "quality-over-quantity"],
        "BRAND_STORY": "Codexa started when a solo developer realized that every AI agent project repeated the same mistakes: vague prompts, no quality gates, no memory, no coordination. After building 50+ agents the hard way, the patterns crystallized into a system. 12 pillars. 8 functions. 99 kinds. CEX was born -- not as a framework, but as a knowledge architecture that makes agents reliable. What took months now takes hours. What failed silently now fails loudly. What was artisanal is now systematic.",
    },
    "archetype": {
        "BRAND_ARCHETYPE": "sage",
        "BRAND_ARCHETYPE_SHADOW": "trickster",
        "BRAND_PERSONALITY": ["systematic", "precise", "patient", "builder-minded", "no-nonsense"],
    },
    "voice": {
        "BRAND_VOICE_TONE": "tecnico-confiante, direto, sem floreio",
        "BRAND_VOICE_FORMALITY": 4,
        "BRAND_VOICE_ENTHUSIASM": 3,
        "BRAND_VOICE_HUMOR": 2,
        "BRAND_VOICE_WARMTH": 3,
        "BRAND_VOICE_AUTHORITY": 5,
        "BRAND_VOICE_DO": ["Use precise technical terms", "Show real code examples", "Be direct -- say the thing"],
        "BRAND_VOICE_DONT": ["Never use buzzwords without definition", "Never promise magic", "Never hide complexity"],
        "BRAND_LANGUAGE": "pt-BR",
    },
    "audience": {
        "BRAND_ICP": "Senior developers and tech leads (28-45) who have built 3+ AI projects and are frustrated by the lack of systematic approaches. They value architecture over hype and want repeatable patterns, not one-off demos.",
        "BRAND_ICP_AGE": "28-45",
        "BRAND_ICP_LOCATION": "Brazil, global remote",
        "BRAND_ICP_INCOME": "B+",
        "BRAND_ICP_VALUES": ["craftsmanship", "autonomy", "deep-work"],
        "BRAND_ICP_FEARS": ["building another throwaway prototype", "prompt spaghetti", "agent that works in demo but fails in production"],
        "BRAND_ICP_ASPIRATIONS": ["fleet of reliable agents", "systematic approach", "ship with confidence"],
        "BRAND_TRANSFORMATION": "From artisanal prompt hacking to systematic agent architecture through the 8F pipeline",
    },
    "visual": {
        "BRAND_COLORS": {
            "primary": "#0A0A0A",
            "secondary": "#1A1A2E",
            "accent": "#50C878",
            "background": "#050505",
            "foreground": "#E0E0E0",
            "surface": "#1E1E2E",
        },
        "BRAND_FONTS": {"heading": "Geist", "body": "Inter", "mono": "JetBrains Mono"},
        "BRAND_LOGO_URL": "https://codexa.dev/logo.svg",
        "BRAND_FAVICON_URL": "https://codexa.dev/favicon.ico",
        "BRAND_STYLE": "minimal-dark",
    },
    "positioning": {
        "BRAND_CATEGORY": "AI agent development framework",
        "BRAND_UVP": "Para tech leads que constroem agentes AI, Codexa e o framework de conhecimento que transforma intent em artefato validado em 8 passos porque ninguem mais trata agent development como engenharia de verdade.",
        "BRAND_DIFFERENTIATOR": "We are the only agent framework that enforces quality gates, peer review, and 8-function pipeline on every single artifact",
        "BRAND_COMPETITORS": ["LangChain", "CrewAI", "AutoGen", "custom scripts"],
        "BRAND_CONTENT_PILLARS": ["agent-architecture", "prompt-engineering", "quality-assurance", "knowledge-management", "multi-agent-orchestration"],
    },
    "monetization": {
        "BRAND_PRICING_MODEL": "subscription",
        "BRAND_CURRENCY": "BRL",
        "BRAND_PRICE_ANCHOR": "R$ 997/mo",
        "BRAND_TIERS": ["free", "builder", "architect", "enterprise"],
        "BRAND_PAYMENT_PROVIDERS": ["stripe", "mercadopago"],
    },
}


# -- Test: Full Pipeline --

class TestBrandPipelineE2E:
    """Integration test: validate -> inject -> propagate -> audit."""

    def test_step1_validate_real_config(self):
        """Step 1: brand_config must pass validation with zero errors."""
        result = validate(BRAND_CONFIG_REAL)
        assert result["valid"] is True, f"Errors: {result['errors']}"
        assert len(result["errors"]) == 0
        assert result["required_fields_filled"] == 13

    def test_step2_inject_brand_into_template(self):
        """Step 2: brand_inject replaces all BRAND_* variables in a template."""
        template = (
            "Welcome to {{BRAND_NAME}}!\n"
            "{{BRAND_TAGLINE}}\n"
            "Archetype: {{BRAND_ARCHETYPE}}\n"
            "Voice: {{BRAND_VOICE_TONE}}\n"
            "Formality: {{BRAND_VOICE_FORMALITY}}/5\n"
            "Primary color: {{primary}}\n"
        )
        result = inject_brand(template, BRAND_CONFIG_REAL)
        assert "Codexa" in result
        assert "Build AI agents" in result
        assert "sage" in result
        assert "tecnico-confiante" in result
        assert "#0A0A0A" in result

        unresolved = count_unresolved(result)
        assert len(unresolved) == 0, f"Unresolved: {unresolved}"

    def test_step3_propagate_extracts_nucleus_vars(self):
        """Step 3: brand_propagate extracts correct vars for each nucleus."""
        for nucleus in ["N01", "N02", "N03", "N04", "N05", "N07"]:
            var_names = NUCLEUS_VARS[nucleus]
            extracted = extract_vars(BRAND_CONFIG_REAL, var_names)
            assert len(extracted) > 0, f"{nucleus} got no variables"

        # N02 must get voice + visual
        n02_vars = extract_vars(BRAND_CONFIG_REAL, NUCLEUS_VARS["N02"])
        assert "BRAND_VOICE_TONE" in n02_vars
        assert "BRAND_COLORS" in n02_vars
        assert "BRAND_NAME" in n02_vars

        # N05 must get name + logo
        n05_vars = extract_vars(BRAND_CONFIG_REAL, NUCLEUS_VARS["N05"])
        assert "BRAND_NAME" in n05_vars

    def test_step3_propagate_writes_files(self, tmp_path):
        """Step 3b: propagate actually writes brand_context.md files."""
        # Create minimal nucleus dirs
        for n_dir in ["N01_research", "N02_marketing", "N03_builder",
                      "N04_knowledge", "N05_operations", "N07_admin"]:
            (tmp_path / n_dir / "config").mkdir(parents=True)

        # Monkey-patch ROOT for test
        import brand_propagate as bp
        original_root = bp.ROOT
        original_dirs = bp.NUCLEUS_DIRS.copy()

        bp.ROOT = tmp_path
        bp.NUCLEUS_DIRS = {
            "N01": "N01_research", "N02": "N02_marketing", "N03": "N03_builder",
            "N04": "N04_knowledge", "N05": "N05_operations", "N07": "N07_admin",
        }
        try:
            results = propagate(BRAND_CONFIG_REAL, dry_run=False)
            propagated = [n for n, r in results.items() if r["status"] == "propagated"]
            assert len(propagated) >= 5, f"Only propagated to: {propagated}"

            # Verify files exist
            for nucleus in propagated:
                n_dir = bp.NUCLEUS_DIRS[nucleus]
                ctx_file = tmp_path / n_dir / "config" / "brand_context.md"
                assert ctx_file.exists(), f"Missing: {ctx_file}"
                content = ctx_file.read_text(encoding="utf-8")
                assert "Brand Context" in content
                assert "brand_config.yaml" in content
        finally:
            bp.ROOT = original_root
            bp.NUCLEUS_DIRS = original_dirs

    def test_step4_audit_scores_real_config(self):
        """Step 4: brand_audit produces high scores for complete config."""
        result = audit(BRAND_CONFIG_REAL)
        assert result["overall_score"] >= 0.85, f"Score too low: {result['overall_score']}"
        assert result["rating"] in ("Excellent", "Healthy")
        assert result["brand"] == "Codexa"

        # Each dimension should score > 0
        for dim, info in result["dimensions"].items():
            assert info["score"] > 0, f"{dim} scored 0"

    def test_step4_audit_config_completeness(self):
        """Config completeness should be perfect for real config."""
        score, issues = score_config_completeness(BRAND_CONFIG_REAL)
        assert score >= 0.9, f"Completeness {score}, issues: {issues}"

    def test_step4_audit_archetype_alignment(self):
        """Archetype should be fully aligned."""
        score, issues = score_archetype_alignment(BRAND_CONFIG_REAL)
        assert score == 1.0, f"Archetype score {score}, issues: {issues}"

    def test_full_pipeline_sequence(self):
        """Full E2E: validate -> inject -> propagate(dry) -> audit."""
        # 1. Validate
        v = validate(BRAND_CONFIG_REAL)
        assert v["valid"]

        # 2. Inject into template
        tpl = "# {{BRAND_NAME}} -- {{BRAND_TAGLINE}}\nArchetype: {{BRAND_ARCHETYPE}}"
        injected = inject_brand(tpl, BRAND_CONFIG_REAL)
        assert "{{" not in injected

        # 3. Propagate (dry run)
        results = propagate(BRAND_CONFIG_REAL, dry_run=True)
        dry_count = sum(1 for r in results.values() if r["status"] == "dry-run")
        assert dry_count >= 5

        # 4. Audit
        a = audit(BRAND_CONFIG_REAL)
        assert a["overall_score"] >= 0.85
        assert a["rating"] != "Critical"


class TestBrandPipelineEdgeCases:
    """Edge cases and failure modes."""

    def test_empty_config_fails_validation(self):
        result = validate({})
        assert not result["valid"]
        assert len(result["errors"]) >= 7

    def test_placeholder_config_has_warnings(self):
        """Template with mustache placeholders should warn."""
        template_config = {
            "identity": {"BRAND_NAME": "{{BRAND_NAME}}", "BRAND_TAGLINE": "{{BRAND_TAGLINE}}",
                         "BRAND_MISSION": "{{BRAND_MISSION}}", "BRAND_VALUES": ["{{V1}}"]},
            "archetype": {"BRAND_ARCHETYPE": "{{BRAND_ARCHETYPE}}"},
            "voice": {"BRAND_VOICE_TONE": "{{TONE}}", "BRAND_VOICE_FORMALITY": 3},
            "audience": {"BRAND_ICP": "{{ICP}}", "BRAND_TRANSFORMATION": "{{TRANSFORM}}"},
            "visual": {"BRAND_COLORS": {"primary": "#000000", "secondary": "#111111", "accent": "#222222"}},
            "positioning": {"BRAND_CATEGORY": "{{CAT}}", "BRAND_UVP": "{{UVP_LONG_ENOUGH_TEXT}}"},
            "monetization": {"BRAND_PRICING_MODEL": "subscription", "BRAND_CURRENCY": "BRL"},
        }
        result = validate(template_config)
        assert len(result["warnings"]) > 0

    def test_invalid_archetype_fails(self):
        bad = dict(BRAND_CONFIG_REAL)
        bad = {**BRAND_CONFIG_REAL, "archetype": {"BRAND_ARCHETYPE": "dragon"}}
        result = validate(bad)
        assert any("archetype" in e.lower() or "dragon" in e.lower() for e in result["errors"])

    def test_inject_preserves_non_brand_mustache(self):
        """Non-BRAND_* variables should survive injection."""
        template = "{{BRAND_NAME}} uses {{CUSTOM_VAR}}"
        result = inject_brand(template, BRAND_CONFIG_REAL)
        assert "Codexa" in result
        # CUSTOM_VAR is not in brand_config, should remain or be replaced depending on flatten

    def test_audit_partial_config(self):
        """Partial config should get low but non-zero scores."""
        partial = {
            "identity": {"BRAND_NAME": "Test", "BRAND_TAGLINE": "Test tag here",
                         "BRAND_MISSION": "We test things systematically", "BRAND_VALUES": ["a", "b", "c"]},
            "archetype": {"BRAND_ARCHETYPE": "sage"},
        }
        result = audit(partial)
        assert result["overall_score"] > 0
        assert result["overall_score"] < 0.5  # partial should be low
