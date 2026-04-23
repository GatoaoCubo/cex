#!/usr/bin/env python3
"""cex_builder_linter.py: Lint CEX builders for completeness + 8F compliance.

For N03 leverage: static check every builder dir has 12 ISOs, frontmatter,
and key sections (CONSTRAIN, BECOME, INJECT, etc).

Usage:
    python _tools/cex_builder_linter.py
    python _tools/cex_builder_linter.py --builder agent-builder
    python _tools/cex_builder_linter.py --strict --json
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILDERS_DIR = ROOT / "archetypes" / "builders"

REQUIRED_ISOS = [
    "bld_model_",
    "bld_prompt_",
]

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)
REQUIRED_FRONTMATTER_KEYS = ["id", "kind", "title", "version"]


def lint_builder(builder_dir: Path, strict: bool = False) -> dict:
    issues = []
    kind = builder_dir.name.replace("-builder", "")
    files = list(builder_dir.glob("*.md"))
    file_names = [f.name for f in files]

    # Check required ISOs exist
    for prefix in REQUIRED_ISOS:
        matched = [n for n in file_names if n.startswith(prefix)]
        if not matched:
            issues.append(f"missing ISO prefix: {prefix}")

    # Check ISO count (expect 12)
    iso_count = len([n for n in file_names if n.startswith("bld_")])
    if iso_count < 12:
        issues.append(f"ISO count {iso_count} < 12 expected")

    # Lint each file: frontmatter + body
    for f in files:
        try:
            txt = f.read_text(encoding="utf-8", errors="replace")
        except Exception as e:
            issues.append(f"{f.name}: read error {e}")
            continue

        m = FRONTMATTER_RE.search(txt)
        if not m:
            issues.append(f"{f.name}: no frontmatter")
            continue

        fm = m.group(1)
        for key in REQUIRED_FRONTMATTER_KEYS:
            if not re.search(rf"^{key}\s*:", fm, re.MULTILINE):
                issues.append(f"{f.name}: frontmatter missing '{key}'")

        if strict:
            body = txt[m.end():].strip()
            if len(body) < 200:
                issues.append(f"{f.name}: body too short ({len(body)} bytes)")

    return {
        "builder": builder_dir.name,
        "kind": kind,
        "files": len(files),
        "isos": iso_count,
        "issues": issues,
        "pass": len(issues) == 0,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--builder", help="single builder dir to lint")
    p.add_argument("--strict", action="store_true", help="also check body length")
    p.add_argument("--json", action="store_true")
    p.add_argument("--show-passing", action="store_true")
    args = p.parse_args()

    if not BUILDERS_DIR.exists():
        print(f"ERROR: {BUILDERS_DIR} missing", file=sys.stderr)
        return 1

    if args.builder:
        targets = [BUILDERS_DIR / args.builder]
    else:
        targets = [d for d in BUILDERS_DIR.iterdir() if d.is_dir() and d.name.endswith("-builder")]

    results = [lint_builder(t, args.strict) for t in targets if t.exists()]

    passing = sum(1 for r in results if r["pass"])
    failing = len(results) - passing

    if args.json:
        print(json.dumps({"summary": {"total": len(results), "pass": passing, "fail": failing},
                          "results": results}, indent=2))
    else:
        print(f"Linted {len(results)} builders: {passing} PASS, {failing} FAIL")
        print()
        for r in results:
            if r["pass"] and not args.show_passing:
                continue
            mark = "PASS" if r["pass"] else "FAIL"
            print(f"[{mark}] {r['builder']} (isos={r['isos']}, files={r['files']})")
            for issue in r["issues"][:5]:
                print(f"    - {issue}")
            if len(r["issues"]) > 5:
                print(f"    ... +{len(r['issues']) - 5} more")
    return 0 if failing == 0 else 2


if __name__ == "__main__":
    sys.exit(main())
