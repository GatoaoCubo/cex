# -*- coding: utf-8 -*-
"""brand_inject.py -- Replace {{BRAND_*}} mustache variables in templates.

Reads .cex/brand/brand_config.yaml, flattens nested keys, and replaces
all {{BRAND_*}} occurrences in input text or files.

Handles:
  - Direct variables: {{BRAND_NAME}} -> "Acme Corp"
  - Derived variables: {{BRAND_SLUG}}, {{BRAND_UPPER}}, {{BRAND_NAME_SHORT}}
  - Aliases: {{BRAND_TONE}} -> BRAND_VOICE_TONE, {{BRAND_VOICE}} -> BRAND_VOICE_TONE
  - Default syntax: {{BRAND_X | default: 'fallback'}} -> fallback (if BRAND_X unset)

Usage:
    python _tools/brand_inject.py <template_file> [--output <out_file>]
    python _tools/brand_inject.py --stdin
    python _tools/brand_inject.py --check  (verify brand_config exists)
"""
import sys
import re
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
BRAND_CONFIG = ROOT / ".cex" / "brand" / "brand_config.yaml"

# Aliases: template variable -> config variable
# These map commonly-used short names to their canonical config keys.
BRAND_ALIASES = {
    "BRAND_TONE":       "BRAND_VOICE_TONE",
    "BRAND_VOICE":      "BRAND_VOICE_TONE",
    "BRAND_NICHE":      "BRAND_CATEGORY",
}

# Regex for {{VAR | default: 'value'}} or {{VAR | default: "value"}} or {{VAR | default: value}}
_DEFAULT_PATTERN = re.compile(
    r"\{\{([A-Z_]+)\s*\|\s*default:\s*['\"]?([^'\"}\]]*)['\"]?\s*\}\}"
)


def load_brand_config(path: Path = BRAND_CONFIG) -> dict:
    """Load brand_config.yaml and return parsed dict."""
    if not path.exists():
        return {}
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f) or {}


def flatten(d: dict, prefix: str = "") -> dict:
    """Flatten nested dict into dot-notation keys.

    Example: {"voice": {"BRAND_VOICE_TONE": "x"}} -> {"BRAND_VOICE_TONE": "x"}
    Also creates prefixed versions: {"voice.BRAND_VOICE_TONE": "x"}
    """
    items = {}
    for k, v in d.items():
        key = f"{prefix}.{k}" if prefix else k
        if isinstance(v, dict):
            items.update(flatten(v, key))
            # Also flatten without section prefix for direct variable access
            items.update(flatten(v, ""))
        elif isinstance(v, list):
            items[k] = ", ".join(str(i) for i in v)
            items[key] = items[k]
        else:
            items[k] = str(v) if v is not None else ""
            if key != k:
                items[key] = items[k]
    return items


def _is_placeholder(val: str) -> bool:
    """Check if a value is still an unresolved placeholder."""
    return not val or val.startswith("{{") or val.startswith("VALUE_") or val.startswith("TRAIT_")


def compute_derived(flat: dict) -> dict:
    """Compute derived brand variables from flattened config.

    Generates:
      BRAND_SLUG       -- kebab-case from BRAND_NAME
      BRAND_UPPER      -- UPPERCASE from BRAND_NAME
      BRAND_NAME_SHORT -- first word of BRAND_NAME
    Applies aliases (BRAND_TONE -> BRAND_VOICE_TONE, etc.)
    """
    derived = {}
    name = flat.get("BRAND_NAME", "")

    if name and not _is_placeholder(name):
        derived["BRAND_SLUG"] = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
        derived["BRAND_UPPER"] = name.upper()
        derived["BRAND_NAME_SHORT"] = name.split()[0] if " " in name else name

    # Apply aliases: short name -> canonical config value
    for alias, canonical in BRAND_ALIASES.items():
        if canonical in flat and not _is_placeholder(flat[canonical]):
            derived[alias] = flat[canonical]

    return derived


def inject_brand(template: str, brand_config: dict = None) -> str:
    """Replace all {{BRAND_*}} and {{KEY}} variables in template text.

    Processing order:
      1. Flatten config into key-value pairs
      2. Compute derived variables (BRAND_SLUG, aliases, etc.)
      3. Replace {{KEY}} exact matches
      4. Resolve {{KEY | default: 'fallback'}} patterns
    """
    if brand_config is None:
        brand_config = load_brand_config()

    flat = flatten(brand_config) if brand_config else {}
    derived = compute_derived(flat)
    # Derived vars fill gaps; config vars take precedence
    merged = {**derived, **{k: v for k, v in flat.items() if not _is_placeholder(v)}}
    result = template

    # Pass 1: Replace {{KEY}} exact matches
    for key, value in merged.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))

    # Pass 2: Resolve {{KEY | default: 'fallback'}} patterns
    # Only triggers for variables NOT already resolved in Pass 1
    def _default_replacer(m):
        var_name = m.group(1)
        default_val = m.group(2)
        # If the var was resolved, this match shouldn't exist; use default
        resolved = merged.get(var_name, "")
        return str(resolved) if resolved and not _is_placeholder(resolved) else default_val

    result = _DEFAULT_PATTERN.sub(_default_replacer, result)

    return result


def count_unresolved(text: str) -> list:
    """Find remaining {{...}} variables that weren't resolved."""
    return re.findall(r"\{\{([A-Z_]+)\}\}", text)


def inject_file(input_path: Path, output_path: Path = None, brand_config: dict = None) -> str:
    """Inject brand variables into a file. Returns injected content."""
    content = input_path.read_text(encoding="utf-8")
    result = inject_brand(content, brand_config)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")

    return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Inject {{BRAND_*}} variables into templates")
    parser.add_argument("template", nargs="?", help="Template file path")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    parser.add_argument("--stdin", action="store_true", help="Read template from stdin")
    parser.add_argument("--check", action="store_true", help="Check if brand_config exists")
    parser.add_argument("--config", help="Custom brand_config.yaml path")
    args = parser.parse_args()

    config_path = Path(args.config) if args.config else BRAND_CONFIG
    brand = load_brand_config(config_path)

    if args.check:
        if brand:
            flat = flatten(brand)
            real = {k: v for k, v in flat.items() if not v.startswith("{{") and v}
            print(f"[OK] brand_config found: {config_path}")
            print(f"   {len(real)} resolved variables, {len(flat) - len(real)} placeholders")
        else:
            print(f"[FAIL] brand_config NOT found at {config_path}")
            print("   Run Brand Discovery first (N06)")
        sys.exit(0 if brand else 1)

    if args.stdin:
        template = sys.stdin.read()
    elif args.template:
        template = Path(args.template).read_text(encoding="utf-8")
    else:
        parser.print_help()
        sys.exit(1)

    result = inject_brand(template, brand)
    unresolved = count_unresolved(result)

    if args.output:
        Path(args.output).write_text(result, encoding="utf-8")
        print(f"[OK] Injected -> {args.output}")
    else:
        print(result)

    if unresolved:
        print(f"\n[WARN]  {len(unresolved)} unresolved variables: {', '.join(unresolved[:10])}", file=sys.stderr)


if __name__ == "__main__":
    main()
