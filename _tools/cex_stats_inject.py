#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_stats_inject.py -- Dynamic stat counter for hardcoded references.

Computes real counts from repo sources of truth, finds stale hardcoded
numbers in .md / .html / .yaml files, and optionally fixes them.

Sources of truth:
  KIND_COUNT    = len(json.load('.cex/kinds_meta.json'))
  BUILDER_COUNT = count of .claude/agents/*-builder.md
  ISO_COUNT     = count of archetypes/builders/**/bld_*.md
  PILLAR_COUNT  = 12 (constant)
  NUCLEUS_COUNT = 8  (constant, N00-N07)
  TOOL_COUNT    = count of _tools/cex_*.py

Modes:
  --check           Report stale counts (exit 0=fresh, 1=stale)
  --fix             Auto-fix all stale numbers in-place
  --fix --dry-run   Show what would change without writing
  --inject          Replace {{KIND_COUNT}} etc. mustache vars (additive to --fix)

Scope:
  Only .md, .html, .yaml files. Never touches .py or .ps1.

Usage:
  python _tools/cex_stats_inject.py --check
  python _tools/cex_stats_inject.py --fix --dry-run
  python _tools/cex_stats_inject.py --fix
  python _tools/cex_stats_inject.py --fix --inject

Exit codes:
  0 = all counts fresh (--check) or fix succeeded
  1 = stale counts found (--check) or fix needed (--dry-run)
"""

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Tuple


# ---------------------------------------------------------------------------
# Repo root detection
# ---------------------------------------------------------------------------

def find_repo_root() -> Path:
    """Walk up from cwd or script dir until .git is found."""
    candidates = [Path.cwd(), Path(__file__).resolve().parent.parent]
    for start in candidates:
        p = start
        while p != p.parent:
            if (p / ".git").exists():
                return p
            p = p.parent
    print("[FAIL] Could not find repo root (.git directory)")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Stat computation (sources of truth)
# ---------------------------------------------------------------------------

def compute_stats(root: Path) -> Dict[str, int]:
    """Compute all live stats from the repo."""
    stats = {}

    # KIND_COUNT: keys in kinds_meta.json
    meta_path = root / ".cex" / "kinds_meta.json"
    if meta_path.exists():
        with open(meta_path, "r", encoding="utf-8") as f:
            data = json.load(f)
        stats["KIND_COUNT"] = len(data)
    else:
        print("[WARN] .cex/kinds_meta.json not found -- KIND_COUNT unavailable")
        stats["KIND_COUNT"] = 0

    # BUILDER_COUNT: .claude/agents/*-builder.md
    agents_dir = root / ".claude" / "agents"
    if agents_dir.exists():
        builders = list(agents_dir.glob("*-builder.md"))
        stats["BUILDER_COUNT"] = len(builders)
    else:
        print("[WARN] .claude/agents/ not found -- BUILDER_COUNT unavailable")
        stats["BUILDER_COUNT"] = 0

    # ISO_COUNT: archetypes/builders/**/bld_*.md
    iso_dir = root / "archetypes" / "builders"
    if iso_dir.exists():
        isos = list(iso_dir.rglob("bld_*.md"))
        stats["ISO_COUNT"] = len(isos)
    else:
        print("[WARN] archetypes/builders/ not found -- ISO_COUNT unavailable")
        stats["ISO_COUNT"] = 0

    # TOOL_COUNT: _tools/cex_*.py
    tools_dir = root / "_tools"
    if tools_dir.exists():
        tools = list(tools_dir.glob("cex_*.py"))
        stats["TOOL_COUNT"] = len(tools)
    else:
        print("[WARN] _tools/ not found -- TOOL_COUNT unavailable")
        stats["TOOL_COUNT"] = 0

    # Constants
    stats["PILLAR_COUNT"] = 12
    stats["NUCLEUS_COUNT"] = 8

    return stats


# ---------------------------------------------------------------------------
# Number formatting helpers
# ---------------------------------------------------------------------------

def fmt_comma(n: int) -> str:
    """Format with comma separator: 3647 -> '3,647'."""
    return "{:,}".format(n)


def fmt_plain(n: int) -> str:
    """Plain integer string: 3647 -> '3647'."""
    return str(n)


# ---------------------------------------------------------------------------
# Replacement pattern definitions
# ---------------------------------------------------------------------------

# Minimum thresholds: numbers below these are per-pillar / per-context
# counts (e.g. "P02 has 23 kinds"), NOT stale totals. Historical minimum
# totals: kinds ~98, builders ~98, ISOs ~2000, tools ~50.
MIN_KINDS = 90
MIN_BUILDERS = 90
MIN_ISOS = 500
MIN_TOOLS = 50


def _above_threshold(match_str: str, threshold: int) -> bool:
    """Check if matched number string is >= threshold."""
    cleaned = match_str.replace(",", "")
    try:
        return int(cleaned) >= threshold
    except ValueError:
        return False


def build_patterns(stats: Dict[str, int]) -> List[Tuple[str, re.Pattern, str]]:
    """Build (stat_name, compiled_regex, replacement_callable) tuples.

    Returns a list of tuples: (stat_name, pattern, replacement_fn).
    The pattern captures the full match; replacement_fn(match) returns the
    corrected string if the number is above threshold, else the original.
    """
    patterns = []
    kind_n = stats["KIND_COUNT"]
    builder_n = stats["BUILDER_COUNT"]
    iso_n = stats["ISO_COUNT"]
    tool_n = stats["TOOL_COUNT"]

    # --- KIND_COUNT ---
    # "NNN kinds" / "NNN typed kinds" / "NNN artifact kinds" / "NNN typed artifact kinds"
    patterns.append((
        "KIND_COUNT",
        re.compile(r"\b(\d{2,4})\s+((?:typed\s+)?(?:artifact\s+)?kinds)\b"),
        lambda m: (
            "%d %s" % (kind_n, m.group(2))
            if _above_threshold(m.group(1), MIN_KINDS)
            else m.group(0)
        ),
    ))
    # Badge: "kinds-NNN-" (shields.io badge URL)
    patterns.append((
        "KIND_COUNT",
        re.compile(r"(kinds-)\d{2,4}(-\w+)"),
        lambda m: "%s%d%s" % (m.group(1), kind_n, m.group(2)),
    ))
    # HTML stat-num for kinds
    patterns.append((
        "KIND_COUNT",
        re.compile(
            r'(<span class="stat-num">)\d{2,4}(</span>'
            r'<span class="stat-label">kinds)'
        ),
        lambda m: "%s%d%s" % (m.group(1), kind_n, m.group(2)),
    ))
    # Parenthetical "(NNN kinds)" -- only if above threshold
    patterns.append((
        "KIND_COUNT",
        re.compile(r"(\()\d{2,4}(\s+kinds\))"),
        lambda m: (
            "%s%d%s" % (m.group(1), kind_n, m.group(2))
            if _above_threshold(
                re.search(r"\d+", m.group(0)).group(), MIN_KINDS)
            else m.group(0)
        ),
    ))

    # --- BUILDER_COUNT ---
    # "NNN builders" / "NNN factories" -- only if above threshold
    patterns.append((
        "BUILDER_COUNT",
        re.compile(r"\b(\d{2,4})\s+(builders)\b"),
        lambda m: (
            "%d %s" % (builder_n, m.group(2))
            if _above_threshold(m.group(1), MIN_BUILDERS)
            else m.group(0)
        ),
    ))
    patterns.append((
        "BUILDER_COUNT",
        re.compile(r"\b(\d{2,4})\s+(factories)\b"),
        lambda m: (
            "%d %s" % (builder_n, m.group(2))
            if _above_threshold(m.group(1), MIN_BUILDERS)
            else m.group(0)
        ),
    ))
    # Badge: "builders-NNN-"
    patterns.append((
        "BUILDER_COUNT",
        re.compile(r"(builders-)\d{2,4}(-\w+)"),
        lambda m: "%s%d%s" % (m.group(1), builder_n, m.group(2)),
    ))
    # HTML stat-num for builders
    patterns.append((
        "BUILDER_COUNT",
        re.compile(
            r'(<span class="stat-num">)\d{2,4}(</span>'
            r'<span class="stat-label">builders)'
        ),
        lambda m: "%s%d%s" % (m.group(1), builder_n, m.group(2)),
    ))

    # --- ISO_COUNT ---
    # "N,NNN ISOs" (comma-formatted)
    patterns.append((
        "ISO_COUNT",
        re.compile(r"\b(\d{1,2},\d{3})\s+ISOs\b"),
        lambda m: (
            "%s ISOs" % fmt_comma(iso_n)
            if _above_threshold(m.group(1), MIN_ISOS)
            else m.group(0)
        ),
    ))
    # "NNNN ISOs" (plain)
    patterns.append((
        "ISO_COUNT",
        re.compile(r"\b(\d{4,5})\s+ISOs\b"),
        lambda m: (
            "%s ISOs" % fmt_plain(iso_n)
            if _above_threshold(m.group(1), MIN_ISOS)
            else m.group(0)
        ),
    ))
    # HTML stat-num for ISOs
    patterns.append((
        "ISO_COUNT",
        re.compile(
            r'(<span class="stat-num">)[\d,]{4,6}(</span>'
            r'<span class="stat-label">ISOs)'
        ),
        lambda m: "%s%s%s" % (m.group(1), fmt_comma(iso_n), m.group(2)),
    ))
    # "NNN factories x 12 ISOs each = N,NNN artifact constructors"
    patterns.append((
        "ISO_COUNT",
        re.compile(
            r"(\d{2,4} factories x 12 ISOs each = )(\d{1,2},\d{3})"
            r"(\s+artifact constructors)"
        ),
        lambda m: "%s%s%s" % (m.group(1), fmt_comma(iso_n), m.group(3)),
    ))

    # --- TOOL_COUNT ---
    # "NNN tools" -- only if above threshold
    patterns.append((
        "TOOL_COUNT",
        re.compile(r"\b(\d{2,4})\s+tools\b"),
        lambda m: (
            "%d tools" % tool_n
            if _above_threshold(m.group(1), MIN_TOOLS)
            else m.group(0)
        ),
    ))

    return patterns


# ---------------------------------------------------------------------------
# Mustache injection patterns
# ---------------------------------------------------------------------------

def build_mustache_patterns(stats: Dict[str, int]) -> List[Tuple[str, re.Pattern, str]]:
    """Build patterns for {{STAT_NAME}} mustache replacement."""
    patterns = []
    for name, value in stats.items():
        pat = re.compile(r"\{\{" + name + r"\}\}")
        replacement = fmt_comma(value) if value >= 1000 else str(value)
        patterns.append((name, pat, lambda m, v=replacement: v))
    return patterns


# ---------------------------------------------------------------------------
# File collection
# ---------------------------------------------------------------------------

SCAN_EXTENSIONS = {".md", ".html", ".yaml", ".yml"}

# Directories to skip
SKIP_DIRS = {
    ".git", "__pycache__", "node_modules", ".obsidian",
    "compiled", ".venv", "venv",
}


def collect_files(root: Path) -> List[Path]:
    """Collect .md, .html, .yaml files from repo root."""
    files = []
    for dirpath, dirnames, filenames in os.walk(root):
        # Prune skipped directories
        dirnames[:] = [
            d for d in dirnames
            if d not in SKIP_DIRS and not d.startswith(".")
        ]
        for fn in sorted(filenames):
            fp = Path(dirpath) / fn
            if fp.suffix.lower() in SCAN_EXTENSIONS:
                files.append(fp)
    return sorted(files)


# ---------------------------------------------------------------------------
# Check mode
# ---------------------------------------------------------------------------

def run_check(
    root: Path,
    stats: Dict[str, int],
    verbose: bool = False,
) -> int:
    """Report stale counts. Returns total mismatch count."""
    files = collect_files(root)
    patterns = build_patterns(stats)

    total_stale = 0
    files_with_stale = 0
    stale_details = []  # (file, line_num, stat, old_val, new_val)

    for fp in files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                content = f.read()
        except (UnicodeDecodeError, OSError):
            continue

        file_stale = 0
        lines = content.split("\n")
        for line_num, line in enumerate(lines, 1):
            for stat_name, pat, repl_fn in patterns:
                for m in pat.finditer(line):
                    new_text = repl_fn(m)
                    if new_text != m.group(0):
                        file_stale += 1
                        stale_details.append((
                            fp, line_num, stat_name,
                            m.group(0), new_text,
                        ))

        if file_stale > 0:
            files_with_stale += 1
            total_stale += file_stale

    # Print report
    if stale_details:
        print("Stale references found:\n")
        for fp, ln, stat, old, new in stale_details:
            try:
                rel = fp.relative_to(root)
            except ValueError:
                rel = fp
            print("  [STALE] %s:%d  %s" % (rel, ln, stat))
            print("          old: %s" % old)
            print("          new: %s" % new)
            print()

    print("=" * 60)
    print("  Live stats:")
    for k, v in sorted(stats.items()):
        formatted = fmt_comma(v) if v >= 1000 else str(v)
        print("    %-16s = %s" % (k, formatted))
    print()
    print("  Files scanned:  %d" % len(files))
    print("  Files stale:    %d" % files_with_stale)
    print("  Total stale:    %d references" % total_stale)
    if total_stale == 0:
        print("  Status:         [OK] All counts are fresh")
    else:
        print("  Status:         [FAIL] %d stale references" % total_stale)
    print("=" * 60)

    return total_stale


# ---------------------------------------------------------------------------
# Fix mode
# ---------------------------------------------------------------------------

def run_fix(
    root: Path,
    stats: Dict[str, int],
    dry_run: bool = False,
    inject: bool = False,
    verbose: bool = False,
) -> int:
    """Fix stale counts in-place. Returns total fixes applied."""
    files = collect_files(root)
    patterns = build_patterns(stats)
    if inject:
        patterns.extend(build_mustache_patterns(stats))

    total_fixes = 0
    files_fixed = 0

    for fp in files:
        try:
            with open(fp, "r", encoding="utf-8") as f:
                original = f.read()
        except (UnicodeDecodeError, OSError):
            continue

        content = original
        file_fixes = 0

        # Apply each pattern. Process line-by-line to count changes
        # but apply to full content for correctness.
        for stat_name, pat, repl_fn in patterns:
            new_content = pat.sub(repl_fn, content)
            if new_content != content:
                # Count how many substitutions happened
                old_matches = list(pat.finditer(content))
                for m in old_matches:
                    replacement = repl_fn(m)
                    if replacement != m.group(0):
                        file_fixes += 1
                content = new_content

        if file_fixes > 0:
            files_fixed += 1
            total_fixes += file_fixes
            try:
                rel = fp.relative_to(root)
            except ValueError:
                rel = fp
            tag = "WOULD FIX" if dry_run else "FIXED"
            print("[%s] %s (%d replacements)" % (tag, rel, file_fixes))

            if not dry_run:
                with open(fp, "w", encoding="utf-8", newline="") as f:
                    f.write(content)

    print()
    print("=" * 60)
    tag = "DRY RUN" if dry_run else "FIX"
    print("  Mode:           %s%s" % (
        tag, " + INJECT" if inject else ""))
    print("  Files scanned:  %d" % len(files))
    print("  Files changed:  %d" % files_fixed)
    print("  Total fixes:    %d replacements" % total_fixes)
    if total_fixes == 0:
        print("  Status:         [OK] Nothing to fix")
    else:
        status_tag = "WOULD APPLY" if dry_run else "APPLIED"
        print("  Status:         [%s] %d fixes" % (status_tag, total_fixes))
    print("=" * 60)

    return total_fixes


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX stats injector -- fix hardcoded count references"
    )
    parser.add_argument(
        "--check", action="store_true",
        help="Report stale counts (exit 1 if any mismatch)")
    parser.add_argument(
        "--fix", action="store_true",
        help="Auto-fix all stale numbers in .md/.html/.yaml files")
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Show what --fix would change without writing files")
    parser.add_argument(
        "--inject", action="store_true",
        help="Also replace {{KIND_COUNT}} etc. mustache variables")
    parser.add_argument(
        "--verbose", "-v", action="store_true",
        help="Show per-file details")

    args = parser.parse_args()

    if not args.check and not args.fix:
        print("ERROR: specify --check or --fix")
        parser.print_help()
        sys.exit(1)

    root = find_repo_root()
    stats = compute_stats(root)

    print("cex_stats_inject -- repo: %s" % root)
    print()

    if args.check:
        stale = run_check(root, stats, verbose=args.verbose)
        sys.exit(1 if stale > 0 else 0)
    elif args.fix:
        fixes = run_fix(
            root, stats,
            dry_run=args.dry_run,
            inject=args.inject,
            verbose=args.verbose,
        )
        if args.dry_run:
            sys.exit(1 if fixes > 0 else 0)
        else:
            # Verify after fix
            print()
            remaining = run_check(root, stats, verbose=False)
            if remaining > 0:
                print("\n[WARN] %d stale references remain after fix" % remaining)
                sys.exit(1)
            else:
                print("\n[OK] All counts are fresh after fix")
                sys.exit(0)


if __name__ == "__main__":
    main()
