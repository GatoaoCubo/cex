# -*- coding: utf-8 -*-
"""brand_propagate.py -- Push brand context to all nuclei prompts.

Reads .cex/brand/brand_config.yaml and injects relevant variables into
each nucleus's system prompt, agent card, and boot file.

Usage:
    python _tools/brand_propagate.py [--dry-run] [--nucleus N02] [--config path]
"""
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
BRAND_CONFIG = ROOT / ".cex" / "brand" / "brand_config.yaml"

# What each nucleus needs from brand_config
NUCLEUS_VARS = {
    "N01": ["BRAND_ICP", "BRAND_COMPETITORS", "BRAND_CATEGORY", "BRAND_CONTENT_PILLARS",
            "BRAND_ICP_LOCATION", "BRAND_ICP_VALUES", "BRAND_COUNTRY"],
    "N02": ["BRAND_VOICE_TONE", "BRAND_VOICE_FORMALITY", "BRAND_VOICE_ENTHUSIASM",
            "BRAND_VOICE_HUMOR", "BRAND_VOICE_WARMTH", "BRAND_VOICE_AUTHORITY",
            "BRAND_VOICE_DO", "BRAND_VOICE_DONT", "BRAND_COLORS", "BRAND_FONTS",
            "BRAND_VALUES", "BRAND_NAME", "BRAND_TAGLINE", "BRAND_LANGUAGE",
            "BRAND_PERSON", "BRAND_ENERGY", "BRAND_BIO", "BRAND_HASHTAG"],
    "N03": ["BRAND_COLORS", "BRAND_FONTS", "BRAND_STYLE", "BRAND_NAME"],
    "N04": ["BRAND_NAME", "BRAND_CATEGORY", "BRAND_CONTENT_PILLARS",
            "BRAND_LANGUAGE", "BRAND_TAGS"],
    "N05": ["BRAND_NAME", "BRAND_LOGO_URL", "BRAND_FAVICON_URL",
            "BRAND_PRICING_MODEL", "BRAND_PAYMENT_PROVIDERS"],
    "N06": ["BRAND_NAME", "BRAND_TAGLINE", "BRAND_ESSENCE", "BRAND_MANIFESTO",
            "BRAND_BIO", "BRAND_ARCHETYPE", "BRAND_STORY"],
    "N07": ["BRAND_NAME", "BRAND_TAGLINE"],
}

NUCLEUS_DIRS = {
    "N01": "N01_intelligence",
    "N02": "N02_marketing",
    "N03": "N03_builder",
    "N04": "N04_knowledge",
    "N05": "N05_operations",
    "N06": "N06_commercial",
    "N07": "N07_admin",
}


def load_brand_config(path: Path = BRAND_CONFIG) -> dict:
    """Load and return brand config."""
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def extract_vars(config: dict, var_names: list) -> dict:
    """Extract specific variables from nested config."""
    result = {}
    for section in config.values():
        if isinstance(section, dict):
            for key, val in section.items():
                if key in var_names:
                    result[key] = val
    return result


def format_brand_context(nucleus: str, variables: dict) -> str:
    """Format brand context block for injection into prompts."""
    lines = [
        "## Brand Context (injected by brand_propagate.py)",
        "## Source: .cex/brand/brand_config.yaml",
        "",
    ]
    for key, val in sorted(variables.items()):
        if isinstance(val, dict):
            lines.append(f"### {key}")
            for k2, v2 in val.items():
                lines.append(f"- {k2}: {v2}")
        elif isinstance(val, list):
            lines.append(f"- {key}: {', '.join(str(v) for v in val)}")
        else:
            lines.append(f"- {key}: {val}")
    return "\n".join(lines)


def propagate(config: dict, target_nuclei: list = None, dry_run: bool = False) -> dict:
    """Propagate brand variables to nuclei."""
    results = {}
    targets = target_nuclei or list(NUCLEUS_VARS.keys())

    for nucleus in targets:
        if nucleus not in NUCLEUS_VARS:
            results[nucleus] = {"status": "skip", "reason": "unknown nucleus"}
            continue

        var_names = NUCLEUS_VARS[nucleus]
        variables = extract_vars(config, var_names)

        # Filter out placeholders
        real_vars = {k: v for k, v in variables.items()
                     if v is not None and not str(v).startswith("{{")}

        if not real_vars:
            results[nucleus] = {"status": "skip", "reason": "no resolved variables"}
            continue

        context_block = format_brand_context(nucleus, real_vars)
        nucleus_dir = ROOT / NUCLEUS_DIRS.get(nucleus, "")

        # Write brand context file to nucleus
        brand_ctx_path = nucleus_dir / "config" / "brand_context.md"

        if dry_run:
            results[nucleus] = {
                "status": "dry-run",
                "vars_count": len(real_vars),
                "vars": list(real_vars.keys()),
                "would_write": str(brand_ctx_path),
            }
        else:
            brand_ctx_path.parent.mkdir(parents=True, exist_ok=True)
            brand_ctx_path.write_text(
                f"---\nid: brand_context_{nucleus.lower()}\nkind: config\n"
                f"pillar: P09\ntitle: Brand Context for {nucleus}\n"
                f"version: 1.0.0\ncreated: 2026-04-01\nauthor: n06_commercial\n"
                f"quality: null\ntags: [brand, context, {nucleus.lower()}]\n"
                f"tldr: Auto-generated brand context for {nucleus} from brand_config.yaml\n"
                f"density_score: 0.90\n---\n\n{context_block}\n",
                encoding="utf-8"
            )
            results[nucleus] = {
                "status": "propagated",
                "vars_count": len(real_vars),
                "path": str(brand_ctx_path),
            }

    return results


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Propagate brand context to nuclei")
    parser.add_argument("--config", default=str(BRAND_CONFIG), help="Path to brand_config.yaml")
    parser.add_argument("--nucleus", "-n", help="Target specific nucleus (e.g., N02)")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be done")
    parser.add_argument("--json", action="store_true", help="Output as JSON")
    args = parser.parse_args()

    config = load_brand_config(Path(args.config))
    if not config:
        print(f"[FAIL] No brand_config at {args.config}")
        sys.exit(1)

    targets = [args.nucleus.upper()] if args.nucleus else None
    results = propagate(config, targets, dry_run=args.dry_run)

    if args.json:
        import json
        print(json.dumps(results, indent=2))
    else:
        mode = "[DRY RUN] " if args.dry_run else ""
        print(f"{mode}Brand Propagation Results:")
        for nucleus, info in results.items():
            status = info["status"]
            if status == "propagated":
                print(f"  [OK] {nucleus}: {info['vars_count']} vars -> {info['path']}")
            elif status == "dry-run":
                print(f"  [DRY] {nucleus}: would write {info['vars_count']} vars -> {info['would_write']}")
                print(f"       vars: {', '.join(info['vars'])}")
            else:
                print(f"  [SKIP] {nucleus}: {info.get('reason', 'skipped')}")


if __name__ == "__main__":
    main()
