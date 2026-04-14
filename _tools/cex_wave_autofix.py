"""cex_wave_autofix -- mechanical autofix for cex_wave_validator failures.

Fixes three classes of issues:
  1. Wrong/missing llm_function (aligns to ISO_LLM_FUNCTION map)
  2. Missing `quality` key in frontmatter (sets to null)
  3. Missing `title` key in frontmatter (derived from filename)
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parents[1]
BUILDER_DIR = CEX_ROOT / "archetypes" / "builders"

ISO_LLM_FUNCTION = {
    "bld_system_prompt":   "BECOME",
    "bld_manifest":        "BECOME",
    "bld_instruction":     "REASON",
    "bld_knowledge_card":  "INJECT",
    "bld_memory":          "INJECT",
    "bld_output_template": "PRODUCE",
    "bld_tools":           "CALL",
    "bld_collaboration":   "COLLABORATE",
    "bld_quality_gate":    "GOVERN",
    "bld_examples":        "GOVERN",
    "bld_architecture":    "CONSTRAIN",
    "bld_config":          "CONSTRAIN",
    "bld_schema":          "CONSTRAIN",
}

FM_RE = re.compile(r"^---\s*\n(.*?)\n---\s*\n", re.DOTALL)


def iso_prefix(name: str) -> str:
    stem = name[:-3] if name.endswith(".md") else name
    for prefix in sorted(ISO_LLM_FUNCTION.keys(), key=len, reverse=True):
        if stem.startswith(prefix + "_") or stem == prefix:
            return prefix
    return ""


def derive_title(stem: str, iso: str, kind: str) -> str:
    role = iso.replace("bld_", "").replace("_", " ").title()
    if kind:
        return f"{role} ISO - {kind}"
    return f"{role} ISO"


def derive_kind(stem: str, iso: str) -> str:
    if not iso:
        return ""
    if stem.startswith(iso + "_"):
        return stem[len(iso) + 1:]
    return ""


def patch_frontmatter(fm_text: str, patches: dict[str, str]) -> str:
    lines = fm_text.split("\n")
    seen = set()
    for i, line in enumerate(lines):
        m = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", line)
        if not m:
            continue
        key = m.group(1)
        if key in patches:
            lines[i] = f"{key}: {patches[key]}"
            seen.add(key)
    for key, val in patches.items():
        if key not in seen:
            lines.append(f"{key}: {val}")
    return "\n".join(lines)


def fix_file(path: Path) -> list[str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    m = FM_RE.match(text)
    if not m:
        return []
    fm_text = m.group(1)
    body = text[m.end():]

    stem = path.stem
    iso = iso_prefix(path.name)
    kind = derive_kind(stem, iso)

    changes: list[str] = []
    patches: dict[str, str] = {}

    existing = {}
    for line in fm_text.split("\n"):
        mm = re.match(r"^([A-Za-z_][A-Za-z0-9_]*)\s*:\s*(.*)$", line)
        if mm:
            existing[mm.group(1)] = mm.group(2).strip()

    expected = ISO_LLM_FUNCTION.get(iso)
    if expected:
        actual = existing.get("llm_function", "").strip().strip("'\"")
        if actual != expected:
            patches["llm_function"] = expected
            changes.append(f"llm_function {actual or 'MISSING'} -> {expected}")

    if "quality" not in existing:
        patches["quality"] = "null"
        changes.append("added quality: null")

    if "title" not in existing or not existing["title"]:
        patches["title"] = derive_title(stem, iso, kind)
        changes.append("added title")

    if not patches:
        return []

    new_fm = patch_frontmatter(fm_text, patches)
    new_text = f"---\n{new_fm}\n---\n{body}"
    path.write_text(new_text, encoding="utf-8", newline="\n")
    return changes


def main() -> int:
    scope = BUILDER_DIR
    if len(sys.argv) > 1:
        scope = Path(sys.argv[1])
    if not scope.exists():
        print(f"[FAIL] scope not found: {scope}")
        return 2

    files = sorted(scope.rglob("bld_*.md"))
    fixed = 0
    total_changes = 0
    for fp in files:
        changes = fix_file(fp)
        if changes:
            fixed += 1
            total_changes += len(changes)
    print(f"Fixed {fixed}/{len(files)} files, {total_changes} total changes.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
