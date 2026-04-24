#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
cex_8f_normalizer.py -- Normalize non-canonical llm_function values in builder ISOs.

Scans all .md files in archetypes/builders/ and normalizes non-canonical
llm_function: values in YAML frontmatter to their canonical 8F equivalents.

Canonical values:
  CONSTRAIN, BECOME, INJECT, REASON, CALL, PRODUCE, GOVERN, COLLABORATE

Non-canonical -> canonical mapping:
  CONTEXT     -> INJECT
  ORCHESTRATE -> COLLABORATE
  GENERATE    -> PRODUCE
  EXECUTE     -> CALL
  DEMONSTRATE -> PRODUCE
  TOOL        -> CALL
  EVALUATE    -> GOVERN
  ACT         -> CALL

Usage:
  python _tools/cex_8f_normalizer.py                # dry-run (default)
  python _tools/cex_8f_normalizer.py --dry-run      # explicit dry-run
  python _tools/cex_8f_normalizer.py --apply         # write changes
  python _tools/cex_8f_normalizer.py --stats         # summary counts only

Exit codes:
  0 = all canonical (nothing to do)
  1 = non-canonical found (dry-run) or unknown values detected
  2 = error (directory missing, etc.)
"""

import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
BUILDERS_DIR = ROOT / "archetypes" / "builders"

# ---- Canonical 8F values ----
CANONICAL = frozenset([
    "CONSTRAIN",
    "BECOME",
    "INJECT",
    "REASON",
    "CALL",
    "PRODUCE",
    "GOVERN",
    "COLLABORATE",
])

# ---- Non-canonical -> canonical mapping ----
NORMALIZE_MAP = {
    "CONTEXT": "INJECT",
    "ORCHESTRATE": "COLLABORATE",
    "GENERATE": "PRODUCE",
    "EXECUTE": "CALL",
    "DEMONSTRATE": "PRODUCE",
    "TOOL": "CALL",
    "EVALUATE": "GOVERN",
    "ACT": "CALL",
}

# ---- Regex patterns ----
# Match frontmatter block (first --- pair)
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---", re.DOTALL)

# Match llm_function line within frontmatter
LLM_FUNC_RE = re.compile(r"^(llm_function:\s*)(.+)$", re.MULTILINE)


def extract_frontmatter(text):
    """Return (frontmatter_str, start_offset, end_offset) or None."""
    m = FRONTMATTER_RE.search(text)
    if not m:
        return None
    # Offsets of the frontmatter content (between --- lines)
    return m.group(1), m.start(1), m.end(1)


def scan_file(filepath):
    """Scan a single file. Returns dict with status info.

    Possible statuses:
      'skip_no_fm'       - no frontmatter found
      'skip_no_llm'      - frontmatter has no llm_function
      'skip_template'    - llm_function is a {{template}} placeholder
      'canonical'        - value is already canonical
      'normalize'        - value needs normalization (includes old + new)
      'unknown'          - value is not canonical and not in normalize map
    """
    try:
        text = filepath.read_text(encoding="utf-8", errors="replace")
    except Exception as exc:
        return {"path": str(filepath), "status": "error", "detail": str(exc)}

    fm_result = extract_frontmatter(text)
    if fm_result is None:
        return {"path": str(filepath), "status": "skip_no_fm"}

    fm_text, _, _ = fm_result
    m = LLM_FUNC_RE.search(fm_text)
    if not m:
        return {"path": str(filepath), "status": "skip_no_llm"}

    value = m.group(2).strip()

    # Template placeholder -- skip
    if "{{" in value:
        return {"path": str(filepath), "status": "skip_template", "value": value}

    # Already canonical
    if value in CANONICAL:
        return {"path": str(filepath), "status": "canonical", "value": value}

    # Non-canonical with known mapping
    if value in NORMALIZE_MAP:
        return {
            "path": str(filepath),
            "status": "normalize",
            "old": value,
            "new": NORMALIZE_MAP[value],
        }

    # Unknown value
    return {"path": str(filepath), "status": "unknown", "value": value}


def apply_normalization(filepath, old_value, new_value):
    """Replace llm_function in frontmatter only. Returns True on success."""
    text = filepath.read_text(encoding="utf-8", errors="replace")

    fm_result = extract_frontmatter(text)
    if fm_result is None:
        return False

    fm_text, fm_start, fm_end = fm_result

    # Replace within frontmatter only
    def replacer(match):
        return match.group(1) + new_value

    new_fm = LLM_FUNC_RE.sub(replacer, fm_text, count=1)

    if new_fm == fm_text:
        return False

    new_text = text[:fm_start] + new_fm + text[fm_end:]
    filepath.write_text(new_text, encoding="utf-8", newline="\n")
    return True


def main():
    p = argparse.ArgumentParser(
        description="Normalize non-canonical llm_function values in builder ISOs."
    )
    mode = p.add_mutually_exclusive_group()
    mode.add_argument(
        "--dry-run",
        action="store_true",
        default=True,
        help="Show what would change (default)",
    )
    mode.add_argument(
        "--apply",
        action="store_true",
        help="Write changes to files",
    )
    mode.add_argument(
        "--stats",
        action="store_true",
        help="Summary counts only",
    )
    args = p.parse_args()

    # --apply flips dry-run off
    if args.apply:
        args.dry_run = False

    if not BUILDERS_DIR.exists():
        print("[FAIL] builders directory not found: %s" % BUILDERS_DIR, file=sys.stderr)
        return 2

    # Collect all .md files
    files = sorted(BUILDERS_DIR.rglob("*.md"))
    if not files:
        print("[WARN] no .md files found in %s" % BUILDERS_DIR)
        return 0

    # Scan
    results = [scan_file(f) for f in files]

    # Categorize
    canonical = [r for r in results if r["status"] == "canonical"]
    to_normalize = [r for r in results if r["status"] == "normalize"]
    unknown = [r for r in results if r["status"] == "unknown"]
    templates = [r for r in results if r["status"] == "skip_template"]
    no_fm = [r for r in results if r["status"] == "skip_no_fm"]
    no_llm = [r for r in results if r["status"] == "skip_no_llm"]
    errors = [r for r in results if r["status"] == "error"]

    # Stats mode -- just counts
    if args.stats:
        print("=== 8F Normalizer Stats ===")
        print("  files scanned:    %d" % len(results))
        print("  canonical:        %d" % len(canonical))
        print("  to normalize:     %d" % len(to_normalize))
        print("  unknown:          %d" % len(unknown))
        print("  template skip:    %d" % len(templates))
        print("  no frontmatter:   %d" % len(no_fm))
        print("  no llm_function:  %d" % len(no_llm))
        print("  errors:           %d" % len(errors))
        return 1 if (to_normalize or unknown) else 0

    # Dry-run or apply mode
    applied = 0
    if to_normalize:
        print("=== Files to normalize ===")
        for r in to_normalize:
            rel = Path(r["path"]).relative_to(ROOT)
            print("  %s -> %s  %s" % (r["old"], r["new"], rel))
            if args.apply:
                ok = apply_normalization(Path(r["path"]), r["old"], r["new"])
                if ok:
                    applied += 1
                else:
                    print("    [FAIL] could not apply")

    if unknown:
        print("=== Unknown values (manual review needed) ===")
        for r in unknown:
            rel = Path(r["path"]).relative_to(ROOT)
            print("  [WARN] %s  %s" % (r["value"], rel))

    # Summary
    print()
    print("=== Summary ===")
    print("  scanned:     %d" % len(results))
    print("  canonical:   %d" % len(canonical))
    print("  normalized:  %d" % (applied if args.apply else len(to_normalize)))
    print("  skipped:     %d" % (len(templates) + len(no_fm) + len(no_llm)))
    print("  warnings:    %d" % len(unknown))
    print("  errors:      %d" % len(errors))

    if args.apply and applied:
        print()
        print("[OK] Applied %d normalization(s)." % applied)

    if not to_normalize and not unknown:
        print()
        print("[OK] All llm_function values are canonical.")
        return 0

    if args.apply:
        return 1 if unknown else 0

    # Dry-run with pending normalizations
    return 1


if __name__ == "__main__":
    sys.exit(main())
