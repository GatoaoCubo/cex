#!/usr/bin/env python3
# -*- coding: ascii -*-
"""CEX ISO Migration: 13-ISO -> 12-ISO pillar-mapped builder structure.

Operations per builder:
  RENAME (4): bld_instruction -> bld_prompt (P03)
              bld_knowledge_card -> bld_knowledge (P01)
              bld_output_template -> bld_output (P05)
              bld_collaboration -> bld_orchestration (P12)
  MERGE  (2): bld_manifest + bld_system_prompt -> bld_model (P02)
              bld_quality_gate + bld_examples -> bld_eval (P07)
  NEW    (1): bld_feedback_{kind}.md (P11) -- generated from template

Usage:
  python _tools/cex_iso_migrate.py --dry-run
  python _tools/cex_iso_migrate.py --scope archetypes/builders/agent-builder/
  python _tools/cex_iso_migrate.py
  python _tools/cex_iso_migrate.py --verify
"""

import argparse
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILDERS_DIR = ROOT / "archetypes" / "builders"

# Migration operations
RENAMES = {
    "bld_instruction_{kind}.md": "bld_prompt_{kind}.md",
    "bld_knowledge_card_{kind}.md": "bld_knowledge_{kind}.md",
    "bld_output_template_{kind}.md": "bld_output_{kind}.md",
    "bld_collaboration_{kind}.md": "bld_orchestration_{kind}.md",
}

MERGES = [
    {
        "sources": ["bld_manifest_{kind}.md", "bld_system_prompt_{kind}.md"],
        "target": "bld_model_{kind}.md",
        "sections": ["Identity", "Persona"],
        "priority": 0,  # index 0 = primary (frontmatter priority)
    },
    {
        "sources": ["bld_quality_gate_{kind}.md", "bld_examples_{kind}.md"],
        "target": "bld_eval_{kind}.md",
        "sections": ["Quality Gate", "Examples"],
        "priority": 0,
    },
]

EXPECTED_12_ISOS = [
    "bld_knowledge_{kind}.md",    # P01
    "bld_model_{kind}.md",        # P02
    "bld_prompt_{kind}.md",       # P03
    "bld_tools_{kind}.md",        # P04
    "bld_output_{kind}.md",       # P05
    "bld_schema_{kind}.md",       # P06
    "bld_eval_{kind}.md",         # P07
    "bld_architecture_{kind}.md", # P08
    "bld_config_{kind}.md",       # P09
    "bld_memory_{kind}.md",       # P10
    "bld_feedback_{kind}.md",     # P11
    "bld_orchestration_{kind}.md",# P12
]

FEEDBACK_TEMPLATE = """\
---
id: p11_fb_{kind}
kind: builder_default
pillar: P11
title: "Feedback: {kind_title}"
domain: {kind}
quality: null
tags: [feedback, anti-patterns, P11, {kind}]
---

# Feedback: {kind_title}

## Anti-Patterns (NEVER do)

- **No self-score**: never assign quality score to your own output
- **No hallucination**: cite sources; do not invent facts, metrics, or references
- **ASCII-only code**: no emoji, no accented chars in .py/.ps1/.sh output
- **No partial output**: produce complete artifact; no truncation, no "..." placeholders
- **No frontmatter omission**: every artifact must start with valid YAML frontmatter
- **No quality below 8.0**: re-draft before publishing if self-assessment < 8.0

## Common Failure Modes for {kind_title}

- Vague identity section (no concrete capabilities, tools, or constraints)
- Missing required frontmatter fields (id, kind, pillar, quality: null)
- Body prose only -- no tables, no structured data (density < 0.85)
- Output not matching the output template schema

## Correction Protocol

1. Identify which H01-H07 gate failed
2. Return to F6 PRODUCE with explicit fix instruction
3. Re-run F7 GOVERN
4. Maximum 2 retries before escalating to N07
"""


def _kind_from_dir(builder_dir: Path) -> str:
    """Extract kind slug from builder directory name (e.g. agent-builder -> agent)."""
    name = builder_dir.name
    if name.endswith("-builder"):
        name = name[: -len("-builder")]
    return name.replace("-", "_")


def _kind_title(kind: str) -> str:
    return kind.replace("_", " ").title()


def _parse_frontmatter(text: str) -> tuple[dict, str]:
    """Return (frontmatter_dict, body_text). Frontmatter keys kept as raw lines."""
    if not text.startswith("---"):
        return {}, text
    end = text.find("---", 3)
    if end == -1:
        return {}, text
    fm_block = text[3:end].strip()
    body = text[end + 3:].lstrip("\n")
    fm: dict = {}
    for line in fm_block.splitlines():
        if ":" in line:
            k, _, v = line.partition(":")
            fm[k.strip()] = v.strip()
    return fm, body


def _merge_frontmatter(primary: dict, secondary: dict) -> str:
    """Merge two frontmatter dicts (primary wins on conflict). Return YAML block."""
    merged = dict(secondary)
    merged.update(primary)
    lines = []
    for k, v in merged.items():
        lines.append(f"{k}: {v}")
    return "\n".join(lines)


def _read(path: Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except OSError:
        return ""


def _git_mv(src: Path, dst: Path, dry_run: bool) -> bool:
    """Rename via git mv to preserve history."""
    if dry_run:
        print(f"  [DRY] git mv {src.name} -> {dst.name}")
        return True
    try:
        result = subprocess.run(
            ["git", "mv", str(src), str(dst)],
            cwd=str(ROOT),
            capture_output=True,
            text=True,
        )
        if result.returncode != 0:
            print(f"  [WARN] git mv failed for {src.name}: {result.stderr.strip()}")
            # Fall back to plain rename
            src.rename(dst)
        return True
    except Exception as e:
        print(f"  [ERR] rename {src.name}: {e}")
        return False


def migrate_builder(builder_dir: Path, dry_run: bool = False) -> dict:
    """Migrate one builder directory. Returns counters dict."""
    kind = _kind_from_dir(builder_dir)
    counts = {"renames": 0, "merges": 0, "created": 0, "skipped": 0, "errors": 0}

    # --- RENAMES ---
    for old_pat, new_pat in RENAMES.items():
        old_name = old_pat.replace("{kind}", kind)
        new_name = new_pat.replace("{kind}", kind)
        old_path = builder_dir / old_name
        new_path = builder_dir / new_name
        if not old_path.exists():
            counts["skipped"] += 1
            continue
        if new_path.exists():
            # Already migrated
            counts["skipped"] += 1
            continue
        if _git_mv(old_path, new_path, dry_run):
            if not dry_run:
                print(f"  RENAME {old_name} -> {new_name}")
            counts["renames"] += 1
        else:
            counts["errors"] += 1

    # --- MERGES ---
    for merge_spec in MERGES:
        src_names = [s.replace("{kind}", kind) for s in merge_spec["sources"]]
        tgt_name = merge_spec["target"].replace("{kind}", kind)
        tgt_path = builder_dir / tgt_name
        src_paths = [builder_dir / n for n in src_names]

        if tgt_path.exists():
            # Already merged -- clean up sources if still present
            for sp in src_paths:
                if sp.exists():
                    if not dry_run:
                        try:
                            subprocess.run(["git", "rm", "-", str(sp)], cwd=str(ROOT),
                                           capture_output=True)
                        except Exception:
                            sp.unlink(missing_ok=True)
                    else:
                        print(f"  [DRY] git rm {sp.name} (already merged)")
            counts["skipped"] += 1
            continue

        if not any(sp.exists() for sp in src_paths):
            counts["skipped"] += 1
            continue

        # Build merged content
        primary_text = _read(src_paths[0]) if src_paths[0].exists() else ""
        secondary_text = _read(src_paths[1]) if len(src_paths) > 1 and src_paths[1].exists() else ""

        primary_fm, primary_body = _parse_frontmatter(primary_text)
        secondary_fm, secondary_body = _parse_frontmatter(secondary_text)

        merged_fm = _merge_frontmatter(primary_fm, secondary_fm)
        section_names = merge_spec["sections"]

        body_parts = []
        if primary_body.strip():
            body_parts.append(f"## {section_names[0]}\n\n{primary_body.strip()}")
        if secondary_body.strip():
            body_parts.append(f"## {section_names[1]}\n\n{secondary_body.strip()}")

        merged_content = f"---\n{merged_fm}\n---\n\n" + "\n\n".join(body_parts)

        if dry_run:
            print(f"  [DRY] MERGE {src_names[0]} + {src_names[1]} -> {tgt_name}")
        else:
            tgt_path.write_text(merged_content, encoding="utf-8")
            print(f"  MERGE {src_names[0]} + {src_names[1]} -> {tgt_name}")
            # Remove source files via git rm
            for sp in src_paths:
                if sp.exists():
                    try:
                        subprocess.run(["git", "rm", "-", str(sp)], cwd=str(ROOT),
                                       capture_output=True)
                    except Exception:
                        sp.unlink(missing_ok=True)
        counts["merges"] += 1

    # --- NEW: bld_feedback ---
    fb_name = f"bld_feedback_{kind}.md"
    fb_path = builder_dir / fb_name
    if fb_path.exists():
        counts["skipped"] += 1
    else:
        content = FEEDBACK_TEMPLATE.replace("{kind}", kind).replace(
            "{kind_title}", _kind_title(kind)
        )
        if dry_run:
            print(f"  [DRY] CREATE {fb_name}")
        else:
            fb_path.write_text(content, encoding="utf-8")
            print(f"  CREATE {fb_name}")
        counts["created"] += 1

    return counts


def verify_all(builders_dir: Path) -> bool:
    """Check all builders have exactly 12 ISOs (or more with extras -- ok)."""
    builder_dirs = sorted(builders_dir.glob("*-builder"))
    failures = []
    for bd in builder_dirs:
        if bd.name.startswith("_"):
            continue  # skip meta/template directories
        if not bd.is_dir():
            continue
        kind = _kind_from_dir(bd)
        missing = []
        for pat in EXPECTED_12_ISOS:
            fname = pat.replace("{kind}", kind)
            if not (bd / fname).exists():
                # Check hyphenated variant
                kind_hyphen = kind.replace("_", "-")
                fname_h = pat.replace("{kind}", kind_hyphen)
                if not (bd / fname_h).exists():
                    missing.append(fname)
        if missing:
            failures.append((bd.name, missing))

    if failures:
        print(f"\n[VERIFY] FAIL -- {len(failures)} builders missing ISOs:")
        for name, missing in failures[:20]:
            print(f"  {name}: missing {missing}")
        if len(failures) > 20:
            print(f"  ... and {len(failures) - 20} more")
        return False
    else:
        total = len(list(builders_dir.glob("*-builder")))
        print(f"\n[VERIFY] PASS -- all {total} builders have 12 ISOs")
        return True


def main():
    parser = argparse.ArgumentParser(description="CEX ISO 13->12 migration")
    parser.add_argument("--dry-run", action="store_true", help="Show changes without executing")
    parser.add_argument("--scope", type=str, default="", help="Migrate single builder dir path")
    parser.add_argument("--verify", action="store_true", help="Verify all builders have 12 ISOs")
    args = parser.parse_args()

    if args.verify:
        ok = verify_all(BUILDERS_DIR)
        sys.exit(0 if ok else 1)

    if args.scope:
        scope_path = Path(args.scope)
        if not scope_path.is_absolute():
            scope_path = ROOT / args.scope
        if not scope_path.is_dir():
            print(f"[ERR] Not a directory: {scope_path}")
            sys.exit(1)
        builder_dirs = [scope_path]
    else:
        builder_dirs = sorted(BUILDERS_DIR.glob("*-builder"))
        builder_dirs = [d for d in builder_dirs if d.is_dir() and not d.name.startswith("_")]

    mode = "[DRY RUN]" if args.dry_run else "[EXECUTE]"
    print(f"\nCEX ISO Migration {mode}")
    print(f"Scope: {len(builder_dirs)} builders\n")

    totals = {"renames": 0, "merges": 0, "created": 0, "skipped": 0, "errors": 0}

    for bd in builder_dirs:
        kind = _kind_from_dir(bd)
        print(f"\n[{kind}]")
        counts = migrate_builder(bd, dry_run=args.dry_run)
        for k, v in counts.items():
            totals[k] += v

    print(f"\n{'='*50}")
    print(f"SUMMARY ({mode}):")
    print(f"  Renames:  {totals['renames']}")
    print(f"  Merges:   {totals['merges']}")
    print(f"  Created:  {totals['created']}")
    print(f"  Skipped:  {totals['skipped']}")
    print(f"  Errors:   {totals['errors']}")
    print(f"{'='*50}\n")

    if totals["errors"] > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
