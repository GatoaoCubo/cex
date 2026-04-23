#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX version bumper -- increments LP or global version in VERSION.yaml."""

import sys

if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")

import argparse
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. Install: pip install pyyaml")
    sys.exit(1)

ROOT = Path(__file__).resolve().parent.parent
VERSION_FILE = ROOT / "_meta" / "VERSION.yaml"
CHANGELOG_FILE = ROOT / "_meta" / "CHANGELOG.md"


def bump(version: str, level: str) -> str:
    parts = [int(x) for x in version.split(".")]
    if level == "major":
        parts[0] += 1
        parts[1] = 0
        parts[2] = 0
    elif level == "minor":
        parts[1] += 1
        parts[2] = 0
    else:
        parts[2] += 1
    return ".".join(str(p) for p in parts)


def main():
    parser = argparse.ArgumentParser(description="Bump CEX version")
    parser.add_argument("--lp", help="LP to bump (e.g. P01). Omit to bump global only.")
    parser.add_argument("--level", choices=["patch", "minor", "major"], default="patch")
    parser.add_argument("--message", "-m", help="Changelog entry message")
    args = parser.parse_args()

    if not VERSION_FILE.exists():
        print(f"ERROR: {VERSION_FILE} not found")
        sys.exit(1)

    data = yaml.safe_load(VERSION_FILE.read_text(encoding="utf-8"))
    old_global = data["cex_version"]

    if args.lp:
        lp_key = None
        for key in data["lps"]:
            if key.upper().startswith(args.lp.upper()):
                lp_key = key
                break
        if not lp_key:
            print(f"ERROR: LP '{args.lp}' not found in VERSION.yaml")
            sys.exit(1)

        old_lp = data["lps"][lp_key]["version"]
        new_lp = bump(old_lp, args.level)
        data["lps"][lp_key]["version"] = new_lp
        print(f"{lp_key}: {old_lp} -> {new_lp}")

    new_global = bump(old_global, args.level)
    data["cex_version"] = new_global
    data["date"] = date.today().isoformat()
    print(f"cex_version: {old_global} -> {new_global}")

    VERSION_FILE.write_text(
        yaml.dump(data, default_flow_style=False, allow_unicode=True, sort_keys=False),
        encoding="utf-8",
    )

    if args.message and CHANGELOG_FILE.exists():
        today = date.today().isoformat()
        entry = f"\n## [{new_global}] - {today}\n\n- {args.message}\n"
        content = CHANGELOG_FILE.read_text(encoding="utf-8")
        marker = "# CHANGELOG"
        if marker in content:
            pos = content.index(marker) + len(marker)
            next_newline = content.index("\n", pos)
            content = content[: next_newline + 1] + entry + content[next_newline + 1 :]
        else:
            content = entry + "\n" + content
        CHANGELOG_FILE.write_text(content, encoding="utf-8")
        print(f"CHANGELOG.md updated with entry for v{new_global}")

    print("Done.")


if __name__ == "__main__":
    main()
