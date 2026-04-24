#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_8f_tagger.py -- Bulk-add 8f: fields to artifact frontmatter.

Reads a YAML mapping (kind -> 8F function) and inserts `8f:` into the
frontmatter of every matching .md artifact in N0*_*/P*_*/ directories.

Usage:
  python _tools/cex_8f_tagger.py                     # dry-run, full scan
  python _tools/cex_8f_tagger.py --apply              # write changes
  python _tools/cex_8f_tagger.py --apply --force      # overwrite existing 8f
  python _tools/cex_8f_tagger.py --scope N03_engineering/
  python _tools/cex_8f_tagger.py --stats              # summary only

Exit codes:
  0 = success (including dry-run)
  1 = errors encountered
"""

import argparse
import os
import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML required. pip install pyyaml", file=sys.stderr)
    sys.exit(1)

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

CEX_ROOT = Path(__file__).resolve().parent.parent
MAPPING_PATH = CEX_ROOT / ".cex" / "config" / "kind_8f_mapping.yaml"

# Regex for frontmatter delimiters
FM_OPEN = re.compile(r"^---\s*$")
FM_CLOSE = re.compile(r"^---\s*$")

# Regex for kind: field (handles quoted and unquoted values)
KIND_RE = re.compile(r"^(\s*kind\s*:\s*)([\"']?)(\S+?)\2\s*$")

# Regex for existing 8f: field
EF_RE = re.compile(r"^\s*8f\s*:")


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def load_mapping(path):
    """Load kind -> 8F function mapping from YAML file."""
    if not path.is_file():
        print(
            "[FAIL] Mapping file not found: %s" % path,
            file=sys.stderr,
        )
        sys.exit(1)
    with open(path, "r", encoding="utf-8") as fh:
        data = yaml.safe_load(fh)
    if not isinstance(data, dict):
        print(
            "[FAIL] Mapping file must be a YAML dict (kind: F{N}_{function})",
            file=sys.stderr,
        )
        sys.exit(1)
    return data


def discover_files(scope):
    """
    Yield .md files under N0*_*/P*_*/ directories, excluding compiled/ subdirs.

    If scope is given, only scan within that path (but still require the
    N0*_*/P*_*/ directory structure).
    """
    search_root = CEX_ROOT / scope if scope else CEX_ROOT

    if not search_root.is_dir():
        print(
            "[FAIL] Scope directory does not exist: %s" % search_root,
            file=sys.stderr,
        )
        sys.exit(1)

    # Walk the search root looking for .md files
    for md_file in sorted(search_root.rglob("*.md")):
        # Skip compiled/ directories
        parts = md_file.relative_to(CEX_ROOT).parts
        if "compiled" in parts:
            continue

        # Verify the file is under a N0*_*/P*_*/ structure
        # (could be nested deeper, that is fine)
        has_nucleus = False
        has_pillar = False
        for part in parts:
            if re.match(r"^N\d+_", part):
                has_nucleus = True
            if re.match(r"^P\d+_", part):
                has_pillar = True
        if has_nucleus and has_pillar:
            yield md_file


def parse_frontmatter(lines):
    """
    Find frontmatter boundaries in a list of lines.

    Returns (start, end, kind_line_idx, kind_value, existing_8f_idx)
    where start/end are line indices of the --- delimiters,
    kind_line_idx is the index of the kind: line,
    kind_value is the stripped kind value,
    existing_8f_idx is the index of an existing 8f: line or -1.

    Returns None if no valid frontmatter found.
    """
    if not lines:
        return None

    # First line must be ---
    if not FM_OPEN.match(lines[0]):
        return None

    # Find closing ---
    close_idx = -1
    for i in range(1, len(lines)):
        if FM_CLOSE.match(lines[i]):
            close_idx = i
            break

    if close_idx < 0:
        return None

    # Scan frontmatter for kind: and 8f:
    kind_idx = -1
    kind_value = None
    ef_idx = -1

    for i in range(1, close_idx):
        line = lines[i]
        km = KIND_RE.match(line)
        if km:
            kind_idx = i
            kind_value = km.group(3)
        if EF_RE.match(line):
            ef_idx = i

    return (0, close_idx, kind_idx, kind_value, ef_idx)


def process_file(md_file, mapping, apply, force):
    """
    Process a single .md file.

    Returns a status string: "tagged", "skipped", "warned", "error", or None.
    Also returns a message string for display.
    """
    rel_path = md_file.relative_to(CEX_ROOT)

    try:
        raw = md_file.read_text(encoding="utf-8")
    except Exception as exc:
        return "error", "[ERR]  %s (%s)" % (rel_path, exc)

    lines = raw.splitlines(keepends=True)
    result = parse_frontmatter(
        [line.rstrip("\n").rstrip("\r") for line in lines]
    )

    if result is None:
        # No frontmatter -- silently skip (not an artifact)
        return None, None

    fm_start, fm_end, kind_idx, kind_value, ef_idx = result

    if kind_idx < 0 or kind_value is None:
        # Frontmatter exists but no kind: field -- not a typed artifact
        return None, None

    # Look up kind in mapping
    if kind_value not in mapping:
        return "warned", "[WARN] %s (kind '%s' not in mapping)" % (
            rel_path,
            kind_value,
        )

    eight_f = mapping[kind_value]

    # Check for existing 8f: field
    if ef_idx >= 0:
        if not force:
            return "skipped", "[SKIP] %s (already has 8f:)" % rel_path
        # Force mode: replace existing 8f line
        old_line = lines[ef_idx]
        # Detect indentation from the existing line
        stripped = old_line.lstrip()
        indent = old_line[: len(old_line) - len(stripped)]
        # Preserve line ending
        line_end = ""
        if old_line.endswith("\r\n"):
            line_end = "\r\n"
        elif old_line.endswith("\n"):
            line_end = "\n"
        elif old_line.endswith("\r"):
            line_end = "\r"

        new_line = "%s8f: %s%s" % (indent, eight_f, line_end)

        if apply:
            lines[ef_idx] = new_line
            try:
                md_file.write_text("".join(lines), encoding="utf-8")
            except Exception as exc:
                return "error", "[ERR]  %s (write failed: %s)" % (
                    rel_path,
                    exc,
                )

        return "tagged", "[OK]   %s -> %s (forced)" % (rel_path, eight_f)

    # Insert 8f: on the line AFTER kind:
    kind_line = lines[kind_idx]
    # Detect line ending from kind line
    line_end = ""
    if kind_line.endswith("\r\n"):
        line_end = "\r\n"
    elif kind_line.endswith("\n"):
        line_end = "\n"
    elif kind_line.endswith("\r"):
        line_end = "\r"

    new_line = "8f: %s%s" % (eight_f, line_end)
    insert_pos = kind_idx + 1

    if apply:
        lines.insert(insert_pos, new_line)
        try:
            md_file.write_text("".join(lines), encoding="utf-8")
        except Exception as exc:
            return "error", "[ERR]  %s (write failed: %s)" % (
                rel_path,
                exc,
            )

    return "tagged", "[OK]   %s -> %s" % (rel_path, eight_f)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Bulk-add 8f: fields to artifact frontmatter.",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Write changes (default is dry-run).",
    )
    parser.add_argument(
        "--force",
        action="store_true",
        help="Overwrite existing 8f: fields.",
    )
    parser.add_argument(
        "--scope",
        type=str,
        default=None,
        help="Limit scan to a specific directory (relative to repo root).",
    )
    parser.add_argument(
        "--stats",
        action="store_true",
        help="Show summary statistics only, no per-file output.",
    )
    parser.add_argument(
        "--mapping",
        type=str,
        default=None,
        help="Path to kind->8F mapping YAML (default: .cex/config/kind_8f_mapping.yaml).",
    )
    args = parser.parse_args()

    # Resolve mapping path
    mapping_path = Path(args.mapping) if args.mapping else MAPPING_PATH
    if not mapping_path.is_absolute():
        mapping_path = CEX_ROOT / mapping_path

    mapping = load_mapping(mapping_path)

    mode = "Apply" if args.apply else "Dry-run"
    print("[8F TAGGER] %s mode%s" % (
        mode,
        " (use --apply to write)" if not args.apply else "",
    ))
    if args.force:
        print("[8F TAGGER] Force mode: will overwrite existing 8f: fields")
    print()

    counts = {"tagged": 0, "skipped": 0, "warned": 0, "error": 0}
    messages = []

    for md_file in discover_files(args.scope):
        status, msg = process_file(md_file, mapping, args.apply, args.force)
        if status is None:
            continue
        counts[status] += 1
        if msg:
            messages.append(msg)

    # Output
    if not args.stats:
        for msg in messages:
            print(msg)
        if messages:
            print()

    print("---")
    print("Tagged: %d | Skipped: %d | Warned: %d | Errors: %d" % (
        counts["tagged"],
        counts["skipped"],
        counts["warned"],
        counts["error"],
    ))

    if counts["error"] > 0:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
