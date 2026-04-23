# -*- coding: utf-8 -*-
"""cex_env_wizard.py -- Interactive API key setup wizard. Writes .env from .env.example.

Usage:
    python _tools/cex_env_wizard.py              # full wizard
    python _tools/cex_env_wizard.py --check      # verify what is set
    python _tools/cex_env_wizard.py --nucleus n01  # only keys for N01
"""
import getpass
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

ROOT = Path(__file__).resolve().parent.parent
ENV_EXAMPLE = ROOT / ".env.example"
ENV_FILE = ROOT / ".env"

# Map .env.example section headers to wizard groups
# Keys are substrings that appear in the comment lines
GROUP_MAP = [
    {
        "id": 0,
        "label": "CRITICAL -- Required to run CEX",
        "section_hints": ["LLM PROVIDERS"],
        "keys": ["ANTHROPIC_API_KEY"],
        "description": "Claude / N07 Orchestrator",
        "link": "console.anthropic.com",
        "required": True,
    },
    {
        "id": 1,
        "label": "RESEARCH -- N01 web intelligence (optional)",
        "section_hints": ["N01 RESEARCH"],
        "keys": ["FIRECRAWL_API_KEY", "SERPER_API_KEY", "EXA_API_KEY", "GREPTILE_API_KEY",
                 "YOUTUBE_API_KEY"],
        "description": "Web scraping and search APIs for N01",
        "required": False,
    },
    {
        "id": 2,
        "label": "INFRA -- N05 deployments (optional)",
        "section_hints": ["N05 OPERATIONS"],
        "keys": ["DATABASE_URL", "SUPABASE_URL", "SUPABASE_SERVICE_ROLE_KEY", "GITHUB_PAT",
                 "GITHUB_PERSONAL_ACCESS_TOKEN", "RAILWAY_TOKEN", "REDIS_URL",
                 "SUPABASE_ANON_KEY", "SUPABASE_JWT_SECRET", "SUPABASE_STORAGE_BUCKET",
                 "E2B_API_KEY"],
        "description": "Database, cloud infra, GitHub -- needed for N05 deploy operations",
        "required": False,
    },
    {
        "id": 3,
        "label": "COMMERCIAL -- N06 payments (optional)",
        "section_hints": ["N06 COMMERCIAL"],
        "keys": ["STRIPE_SECRET_KEY", "STRIPE_WEBHOOK_SECRET", "NEXT_PUBLIC_STRIPE_PUBLISHABLE_KEY",
                 "MERCADOPAGO_ACCESS_TOKEN", "MERCADOPAGO_PUBLIC_KEY", "SHOPIFY_ACCESS_TOKEN",
                 "BASELINKER_TOKEN", "BLING_CLIENT_ID", "BLING_CLIENT_SECRET", "BLING_TENANT_ID"],
        "description": "Payment processors and e-commerce integrations",
        "required": False,
    },
    {
        "id": 4,
        "label": "EXTRAS -- LLM providers, media, storage, comms (optional)",
        "section_hints": ["OPENAI", "N02 MARKETING", "N04 KNOWLEDGE", "N07 COMMS",
                          "MEDIA", "STORAGE", "MCP SERVERS", "FREE FALLBACK"],
        "description": "All remaining optional integrations",
        "required": False,
    },
]

# Nucleus -> group IDs filter
NUCLEUS_GROUPS = {
    "n01": [0, 1],
    "n02": [0, 4],
    "n03": [0],
    "n04": [0, 4],
    "n05": [0, 2],
    "n06": [0, 3],
    "n07": [0],
}

SECRET_SUFFIXES = ("_KEY", "_TOKEN", "_SECRET", "_PASSWORD", "_CREDENTIAL")


def is_secret(key_name: str) -> bool:
    return any(key_name.upper().endswith(s) for s in SECRET_SUFFIXES)


def parse_env_example() -> dict:
    """Parse .env.example into {key: comment_line} dict."""
    if not ENV_EXAMPLE.exists():
        return {}
    result = {}
    last_comment = ""
    for line in ENV_EXAMPLE.read_text(encoding="utf-8").splitlines():
        line = line.rstrip()
        if line.startswith("#"):
            last_comment = line.lstrip("# ").strip()
        elif "=" in line and not line.startswith("#"):
            key = line.split("=", 1)[0].strip()
            if key:
                result[key] = last_comment
                last_comment = ""
    return result


def load_current_env() -> dict:
    """Load existing .env into dict."""
    if not ENV_FILE.exists():
        return {}
    result = {}
    for line in ENV_FILE.read_text(encoding="utf-8").splitlines():
        line = line.rstrip()
        if not line or line.startswith("#"):
            continue
        if "=" in line:
            k, v = line.split("=", 1)
            result[k.strip()] = v.strip()
    return result


def mask_value(val: str) -> str:
    if not val:
        return "(empty)"
    if len(val) <= 8:
        return "*" * len(val)
    return val[:4] + "*" * (len(val) - 8) + val[-4:]


def save_env(current: dict, updates: dict) -> int:
    """Merge updates into current env and write .env. Returns count of new keys set."""
    merged = dict(current)
    count = 0
    for k, v in updates.items():
        if v and v != merged.get(k, ""):
            merged[k] = v
            count += 1

    lines = []
    for k, v in merged.items():
        lines.append(f"{k}={v}")
    ENV_FILE.write_text("\n".join(lines) + "\n", encoding="utf-8")
    return count


def prompt_key(key: str, description: str, link: str = "") -> str:
    """Prompt user for a single key. Returns value or empty string."""
    print(f"\n  {key}")
    if description:
        print(f"    {description}")
    if link:
        print(f"    Get it at: {link}")

    current_env = load_current_env()
    if key in current_env and current_env[key]:
        print(f"    [SET] currently: {mask_value(current_env[key])}")
        ans = input("    Update? (y/n, Enter=keep): ").strip().lower()
        if ans != "y":
            return current_env[key]

    try:
        if is_secret(key):
            val = getpass.getpass("    > [paste key or Enter to skip]: ")
        else:
            val = input("    > [paste value or Enter to skip]: ").strip()
    except (KeyboardInterrupt, EOFError):
        print("\n[SKIP]")
        return ""
    return val.strip()


def run_check(nucleus: str = "") -> None:
    """Print current .env state."""
    current = load_current_env()
    all_keys = parse_env_example()

    groups = GROUP_MAP
    if nucleus:
        allowed_ids = NUCLEUS_GROUPS.get(nucleus.lower(), list(range(len(GROUP_MAP))))
        groups = [g for g in GROUP_MAP if g["id"] in allowed_ids]

    print("\n[CEX ENV CHECK]")
    print("=" * 50)

    set_count = 0
    skip_count = 0

    for group in groups:
        keys_in_group = group.get("keys", [])
        if not keys_in_group:
            # "extras" group -- all keys not in other groups
            explicit_keys = set()
            for g in GROUP_MAP:
                explicit_keys.update(g.get("keys", []))
            keys_in_group = [k for k in all_keys if k not in explicit_keys]

        if not keys_in_group:
            continue

        print(f"\n  [{group['label']}]")
        for key in keys_in_group:
            val = current.get(key, "")
            if val:
                print(f"    [SET]  {key}: {mask_value(val)}")
                set_count += 1
            else:
                status = "[REQUIRED]" if group.get("required") else "[SKIP]"
                print(f"    {status} {key}")
                skip_count += 1

    print(f"\n  Total: {set_count} set, {skip_count} not set")
    if nucleus:
        print(f"  Filtered to nucleus: {nucleus}")
    print("=" * 50)


def run_wizard(nucleus: str = "") -> None:
    """Interactive wizard. Prompts user group by group."""
    all_keys = parse_env_example()
    current = load_current_env()
    updates = {}

    groups = GROUP_MAP
    if nucleus:
        allowed_ids = NUCLEUS_GROUPS.get(nucleus.lower(), list(range(len(GROUP_MAP))))
        groups = [g for g in GROUP_MAP if g["id"] in allowed_ids]

    print("\n[CEX ENV WIZARD]")
    print("=" * 50)
    print("Let's set up your API keys.")
    print("You can skip optional groups by pressing Enter.")
    print("=" * 50)

    for group in groups:
        print(f"\n[{group['label']}]")
        if not group.get("required"):
            try:
                skip_grp = input("  Skip this group? (y/Enter=yes, n=configure): ").strip().lower()
            except (KeyboardInterrupt, EOFError):
                skip_grp = "y"
            if skip_grp != "n":
                print("  [SKIP]")
                continue

        keys_in_group = group.get("keys", [])
        if not keys_in_group:
            # Extras group -- all keys not covered by other groups
            explicit_keys = set()
            for g in GROUP_MAP:
                explicit_keys.update(g.get("keys", []))
            keys_in_group = [k for k in all_keys if k not in explicit_keys]

        link = group.get("link", "")
        for key in keys_in_group:
            desc = all_keys.get(key, "")
            val = prompt_key(key, desc, link if key == keys_in_group[0] else "")
            if val:
                updates[key] = val

    count = save_env(current, updates)
    print("\n" + "=" * 50)
    print(f"[OK] Saved .env with {count} key(s) updated.")
    print("Run: python _tools/cex_setup_validator.py to verify.")
    print("=" * 50)


def main():
    import argparse
    parser = argparse.ArgumentParser(description="CEX API key setup wizard")
    parser.add_argument("--check", action="store_true",
                        help="Show current .env state without modifying")
    parser.add_argument("--nucleus", default="",
                        help="Only show keys relevant to this nucleus (n01..n07)")
    args = parser.parse_args()

    if args.check:
        run_check(nucleus=args.nucleus)
    else:
        run_wizard(nucleus=args.nucleus)


if __name__ == "__main__":
    main()
