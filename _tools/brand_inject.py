# -*- coding: utf-8 -*-
"""brand_inject.py -- Replace {{BRAND_*}} and instance mustache variables in templates.

Reads .cex/brand/brand_config.yaml AND .cex/instance/instance_config.yaml,
flattens nested keys, and replaces all {{VAR}} occurrences in input text or files.

Handles:
  - Brand variables: {{BRAND_NAME}} -> "Acme Corp"
  - Instance variables: {{INDUSTRY}} -> "pet", {{MAP_CENTER_LAT}} -> "-23.6235"
  - Derived variables: {{BRAND_SLUG}}, {{BRAND_UPPER}}, {{BRAND_NAME_SHORT}}
  - Derived from brand: {{BRAND_EMAIL}}, {{BRAND_DOMAIN}}, {{REGION}}, {{PLATFORMS}}
  - Aliases: {{BRAND_TONE}} -> BRAND_VOICE_TONE, {{BRAND_VOICE}} -> BRAND_VOICE_TONE
  - Default syntax: {{BRAND_X | default: 'fallback'}} -> fallback (if BRAND_X unset)

Usage:
    python _tools/brand_inject.py <template_file> [--output <out_file>]
    python _tools/brand_inject.py --stdin
    python _tools/brand_inject.py --check  (verify brand_config exists)
    python _tools/brand_inject.py --check-instance  (verify instance_config exists)
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
BRAND_CONFIG = ROOT / ".cex" / "brand" / "brand_config.yaml"
INSTANCE_CONFIG = ROOT / ".cex" / "instance" / "instance_config.yaml"

# Aliases: template variable -> config variable
# These map commonly-used short names to their canonical config keys.
BRAND_ALIASES = {
    "BRAND_TONE":       "BRAND_VOICE_TONE",
    "BRAND_VOICE":      "BRAND_VOICE_TONE",
    "BRAND_NICHE":      "BRAND_CATEGORY",
    "REGION":           "BRAND_REGION",
    "PLATFORMS":        "BRAND_CHANNELS",
}

# All 23 known instance variable names (for unresolved tracking)
INSTANCE_VARS = {
    "INDUSTRY", "TARGET_COUNT", "BATCH_SOURCES", "DIRECTORY_SOURCES",
    "SEARCH_QUERIES", "CATEGORIES", "CITIES", "RADIUS_KM", "HASHTAGS",
    "MARKETPLACES", "CNAE_CODES", "LEGAL_SOURCES",
    "MAP_CENTER_LAT", "MAP_CENTER_LNG", "MAP_ZOOM", "CRM_DATA_SOURCE",
    "DB_PROVIDER", "TABLES", "MAP_PROVIDER", "AUTH_METHOD",
    "SEARCH_PROVIDERS", "MERGE_STRATEGY", "DEDUP_FIELDS",
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


def load_instance_config(path: Path = INSTANCE_CONFIG) -> dict:
    """Load instance_config.yaml and return parsed dict.

    Instance config holds operational variables (CRM, dashboards, infra, research)
    that are separate from brand identity. See kc_instance_variable_registry.md.
    """
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
      BRAND_EMAIL      -- derived from BRAND_HQ or contact info (if present)
      BRAND_DOMAIN     -- derived from BRAND_LOGO_URL (if present)
    Applies aliases (BRAND_TONE -> BRAND_VOICE_TONE, REGION -> BRAND_REGION, etc.)
    """
    derived = {}
    name = flat.get("BRAND_NAME", "")

    if name and not _is_placeholder(name):
        derived["BRAND_SLUG"] = re.sub(r'[^a-z0-9]+', '-', name.lower()).strip('-')
        derived["BRAND_UPPER"] = name.upper()
        derived["BRAND_NAME_SHORT"] = name.split()[0] if " " in name else name

    # Derive BRAND_DOMAIN from BRAND_LOGO_URL or BRAND_FAVICON_URL
    for url_key in ("BRAND_LOGO_URL", "BRAND_FAVICON_URL"):
        url_val = flat.get(url_key, "")
        if url_val and not _is_placeholder(url_val) and "://" in url_val:
            # Extract domain: https://example.com/path -> example.com
            try:
                domain = url_val.split("://", 1)[1].split("/", 1)[0]
                if "." in domain:
                    derived["BRAND_DOMAIN"] = domain
                    break
            except (IndexError, ValueError):
                pass

    # Apply aliases: short name -> canonical config value
    for alias, canonical in BRAND_ALIASES.items():
        if canonical in flat and not _is_placeholder(flat[canonical]):
            derived[alias] = flat[canonical]

    return derived


def inject_brand(template: str, brand_config: dict = None,
                  instance_config: dict = None) -> str:
    """Replace all {{BRAND_*}} and {{KEY}} variables in template text.

    Processing order:
      1. Flatten brand + instance configs into key-value pairs
      2. Compute derived variables (BRAND_SLUG, aliases, etc.)
      3. Replace {{KEY}} exact matches
      4. Resolve {{KEY | default: 'fallback'}} patterns

    Args:
        template: Template text containing {{VAR}} placeholders.
        brand_config: Brand identity config dict. Loads from disk if None.
        instance_config: Instance operational config dict. Loads from disk if None.
    """
    if brand_config is None:
        brand_config = load_brand_config()
    if instance_config is None:
        instance_config = load_instance_config()

    flat = flatten(brand_config) if brand_config else {}
    # Merge instance config (flattened) -- brand vars take precedence on collision
    if instance_config:
        instance_flat = flatten(instance_config)
        for k, v in instance_flat.items():
            if k not in flat:
                flat[k] = v
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
    """Find remaining {{...}} variables that weren't resolved.

    Catches both BRAND_* and instance variables (INDUSTRY, MAP_CENTER_LAT, etc.)
    """
    return re.findall(r"\{\{([A-Z][A-Z0-9_]*)\}\}", text)


def inject_file(input_path: Path, output_path: Path = None,
                brand_config: dict = None, instance_config: dict = None) -> str:
    """Inject brand + instance variables into a file. Returns injected content."""
    content = input_path.read_text(encoding="utf-8")
    result = inject_brand(content, brand_config, instance_config)

    if output_path:
        output_path.parent.mkdir(parents=True, exist_ok=True)
        output_path.write_text(result, encoding="utf-8")

    return result


def main():
    import argparse
    parser = argparse.ArgumentParser(description="Inject {{BRAND_*}} and instance variables into templates")
    parser.add_argument("template", nargs="?", help="Template file path")
    parser.add_argument("--output", "-o", help="Output file (default: stdout)")
    parser.add_argument("--stdin", action="store_true", help="Read template from stdin")
    parser.add_argument("--check", action="store_true", help="Check if brand_config exists")
    parser.add_argument("--check-instance", action="store_true", help="Check if instance_config exists")
    parser.add_argument("--config", help="Custom brand_config.yaml path")
    parser.add_argument("--instance-config", help="Custom instance_config.yaml path")
    args = parser.parse_args()

    config_path = Path(args.config) if args.config else BRAND_CONFIG
    instance_path = Path(args.instance_config) if args.instance_config else INSTANCE_CONFIG
    brand = load_brand_config(config_path)
    instance = load_instance_config(instance_path)

    if args.check_instance:
        if instance:
            flat = flatten(instance)
            real = {k: v for k, v in flat.items() if not v.startswith("{{") and v}
            print(f"[OK] instance_config found: {instance_path}")
            print(f"   {len(real)} resolved variables, {len(flat) - len(real)} placeholders")
            # Show coverage by section
            for section in ("crm_pipeline", "dashboard", "infrastructure", "research"):
                section_data = instance.get(section, {})
                if section_data:
                    resolved = sum(1 for v in section_data.values()
                                   if isinstance(v, str) and not _is_placeholder(v))
                    print(f"   {section}: {resolved}/{len(section_data)} resolved")
        else:
            print(f"[WARN] instance_config NOT found at {instance_path}")
            print("   Copy .cex/instance/instance_config_template.yaml -> instance_config.yaml")
            print("   Then fill in your operational variables.")
        sys.exit(0 if instance else 1)

    if args.check:
        if brand:
            flat = flatten(brand)
            real = {k: v for k, v in flat.items() if not v.startswith("{{") and v}
            print(f"[OK] brand_config found: {config_path}")
            print(f"   {len(real)} resolved variables, {len(flat) - len(real)} placeholders")
        else:
            print(f"[FAIL] brand_config NOT found at {config_path}")
            print("   Run Brand Discovery first (N06)")
        # Also report instance config status
        if instance:
            inst_flat = flatten(instance)
            inst_real = {k: v for k, v in inst_flat.items() if not v.startswith("{{") and v}
            print(f"[OK] instance_config found: {instance_path} ({len(inst_real)} resolved)")
        else:
            print("[INFO] instance_config not found (optional: .cex/instance/instance_config.yaml)")
        sys.exit(0 if brand else 1)

    if args.stdin:
        template = sys.stdin.read()
    elif args.template:
        template = Path(args.template).read_text(encoding="utf-8")
    else:
        parser.print_help()
        sys.exit(1)

    result = inject_brand(template, brand, instance)
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
