"""
Regression tests for wave1_builder_gen_v2.py

Tests the 4 systemic fixes from HYBRID_REVIEW + HYBRID_REVIEW2 audits:
  1. system_prompt llm_function=BECOME (not INJECT)
  2. schema frontmatter has quality: null
  3. validator rejects blockchain keywords for non-blockchain kinds (e.g. voice_pipeline)
  4. validator rejects bare {{field}} placeholders in output_template

Usage:
  python _tools/test_wave1_builder_gen_v2.py
"""
import os
import sys

# Add _tools to path so we can import the generator
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from wave1_builder_gen_v2 import (DOMAIN_KEYWORDS, ISO_SPECS,
                                  derive_id_pattern, generate_frontmatter,
                                  validate_iso_body)

PASS = "[PASS]"
FAIL = "[FAIL]"


def test_system_prompt_llm_function_is_become() -> None:
    """
    Fix 1: system_prompt ISO MUST have llm_function=BECOME in both
    ISO_SPECS definition and generated frontmatter.
    """
    # Find system_prompt entry in ISO_SPECS
    sp_spec = None
    for spec in ISO_SPECS:
        if spec[1] == "system_prompt":
            sp_spec = spec
            break

    assert sp_spec is not None, "system_prompt not found in ISO_SPECS"
    assert sp_spec[3] == "BECOME", (
        "system_prompt llm_function in ISO_SPECS should be BECOME, got: " + sp_spec[3]
    )

    # Verify generate_frontmatter outputs BECOME
    meta = {
        "pillar": "P04",
        "llm_function": "CALL",
        "naming": "p04_vp_{{name}}",
        "max_bytes": 5120,
        "description": "voice pipeline",
        "boundary": "no video",
    }
    fm = generate_frontmatter(sp_spec, "voice_pipeline", meta)
    assert "llm_function: BECOME" in fm, (
        "generate_frontmatter must emit 'llm_function: BECOME' for system_prompt. Got:\n" + fm
    )
    print(PASS + " system_prompt llm_function=BECOME (ISO_SPECS + frontmatter)")


def test_schema_quality_field_is_null() -> None:
    """
    Fix 2: schema ISO frontmatter must have quality: null.
    All ISOs should emit quality: null -- verify for the schema ISO specifically.
    """
    schema_spec = None
    for spec in ISO_SPECS:
        if spec[1] == "schema":
            schema_spec = spec
            break

    assert schema_spec is not None, "schema not found in ISO_SPECS"

    meta = {
        "pillar": "P04",
        "llm_function": "CONSTRAIN",
        "naming": "p04_vp_{{name}}",
        "max_bytes": 5120,
        "description": "voice pipeline schema",
        "boundary": "no audio post-processing",
    }
    fm = generate_frontmatter(schema_spec, "voice_pipeline", meta)
    assert "quality: null" in fm, (
        "generate_frontmatter must emit 'quality: null' for schema ISO. Got:\n" + fm
    )
    # Also verify it does not emit a non-null quality value
    import re
    quality_line = re.search(r"^quality:\s*(.+)$", fm, re.MULTILINE)
    assert quality_line, "No quality field found in frontmatter"
    assert quality_line.group(1).strip() == "null", (
        "quality must be 'null', got: " + quality_line.group(1)
    )
    print(PASS + " schema quality: null in frontmatter")


def test_validator_rejects_blockchain_in_architecture() -> None:
    """
    Fix 6: architecture ISO containing blockchain keywords for voice_pipeline MUST be rejected.
    Audit found architecture ISOs with trading/DeFi/Solana text for voice builders.
    """
    blockchain_body = (
        "## Component Inventory\n"
        "| Solana Validator | Validates transactions on-chain | P09 | Active |\n"
        "| Ethereum Node | Staking and DeFi protocol interface | P09 | Active |\n"
        "| trading engine | Market order execution | P09 | Active |\n"
        "## Architectural Position\n"
        "This builder participates in the DeFi ecosystem for audio streaming.\n"
    )

    passed, errors = validate_iso_body("architecture", "voice_pipeline", blockchain_body)

    assert not passed, (
        "Validator should REJECT architecture ISO with blockchain keywords for voice_pipeline"
    )
    # At least one error should mention wrong domain or the keyword
    relevant = [e for e in errors if any(
        kw in e.lower() for kw in ["domain", "blockchain", "trading", "solana", "ethereum", "defi", "staking", "wrong"]
    )]
    assert relevant, (
        "Error messages should mention wrong-domain keywords. Got: " + str(errors)
    )
    print(PASS + " validator rejects blockchain keywords in voice_pipeline architecture ISO")


def test_validator_rejects_bare_placeholders_in_output_template() -> None:
    """
    Fix 5: output_template ISO with bare {{field}} placeholders and no
    schema context (no <!-- comments -->, no 'schema' or 'frontmatter' mention) MUST be rejected.
    Audit found templates with '{{placeholder}} content for...' literal text.
    """
    bare_body = (
        "## Output Template\n"
        "{{id}} some field value here.\n"
        "{{kind}} another value.\n"
        "{{title}} content for the title.\n"
        "{{domain}} your domain here.\n"
    )

    passed, errors = validate_iso_body("output_template", "voice_pipeline", bare_body)

    assert not passed, (
        "Validator should REJECT output_template with bare placeholders and no schema context"
    )
    placeholder_errors = [e for e in errors if "placeholder" in e.lower()]
    assert placeholder_errors, (
        "Error should mention placeholders. Got: " + str(errors)
    )
    print(PASS + " validator rejects bare {{field}} placeholders in output_template")


def test_validator_accepts_good_output_template() -> None:
    """
    Regression: output_template WITH schema context (comments or 'frontmatter' reference)
    should pass the placeholder check.
    """
    good_body = (
        "## Output Template\n"
        "```yaml\n"
        "id: {{id}}  <!-- required: ID matching schema pattern e.g. p04_vp_my_pipeline -->\n"
        "kind: {{kind}}  <!-- must be: voice_pipeline -->\n"
        "quality: null  <!-- always null; never self-score -->\n"
        "```\n"
        "## Body Structure\n"
        "Frontmatter must include all required schema fields.\n"
        "audio stream latency VAD TTS\n"
    )

    passed, errors = validate_iso_body("output_template", "voice_pipeline", good_body)
    assert passed, (
        "Good output_template with comments should PASS. Errors: " + str(errors)
    )
    print(PASS + " good output_template with comments passes validator")


def test_domain_keywords_coverage() -> None:
    """
    Sanity check: DOMAIN_KEYWORDS covers all Wave 2 voice kinds.
    These had the worst domain mismatch issues per HYBRID_REVIEW2.
    """
    voice_kinds = [
        "voice_pipeline", "realtime_session", "vad_config",
        "tts_provider", "stt_provider", "prosody_config", "transport_config",
    ]
    missing = [k for k in voice_kinds if k not in DOMAIN_KEYWORDS]
    assert not missing, "Missing DOMAIN_KEYWORDS for voice kinds: " + str(missing)
    print(PASS + " DOMAIN_KEYWORDS covers all 7 voice kinds")


def test_derive_id_pattern() -> None:
    """
    Verify derive_id_pattern produces sensible regex from naming templates.
    """
    cases = [
        ("p04_vp_{{name}}", "^p04_vp_[a-z][a-z0-9_]+$"),
        ("p02_rlalg_{{name}}", "^p02_rlalg_[a-z][a-z0-9_]+$"),
        ("p07_rwm_{{name}}_{{timestamp}}", "^p07_rwm_[a-z][a-z0-9_]+_[0-9]+$"),
    ]
    for naming, expected in cases:
        result = derive_id_pattern(naming, "test_kind")
        assert result == expected, (
            "derive_id_pattern('" + naming + "') expected '" + expected + "' got '" + result + "'"
        )
    print(PASS + " derive_id_pattern produces correct regexes")


def run_all_tests() -> bool:
    tests = [
        test_system_prompt_llm_function_is_become,
        test_schema_quality_field_is_null,
        test_validator_rejects_blockchain_in_architecture,
        test_validator_rejects_bare_placeholders_in_output_template,
        test_validator_accepts_good_output_template,
        test_domain_keywords_coverage,
        test_derive_id_pattern,
    ]
    passed = 0
    failed = 0
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(FAIL + " " + test.__name__ + ": " + str(e))
            failed += 1
        except Exception as e:
            print("[ERROR] " + test.__name__ + ": " + type(e).__name__ + ": " + str(e))
            failed += 1

    print("\n" + "="*50)
    print("Results: " + str(passed) + " passed, " + str(failed) + " failed out of " + str(len(tests)))
    print("="*50)
    return failed == 0


if __name__ == "__main__":
    success = run_all_tests()
    sys.exit(0 if success else 1)
