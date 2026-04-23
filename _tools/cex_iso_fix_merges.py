#!/usr/bin/env python3
# -*- coding: ascii -*-
"""Fix bld_model_*.md and bld_eval_*.md with invalid YAML frontmatter.

The initial merge used naive frontmatter parsing. This script:
1. Reads original source files from git HEAD
2. Parses with yaml.safe_load (proper YAML)
3. Merges frontmatter correctly
4. Re-writes merged files with valid YAML using yaml.safe_dump
5. Keeps body unchanged

Usage:
  python _tools/cex_iso_fix_merges.py --dry-run
  python _tools/cex_iso_fix_merges.py
  python _tools/cex_iso_fix_merges.py --scope archetypes/builders/agent-builder/
"""

import argparse
import subprocess
import sys
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parent.parent
BUILDERS_DIR = ROOT / "archetypes" / "builders"

MERGE_CONFIGS = [
    {
        "target_prefix": "bld_model",
        "source_prefixes": ["bld_manifest", "bld_system_prompt"],
        "sections": ["Identity", "Persona"],
        "llm_function": "BECOME",
    },
    {
        "target_prefix": "bld_eval",
        "source_prefixes": ["bld_quality_gate", "bld_examples"],
        "sections": ["Quality Gate", "Examples"],
        "llm_function": "GOVERN",
    },
]


def _kind_from_dir(builder_dir: Path) -> str:
    name = builder_dir.name
    if name.endswith("-builder"):
        name = name[: -len("-builder")]
    return name.replace("-", "_")


def _git_show(path_in_repo: str) -> str:
    """Get file content from git HEAD."""
    try:
        result = subprocess.run(
            ["git", "show", f"HEAD:{path_in_repo}"],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        if result.returncode == 0:
            return result.stdout
    except Exception:
        pass
    return ""


def _parse_frontmatter_yaml(text: str) -> tuple[dict, str]:
    """Parse frontmatter using yaml.safe_load. Returns (fm_dict, body)."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end]
    body = text[end + 3:].lstrip("\n")
    try:
        fm = yaml.safe_load(fm_block) or {}
        if not isinstance(fm, dict):
            fm = {}
    except Exception:
        fm = {}
    return fm, body


def _merge_frontmatter_yaml(primary: dict, secondary: dict) -> str:
    """Merge two frontmatter dicts with proper YAML output."""
    merged = {}
    merged.update(secondary)
    merged.update(primary)
    # Remove complex/problematic fields that are builder-internal
    drop_keys = {"capabilities", "triggers", "keywords", "rules_count", "isolation",
                 "isolation_reason", "output_format_type", "density_score"}
    for k in drop_keys:
        merged.pop(k, None)
    # Ensure llm_function is set appropriately for merged file
    if "llm_function" not in merged:
        merged["llm_function"] = "BECOME"
    try:
        return yaml.safe_dump(merged, allow_unicode=False, default_flow_style=False,
                              sort_keys=False).rstrip()
    except Exception:
        # Fallback: minimal frontmatter
        return yaml.safe_dump(
            {"id": merged.get("id", "unknown"), "kind": merged.get("kind", ""),
             "pillar": merged.get("pillar", ""), "quality": None},
            allow_unicode=False
        ).rstrip()


def fix_builder(builder_dir: Path, dry_run: bool = False) -> dict:
    """Fix merged files in one builder directory."""
    kind = _kind_from_dir(builder_dir)
    counts = {"fixed": 0, "ok": 0, "skipped": 0, "errors": 0}

    for config in MERGE_CONFIGS:
        tgt_prefix = config["target_prefix"]
        tgt_name = f"{tgt_prefix}_{kind}.md"
        tgt_path = builder_dir / tgt_name

        if not tgt_path.exists():
            counts["skipped"] += 1
            continue

        # Check if frontmatter is already valid
        current_text = tgt_path.read_text(encoding="utf-8", errors="replace")
        fm, body = _parse_frontmatter_yaml(current_text)

        if fm and "id" in fm and "kind" in fm:
            counts["ok"] += 1
            continue

        # Need to fix: get originals from git HEAD
        src1_name = f"{config['source_prefixes'][0]}_{kind}.md"
        src2_name = f"{config['source_prefixes'][1]}_{kind}.md"
        rel1 = f"archetypes/builders/{builder_dir.name}/{src1_name}"
        rel2 = f"archetypes/builders/{builder_dir.name}/{src2_name}"

        src1_text = _git_show(rel1)
        src2_text = _git_show(rel2)

        if not src1_text and not src2_text:
            counts["errors"] += 1
            print(f"  [ERR] {kind}: no git HEAD source for {tgt_name}")
            continue

        fm1, body1 = _parse_frontmatter_yaml(src1_text)
        fm2, body2 = _parse_frontmatter_yaml(src2_text)

        # Set correct llm_function for merged file
        fm1["llm_function"] = config["llm_function"]

        merged_fm_yaml = _merge_frontmatter_yaml(fm1, fm2)
        sections = config["sections"]

        body_parts = []
        if body1.strip():
            body_parts.append(f"## {sections[0]}\n\n{body1.strip()}")
        if body2.strip():
            body_parts.append(f"## {sections[1]}\n\n{body2.strip()}")

        new_content = f"---\n{merged_fm_yaml}\n---\n\n" + "\n\n".join(body_parts)
        if body_parts:
            new_content += "\n"

        if dry_run:
            print(f"  [DRY] FIX {tgt_name}")
        else:
            tgt_path.write_text(new_content, encoding="ascii", errors="replace")
            print(f"  FIX {tgt_name}")
        counts["fixed"] += 1

    return counts


def main():
    parser = argparse.ArgumentParser(description="Fix merged ISO frontmatter")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--scope", type=str, default="")
    args = parser.parse_args()

    if args.scope:
        scope_path = Path(args.scope)
        if not scope_path.is_absolute():
            scope_path = ROOT / args.scope
        builder_dirs = [scope_path]
    else:
        builder_dirs = sorted(BUILDERS_DIR.glob("*-builder"))
        builder_dirs = [d for d in builder_dirs if d.is_dir() and not d.name.startswith("_")]

    mode = "[DRY RUN]" if args.dry_run else "[EXECUTE]"
    print(f"\nISO Merge Fix {mode}")
    print(f"Scope: {len(builder_dirs)} builders\n")

    totals = {"fixed": 0, "ok": 0, "skipped": 0, "errors": 0}

    for bd in builder_dirs:
        kind = _kind_from_dir(bd)
        counts = fix_builder(bd, dry_run=args.dry_run)
        for k, v in counts.items():
            totals[k] += v
        if counts["fixed"] > 0:
            print(f"  [{kind}] fixed {counts['fixed']}")

    print(f"\n{'='*50}")
    print(f"SUMMARY {mode}:")
    print(f"  Fixed:   {totals['fixed']}")
    print(f"  OK:      {totals['ok']}")
    print(f"  Skipped: {totals['skipped']}")
    print(f"  Errors:  {totals['errors']}")
    print(f"{'='*50}\n")

    if totals["errors"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
