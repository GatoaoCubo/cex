#!/usr/bin/env python3
"""CEX Naming Validator -- enforce pxx_kind_descriptor_nxx naming convention.

New convention: p{nn}_{kind}_{descriptor}_{nxx}.{ext}
  pnn  = pillar code (p01-p12)
  kind = kind name snake_case (e.g. knowledge_card, agent, env_config)
  desc = short contextual descriptor (snake_case)
  nxx  = nucleus code (n00-n07)
  ext  = .md (docs) or .yaml (configs)

Usage:
  python _tools/cex_naming_validator.py --check               # all nuclei
  python _tools/cex_naming_validator.py --check N01_intelligence/
  python _tools/cex_naming_validator.py --check --summary     # counts only
  python _tools/cex_naming_validator.py --fix N01_intelligence/
  python _tools/cex_naming_validator.py --fix N01_intelligence/ --confirm

Exit codes:
  0 = all [OK] or only skipped
  1 = [WARN] or [FAIL] found
"""

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

NUCLEUS_DIRS = [
    "N01_intelligence",
    "N02_marketing",
    "N03_engineering",
    "N04_knowledge",
    "N05_operations",
    "N06_commercial",
    "N07_admin",
]

# Dirs to skip when scanning for naming violations
SKIP_DIRS = frozenset({
    "rules", "compiled", "boot", "crews", "reports",
    "atlas", "library", "kind",  # nested content dirs -- have own conventions
})

# Filenames to always skip
SKIP_FILENAMES = frozenset({
    "README.md", "_schema.yaml", "kind_index.md", ".gitkeep",
})

# Legacy prefix patterns (flag as WARN)
LEGACY_PREFIXES = (
    "kc_", "sch_", "age_", "con_", "mem_", "pro_",
    "bld_", "tpl_", "ex_", "atom_",
)

# Canonical: p{nn}_{body}_n{nn}.{ext}
# body must have at least two underscore-separated segments (kind + descriptor)
# We check for p-prefix, _n{nn} suffix, and non-empty body in between.
CANONICAL_RE = re.compile(
    r'^p\d{2}_[a-z][a-z0-9_]+_[a-z][a-z0-9_]*_n\d{2}\.(md|yaml)$'
)

# Partial: has pillar prefix but no nucleus suffix
PARTIAL_PILLAR_RE = re.compile(r'^p\d{2}_[a-z][a-z0-9_.]+\.(md|yaml)$')

# Has nucleus suffix but no pillar prefix
PARTIAL_NUCLEUS_RE = re.compile(r'^[a-z][a-z0-9_]*_n\d{2}\.(md|yaml)$')


def _classify(filename: str) -> tuple:
    """Return (status, reason) for a single filename.

    status: 'OK' | 'WARN' | 'FAIL' | 'SKIP'
    reason: human-readable explanation (empty if OK/SKIP)
    """
    name = filename.lower()
    stem = name.rsplit('.', 1)[0] if '.' in name else name

    # kind_manifest_n00.md and similar N00 archetype files
    if name.startswith("kind_manifest_") or name.startswith("kind_manifest"):
        return "SKIP", "N00 archetype file"

    if name in SKIP_FILENAMES:
        return "SKIP", "explicitly skipped"

    if CANONICAL_RE.match(name):
        return "OK", ""

    # Check legacy prefixes
    for prefix in LEGACY_PREFIXES:
        if name.startswith(prefix):
            # Build suggested canonical suggestion
            clean = stem[len(prefix):]
            # Strip trailing _nxx if present
            clean = re.sub(r'_n\d{2}$', '', clean)
            return "WARN", f"legacy prefix '{prefix}' -- migrate to p{{nn}}_{clean}_n{{nn}}.ext"

    # Has pillar prefix but no/wrong nucleus suffix
    if PARTIAL_PILLAR_RE.match(name):
        return "WARN", "pillar prefix present but nucleus suffix _n{nn} missing"

    # Has nucleus suffix but no pillar prefix
    if PARTIAL_NUCLEUS_RE.match(name):
        return "WARN", "nucleus suffix _n{nn} present but pillar prefix p{nn}_ missing"

    # Has p-prefix but doesn't fully match
    if re.match(r'^p\d{2}_', name):
        return "WARN", "pillar prefix present but pattern incomplete (need kind + descriptor + _n{nn})"

    # No recognizable structure
    return "FAIL", "no pillar prefix -- expected p{nn}_{kind}_{descriptor}_n{nn}.ext"


def _should_skip_path(f: Path, scan_root: Path) -> bool:
    """True if this file path should be excluded from validation."""
    if f.name.lower() in SKIP_FILENAMES:
        return True
    if f.name.lower().startswith("kind_manifest_"):
        return True

    try:
        rel_parts = f.relative_to(scan_root).parts
    except ValueError:
        rel_parts = f.parts

    # Skip if any parent directory component is in SKIP_DIRS
    for part in rel_parts[:-1]:  # exclude the filename itself
        if part in SKIP_DIRS:
            return True

    return False


def _scan_path(scan_root: Path, quiet: bool = False) -> list:
    """Scan scan_root recursively, return list of result dicts."""
    results = []

    # Collect both .md and .yaml files
    candidates = sorted(
        list(scan_root.rglob("*.md")) + list(scan_root.rglob("*.yaml"))
    )

    for f in candidates:
        if not f.is_file():
            continue

        if _should_skip_path(f, scan_root):
            continue

        status, reason = _classify(f.name)

        if status == "SKIP":
            continue

        try:
            rel = str(f.relative_to(ROOT))
        except ValueError:
            rel = str(f)

        results.append({
            "path": f,
            "rel": rel,
            "status": status,
            "reason": reason,
        })

        if not quiet:
            tag = f"[{status}]"
            if status == "OK":
                print(f"  {tag:<8} {rel}")
            else:
                print(f"  {tag:<8} {rel}")
                if reason:
                    print(f"           --> {reason}")

    return results


def _print_summary(results: list, label: str = "") -> None:
    ok = sum(1 for r in results if r["status"] == "OK")
    warn = sum(1 for r in results if r["status"] == "WARN")
    fail = sum(1 for r in results if r["status"] == "FAIL")
    prefix = f"[{label}] " if label else ""
    print(f"  {prefix}[OK]={ok}  [WARN]={warn}  [FAIL]={fail}  total={ok+warn+fail}")


def cmd_check(args: argparse.Namespace) -> int:
    """Execute --check mode."""
    if args.check == "all" or args.check is None:
        paths = [ROOT / nd for nd in NUCLEUS_DIRS if (ROOT / nd).is_dir()]
    else:
        paths = [Path(args.check)]

    all_results = []
    for p in paths:
        if not p.is_dir():
            print(f"[WARN] Not a directory: {p}")
            continue
        if not args.summary:
            print(f"\n--- {p.name} ---")
        results = _scan_path(p, quiet=args.summary)
        if args.summary:
            _print_summary(results, label=p.name)
        all_results.extend(results)

    if len(paths) > 1:
        print(f"\n=== TOTAL ===")
        _print_summary(all_results)

    warn_count = sum(1 for r in all_results if r["status"] == "WARN")
    fail_count = sum(1 for r in all_results if r["status"] == "FAIL")
    return 1 if (warn_count + fail_count) > 0 else 0


def _suggest_canonical(f: Path) -> str:
    """Suggest a canonical name for f (best-effort, manual review needed)."""
    name = f.name.lower()
    stem = name.rsplit('.', 1)[0]
    ext = '.' + name.rsplit('.', 1)[1] if '.' in name else ''

    # Strip legacy prefix
    for prefix in LEGACY_PREFIXES:
        if stem.startswith(prefix):
            stem = stem[len(prefix):]
            break

    # Strip trailing _nxx
    stem = re.sub(r'_n\d{2}$', '', stem)

    # Infer nucleus code from path
    nxx = "n??"
    for part in f.parts:
        m = re.match(r'^[Nn](\d{2})_', part)
        if m:
            nxx = f"n{m.group(1)}"
            break

    return f"p{{nn}}_{stem}_{nxx}{ext}  (pillar code required)"


def cmd_fix(args: argparse.Namespace) -> int:
    """Execute --fix mode."""
    fix_path = Path(args.fix)
    if not fix_path.is_dir():
        print(f"[FAIL] Not a directory: {fix_path}")
        return 1

    # Scan quietly first
    results = _scan_path(fix_path, quiet=True)
    non_ok = [r for r in results if r["status"] != "OK"]

    if not non_ok:
        print("[OK] No renames needed.")
        return 0

    mode = "EXECUTING" if args.confirm else "DRY-RUN"
    print(f"{mode}: {len(non_ok)} file(s) need attention\n")

    # Files that have a clear nxx and just need pillar prefix
    auto_renameable = []
    manual_review = []

    for r in non_ok:
        f = r["path"]
        suggestion = _suggest_canonical(f)
        has_nxx = bool(re.search(r'_n\d{2}\.(md|yaml)$', f.name.lower()))
        has_pillar = bool(re.match(r'^p\d{2}_', f.name.lower()))

        if has_nxx and not has_pillar:
            manual_review.append((r, suggestion, "needs pillar prefix"))
        else:
            manual_review.append((r, suggestion, "review required"))

    for r, suggestion, note in manual_review:
        print(f"  [RENAME] {r['rel']}")
        print(f"        -> {suggestion}")
        print(f"        note: {note}")
        if args.confirm:
            # Conservative: only log, require manual git mv
            # Automated rename risks breaking frontmatter 'id' field + cross-references
            print(f"        [SKIP] Automated rename skipped -- manual git mv required")
            print(f"               After rename: update 'id:' in frontmatter + grep for old name")
        print()

    if not args.confirm:
        print("[i] Review suggestions above.")
        print("[i] Add --confirm to run (conservative: logs renames but requires manual git mv).")
        print("[i] After renaming, update 'id:' in frontmatter and run:")
        print("    grep -r '<old_name>' . --include='*.md' --include='*.yaml' -l")

    return 0


def main() -> int:
    parser = argparse.ArgumentParser(
        description="CEX Naming Validator -- enforce pxx_kind_desc_nxx convention",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )
    parser.add_argument(
        "--check",
        nargs="?",
        const="all",
        metavar="PATH",
        help="Validate naming (all nuclei if PATH omitted)",
    )
    parser.add_argument(
        "--fix",
        metavar="PATH",
        help="Suggest renames for a path (use --confirm to execute)",
    )
    parser.add_argument(
        "--confirm",
        action="store_true",
        help="Execute renames (with --fix); default is dry-run",
    )
    parser.add_argument(
        "--summary",
        action="store_true",
        help="Show counts only, not individual files",
    )
    parser.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress [OK] lines, show only issues",
    )

    args = parser.parse_args()

    if args.check is not None:
        return cmd_check(args)
    elif args.fix:
        return cmd_fix(args)
    else:
        parser.print_help()
        return 0


if __name__ == "__main__":
    sys.exit(main())
