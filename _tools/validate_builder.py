#!/usr/bin/env python3
"""Validate a CEX builder directory against the archetype checklist."""

from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

EXPECTED_FILES = [
    "MANIFEST.md",
    "SYSTEM_PROMPT.md",
    "KNOWLEDGE.md",
    "INSTRUCTIONS.md",
    "TOOLS.md",
    "OUTPUT_TEMPLATE.md",
    "SCHEMA.md",
    "EXAMPLES.md",
    "ARCHITECTURE.md",
    "CONFIG.md",
    "MEMORY.md",
    "QUALITY_GATES.md",
    "COLLABORATION.md",
]

FILE_SPECS = {
    "MANIFEST.md": ("P02", "BECOME"),
    "SYSTEM_PROMPT.md": ("P03", "BECOME"),
    "KNOWLEDGE.md": ("P01", "INJECT"),
    "INSTRUCTIONS.md": ("P03", "GUIDE"),
    "TOOLS.md": ("P04", "ENABLE"),
    "OUTPUT_TEMPLATE.md": ("P05", "PRODUCE"),
    "SCHEMA.md": ("P06", "CONSTRAIN"),
    "EXAMPLES.md": ("P07", "PROVE"),
    "ARCHITECTURE.md": ("P08", "MAP"),
    "CONFIG.md": ("P09", "CONSTRAIN"),
    "MEMORY.md": ("P10", "REMEMBER"),
    "QUALITY_GATES.md": ("P11", "GOVERN"),
    "COLLABORATION.md": ("P12", "COLLABORATE"),
}

SNAKE_RE = re.compile(r"\b[a-z][a-z0-9]*(?:_[a-z0-9]+)+\b")
KEBAB_RE = re.compile(r"\b[a-z0-9]+(?:-[a-z0-9]+)+\b")
TOOL_RE = re.compile(r"\b(?:validate|compile|distill|forge|bootstrap|scaffold|rename|decompile)_[a-z0-9_]+\.py\b")
ENUM_SPLIT_RE = re.compile(r"\s*[|,/]\s*|\s*,\s*")
WORDLIST_IGNORE = {
    "yes", "no", "maybe", "true", "false", "bool", "null", "string",
    "integer", "float", "yaml", "json", "omit", "dash", "or", "and",
}


@dataclass
class Check:
    name: str
    status: str
    detail: str
    hard: bool = True
    issues: list[str] = field(default_factory=list)


def parse_frontmatter(text: str) -> tuple[dict[str, Any] | None, str]:
    if not text.startswith("---"):
        return None, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return None, text
    try:
        return yaml.safe_load(parts[1]) or {}, parts[2].strip()
    except yaml.YAMLError:
        return None, text


def fenced_block(text: str) -> str:
    match = re.search(r"```(?:[a-zA-Z0-9_+-]+)?\n(.*?)```", text, flags=re.S)
    return match.group(1) if match else ""


def flatten_keys(data: Any) -> set[str]:
    out: set[str] = set()
    if isinstance(data, dict):
        for key, value in data.items():
            out.add(str(key))
            out.update(flatten_keys(value))
    elif isinstance(data, list):
        for item in data:
            out.update(flatten_keys(item))
    return out


def extract_schema_fields(text: str) -> set[str]:
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
    fields: set[str] = set()
    for line in fenced_block(text).splitlines():
        m = re.match(r'^\s*"?([A-Za-z_][A-Za-z0-9_]*)"?\s*:', line)
        if m:
            fields.add(m.group(1))
    return fields


def extract_config_fields(text: str, candidates: set[str]) -> set[str]:
    found = {token for token in SNAKE_RE.findall(text) if token in candidates}
    for token in re.findall(r"`([A-Za-z_][A-Za-z0-9_]*)`", text):
        if token in candidates:
            found.add(token)
    return found


def normalize_enum_values(raw: str) -> set[str]:
    raw = raw.strip().strip("`")
    if len(raw) > 200:
        return set()
    values = {
        value.strip("`\"'(){}[] ").lower()
        for value in ENUM_SPLIT_RE.split(raw)
        if value.strip("`\"'(){}[] ")
    }
    values = {value for value in values if value not in WORDLIST_IGNORE and not value.startswith("http")}
    return values if len(values) >= 2 else set()


def extract_named_enums_schema(text: str) -> dict[str, set[str]]:
    enums: dict[str, set[str]] = {}
    for line in text.splitlines():
        m = re.search(r"\|\s*([A-Za-z_][A-Za-z0-9_]*)\s*\|\s*enum\s*\(([^)]+)\)", line)
        if m:
            enums[m.group(1)] = normalize_enum_values(m.group(2))
    for m in re.finditer(r"##\s+([A-Za-z0-9_ ]+?) Enum\s*\nValid:\s*(.+)", text, flags=re.I):
        enums[m.group(1).strip().lower().replace(" ", "_")] = normalize_enum_values(m.group(2))
    return enums


def extract_named_enums_template(text: str) -> dict[str, set[str]]:
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


def collect_forward_refs(builder_dir: Path) -> tuple[list[tuple[str, str, bool]], list[tuple[str, str, bool]]]:
    builder_refs: list[tuple[str, str, bool]] = []
    tool_refs: list[tuple[str, str, bool]] = []
    for path in sorted(builder_dir.glob("*.md")):
        section_planned = False
        for line in path.read_text(encoding="utf-8").splitlines():
            if line.strip().startswith("#"):
                section_planned = "[PLANNED]" in line
            for match in sorted(set(KEBAB_RE.findall(line))):
                if match == builder_dir.name or match == "type-builder" or not match.endswith("-builder"):
                    continue
                builder_refs.append((path.name, match, "[PLANNED]" in line or section_planned))
            for match in sorted(set(TOOL_RE.findall(line))):
                tool_refs.append((path.name, match, "[PLANNED]" in line or section_planned))
    return builder_refs, tool_refs


def validate_builder(builder_dir: Path) -> dict[str, Any]:
    checks: list[Check] = []
    issues: list[str] = []
    actual_files = sorted(path.name for path in builder_dir.glob("*.md"))
    missing = [name for name in EXPECTED_FILES if name not in actual_files]
    extra = [name for name in actual_files if name not in EXPECTED_FILES]
    structure_issues = []
    if missing:
        structure_issues.append(f"missing={missing}")
    if extra:
        structure_issues.append(f"extra={extra}")
    checks.append(Check("structure", "PASS" if not structure_issues else "FAIL", f"{len(actual_files)}/13 files", True, structure_issues))
    issues.extend(structure_issues)

    fm_issues: list[str] = []
    for name in EXPECTED_FILES:
        path = builder_dir / name
        if not path.exists():
            continue
        fm, _body = parse_frontmatter(path.read_text(encoding="utf-8"))
        if fm is None:
            fm_issues.append(f"{name}: missing or invalid frontmatter")
            continue
        for key in ("lp", "llm_function", "purpose"):
            if not fm.get(key):
                fm_issues.append(f"{name}: missing `{key}`")
    checks.append(Check("frontmatter", "PASS" if not fm_issues else "FAIL", f"{len(EXPECTED_FILES) - len(fm_issues)}/{len(EXPECTED_FILES)} aligned", True, fm_issues))
    issues.extend(fm_issues)

    schema_text = (builder_dir / "SCHEMA.md").read_text(encoding="utf-8") if (builder_dir / "SCHEMA.md").exists() else ""
    template_text = (builder_dir / "OUTPUT_TEMPLATE.md").read_text(encoding="utf-8") if (builder_dir / "OUTPUT_TEMPLATE.md").exists() else ""
    config_text = (builder_dir / "CONFIG.md").read_text(encoding="utf-8") if (builder_dir / "CONFIG.md").exists() else ""
    schema_fields = extract_schema_fields(schema_text)
    template_fields = extract_template_fields(template_text)
    config_fields = extract_config_fields(config_text, schema_fields | template_fields)
    hierarchy_issues: list[str] = []
    core_schema_fields = {field for field in schema_fields if field in template_fields or field in config_fields}
    missing_in_template = sorted(field for field in core_schema_fields if field not in template_fields)
    extra_in_template = sorted(field for field in template_fields if field not in schema_fields and field not in {"primary", "related"})
    if missing_in_template:
        hierarchy_issues.append(f"template_missing={missing_in_template[:12]}")
    if extra_in_template:
        hierarchy_issues.append(f"template_extra={extra_in_template[:12]}")
    if not config_fields:
        hierarchy_issues.append("config_restricts_no_schema_fields")
    checks.append(Check("source_hierarchy", "PASS" if not hierarchy_issues else "FAIL", f"schema={len(schema_fields)} template={len(template_fields)} config_refs={len(config_fields)}", True, hierarchy_issues))
    issues.extend(hierarchy_issues)

    schema_enums = extract_named_enums_schema(schema_text)
    template_enums = extract_named_enums_template(template_text)
    config_enums = extract_named_enums_config(config_text)
    enum_issues: list[str] = []
    shared_any = False
    for name, schema_values in schema_enums.items():
        template_values = template_enums.get(name)
        config_values = config_enums.get(name) or config_enums.get(f"{name}_enum")
        if template_values:
            shared_any = True
            if template_values != schema_values:
                enum_issues.append(f"{name}: schema!=template {sorted(schema_values)} vs {sorted(template_values)}")
        if config_values:
            shared_any = True
            if config_values != schema_values:
                enum_issues.append(f"{name}: schema!=config {sorted(schema_values)} vs {sorted(config_values)}")
    if not shared_any and schema_enums:
        enum_issues.append("no shared enums found across schema/template/config")
    checks.append(Check("cross_reference", "PASS" if not enum_issues else "FAIL", f"schema_enums={len(schema_enums)} template_enums={len(template_enums)} config_enums={len(config_enums)}", True, enum_issues))
    issues.extend(enum_issues)

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
        if not exists and not any(planned for _filename, planned in refs):
            fp_issues.append(f"{refs[0][0]}: builder `{builder_name}` missing and not [PLANNED]")
    for tool_name, refs in tool_index.items():
        exists = (repo_root / "_tools" / tool_name).exists()
        if not exists and not any(planned for _filename, planned in refs):
            fp_issues.append(f"{refs[0][0]}: tool `{tool_name}` missing and not [PLANNED]")
    checks.append(Check("forward_promises", "PASS" if not fp_issues else "FAIL", f"{len(builder_refs)} builder refs, {len(tool_refs)} tool refs", True, fp_issues))
    issues.extend(fp_issues)

    size_issues: list[str] = []
    total_bytes = 0
    for name in EXPECTED_FILES:
        path = builder_dir / name
        if not path.exists():
            continue
        size = path.stat().st_size
        total_bytes += size
        if not 500 <= size <= 5 * 1024:
            size_issues.append(f"{name}: {size}B outside 500B-5KB")
    if not 4 * 1024 <= total_bytes <= 15 * 1024:
        size_issues.append(f"total: {total_bytes}B outside 4KB-15KB")
    checks.append(Check("size", "PASS" if not size_issues else "WARN", f"total={total_bytes}B", False, size_issues))

    hard_checks = [check for check in checks if check.hard]
    hard_passed = sum(1 for check in hard_checks if check.status == "PASS")
    hard_failed = len(hard_checks) - hard_passed
    score = round(sum(10.0 if check.status == "PASS" else 8.0 if check.status == "WARN" else 0.0 for check in checks) / len(checks), 1)
    return {
        "builder": builder_dir.name,
        "path": str(builder_dir),
        "checks": {check.name: check.status for check in checks},
        "hard_gates": {"passed": hard_passed, "failed": hard_failed},
        "soft_score": score,
        "issues": issues + size_issues,
        "details": {
            check.name: {"status": check.status, "detail": check.detail, "issues": check.issues}
            for check in checks
        },
    }


def print_human(result: dict[str, Any]) -> None:
    sep = "=" * 72
    print(sep)
    print(
        f"  {result['builder']}  HARD {result['hard_gates']['passed']}/"
        f"{result['hard_gates']['passed'] + result['hard_gates']['failed']}  "
        f"SCORE {result['soft_score']}/10"
    )
    print(sep)
    for name, detail in result["details"].items():
        icon = "+" if detail["status"] == "PASS" else "!" if detail["status"] == "WARN" else "X"
        print(f"  [{icon}] {name:<17} {detail['status']:<4}  {detail['detail']}")
        for issue in detail["issues"]:
            print(f"      - {issue}")


def main() -> None:
    parser = argparse.ArgumentParser(description="Validate a CEX builder directory.")
    parser.add_argument("builder", help="Path to builder directory")
    parser.add_argument("--json", action="store_true", help="Print JSON only")
    parser.add_argument("--summary", action="store_true", help="Print compact summary")
    args = parser.parse_args()

    target = Path(args.builder).resolve()
    if not target.exists() or not target.is_dir():
        print(f"Not found: {target}", file=sys.stderr)
        sys.exit(1)

    result = validate_builder(target)
    if args.json:
        print(json.dumps(result, indent=2, ensure_ascii=False))
    elif args.summary:
        counts = Counter(result["checks"].values())
        print(
            f"{result['builder']:<28} "
            f"HARD {result['hard_gates']['passed']}/{result['hard_gates']['passed'] + result['hard_gates']['failed']} "
            f"SCORE {result['soft_score']}/10 {dict(counts)}"
        )
    else:
        print_human(result)
        print()
        print(json.dumps(result, indent=2, ensure_ascii=False))
    sys.exit(1 if result["hard_gates"]["failed"] else 0)


if __name__ == "__main__":
    main()
