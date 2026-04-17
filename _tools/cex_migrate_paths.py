#!/usr/bin/env python3
"""CEX Migrate Paths -- execute 96 git mv operations + update all refs.

Usage:
  python _tools/cex_migrate_paths.py --dry-run          # list ops, no changes
  python _tools/cex_migrate_paths.py --execute           # run all git mv
  python _tools/cex_migrate_paths.py --update-refs       # grep+sed pass on tools/boot/CLAUDE.md
  python _tools/cex_migrate_paths.py --update-handoffs   # update .cex/runtime/handoffs/
  python _tools/cex_migrate_paths.py --execute --update-refs --update-handoffs  # full run

Exit codes:
  0 = success
  1 = one or more errors
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

SEMANTIC_TO_PILLAR = {
    "knowledge":     "P01_knowledge",
    "agents":        "P02_model",
    "prompts":       "P03_prompt",
    "tools":         "P04_tools",
    "output":        "P05_output",
    "schemas":       "P06_schema",
    "quality":       "P07_evals",
    "architecture":  "P08_architecture",
    "config":        "P09_config",
    "memory":        "P10_memory",
    "feedback":      "P11_feedback",
    "orchestration": "P12_orchestration",
}

NUCLEUS_DIRS = [
    "N00_genesis",
    "N01_intelligence",
    "N02_marketing",
    "N03_engineering",
    "N04_knowledge",
    "N05_operations",
    "N06_commercial",
    "N07_admin",
]

# Files that get ref-update pass
REF_UPDATE_GLOBS = [
    "_tools/*.py",
    "boot/*.ps1",
    "boot/*.sh",
    "CLAUDE.md",
    ".claude/rules/*.md",
    ".claude/commands/*.md",
    ".cex/P09_config/*.yaml",
    ".cex/P09_config/*.yml",
]

HANDOFF_GLOB = ".cex/runtime/handoffs/*.md"


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _run_git_mv(src: Path, dst: Path, dry_run: bool) -> bool:
    """Run git mv and return True on success."""
    if not src.exists():
        return True  # already done or never existed, skip silently

    rel_src = src.relative_to(ROOT)
    rel_dst = dst.relative_to(ROOT)

    if dry_run:
        print(f"  [DRY] git mv {rel_src}  ->  {rel_dst}")
        return True

    result = subprocess.run(
        ["git", "mv", str(rel_src), str(rel_dst)],
        cwd=ROOT,
        capture_output=True,
        text=True,
    )
    if result.returncode != 0:
        print(f"  [FAIL] git mv {rel_src}: {result.stderr.strip()}")
        return False

    print(f"  [MV]   {rel_src}  ->  {rel_dst}")
    return True


def _replace_in_file(path: Path, old: str, new: str) -> bool:
    """Replace all occurrences of old -> new in file. Return True if changed."""
    try:
        original = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, PermissionError):
        return False

    updated = original.replace(old, new)
    if updated == original:
        return False

    path.write_text(updated, encoding="utf-8")
    return True


# ---------------------------------------------------------------------------
# Phase 1: git mv
# ---------------------------------------------------------------------------

def collect_mv_ops() -> list[tuple[Path, Path]]:
    """Return list of (src, dst) paths for all needed git mv operations."""
    ops = []
    for nucleus_name in NUCLEUS_DIRS:
        ndir = ROOT / nucleus_name
        if not ndir.is_dir():
            continue
        for semantic, canonical in SEMANTIC_TO_PILLAR.items():
            src = ndir / semantic
            dst = ndir / canonical
            if src.exists() and not dst.exists():
                ops.append((src, dst))
    return ops


def run_migration(dry_run: bool) -> int:
    """Execute (or preview) all git mv operations. Return error count."""
    ops = collect_mv_ops()

    if not ops:
        print("No rename operations needed -- already canonical or nothing found.")
        return 0

    print(f"{'[DRY RUN] ' if dry_run else ''}Running {len(ops)} git mv operations...\n")
    errors = 0
    for src, dst in ops:
        ok = _run_git_mv(src, dst, dry_run)
        if not ok:
            errors += 1

    label = "previewed" if dry_run else "completed"
    print(f"\n{len(ops)} operations {label}, {errors} errors.")
    return errors


# ---------------------------------------------------------------------------
# Phase 2: ref updates
# ---------------------------------------------------------------------------

def run_ref_updates(dry_run: bool) -> int:
    """Replace semantic subdir names with canonical names in all ref files."""
    files_updated = 0
    replacements = 0

    # Collect actual files from globs
    target_files: list[Path] = []
    for pattern in REF_UPDATE_GLOBS:
        target_files.extend(ROOT.glob(pattern))

    for fpath in sorted(set(target_files)):
        if not fpath.is_file():
            continue
        file_changed = False
        for semantic, canonical in SEMANTIC_TO_PILLAR.items():
            # Match path-like occurrences: /semantic/ or \semantic\ or /semantic\n
            # We use word-boundary-style patterns to avoid partial matches.
            # Match as a path segment: preceded by / or \ and followed by / \ . or end
            pattern = rf'((?<=[/\\]){re.escape(semantic)}(?=[/\\.\n])|(?<=[/\\]){re.escape(semantic)}$)'
            try:
                original = fpath.read_text(encoding="utf-8")
            except (UnicodeDecodeError, PermissionError):
                continue

            # Simple string replacement: /semantic/ -> /canonical/ and \semantic\ -> \canonical\
            changed = False
            new_content = original
            for sep in ["/", "\\"]:
                needle   = sep + semantic + sep
                replace  = sep + canonical + sep
                if needle in new_content:
                    new_content = new_content.replace(needle, replace)
                    changed = True
                # Also handle end-of-string segment (no trailing sep)
                needle2  = sep + semantic + "\n"
                replace2 = sep + canonical + "\n"
                if needle2 in new_content:
                    new_content = new_content.replace(needle2, replace2)
                    changed = True

            if changed:
                file_changed = True
                replacements += 1
                if not dry_run:
                    fpath.write_text(new_content, encoding="utf-8")
                    print(f"  [UPDATED] {fpath.relative_to(ROOT)}")
                else:
                    print(f"  [DRY-REFS] {fpath.relative_to(ROOT)}")

        if file_changed:
            files_updated += 1

    print(f"\nRef update: {files_updated} files, {replacements} replacements {'(dry run)' if dry_run else 'applied'}.")
    return 0


# ---------------------------------------------------------------------------
# Phase 3: handoff updates
# ---------------------------------------------------------------------------

def run_handoff_updates(dry_run: bool) -> int:
    """Update .cex/runtime/handoffs/*.md path references."""
    handoff_files = list(ROOT.glob(HANDOFF_GLOB))
    updated = 0

    for fpath in handoff_files:
        try:
            content = fpath.read_text(encoding="utf-8")
        except (UnicodeDecodeError, PermissionError):
            continue

        new_content = content
        changed = False
        for semantic, canonical in SEMANTIC_TO_PILLAR.items():
            for sep in ["/", "\\"]:
                needle  = sep + semantic + sep
                replace = sep + canonical + sep
                if needle in new_content:
                    new_content = new_content.replace(needle, replace)
                    changed = True
                needle2  = sep + semantic + "\n"
                replace2 = sep + canonical + "\n"
                if needle2 in new_content:
                    new_content = new_content.replace(needle2, replace2)
                    changed = True

        if changed:
            updated += 1
            if not dry_run:
                fpath.write_text(new_content, encoding="utf-8")
                print(f"  [UPDATED] {fpath.relative_to(ROOT)}")
            else:
                print(f"  [DRY-HANDOFF] {fpath.relative_to(ROOT)}")

    print(f"\nHandoff update: {updated} files {'(dry run)' if dry_run else 'applied'}.")
    return 0


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX path migrator -- executes git mv + updates all refs."
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="List all operations without executing"
    )
    parser.add_argument(
        "--execute", action="store_true",
        help="Run all git mv operations"
    )
    parser.add_argument(
        "--update-refs", action="store_true",
        help="Grep+replace pass on tools, boot scripts, CLAUDE.md"
    )
    parser.add_argument(
        "--update-handoffs", action="store_true",
        help="Update paths in .cex/runtime/handoffs/*.md"
    )
    args = parser.parse_args()

    if not any([args.dry_run, args.execute, args.update_refs, args.update_handoffs]):
        parser.print_help()
        sys.exit(0)

    errors = 0
    dry = args.dry_run and not args.execute

    if args.dry_run or args.execute:
        print("=== Phase 1: Directory Renames ===")
        errors += run_migration(dry_run=dry)

    if args.update_refs:
        print("\n=== Phase 2: Reference Updates ===")
        errors += run_ref_updates(dry_run=dry)

    if args.update_handoffs:
        print("\n=== Phase 3: Handoff Updates ===")
        errors += run_handoff_updates(dry_run=dry)

    if errors:
        print(f"\n[FAIL] {errors} error(s) encountered.")
        sys.exit(1)
    else:
        print("\n[OK] Migration complete.")
        sys.exit(0)


if __name__ == "__main__":
    main()
