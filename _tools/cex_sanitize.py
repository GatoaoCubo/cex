#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_sanitize.py -- Universal non-ASCII sanitizer for CEX executable code.

Scans .py, .ps1, .sh, .cmd files for non-ASCII characters and replaces them
with ASCII equivalents. Designed to prevent UnicodeEncodeError on Windows
terminals that default to cp1252.

Modes:
  --check   Report-only (exit 0=clean, 1=issues found)
  --fix     Replace all non-ASCII with ASCII equivalents
  --scope   Directory to scan (default: _tools/)

Usage:
  python _tools/cex_sanitize.py --check --scope _tools/
  python _tools/cex_sanitize.py --fix --scope _tools/
  python _tools/cex_sanitize.py --check --scope .          # full repo
  python _tools/cex_sanitize.py --fix --scope _tools/ --dry-run

Exit codes:
  0 = clean (no non-ASCII found or all fixed)
  1 = issues found (--check) or fix failed
"""

import os
import sys
import argparse
from pathlib import Path
from typing import Union

# ---------------------------------------------------------------------------
# Replacement maps -- MUST be 100% ASCII in this source file
# ---------------------------------------------------------------------------

# Box drawing -> ASCII art
BOX_MAP = {
    0x2500: "-",   # light horizontal
    0x2501: "-",   # heavy horizontal
    0x2502: "|",   # light vertical
    0x2503: "|",   # heavy vertical
    0x250C: "+",   # light down-right
    0x250F: "+",   # heavy down-right
    0x2510: "+",   # light down-left
    0x2513: "+",   # heavy down-left
    0x2514: "+",   # light up-right
    0x2517: "+",   # heavy up-right
    0x2518: "+",   # light up-left
    0x251B: "+",   # heavy up-left
    0x251C: "+",   # light vertical-right
    0x2523: "+",   # heavy vertical-right
    0x2524: "+",   # light vertical-left
    0x252B: "+",   # heavy vertical-left
    0x252C: "+",   # light down-horizontal
    0x2533: "+",   # heavy down-horizontal
    0x2534: "+",   # light up-horizontal
    0x253B: "+",   # heavy up-horizontal
    0x253C: "+",   # light cross
    0x254B: "+",   # heavy cross
    0x2550: "=",   # double horizontal
    0x2551: "|",   # double vertical
    0x2552: "+",   # down-single-right-double
    0x2553: "+",   # down-double-right-single
    0x2554: "+",   # double down-right
    0x2555: "+",   # down-single-left-double
    0x2556: "+",   # down-double-left-single
    0x2557: "+",   # double down-left
    0x2558: "+",   # up-single-right-double
    0x2559: "+",   # up-double-right-single
    0x255A: "+",   # double up-right
    0x255B: "+",   # up-single-left-double
    0x255C: "+",   # up-double-left-single
    0x255D: "+",   # double up-left
    0x255E: "+",   # vertical-single-right-double
    0x255F: "+",   # vertical-double-right-single
    0x2560: "+",   # double vertical-right
    0x2561: "+",   # vertical-single-left-double
    0x2562: "+",   # vertical-double-left-single
    0x2563: "+",   # double vertical-left
    0x2564: "+",   # down-single-horizontal-double
    0x2565: "+",   # down-double-horizontal-single
    0x2566: "+",   # double down-horizontal
    0x2567: "+",   # up-single-horizontal-double
    0x2568: "+",   # up-double-horizontal-single
    0x2569: "+",   # double up-horizontal
    0x256A: "+",   # vertical-single-horizontal-double
    0x256B: "+",   # vertical-double-horizontal-single
    0x256C: "+",   # double cross
}

# Dashes and quotes
DASH_MAP = {
    0x2014: "--",  # em-dash
    0x2013: "-",   # en-dash
    0x2012: "-",   # figure dash
    0x2015: "--",  # horizontal bar
    0x201C: '"',   # left double quote
    0x201D: '"',   # right double quote
    0x2018: "'",   # left single quote
    0x2019: "'",   # right single quote
    0x00AB: '"',   # left guillemet
    0x00BB: '"',   # right guillemet
}

# Arrows
ARROW_MAP = {
    0x2192: "->",  # right arrow
    0x2190: "<-",  # left arrow
    0x2191: "^",   # up arrow
    0x2193: "v",   # down arrow
    0x21A9: "<-",  # left hook arrow
    0x21D2: "=>",  # double right arrow
    0x21D0: "<=",  # double left arrow
    0x23ED: ">>",  # next track
}

# Emoji -> ASCII tags
EMOJI_MAP = {
    0x2705: "[OK]",      # check mark
    0x274C: "[FAIL]",    # cross mark
    0x2717: "[X]",       # ballot X
    0x2714: "[OK]",      # heavy check
    0x26A0: "[WARN]",    # warning
    0x1F4CB: "[>>]",     # clipboard
    0x1F680: "[>>]",     # rocket
    0x1F50D: "[?]",      # magnifying glass
    0x1F4E6: "[>>]",     # package
    0x1F3AF: "[>>]",     # target
    0x1F4E1: "[>>]",     # agent_group
    0x1F534: "[!!]",     # red circle
    0x1F7E0: "[!!]",     # orange circle
    0x1F7E1: "[..]",     # yellow circle
    0x1F7E2: "[OK]",     # green circle
    0x26AA: "[--]",      # white circle
    0x1F4B0: "[$]",      # money bag
    0x26A1: "[!]",       # lightning
    0x2728: "[*]",       # sparkles
    0x1F4A1: "[i]",      # light bulb
    0x1F527: "[>>]",     # wrench
    0x1F6E0: "[>>]",     # hammer and wrench
    0x1F4DD: "[>>]",     # memo
    0x1F4CA: "[>>]",     # chart
    0x1F9EA: "[>>]",     # test tube
    0x2B50: "[*]",       # star
    0xFE0F: "",          # variation selector (strip)
}

# Accented -> ASCII (PT-BR and common)
ACCENT_MAP = {
    0x00E3: "a",   # a-tilde
    0x00E1: "a",   # a-acute
    0x00E0: "a",   # a-grave
    0x00E2: "a",   # a-circumflex
    0x00C3: "A",   # A-tilde
    0x00C1: "A",   # A-acute
    0x00C0: "A",   # A-grave
    0x00C2: "A",   # A-circumflex
    0x00E7: "c",   # c-cedilla
    0x00C7: "C",   # C-cedilla
    0x00E9: "e",   # e-acute
    0x00EA: "e",   # e-circumflex
    0x00C9: "E",   # E-acute
    0x00CA: "E",   # E-circumflex
    0x00ED: "i",   # i-acute
    0x00CD: "I",   # I-acute
    0x00F3: "o",   # o-acute
    0x00F4: "o",   # o-circumflex
    0x00F5: "o",   # o-tilde
    0x00D3: "O",   # O-acute
    0x00D4: "O",   # O-circumflex
    0x00D5: "O",   # O-tilde
    0x00FA: "u",   # u-acute
    0x00FC: "u",   # u-umlaut
    0x00DA: "U",   # U-acute
    0x00DC: "U",   # U-umlaut
    0x00F1: "n",   # n-tilde
    0x00D1: "N",   # N-tilde
}

# Math/symbols
SYMBOL_MAP = {
    0x00D7: "x",       # multiplication sign
    0x00F7: "/",       # division sign
    0x0394: "delta",   # greek delta
    0x03B1: "alpha",   # greek alpha
    0x03B2: "beta",    # greek beta
    0x03B3: "gamma",   # greek gamma
    0x2022: "*",       # bullet
    0x00B7: "*",       # middle dot
    0x2026: "...",     # ellipsis
    0x00A0: " ",       # non-breaking space
    0x200B: "",        # zero-width space
    0x200E: "",        # left-to-right mark
    0x200F: "",        # right-to-left mark
    0xFEFF: "",        # BOM / zero-width no-break space
}


def build_full_map() -> dict[int, str]:
    """Merge all maps into one lookup dict keyed by codepoint."""
    full = {}
    for m in [BOX_MAP, DASH_MAP, ARROW_MAP, EMOJI_MAP, ACCENT_MAP, SYMBOL_MAP]:
        full.update(m)
    return full


FULL_MAP = build_full_map()

# File extensions to scan
SCAN_EXTENSIONS = {".py", ".ps1", ".sh", ".cmd", ".bat"}


def sanitize_char(ch: str) -> str:
    """Replace a single non-ASCII character with its ASCII equivalent."""
    cp = ord(ch)
    if cp < 128:
        return ch
    replacement = FULL_MAP.get(cp)
    if replacement is not None:
        return replacement
    # Fallback: unicode escape for unknown chars
    if cp <= 0xFFFF:
        return "\\u%04x" % cp
    return "\\U%08x" % cp


def sanitize_text(text: str) -> str:
    """Replace all non-ASCII characters in text with ASCII equivalents."""
    result = []
    for ch in text:
        result.append(sanitize_char(ch))
    return "".join(result)


def has_non_ascii(text: str) -> bool:
    """Check if text contains any non-ASCII characters (except BOM at pos 0)."""
    for i, ch in enumerate(text):
        cp = ord(ch)
        if cp > 127:
            # Allow BOM at position 0 for .ps1 files (handled separately)
            return True
    return False


def scan_file(filepath: str, allow_bom: bool = False) -> list[tuple[int, int, str, int, str]]:
    """Scan a single file for non-ASCII characters.

    Returns list of (line_num, col, char, codepoint, replacement) tuples.
    """
    issues = []
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (UnicodeDecodeError, OSError) as e:
        return [(-1, 0, "", 0, "READ ERROR: %s" % str(e))]

    for line_num, line in enumerate(content.split("\n"), 1):
        for col, ch in enumerate(line):
            cp = ord(ch)
            if cp <= 127:
                continue
            # Allow BOM at very start of .ps1 files
            if allow_bom and cp == 0xFEFF and line_num == 1 and col == 0:
                continue
            replacement = sanitize_char(ch)
            issues.append((line_num, col + 1, ch, cp, replacement))
    return issues


def fix_file(filepath: str, dry_run: bool = False, allow_bom: bool = False) -> tuple[int, int, str]:
    """Fix all non-ASCII characters in a file.

    Returns (original_count, fixed_count, new_content).
    """
    try:
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
    except (UnicodeDecodeError, OSError) as e:
        return (-1, 0, "READ ERROR: %s" % str(e))

    original_count = 0
    chars = list(content)
    for i, ch in enumerate(chars):
        cp = ord(ch)
        if cp <= 127:
            continue
        # Preserve BOM at position 0 for .ps1 files
        if allow_bom and cp == 0xFEFF and i == 0:
            continue
        original_count += 1

    if original_count == 0:
        return (0, 0, content)

    # Build new content preserving BOM if needed
    new_chars = []
    fixed = 0
    for i, ch in enumerate(content):
        cp = ord(ch)
        if cp <= 127:
            new_chars.append(ch)
            continue
        if allow_bom and cp == 0xFEFF and i == 0:
            new_chars.append(ch)
            continue
        replacement = sanitize_char(ch)
        new_chars.append(replacement)
        fixed += 1

    new_content = "".join(new_chars)

    if not dry_run:
        with open(filepath, "w", encoding="utf-8", newline="") as f:
            f.write(new_content)

    return (original_count, fixed, new_content)


def collect_files(
    scope_path: Union[str, Path],
    extensions: set[str] | None = None,
) -> list[Path]:
    """Collect all scannable files under scope_path."""
    if extensions is None:
        extensions = SCAN_EXTENSIONS
    scope = Path(scope_path)
    if not scope.exists():
        print("ERROR: scope path does not exist: %s" % scope_path)
        return []

    files = []
    if scope.is_file():
        if scope.suffix in extensions:
            files.append(scope)
    else:
        for root, dirs, filenames in os.walk(scope):
            # Skip hidden dirs, __pycache__, .git, node_modules
            dirs[:] = [d for d in dirs if not d.startswith(".")
                       and d != "__pycache__" and d != "node_modules"
                       and d != ".git"]
            for fn in sorted(filenames):
                fp = Path(root) / fn
                if fp.suffix in extensions:
                    files.append(fp)
    return sorted(files)


def run_check(
    scope: Union[str, Path],
    extensions: set[str] | None = None,
    verbose: bool = False,
) -> int:
    """Check mode: report non-ASCII issues. Returns total issue count."""
    files = collect_files(scope, extensions)
    if not files:
        print("No files found in scope: %s" % scope)
        return 0

    total_issues = 0
    files_with_issues = 0

    for fp in files:
        allow_bom = fp.suffix == ".ps1"
        issues = scan_file(str(fp), allow_bom=allow_bom)
        if issues:
            files_with_issues += 1
            total_issues += len(issues)
            rel = fp
            try:
                rel = fp.relative_to(Path.cwd())
            except ValueError:
                pass
            print("[FAIL] %s (%d non-ASCII chars)" % (rel, len(issues)))
            if verbose:
                for ln, col, ch, cp, repl in issues[:10]:
                    if ln == -1:
                        print("  ERROR: %s" % repl)
                    else:
                        print("  L%d:C%d U+%04X -> %s" % (ln, col, cp, repr(repl)))
                if len(issues) > 10:
                    print("  ... and %d more" % (len(issues) - 10))
        else:
            if verbose:
                rel = fp
                try:
                    rel = fp.relative_to(Path.cwd())
                except ValueError:
                    pass
                print("[OK]   %s" % rel)

    print("")
    print("=" * 60)
    print("  Scanned: %d files" % len(files))
    print("  Clean:   %d" % (len(files) - files_with_issues))
    print("  Dirty:   %d" % files_with_issues)
    print("  Issues:  %d non-ASCII chars" % total_issues)
    print("=" * 60)

    return total_issues


def run_fix(
    scope: Union[str, Path],
    dry_run: bool = False,
    extensions: set[str] | None = None,
    verbose: bool = False,
) -> int:
    """Fix mode: replace non-ASCII chars. Returns total fixed count."""
    files = collect_files(scope, extensions)
    if not files:
        print("No files found in scope: %s" % scope)
        return 0

    total_fixed = 0
    files_fixed = 0

    for fp in files:
        allow_bom = fp.suffix == ".ps1"
        original, fixed, result = fix_file(str(fp), dry_run=dry_run,
                                           allow_bom=allow_bom)
        if original == -1:
            print("[ERROR] %s: %s" % (fp, result))
            continue
        if fixed > 0:
            files_fixed += 1
            total_fixed += fixed
            rel = fp
            try:
                rel = fp.relative_to(Path.cwd())
            except ValueError:
                pass
            tag = "WOULD FIX" if dry_run else "FIXED"
            print("[%s] %s (%d chars)" % (tag, rel, fixed))
        elif verbose:
            rel = fp
            try:
                rel = fp.relative_to(Path.cwd())
            except ValueError:
                pass
            print("[CLEAN] %s" % rel)

    print("")
    print("=" * 60)
    tag = "DRY RUN" if dry_run else "FIX"
    print("  Mode:    %s" % tag)
    print("  Scanned: %d files" % len(files))
    print("  Fixed:   %d files (%d chars)" % (files_fixed, total_fixed))
    print("=" * 60)

    return total_fixed


def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX non-ASCII sanitizer for executable code"
    )
    parser.add_argument("--check", action="store_true",
                        help="Report-only mode (exit 1 if issues found)")
    parser.add_argument("--fix", action="store_true",
                        help="Replace non-ASCII with ASCII equivalents")
    parser.add_argument("--scope", default="_tools/",
                        help="Directory or file to scan (default: _tools/)")
    parser.add_argument("--dry-run", action="store_true",
                        help="Show what would be fixed without writing")
    parser.add_argument("--verbose", "-v", action="store_true",
                        help="Show per-file details")
    parser.add_argument("--extensions", default=None,
                        help="Comma-separated extensions (default: .py,.ps1,.sh,.cmd,.bat)")

    args = parser.parse_args()

    if not args.check and not args.fix:
        print("ERROR: specify --check or --fix")
        parser.print_help()
        sys.exit(1)

    extensions = None
    if args.extensions:
        extensions = set("." + e.strip(".") for e in args.extensions.split(","))

    if args.check:
        issues = run_check(args.scope, extensions=extensions, verbose=args.verbose)
        sys.exit(1 if issues > 0 else 0)
    elif args.fix:
        fixed = run_fix(args.scope, dry_run=args.dry_run, extensions=extensions,
                        verbose=args.verbose)
        if args.dry_run:
            sys.exit(1 if fixed > 0 else 0)
        else:
            # Verify after fix
            remaining = run_check(args.scope, extensions=extensions, verbose=False)
            if remaining > 0:
                print("\n[WARN] %d non-ASCII chars remain after fix" % remaining)
                sys.exit(1)
            else:
                print("\n[OK] All clean after fix")
                sys.exit(0)


if __name__ == "__main__":
    main()
