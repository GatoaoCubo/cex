#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX changelog generator -- reads git log, groups by LP, formats entry."""

import sys

if hasattr(sys.stdout, "reconfigure"): sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"): sys.stderr.reconfigure(encoding="utf-8")

import re
import subprocess
import sys
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

LP_PATTERN = re.compile(r"(P\d{2}_\w+)")


def get_last_tag() -> str | None:
    try:
        result = subprocess.run(
            ["git", "describe", "--tags", "--abbrev=0"],
            capture_output=True,
            text=True,
            cwd=ROOT,
        )
        if result.returncode == 0:
            return result.stdout.strip()
    except FileNotFoundError:
        pass
    return None


def get_commits(since_ref: str | None) -> list[dict]:
    cmd = ["git", "log", "--pretty=format:%H|%s", "--name-only"]
    if since_ref:
        cmd.append(f"{since_ref}..HEAD")
    try:
        result = subprocess.run(cmd, capture_output=True, text=True, cwd=ROOT)
    except FileNotFoundError:
        print("ERROR: git not found")
        sys.exit(1)

    commits = []
    current = None
    for line in result.stdout.split("\n"):
        if "|" in line and len(line.split("|")[0]) == 40:
            parts = line.split("|", 1)
            current = {"hash": parts[0][:8], "message": parts[1], "files": [], "lps": set()}
            commits.append(current)
        elif current and line.strip():
            current["files"].append(line.strip())
            match = LP_PATTERN.search(line)
            if match:
                current["lps"].add(match.group(1))

    return commits


def group_by_lp(commits: list[dict]) -> dict[str, list[str]]:
    groups: dict[str, list[str]] = {}
    for c in commits:
        if c["lps"]:
            for lp in c["lps"]:
                groups.setdefault(lp, []).append(c["message"])
        else:
            groups.setdefault("_general", []).append(c["message"])
    return groups


def format_changelog(groups: dict[str, list[str]], version: str) -> str:
    today = date.today().isoformat()
    lines = [f"## [{version}] - {today}", ""]

    for lp in sorted(groups.keys()):
        if lp == "_general":
            continue
        lines.append(f"### {lp}")
        for msg in groups[lp]:
            lines.append(f"- {msg}")
        lines.append("")

    if "_general" in groups:
        lines.append("### General")
        for msg in groups["_general"]:
            lines.append(f"- {msg}")
        lines.append("")

    return "\n".join(lines)


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Generate changelog from git log")
    parser.add_argument(
        "--since", help="Git ref to start from (tag or commit). Auto-detects last tag if omitted."
    )
    parser.add_argument("--dry-run", action="store_true", help="Print without writing")
    args = parser.parse_args()

    since = args.since or get_last_tag()
    if since:
        print(f"Generating changelog since: {since}")
    else:
        print("No tag found, using full git log")

    data = yaml.safe_load(VERSION_FILE.read_text(encoding="utf-8"))
    version = data["cex_version"]

    commits = get_commits(since)
    if not commits:
        print("No commits found.")
        sys.exit(0)

    groups = group_by_lp(commits)
    entry = format_changelog(groups, version)

    if args.dry_run:
        print("\n--- Generated Entry ---")
        print(entry)
        return

    content = CHANGELOG_FILE.read_text(encoding="utf-8")
    marker = "---\n\n## ["
    if marker in content:
        pos = content.index(marker) + 4
        content = content[:pos] + "\n" + entry + "\n" + content[pos:]
    else:
        content += "\n" + entry

    CHANGELOG_FILE.write_text(content, encoding="utf-8")
    print(f"CHANGELOG.md updated with {len(commits)} commits across {len(groups)} groups")


if __name__ == "__main__":
    main()
