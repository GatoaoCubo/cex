"""brand_inject.py -- Replace {{BRAND_*}} mustache variables in templates.

Reads .cex/brand/brand_config.yaml, flattens nested keys, and replaces
all {{BRAND_*}} occurrences in input text or files.

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
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml", "-q"])
    import yaml

ROOT = Path(__file__).resolve().parent.parent
BRAND_CONFIG = ROOT / ".cex" / "brand" / "brand_config.yaml"


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


def inject_brand(template: str, brand_config: dict = None) -> str:
    """Replace all {{BRAND_*}} and {{KEY}} variables in template text."""
    if brand_config is None:
        brand_config = load_brand_config()
    if not brand_config:
        return template

    flat = flatten(brand_config)
    result = template

    # Replace {{KEY}} patterns
    for key, value in flat.items():
        result = result.replace(f"{{{{{key}}}}}", str(value))

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
