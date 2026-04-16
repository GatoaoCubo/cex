#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validate a CEX builder directory against the archetype checklist.

v2.0 -- bld_* naming, density >= 0.8, size <= 4096B per file.

Usage:
  python _tools/validate_builder.py archetypes/builders/agent-builder
  python _tools/validate_builder.py archetypes/builders/agent-builder --json
  python _tools/validate_builder.py --all
  python _tools/validate_builder.py --all --summary
  python _tools/validate_builder.py --changed   # only staged builders
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_shared import split_frontmatter as _shared_split_frontmatter

# -- Constants ----------------------------------------------------------------

EXPECTED_KINDS = [
    "architecture",
    "collaboration",
    "config",
    "examples",
    "instruction",
    "knowledge_card",
    "manifest",
    "memory",
    "output_template",
    "quality_gate",
    "schema",
    "system_prompt",
    "tools",
]

KIND_SPECS = {
    "manifest": ("P02", "BECOME"),
    "system_prompt": ("P03", "BECOME"),
    "knowledge_card": ("P01", "INJECT"),
    "instruction": ("P03", "GUIDE"),
    "tools": ("P04", "ENABLE"),
    "output_template": ("P05", "PRODUCE"),
    "schema": ("P06", "CONSTRAIN"),
    "examples": ("P07", "PROVE"),
    "architecture": ("P08", "MAP"),
    "config": ("P09", "CONSTRAIN"),
    "memory": ("P10", "REMEMBER"),
    "quality_gate": ("P11", "GOVERN"),
    "collaboration": ("P12", "COLLABORATE"),
}

MAX_BYTES = 4096
MIN_DENSITY = 0.80
NAMING_RE = re.compile(r"^bld_[a-z][a-z0-9_]+_[a-z][a-z0-9_]+\.md$")

SNAKE_RE = re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b")
KEBAB_RE = re.compile(r"\b[a-z0-9]+(?:-[a-z0-9]+)+\b")
TOOL_RE = re.compile(
    r"\b(?:validate|compile|distill|forge|bootstrap|scaffold|rename|decompile)_[a-z0-9_]+\.py\b"
)
ENUM_SPLIT_RE = re.compile(r"\s*[|,/]\s*|\s*,\s*")
WORDLIST_IGNORE = {
    "yes",
    "no",
    "maybe",
    "true",
    "false",
    "bool",
    "null",
    "string",
    "integer",
    "float",
    "yaml",
    "json",
    "omit",
    "dash",
    "or",
    "and",
}


# -- Data classes -------------------------------------------------------------


@dataclass
class Check:
    name: str
    status: str
    detail: str
    hard: bool = True
    issues: list[str] = field(default_factory=list)


# -- Helpers ------------------------------------------------------------------


def extract_topic(dirname: str) -> str:
    """Convert builder dir name to topic suffix.

    'agent-builder' -> 'agent'
    'knowledge-card-builder' -> 'knowledge_card'
    """
    name = dirname.replace("-builder", "").replace("_builder", "")
    if name.startswith("_"):
        name = name[1:]
    return name.replace("-", "_")


def expected_filename(kind: str, topic: str) -> str:
    """Build the canonical filename for a builder ISO."""
    return f"bld_{kind}_{topic}.md"


def parse_frontmatter(text: str) -> tuple[dict[str, Any] | None, str]:
    """Split markdown into parsed frontmatter and body text."""
    fm, body = _shared_split_frontmatter(text)
    return (fm if fm else None), body


def calc_density(text: str) -> float:
    """Content lines / total lines, excluding frontmatter and filler."""
    body = text
    if text.startswith("---"):
        try:
            end = text.index("---", 3)
            body = text[end + 3 :].lstrip("\n")
        except ValueError:
            pass
    lines = body.splitlines()
    if not lines:
        return 0.0
    content = sum(1 for line in lines if line.strip() and line.strip() != "---")
    return content / len(lines)


def fenced_block(text: str) -> str:
    """Return the first fenced code block body from markdown text."""
    match = re.search(r"```(?:[a-zA-Z0-9_+-]+)?\n(.*?)```", text, flags=re.S)
    return match.group(1) if match else ""


def extract_schema_fields(text: str) -> set[str]:
    """Extract schema field names from tables and YAML or JSON examples."""
    fields: set[str] = set()
    for line in text.splitlines():
        line = line.strip()
        if line.startswith("|") and not line.startswith("|---"):
            parts = [part.strip(" `") for part in line.strip("|").split("|")]
            if parts and parts[0] and parts[0].lower() != "field":
                key = parts[0]
                if re.fullmatch(r"[A-Za-z_][A-Za-z0-9_]*", key):
                    fields.add(key)
    for block in re.findall(r"```(?:yaml|json)\n(.*?)```", text, flags=re.S):
        for line in block.splitlines():
            m = re.match(r'^\s*"?([A-Za-z_][A-Za-z0-9_]*)"?\s*:', line)
            if m:
                fields.add(m.group(1))
    return fields


def extract_template_fields(text: str) -> set[str]:
    """Extract field names from the template's first fenced block."""
    fields: set[str] = set()
    for line in fenced_block(text).splitlines():
        m = re.match(r'^\s*"?([A-Za-z_][A-Za-z0-9_]*)"?\s*:', line)
        if m:
            fields.add(m.group(1))
    return fields


def extract_config_fields(text: str, candidates: set[str]) -> set[str]:
    """Find schema field references mentioned in config prose or code spans."""
    found = {token for token in SNAKE_RE.findall(text) if token in candidates}
    for token in re.findall(r"`([A-Za-z_][A-Za-z0-9_]*)`", text):
        if token in candidates:
            found.add(token)
    return found


def normalize_enum_values(raw: str) -> set[str]:
    """Normalize an enum definition into comparable lowercase values."""
    raw = raw.strip().strip("`")
    if len(raw) > 200:
        return set()
    values = {
        value.strip("`\"'(){}[] ").lower()
        for value in ENUM_SPLIT_RE.split(raw)
        if value.strip("`\"'(){}[] ")
    }
    values = {v for v in values if v not in WORDLIST_IGNORE and not v.startswith("http")}
    return values if len(values) >= 2 else set()


def extract_named_enums_schema(text: str) -> dict[str, set[str]]:
    """Extract named enums declared in the schema document."""
    enums: dict[str, set[str]] = {}
    for line in text.splitlines():
        m = re.search(r"\|\s*([A-Za-z_][A-Za-z0-9_]*)\s*\|\s*enum\s*\(([^)]+)\)", line)
        if m:
            enums[m.group(1)] = normalize_enum_values(m.group(2))
    for m in re.finditer(r"##\s+([A-Za-z0-9_ ]+?) Enum\s*\nValid:\s*(.+)", text, flags=re.I):
        enums[m.group(1).strip().lower().replace(" ", "_")] = normalize_enum_values(m.group(2))
    return enums


def extract_named_enums_template(text: str) -> dict[str, set[str]]:
    """Extract named enums encoded as template placeholders."""
    enums: dict[str, set[str]] = {}
    for line in fenced_block(text).splitlines():
        m = re.search(r'^\s*"?([A-Za-z_][A-Za-z0-9_]*)"?\s*:\s*"?\{\{([^{}]+)\}\}"?', line)
        if not m:
            continue
        values = normalize_enum_values(m.group(2))
        if len(values) >= 2:
            enums[m.group(1)] = values
    return enums


def extract_named_enums_config(text: str) -> dict[str, set[str]]:
    """Extract named enums documented in the config document."""
    enums: dict[str, set[str]] = {}
    current = ""
    for line in text.splitlines():
        heading = re.match(r"##\s+(.+)", line.strip())
        if heading:
            current = heading.group(1).lower().replace(" ", "_")
        valid = re.search(r"Valid:\s*(.+)", line)
        if valid:
            enums[current or "enum"] = normalize_enum_values(valid.group(1))
        row = re.search(r"\|\s*([A-Za-z_][A-Za-z0-9_ ]+)\s*\|\s*[^|]*\|\s*`([^`]+)`\s*\|", line)
        if row:
            values = normalize_enum_values(row.group(2))
            if len(values) >= 2:
                enums[row.group(1).strip().lower().replace(" ", "_")] = values
    return enums


def collect_forward_refs(
    builder_dir: Path,
) -> tuple[list[tuple[str, str, bool]], list[tuple[str, str, bool]]]:
    """Collect builder and tool references mentioned across builder files."""
    builder_refs: list[tuple[str, str, bool]] = []
    tool_refs: list[tuple[str, str, bool]] = []
    for path in sorted(builder_dir.glob("*.md")):
        section_planned = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("#"):
                section_planned = "[PLANNED]" in line
            for match in sorted(set(KEBAB_RE.findall(line))):
                if (
                    match == builder_dir.name
                    or match == "type-builder"
                    or not match.endswith("-builder")
                ):
                    continue
                builder_refs.append((path.name, match, "[PLANNED]" in line or section_planned))
            for match in sorted(set(TOOL_RE.findall(line))):
                tool_refs.append((path.name, match, "[PLANNED]" in line or section_planned))
    return builder_refs, tool_refs


def find_file_by_kind(builder_dir: Path, kind: str, topic: str) -> Path | None:
    """Find a builder file by kind, trying bld_ naming first, then legacy."""
    bld_path = builder_dir / expected_filename(kind, topic)
    if bld_path.exists():
        return bld_path
    # Legacy fallback mapping
    legacy_map = {
        "manifest": "MANIFEST.md",
        "system_prompt": "SYSTEM_PROMPT.md",
        "knowledge_card": "KNOWLEDGE.md",
        "instruction": "INSTRUCTIONS.md",
        "tools": "TOOLS.md",
        "output_template": "OUTPUT_TEMPLATE.md",
        "schema": "SCHEMA.md",
        "examples": "EXAMPLES.md",
        "architecture": "ARCHITECTURE.md",
        "config": "CONFIG.md",
        "memory": "MEMORY.md",
        "quality_gate": "QUALITY_GATES.md",
        "collaboration": "COLLABORATION.md",
    }
    legacy = builder_dir / legacy_map.get(kind, "")
    if legacy.exists():
        return legacy
    return None


# -- Core validator -----------------------------------------------------------


def validate_builder(builder_dir: Path) -> dict[str, Any]:
    """Run the full structural and semantic validation suite for one builder."""
    checks: list[Check] = []
    issues: list[str] = []
    topic = extract_topic(builder_dir.name)

    # -- Check 1: Structure (13 files present) --------------------------------
    found_kinds: dict[str, Path] = {}
    missing_kinds: list[str] = []
    for kind in EXPECTED_KINDS:
        path = find_file_by_kind(builder_dir, kind, topic)
        if path:
            found_kinds[kind] = path
        else:
            missing_kinds.append(kind)

    extra_files = [
        f.name
        for f in builder_dir.glob("*.md")
        if f.name not in {p.name for p in found_kinds.values()} and f.name != "README.md"
    ]
    struct_issues: list[str] = []
    if missing_kinds:
        struct_issues.append(f"missing_kinds={missing_kinds}")
    if extra_files:
        struct_issues.append(f"extra={extra_files[:5]}")
    checks.append(
        Check(
            "structure",
            "PASS" if not struct_issues else "FAIL",
            f"{len(found_kinds)}/13 files",
            True,
            struct_issues,
        )
    )
    issues.extend(struct_issues)

    # -- Check 2: Naming convention (bld_{kind}_{topic}.md) -------------------
    naming_issues: list[str] = []
    for kind, path in found_kinds.items():
        expected = expected_filename(kind, topic)
        if path.name != expected:
            naming_issues.append(f"{path.name} should be {expected}")
        elif not NAMING_RE.match(path.name):
            naming_issues.append(f"{path.name} does not match bld_* pattern")
    checks.append(
        Check(
            "naming",
            "PASS" if not naming_issues else "WARN",
            f"{len(found_kinds) - len(naming_issues)}/{len(found_kinds)} bld_* compliant",
            False,
            naming_issues,
        )
    )

    # -- Check 3: Frontmatter (valid YAML, required fields) ------------------
    fm_issues: list[str] = []
    for kind, path in found_kinds.items():
        text = path.read_text(encoding="utf-8", errors="ignore")
        fm, _body = parse_frontmatter(text)
        if fm is None:
            fm_issues.append(f"{path.name}: missing or invalid frontmatter")
            continue
        for key in ("lp", "llm_function", "purpose"):
            if not fm.get(key):
                fm_issues.append(f"{path.name}: missing `{key}`")
    checks.append(
        Check(
            "frontmatter",
            "PASS" if not fm_issues else "FAIL",
            f"{len(found_kinds) - len(fm_issues)}/{len(found_kinds)} aligned",
            True,
            fm_issues,
        )
    )
    issues.extend(fm_issues)

    # -- Check 4: Density >= 0.8 per file ------------------------------------
    density_issues: list[str] = []
    densities: list[float] = []
    for kind, path in found_kinds.items():
        text = path.read_text(encoding="utf-8", errors="ignore")
        d = calc_density(text)
        densities.append(d)
        if d < MIN_DENSITY:
            density_issues.append(f"{path.name}: density={d:.2f} (min {MIN_DENSITY})")
    avg_density = sum(densities) / len(densities) if densities else 0.0
    checks.append(
        Check(
            "density",
            "PASS" if not density_issues else "FAIL",
            f"avg={avg_density:.2f} min={min(densities):.2f}" if densities else "no files",
            True,
            density_issues,
        )
    )
    issues.extend(density_issues)

    # -- Check 5: Size <= 4096 bytes per file ---------------------------------
    size_issues: list[str] = []
    total_bytes = 0
    for kind, path in found_kinds.items():
        size = path.stat().st_size
        total_bytes += size
        if size > MAX_BYTES:
            size_issues.append(f"{path.name}: {size}B > {MAX_BYTES}B limit")
        elif size < 200:
            size_issues.append(f"{path.name}: {size}B suspiciously small")
    checks.append(
        Check(
            "size",
            "PASS" if not size_issues else "WARN",
            f"total={total_bytes}B avg={total_bytes // max(len(found_kinds), 1)}B",
            False,
            size_issues,
        )
    )

    # -- Check 6: Source hierarchy (schema > template > config) ---------------
    schema_text = (
        found_kinds["schema"].read_text(encoding="utf-8") if "schema" in found_kinds else ""
    )
    template_text = (
        found_kinds["output_template"].read_text(encoding="utf-8")
        if "output_template" in found_kinds
        else ""
    )
    config_text = (
        found_kinds["config"].read_text(encoding="utf-8") if "config" in found_kinds else ""
    )
    schema_fields = extract_schema_fields(schema_text)
    template_fields = extract_template_fields(template_text)
    config_fields = extract_config_fields(config_text, schema_fields | template_fields)
    hierarchy_issues: list[str] = []
    core_schema_fields = {f for f in schema_fields if f in template_fields or f in config_fields}
    missing_in_template = sorted(f for f in core_schema_fields if f not in template_fields)
    extra_in_template = sorted(
        f for f in template_fields if f not in schema_fields and f not in {"primary", "related"}
    )
    if missing_in_template:
        hierarchy_issues.append(f"template_missing={missing_in_template[:12]}")
    if extra_in_template:
        hierarchy_issues.append(f"template_extra={extra_in_template[:12]}")
    if not config_fields:
        hierarchy_issues.append("config_restricts_no_schema_fields")
    checks.append(
        Check(
            "source_hierarchy",
            "PASS" if not hierarchy_issues else "FAIL",
            f"schema={len(schema_fields)} template={len(template_fields)} config_refs={len(config_fields)}",
            True,
            hierarchy_issues,
        )
    )
    issues.extend(hierarchy_issues)

    # -- Check 7: Forward promises (referenced builders/tools exist) ----------
    fp_issues: list[str] = []
    builder_refs, tool_refs = collect_forward_refs(builder_dir)
    repo_root = builder_dir.parents[2]
    builder_index: dict[str, list[tuple[str, bool]]] = {}
    tool_index: dict[str, list[tuple[str, bool]]] = {}
    for filename, builder_name, planned in builder_refs:
        builder_index.setdefault(builder_name, []).append((filename, planned))
    for filename, tool_name, planned in tool_refs:
        tool_index.setdefault(tool_name, []).append((filename, planned))
    for builder_name, refs in builder_index.items():
        exists = (repo_root / "archetypes" / "builders" / builder_name).exists()
        if not exists and not any(planned for _fn, planned in refs):
            fp_issues.append(f"{refs[0][0]}: builder `{builder_name}` missing and not [PLANNED]")
    for tool_name, refs in tool_index.items():
        exists = (repo_root / "_tools" / tool_name).exists()
        if not exists and not any(planned for _fn, planned in refs):
            fp_issues.append(f"{refs[0][0]}: tool `{tool_name}` missing and not [PLANNED]")
    checks.append(
        Check(
            "forward_promises",
            "PASS" if not fp_issues else "FAIL",
            f"{len(builder_refs)} builder refs, {len(tool_refs)} tool refs",
            True,
            fp_issues,
        )
    )
    issues.extend(fp_issues)

    # -- Score ----------------------------------------------------------------
    hard_checks = [c for c in checks if c.hard]
    hard_passed = sum(1 for c in hard_checks if c.status == "PASS")
    hard_failed = len(hard_checks) - hard_passed
    score = round(
        sum(10.0 if c.status == "PASS" else 8.0 if c.status == "WARN" else 0.0 for c in checks)
        / len(checks),
        1,
    )
    return {
        "builder": builder_dir.name,
        "topic": topic,
        "path": str(builder_dir),
        "checks": {c.name: c.status for c in checks},
        "hard_gates": {"passed": hard_passed, "failed": hard_failed},
        "soft_score": score,
        "density_avg": round(avg_density, 2),
        "total_bytes": total_bytes,
        "issues": issues + size_issues,
        "details": {
            c.name: {"status": c.status, "detail": c.detail, "issues": c.issues} for c in checks
        },
    }


# -- Output -------------------------------------------------------------------


def print_human(result: dict[str, Any]) -> None:
    """Render one builder validation result in a compact terminal format."""
    sep = "=" * 72
    print(sep)
    print(
        f"  {result['builder']}  HARD {result['hard_gates']['passed']}/"
        f"{result['hard_gates']['passed'] + result['hard_gates']['failed']}  "
        f"SCORE {result['soft_score']}/10  "
        f"DENSITY {result['density_avg']}  SIZE {result['total_bytes']}B"
    )
    print(sep)
    for name, detail in result["details"].items():
        icon = "+" if detail["status"] == "PASS" else "!" if detail["status"] == "WARN" else "X"
        print(f"  [{icon}] {name:<20} {detail['status']:<4}  {detail['detail']}")
        for issue in detail["issues"]:
            print(f"      - {issue}")


def get_changed_builders() -> list[Path]:
    """Return builder dirs with staged changes."""
    try:
        output = subprocess.check_output(
            ["git", "diff", "--cached", "--name-only"],
            text=True,
            cwd=Path(__file__).resolve().parent.parent,
        )
    except (subprocess.CalledProcessError, FileNotFoundError):
        return []
    builders_dir = Path(__file__).resolve().parent.parent / "archetypes" / "builders"
    changed: set[Path] = set()
    for line in output.strip().splitlines():
        path = Path(line)
        if path.parts[:3] == ("archetypes", "builders") and len(path.parts) > 3:
            builder_dir = builders_dir / path.parts[2]
            if builder_dir.is_dir():
                changed.add(builder_dir)
    return sorted(changed)


def main() -> None:
    """Validate one or more builders selected from the CLI."""
    parser = argparse.ArgumentParser(description="Validate CEX builder directories (v2).")
    parser.add_argument("builder", nargs="?", help="Path to builder directory")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    parser.add_argument("--summary", action="store_true", help="Print compact summary")
    parser.add_argument("--all", action="store_true", help="Validate all builders")
    parser.add_argument("--changed", action="store_true", help="Validate only staged builders")
    args = parser.parse_args()

    targets: list[Path] = []

    if args.all:
        builders_dir = Path(__file__).resolve().parent.parent / "archetypes" / "builders"
        targets = sorted(
            d for d in builders_dir.iterdir() if d.is_dir() and not d.name.startswith(".")
        )
    elif args.changed:
        targets = get_changed_builders()
        if not targets:
            print("No staged builder changes found.")
            sys.exit(0)
    elif args.builder:
        targets = [Path(args.builder).resolve()]
    else:
        parser.print_help()
        sys.exit(1)

    results: list[dict[str, Any]] = []
    any_failed = False

    for target in targets:
        if not target.exists() or not target.is_dir():
            print(f"Not found: {target}", file=sys.stderr)
            any_failed = True
            continue
        result = validate_builder(target)
        results.append(result)
        if result["hard_gates"]["failed"]:
            any_failed = True

    if args.json:
        print(json.dumps(results if len(results) > 1 else results[0], indent=2, ensure_ascii=False))
    elif args.summary:
        for result in results:
            counts = Counter(result["checks"].values())
            print(
                f"{result['builder']:<35} "
                f"HARD {result['hard_gates']['passed']}/{result['hard_gates']['passed'] + result['hard_gates']['failed']} "
                f"SCORE {result['soft_score']}/10 "
                f"D={result['density_avg']} "
                f"{dict(counts)}"
            )
        print(
            f"\n--- {len(results)} builders | "
            f"{sum(1 for r in results if not r['hard_gates']['failed'])} PASS | "
            f"{sum(1 for r in results if r['hard_gates']['failed'])} FAIL ---"
        )
    else:
        for result in results:
            print_human(result)
            print()
        if len(results) > 1:
            print(
                f"--- {len(results)} builders | "
                f"{sum(1 for r in results if not r['hard_gates']['failed'])} PASS | "
                f"{sum(1 for r in results if r['hard_gates']['failed'])} FAIL ---"
            )

    sys.exit(1 if any_failed else 0)


if __name__ == "__main__":
    main()
