"""Audit W4 DOCS + UX: opensource-readiness of user-facing docs.

Checks:
- Required files: README.md, LICENSE, CONTRIBUTING.md, CHANGELOG.md, CODE_OF_CONDUCT.md, SECURITY.md
- README sections: install / quickstart / examples / contributing / license / badges
- LICENSE is OSI-recognized (MIT/Apache/BSD/...)
- Top-level: examples/, docs/, _docs/
- _docs/ structure
- .github/ presence (issue templates, PR templates)

Output: _reports/audit/docs_ux.md
"""
from __future__ import annotations

import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "_reports" / "audit" / "docs_ux.md"

REQUIRED_TOP = {
    "README.md": "project entry point",
    "LICENSE": "legal terms",
    "CONTRIBUTING.md": "contributor onboarding",
    "CHANGELOG.md": "version history",
    "CODE_OF_CONDUCT.md": "community norms (recommended)",
    "SECURITY.md": "vulnerability reporting (recommended)",
}

README_SECTIONS = {
    "install": [r"##\s*install", r"##\s*setup", r"##\s*getting\s+started"],
    "quickstart": [r"##\s*quickstart", r"##\s*quick\s+start", r"```bash"],
    "usage": [r"##\s*usage", r"##\s*how\s+it\s+works", r"##\s*example"],
    "license_section": [r"##\s*license"],
    "badges": [r"\!\[.+?\]\(https://"],
    "toc": [r"\[.+\]\(#.+\)"],
    "screenshots": [r"\!\[.+\]\(.+\.(png|jpg|gif|svg)"],
}

OSI_LICENSES = {
    "MIT": ["MIT License", "Permission is hereby granted"],
    "Apache-2.0": ["Apache License", "Version 2.0"],
    "BSD-3-Clause": ["BSD 3-Clause", "Redistribution and use"],
    "BSD-2-Clause": ["BSD 2-Clause", "Redistributions of source code"],
    "GPL-3.0": ["GNU General Public License", "version 3"],
    "MPL-2.0": ["Mozilla Public License", "Version 2.0"],
    "ISC": ["ISC License"],
    "Unlicense": ["This is free and unencumbered software"],
}


def check_file_exists(name: str) -> tuple[bool, int]:
    """Return (exists, lines)."""
    p = ROOT / name
    if not p.exists():
        return False, 0
    try:
        return True, len(p.read_text(encoding="utf-8", errors="replace").splitlines())
    except OSError:
        return False, 0


def detect_license(license_path: Path) -> str:
    """Identify OSI license."""
    if not license_path.exists():
        return "MISSING"
    try:
        text = license_path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return "UNREADABLE"
    for name, markers in OSI_LICENSES.items():
        if all(m in text for m in markers):
            return name
    return "UNRECOGNIZED"


def scan_readme_sections() -> dict:
    """Scan README for expected sections + features."""
    p = ROOT / "README.md"
    if not p.exists():
        return {k: False for k in README_SECTIONS}
    try:
        text = p.read_text(encoding="utf-8", errors="replace").lower()
    except OSError:
        return {k: False for k in README_SECTIONS}
    out = {}
    for section, patterns in README_SECTIONS.items():
        out[section] = any(re.search(p, text, re.IGNORECASE | re.MULTILINE)
                           for p in patterns)
    return out


def list_dir(rel: str, max_items: int = 30) -> list[str]:
    """List immediate children of a directory."""
    p = ROOT / rel
    if not p.exists() or not p.is_dir():
        return []
    return sorted([c.name for c in p.iterdir()])[:max_items]


def main() -> int:
    """Run W4 docs+UX audit."""
    print("[W4] checking required files...")
    file_results = {}
    for name, purpose in REQUIRED_TOP.items():
        exists, lines = check_file_exists(name)
        file_results[name] = {"exists": exists, "lines": lines, "purpose": purpose}

    print("[W4] detecting license...")
    license_kind = detect_license(ROOT / "LICENSE")

    print("[W4] scanning README sections...")
    readme_sections = scan_readme_sections()

    print("[W4] listing directories...")
    examples = list_dir("examples")
    docs = list_dir("_docs")
    github_root = list_dir(".github")
    issue_templates = list_dir(".github/ISSUE_TEMPLATE")
    workflows = list_dir(".github/workflows")

    out = ["# W4 DOCS + UX READINESS", ""]
    out.append("Public push readiness: required files, README quality, license, examples.")
    out.append("")
    out.append("## Required top-level files")
    out.append("")
    out.append("| File | Present? | Lines | Purpose |")
    out.append("|------|----------|-------|---------|")
    for name, info in file_results.items():
        present = "YES" if info["exists"] else "**MISSING**"
        lines = info["lines"] if info["exists"] else "-"
        out.append(f"| `{name}` | {present} | {lines} | {info['purpose']} |")
    out.append("")
    missing = [n for n, i in file_results.items() if not i["exists"]]
    if missing:
        out.append(f"**{len(missing)} required file(s) missing**: "
                   + ", ".join(f"`{n}`" for n in missing))
    else:
        out.append("**All required files present.**")
    out.append("")
    out.append(f"## License: **{license_kind}**")
    out.append("")
    if license_kind == "MISSING":
        out.append("**BLOCKER**: No LICENSE file. Cannot publish without one.")
    elif license_kind == "UNRECOGNIZED":
        out.append("**WARNING**: License not recognized. Verify it's OSI-approved.")
    else:
        out.append(f"OSI-approved: `{license_kind}`. OK for opensource publish.")
    out.append("")
    out.append("## README sections detected")
    out.append("")
    out.append("| Section | Present? |")
    out.append("|---------|----------|")
    for section, found in readme_sections.items():
        out.append(f"| {section} | {'YES' if found else '**NO**'} |")
    out.append("")
    missing_sections = [s for s, f in readme_sections.items() if not f]
    if missing_sections:
        out.append(f"**{len(missing_sections)} README section(s) missing**: "
                   + ", ".join(missing_sections))
    out.append("")
    out.append("## Examples / docs / .github")
    out.append("")
    out.append(f"### `examples/` ({len(examples)} items)")
    if examples:
        for x in examples[:15]:
            out.append(f"- `{x}`")
    else:
        out.append("_Empty or missing._ Recommend: add quickstart examples.")
    out.append("")
    out.append(f"### `_docs/` ({len(docs)} items)")
    if docs:
        for x in docs[:20]:
            out.append(f"- `{x}`")
    out.append("")
    out.append(f"### `.github/` ({len(github_root)} items)")
    if github_root:
        for x in github_root:
            out.append(f"- `{x}`")
    out.append("")
    out.append(f"### `.github/ISSUE_TEMPLATE/` ({len(issue_templates)} items)")
    if issue_templates:
        for x in issue_templates:
            out.append(f"- `{x}`")
    else:
        out.append("_Empty._ Recommend: add bug/feature templates.")
    out.append("")
    out.append(f"### `.github/workflows/` ({len(workflows)} items)")
    if workflows:
        for x in workflows:
            out.append(f"- `{x}`")
    out.append("")
    out.append("## Verdict")
    out.append("")
    blockers = []
    if missing:
        blockers.append(f"Add {len(missing)} missing top-level file(s)")
    if license_kind in ("MISSING", "UNRECOGNIZED"):
        blockers.append("Fix LICENSE")
    if not readme_sections.get("install") and not readme_sections.get("quickstart"):
        blockers.append("README needs install/quickstart section")
    if not examples:
        blockers.append("examples/ is empty -- add 1-3 runnable examples")
    if blockers:
        out.append("**BLOCKERS for opensource publish:**")
        for b in blockers:
            out.append(f"- {b}")
    else:
        out.append("**No critical blockers detected.** Ready for public push (after security fixes).")
    out.append("")
    out.append("## DOCS_UX_PASS")

    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(out), encoding="utf-8")
    print(f"[W4] report written: {OUT}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
