# -*- coding: utf-8 -*-
"""cex_bootstrap.py -- First-run brand setup for CEX instances.

When a user first clones/installs CEX, this script:
1. Detects if .cex/brand/brand_config.yaml has real values (not template)
2. If not -> launches interactive Brand Discovery (N06)
3. Validates the filled config
4. Propagates brand to all nuclei
5. Generates branded CLAUDE.md header
6. Audits brand consistency

The X in CEX is YOUR brand. This script fills it.

Usage:
    python _tools/cex_bootstrap.py                  # interactive first-run
    python _tools/cex_bootstrap.py --check           # just check if bootstrapped
    python _tools/cex_bootstrap.py --from-file input.yaml  # non-interactive
    python _tools/cex_bootstrap.py --reset           # clear brand (re-bootstrap)
"""
import re
import shutil
import sys
from datetime import datetime
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    import subprocess
    subprocess.check_call([sys.executable, "-m", "pip", "install", "pyyaml", "-q"])
    import yaml

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "_tools"))

BRAND_DIR = ROOT / ".cex" / "brand"
BRAND_CONFIG = BRAND_DIR / "brand_config.yaml"
BRAND_TEMPLATE = BRAND_DIR / "brand_config_template.yaml"
BRAND_LOCK = BRAND_DIR / ".bootstrapped"
CLAUDE_MD = ROOT / "CLAUDE.md"


def is_bootstrapped() -> bool:
    """Check if CEX instance has been bootstrapped with a real brand."""
    if not BRAND_CONFIG.exists():
        return False
    if BRAND_LOCK.exists():
        return True
    # Check if config has real values (not template placeholders)
    try:
        with open(BRAND_CONFIG, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
        name = config.get("identity", {}).get("BRAND_NAME", "")
        return bool(name) and not str(name).startswith("{{")
    except Exception:
        return False


def count_placeholders(config: dict) -> int:
    """Count remaining {{...}} placeholders in config."""
    text = yaml.dump(config, default_flow_style=False)
    return len(re.findall(r"\{\{[A-Z_]+\}\}", text))


def count_filled(config: dict) -> int:
    """Count non-placeholder, non-empty values."""
    text = yaml.dump(config, default_flow_style=False)
    total_values = len(re.findall(r": .+", text))
    placeholders = len(re.findall(r"\{\{[A-Z_]+\}\}", text))
    return total_values - placeholders


def inject_brand_header(config: dict) -> None:
    """Inject brand identity into CLAUDE.md header."""
    if not CLAUDE_MD.exists():
        return

    content = CLAUDE_MD.read_text(encoding="utf-8")
    name = config.get("identity", {}).get("BRAND_NAME", "CEX")
    tagline = config.get("identity", {}).get("BRAND_TAGLINE", "")
    archetype = config.get("archetype", {}).get("BRAND_ARCHETYPE", "")

    # Build brand header block
    brand_block = """## Brand Identity (bootstrapped)

| Key | Value |
|-----|-------|
| **Brand** | {name} |
| **Tagline** | {tagline} |
| **Archetype** | {archetype} |
| **Config** | `.cex/brand/brand_config.yaml` |
| **Bootstrapped** | {datetime.now().strftime('%Y-%m-%d')} |

> All nuclei auto-inject brand context from `brand_config.yaml` into every prompt.
> To re-bootstrap: `python _tools/cex_bootstrap.py --reset`
"""

    # Insert after first heading, before "## Who Am I?"
    marker = "## Who Am I?"
    if marker in content:
        # Remove existing brand block if present
        content = re.sub(
            r"## Brand Identity \(bootstrapped\).*?(?=## Who Am I\?)",
            "",
            content,
            flags=re.DOTALL,
        )
        content = content.replace(marker, brand_block + "\n" + marker)
    else:
        # Fallback: insert after first line
        lines = content.split("\n", 2)
        if len(lines) >= 3:
            content = lines[0] + "\n" + lines[1] + "\n\n" + brand_block + "\n" + lines[2]

    CLAUDE_MD.write_text(content, encoding="utf-8")


def update_boot_titles(config: dict) -> None:
    """Update boot/*.ps1 window titles with brand name."""
    name = config.get("identity", {}).get("BRAND_NAME", "")
    if not name or name.startswith("{{"):
        return

    boot_dir = ROOT / "boot"
    for ps1_file in boot_dir.glob("*.ps1"):
        try:
            content = ps1_file.read_text(encoding="utf-8")
            # Replace sin-aware title prefix -- `$t = "N07 ...` or `$t = "N0X ...`
            content = re.sub(
                r'(\$t\s*=\s*"N0\d+ )',
                lambda m: m.group(1).replace('"N0', f'"{name} N0'),
                content,
            )
            ps1_file.write_text(content, encoding="utf-8")
        except Exception:
            continue


def bootstrap_interactive(config: dict) -> dict:
    """Interactive brand setup -- minimal questions for quick bootstrap."""
    print("\n" + "=" * 60)
    print("  CEX BOOTSTRAP -- The X is YOUR brand")
    print("=" * 60)
    print()
    print("  CEX is a generic AI brain. This bootstrap makes it YOURS.")
    print("  Answer a few questions to fill brand_config.yaml.")
    print("  For full Brand Discovery, run N06 after bootstrap.")
    print()

    identity = config.get("identity", {})
    archetype_sec = config.get("archetype", {})
    voice = config.get("voice", {})
    audience = config.get("audience", {})
    positioning = config.get("positioning", {})
    monetization = config.get("monetization", {})

    def ask(prompt, current="", required=True):
        default = f" [{current}]" if current and not str(current).startswith("{{") else ""
        while True:
            answer = input(f"  {prompt}{default}: ").strip()
            if not answer and current and not str(current).startswith("{{"):
                return current
            if answer:
                return answer
            if not required:
                return current
            print("    (required -- please enter a value)")

    # Phase 1: Identity (required)
    print("--- IDENTITY ---")
    identity["BRAND_NAME"] = ask("Brand/company name", identity.get("BRAND_NAME", ""))
    identity["BRAND_TAGLINE"] = ask("Tagline (10-100 chars)", identity.get("BRAND_TAGLINE", ""))
    identity["BRAND_MISSION"] = ask("Mission (why you exist)", identity.get("BRAND_MISSION", ""))

    values_raw = ask("3-5 core values (comma-separated)", ", ".join(identity.get("BRAND_VALUES", [])))
    identity["BRAND_VALUES"] = [v.strip() for v in values_raw.split(",") if v.strip()]

    # Phase 2: Archetype (required)
    print("\n--- ARCHETYPE ---")
    archetypes = "creator|hero|sage|explorer|rebel|magician|lover|caregiver|jester|ruler|innocent|everyman"
    print(f"    Options: {archetypes}")
    archetype_sec["BRAND_ARCHETYPE"] = ask("Primary archetype", archetype_sec.get("BRAND_ARCHETYPE", "")).lower()

    # Phase 3: Voice (required)
    print("\n--- VOICE ---")
    voice["BRAND_VOICE_TONE"] = ask("Voice tone (e.g. 'direct, technical, warm')", voice.get("BRAND_VOICE_TONE", ""))
    try:
        voice["BRAND_VOICE_FORMALITY"] = int(ask("Formality 1-5 (1=casual 5=formal)", str(voice.get("BRAND_VOICE_FORMALITY", 3))))
    except ValueError:
        voice["BRAND_VOICE_FORMALITY"] = 3
    voice["BRAND_LANGUAGE"] = ask("Language (e.g. pt-BR, en-US)", voice.get("BRAND_LANGUAGE", "pt-BR"), required=False)

    # Phase 4: Audience (required)
    print("\n--- AUDIENCE ---")
    audience["BRAND_ICP"] = ask("Ideal customer (20+ chars)", audience.get("BRAND_ICP", ""))
    audience["BRAND_TRANSFORMATION"] = ask("Transformation: From X to Y through Z", audience.get("BRAND_TRANSFORMATION", ""))

    # Phase 5: Positioning (required)
    print("\n--- POSITIONING ---")
    positioning["BRAND_CATEGORY"] = ask("Category (what market)", positioning.get("BRAND_CATEGORY", ""))
    positioning["BRAND_UVP"] = ask("UVP (unique value proposition, 20+ chars)", positioning.get("BRAND_UVP", ""))

    # Phase 6: Monetization (required)
    print("\n--- MONETIZATION ---")
    models = "subscription|one-time|credits|freemium|marketplace|hybrid"
    print(f"    Options: {models}")
    monetization["BRAND_PRICING_MODEL"] = ask("Pricing model", monetization.get("BRAND_PRICING_MODEL", "subscription"))
    monetization["BRAND_CURRENCY"] = ask("Currency (BRL, USD, EUR)", monetization.get("BRAND_CURRENCY", "BRL")).upper()

    config["identity"] = identity
    config["archetype"] = archetype_sec
    config["voice"] = voice
    config["audience"] = audience
    config["positioning"] = positioning
    config["monetization"] = monetization

    return config


def run_bootstrap(config: dict, interactive: bool = True) -> bool:
    """Execute the full bootstrap pipeline."""
    from brand_audit import audit
    from brand_propagate import propagate
    from brand_validate import validate

    # 1. Fill config
    if interactive:
        config = bootstrap_interactive(config)

    # 2. Save config
    BRAND_DIR.mkdir(parents=True, exist_ok=True)
    with open(BRAND_CONFIG, "w", encoding="utf-8") as f:
        f.write("# .cex/brand/brand_config.yaml\n")
        f.write(f"# Bootstrapped: {datetime.now().isoformat()}\n")
        f.write(f"# Brand: {config.get('identity', {}).get('BRAND_NAME', 'unknown')}\n\n")
        yaml.dump(config, f, default_flow_style=False, allow_unicode=True, sort_keys=False)

    # 3. Validate
    result = validate(config)
    if not result["valid"]:
        print(f"\n  WARNING: Validation found {len(result['errors'])} errors:")
        for e in result["errors"][:5]:
            print(f"    - {e}")
        print("  Config saved but may need fixes. Run N06 Brand Discovery for full setup.")
    else:
        print(f"\n  OK: Validation passed ({result['required_fields_filled']}/13 required fields)")

    # 4. Propagate
    prop_results = propagate(config, dry_run=False)
    propagated = [n for n, r in prop_results.items() if r["status"] == "propagated"]
    print(f"  OK: Brand propagated to {len(propagated)} nuclei: {', '.join(propagated)}")

    # 5. Inject into CLAUDE.md
    inject_brand_header(config)
    print("  OK: CLAUDE.md updated with brand identity")

    # 6. Update boot titles
    update_boot_titles(config)
    print("  OK: Boot scripts updated with brand name")

    # 7. Audit
    audit_result = audit(config)
    print(f"  OK: Brand audit score: {audit_result['overall_score']:.3f} ({audit_result['rating']})")

    # 8. Write lock file
    BRAND_LOCK.write_text(
        f"bootstrapped: {datetime.now().isoformat()}\n"
        f"brand: {config.get('identity', {}).get('BRAND_NAME', '')}\n"
        f"audit_score: {audit_result['overall_score']}\n",
        encoding="utf-8",
    )

    brand_name = config.get("identity", {}).get("BRAND_NAME", "CEX")
    print("\n  BOOTSTRAP COMPLETE")
    print(f"  CEX is now the brain of: {brand_name}")
    print("  For full Brand Discovery: boot/n06.ps1")
    print("  To re-bootstrap: python _tools/cex_bootstrap.py --reset")
    return True


def main():
    import argparse
    parser = argparse.ArgumentParser(description="CEX Bootstrap -- fill the X with YOUR brand")
    parser.add_argument("--check", action="store_true", help="Check if bootstrapped")
    parser.add_argument("--from-file", help="Non-interactive: load brand values from YAML file")
    parser.add_argument("--reset", action="store_true", help="Clear brand and re-bootstrap")
    parser.add_argument("--status", action="store_true", help="Show current brand status")
    args = parser.parse_args()

    if args.check:
        if is_bootstrapped():
            with open(BRAND_CONFIG, "r", encoding="utf-8") as f:
                c = yaml.safe_load(f) or {}
            name = c.get("identity", {}).get("BRAND_NAME", "unknown")
            print(f"BOOTSTRAPPED: {name}")
            sys.exit(0)
        else:
            print("NOT BOOTSTRAPPED: run python _tools/cex_bootstrap.py")
            sys.exit(1)

    if args.status:
        if not BRAND_CONFIG.exists():
            print("Status: NOT BOOTSTRAPPED")
            print("  Run: python _tools/cex_bootstrap.py")
            sys.exit(0)
        with open(BRAND_CONFIG, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
        filled = count_filled(config)
        placeholders = count_placeholders(config)
        name = config.get("identity", {}).get("BRAND_NAME", "unknown")
        print(f"Status: {'BOOTSTRAPPED' if is_bootstrapped() else 'PARTIAL'}")
        print(f"  Brand: {name}")
        print(f"  Filled values: {filled}")
        print(f"  Placeholders remaining: {placeholders}")
        if BRAND_LOCK.exists():
            print(f"  Lock: {BRAND_LOCK.read_text(encoding='utf-8').strip()}")
        sys.exit(0)

    if args.reset:
        if BRAND_LOCK.exists():
            BRAND_LOCK.unlink()
        if BRAND_CONFIG.exists():
            backup = BRAND_CONFIG.with_suffix(".yaml.bak")
            shutil.copy2(BRAND_CONFIG, backup)
            print(f"  Backup saved: {backup}")
        # Copy template back
        if BRAND_TEMPLATE.exists():
            shutil.copy2(BRAND_TEMPLATE, BRAND_CONFIG)
        print("  Brand reset. Run bootstrap again.")
        sys.exit(0)

    # Load existing config or template
    if args.from_file:
        with open(args.from_file, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
        run_bootstrap(config, interactive=False)
    else:
        if BRAND_CONFIG.exists():
            with open(BRAND_CONFIG, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f) or {}
        elif BRAND_TEMPLATE.exists():
            with open(BRAND_TEMPLATE, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f) or {}
        else:
            config = {}
        run_bootstrap(config, interactive=True)


if __name__ == "__main__":
    main()
