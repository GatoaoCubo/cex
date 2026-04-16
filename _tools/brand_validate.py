# -*- coding: utf-8 -*-
"""brand_validate.py -- Validate brand_config.yaml against schema.

Checks required fields, enum values, format constraints (HEX, language code),
and value quality (non-placeholder, non-empty).

Usage:
    python _tools/brand_validate.py [--config path] [--strict] [--json]
"""
import sys
import re
from pathlib import Path
from typing import Any

try:
    import yaml
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml", "-q"])
    import yaml

ROOT = Path(__file__).resolve().parent.parent
BRAND_CONFIG = ROOT / ".cex" / "brand" / "brand_config.yaml"
SCHEMA_PATH = ROOT / ".cex" / "brand" / "brand_config_schema.yaml"

VALID_ARCHETYPES = {
    "creator", "hero", "sage", "explorer", "rebel", "magician",
    "lover", "caregiver", "jester", "ruler", "innocent", "everyman"
}

VALID_PRICING_MODELS = {
    "subscription", "one-time", "credits", "freemium", "marketplace", "hybrid"
}

HEX_PATTERN = re.compile(r"^#[0-9a-fA-F]{6}$")
LANG_PATTERN = re.compile(r"^[a-z]{2}-[A-Z]{2}$")
TRANSFORM_PATTERN = re.compile(r"From .+ to .+ through .+", re.IGNORECASE)


def is_placeholder(value: Any) -> bool:
    """Check if value is still a mustache placeholder."""
    if value is None:
        return True
    s = str(value)
    return s.startswith("{{") and s.endswith("}}")


def validate_section(
    config: dict[str, Any],
    section: str,
    required: list[str],
    errors: list[str],
    warnings: list[str],
) -> None:
    """Validate a section of brand_config."""
    if section not in config:
        errors.append(f"Missing section: {section}")
        return
    data = config[section]
    if not isinstance(data, dict):
        errors.append(f"Section {section} must be a dict, got {type(data).__name__}")
        return
    for field in required:
        if field not in data:
            errors.append(f"Missing required: {section}.{field}")
        elif is_placeholder(data[field]):
            warnings.append(f"Placeholder: {section}.{field} = {data[field]}")


def validate(config: dict[str, Any], strict: bool = False) -> dict[str, Any]:
    """Validate brand_config against schema rules."""
    errors = []
    warnings = []

    # Section: identity
    validate_section(config, "identity",
                     ["BRAND_NAME", "BRAND_TAGLINE", "BRAND_MISSION", "BRAND_VALUES"],
                     errors, warnings)
    if "identity" in config:
        vals = config["identity"].get("BRAND_VALUES", [])
        if isinstance(vals, list) and not is_placeholder(vals):
            if len(vals) < 3:
                errors.append(f"BRAND_VALUES needs 3+ items, has {len(vals)}")
            elif len(vals) > 7:
                warnings.append(f"BRAND_VALUES has {len(vals)} items (recommended 3-7)")

    # Section: archetype
    validate_section(config, "archetype", ["BRAND_ARCHETYPE"], errors, warnings)
    if "archetype" in config:
        arch = config["archetype"].get("BRAND_ARCHETYPE", "")
        if not is_placeholder(arch) and arch.lower() not in VALID_ARCHETYPES:
            errors.append(f"Invalid archetype: '{arch}'. Must be one of: {', '.join(sorted(VALID_ARCHETYPES))}")

    # Section: voice
    validate_section(config, "voice", ["BRAND_VOICE_TONE", "BRAND_VOICE_FORMALITY"], errors, warnings)
    if "voice" in config:
        for dim in ["BRAND_VOICE_FORMALITY", "BRAND_VOICE_ENTHUSIASM", "BRAND_VOICE_HUMOR",
                     "BRAND_VOICE_WARMTH", "BRAND_VOICE_AUTHORITY"]:
            val = config["voice"].get(dim)
            if val is not None and not is_placeholder(val):
                if not isinstance(val, int) or val < 1 or val > 5:
                    errors.append(f"{dim} must be integer 1-5, got {val}")
        lang = config["voice"].get("BRAND_LANGUAGE")
        if lang and not is_placeholder(lang) and not LANG_PATTERN.match(str(lang)):
            warnings.append(f"BRAND_LANGUAGE '{lang}' doesn't match pattern xx-XX")
        person = config["voice"].get("BRAND_PERSON")
        if person and not is_placeholder(person) and str(person) not in ("1st", "2nd", "3rd"):
            warnings.append(f"BRAND_PERSON should be '1st', '2nd', or '3rd', got '{person}'")
        energy = config["voice"].get("BRAND_ENERGY")
        if energy and not is_placeholder(energy) and str(energy) not in ("calm", "moderate", "energetic", "bold"):
            warnings.append(f"BRAND_ENERGY should be calm|moderate|energetic|bold, got '{energy}'")

    # Section: audience
    validate_section(config, "audience", ["BRAND_ICP", "BRAND_TRANSFORMATION"], errors, warnings)
    if "audience" in config:
        transform = config["audience"].get("BRAND_TRANSFORMATION", "")
        if transform and not is_placeholder(transform) and not TRANSFORM_PATTERN.match(str(transform)):
            warnings.append(f"BRAND_TRANSFORMATION doesn't follow 'From X to Y through Z' pattern")

    # Section: visual
    validate_section(config, "visual", ["BRAND_COLORS"], errors, warnings)
    if "visual" in config and "BRAND_COLORS" in config["visual"]:
        colors = config["visual"]["BRAND_COLORS"]
        if isinstance(colors, dict):
            for req in ["primary", "secondary", "accent"]:
                if req not in colors:
                    errors.append(f"Missing required color: BRAND_COLORS.{req}")
                elif not is_placeholder(colors[req]) and not HEX_PATTERN.match(str(colors[req])):
                    errors.append(f"Invalid HEX color: BRAND_COLORS.{req} = {colors[req]}")

    # Section: positioning
    validate_section(config, "positioning", ["BRAND_CATEGORY", "BRAND_UVP"], errors, warnings)
    if "positioning" in config:
        uvp = config["positioning"].get("BRAND_UVP", "")
        if uvp and not is_placeholder(uvp) and len(str(uvp)) < 20:
            warnings.append(f"BRAND_UVP is short ({len(str(uvp))} chars, recommended 20+)")

    # Section: monetization
    validate_section(config, "monetization", ["BRAND_PRICING_MODEL", "BRAND_CURRENCY"], errors, warnings)
    if "monetization" in config:
        model = config["monetization"].get("BRAND_PRICING_MODEL", "")
        if model and not is_placeholder(model) and model not in VALID_PRICING_MODELS:
            errors.append(f"Invalid pricing model: '{model}'. Must be: {', '.join(sorted(VALID_PRICING_MODELS))}")

    if strict:
        errors.extend(warnings)
        warnings = []

    return {
        "valid": len(errors) == 0,
        "errors": errors,
        "warnings": warnings,
        "sections_present": [s for s in ["identity", "archetype", "voice", "audience", "visual", "positioning", "monetization"] if s in config],
        "required_fields_filled": 13 - len([e for e in errors if "Missing required" in e]),
    }


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Validate brand_config.yaml")
    parser.add_argument("--config", default=str(BRAND_CONFIG), help="Path to brand_config.yaml")
    parser.add_argument("--strict", action="store_true", help="Treat warnings as errors")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    parser.add_argument("--check", action="store_true", help="Quick existence check")
    args = parser.parse_args()

    config_path = Path(args.config)
    if not config_path.exists():
        print(f"[FAIL] brand_config not found: {config_path}")
        sys.exit(1)

    with open(config_path, "r", encoding="utf-8") as f:
        config = yaml.safe_load(f) or {}

    if args.check:
        print(f"[OK] brand_config exists: {config_path}")
        sys.exit(0)

    result = validate(config, strict=args.strict)

    if args.json:
        import json
        print(json.dumps(result, indent=2))
    else:
        status = "[OK] VALID" if result["valid"] else "[FAIL] INVALID"
        print(f"{status} -- {result['required_fields_filled']}/13 required fields")
        print(f"Sections: {', '.join(result['sections_present'])}")
        if result["errors"]:
            print(f"\n[FAIL] Errors ({len(result['errors'])}):")
            for e in result["errors"]:
                print(f"  - {e}")
        if result["warnings"]:
            print(f"\n[WARN] Warnings ({len(result['warnings'])}):")
            for w in result["warnings"]:
                print(f"  - {w}")

    sys.exit(0 if result["valid"] else 1)


if __name__ == "__main__":
    main()
