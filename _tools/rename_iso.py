"""
rename_iso.py — Convert legacy ISO_{SAT}_{NNN}_{TYPE}.md files to canonical ISO Package names.

Usage:
    python _tools/rename_iso.py --source records/agents/anuncio/iso_vectorstore/ --output packages/anuncio/ --dry-run
    python _tools/rename_iso.py --source records/agents/anuncio/iso_vectorstore/ --output packages/anuncio/
    python _tools/rename_iso.py --batch records/agents/ --output packages/ --dry-run
"""

import argparse
import re
import shutil
import sys
from pathlib import Path


# Canonical name mapping: TYPE suffix -> new filename
# Ordered: more specific patterns first
TYPE_MAP = [
    # Manifest
    (r"MANIFEST",                         "manifest.yaml"),
    # System instructions
    (r"SYSTEM_INSTRUCTION_WHITELABEL",    "system_instruction_whitelabel.md"),
    (r"SYSTEM_INSTRUCTION",               "system_instruction.md"),
    # Upload kits
    (r"UPLOAD_KIT_WHITELABEL",            "upload_kit_whitelabel.md"),
    (r"UPLOAD_KIT",                       "upload_kit.md"),
    # Core docs
    (r"INSTRUCTIONS",                     "instructions.md"),
    (r"ARCHITECTURE",                     "architecture.md"),
    (r"OUTPUT_TEMPLATE",                  "output_template.md"),
    (r"EXAMPLES",                         "examples.md"),
    (r"ERROR_HANDLING",                   "error_handling.md"),
    (r"QUICK_START",                      "quick_start.md"),
    # Schemas
    (r"INPUT_SCHEMA",                     "input_schema.yaml"),
    # README
    (r"README",                           "README.md"),
]

# Compiled patterns: (regex, canonical_name)
_COMPILED = [(re.compile(rf"ISO_[A-Z]+_\d+_{pat}"), canon) for pat, canon in TYPE_MAP]
# Also handle files that ARE already canonical (pass-through)
_CANONICAL_NAMES = {canon for _, canon in TYPE_MAP}

HARDCODED_PATH_PATTERNS = [
    re.compile(r"C:[/\\]"),
    re.compile(r"/home/"),
    re.compile(r"/Users/"),
]


def detect_canonical_name(filename: str) -> str | None:
    """Return the canonical target filename for a legacy ISO file, or None if unrecognized."""
    stem = Path(filename).stem.upper()
    for pattern, canon in _COMPILED:
        if pattern.match(filename.upper()):
            return canon
    # Already canonical?
    if filename in _CANONICAL_NAMES:
        return filename
    return None


def check_portability(content: str) -> list[str]:
    """Return list of portability issues found in file content."""
    issues = []
    for pat in HARDCODED_PATH_PATTERNS:
        matches = pat.findall(content)
        if matches:
            issues.append(f"Hardcoded path pattern: {pat.pattern!r} ({len(matches)} occurrences)")
    return issues


def rename_one(source_dir: Path, output_dir: Path, dry_run: bool, verbose: bool = True) -> dict:
    """Rename ISO files from source_dir into output_dir with canonical names."""
    results = {
        "renamed": [],
        "skipped": [],
        "warnings": [],
        "errors": [],
    }

    if not source_dir.exists():
        results["errors"].append(f"Source dir not found: {source_dir}")
        return results

    if not dry_run:
        output_dir.mkdir(parents=True, exist_ok=True)

    iso_files = sorted(source_dir.glob("*.md")) + sorted(source_dir.glob("*.yaml"))

    if not iso_files:
        results["warnings"].append(f"No .md or .yaml files found in {source_dir}")
        return results

    seen_canonical = {}  # canonical_name -> source_file (detect collisions)

    for src_file in iso_files:
        canonical = detect_canonical_name(src_file.name)

        if canonical is None:
            results["skipped"].append(str(src_file.name))
            if verbose:
                print(f"  SKIP  {src_file.name} (unrecognized pattern)")
            continue

        # Collision check
        if canonical in seen_canonical:
            msg = f"COLLISION: {src_file.name} -> {canonical} (already mapped from {seen_canonical[canonical]})"
            results["warnings"].append(msg)
            if verbose:
                print(f"  WARN  {msg}")
            continue
        seen_canonical[canonical] = src_file.name

        # Portability check
        content = src_file.read_text(encoding="utf-8", errors="replace")
        issues = check_portability(content)
        if issues:
            for issue in issues:
                results["warnings"].append(f"{src_file.name}: {issue}")
                if verbose:
                    print(f"  WARN  {src_file.name}: {issue}")

        dest_file = output_dir / canonical
        action = "DRY"if dry_run else "COPY"

        if not dry_run:
            shutil.copy2(src_file, dest_file)

        results["renamed"].append((src_file.name, canonical))
        if verbose:
            print(f"  {action}  {src_file.name} -> {canonical}")

    return results


def rename_batch(source_agents_dir: Path, output_packages_dir: Path, dry_run: bool) -> None:
    """Process all agent subdirectories under source_agents_dir."""
    agent_dirs = [d for d in source_agents_dir.iterdir() if d.is_dir()]
    if not agent_dirs:
        print(f"No agent directories found under {source_agents_dir}")
        return

    total_renamed = 0
    total_skipped = 0
    total_warnings = 0
    total_errors = 0

    for agent_dir in sorted(agent_dirs):
        iso_dir = agent_dir / "iso_vectorstore"
        if not iso_dir.exists():
            continue

        out_dir = output_packages_dir / agent_dir.name
        print(f"\n[{agent_dir.name}]")
        results = rename_one(iso_dir, out_dir, dry_run=dry_run, verbose=True)

        total_renamed += len(results["renamed"])
        total_skipped += len(results["skipped"])
        total_warnings += len(results["warnings"])
        total_errors += len(results["errors"])

    print(f"\n{'='*60}")
    print(f"BATCH SUMMARY {'(DRY RUN)' if dry_run else '(EXECUTED)'}")
    print(f"  Renamed:  {total_renamed}")
    print(f"  Skipped:  {total_skipped}")
    print(f"  Warnings: {total_warnings}")
    print(f"  Errors:   {total_errors}")
    print(f"{'='*60}")


def print_mapping_table() -> None:
    """Print the full OLD->NEW mapping table."""
    print("\nISO File Rename Mapping Table")
    print(f"{'OLD Pattern':<50} {'NEW (canonical)'}")
    print("-" * 70)
    for pat, canon in TYPE_MAP:
        print(f"  ISO_{{SAT}}_{{NNN}}_{pat:<40} -> {canon}")
    print()


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Rename legacy ISO_{SAT}_{NNN}_{TYPE}.md files to canonical ISO Package names.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__,
    )

    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument("--source", type=Path, help="Source iso_vectorstore/ directory (single agent)")
    mode.add_argument("--batch", type=Path, help="Source records/agents/ directory (all agents)")
    mode.add_argument("--list-mappings", action="store_true", help="Print the full mapping table and exit")

    parser.add_argument("--output", type=Path, help="Output directory (packages/anuncio/ or packages/)")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    parser.add_argument("--quiet", action="store_true", help="Suppress per-file output")

    args = parser.parse_args()

    if args.list_mappings:
        print_mapping_table()
        return 0

    if args.source and not args.output:
        parser.error("--output is required when using --source")

    if args.batch and not args.output:
        parser.error("--output is required when using --batch")

    if args.dry_run:
        print("[DRY RUN] No files will be written.\n")

    if args.source:
        print(f"Source: {args.source}")
        print(f"Output: {args.output}")
        print()
        results = rename_one(
            source_dir=args.source,
            output_dir=args.output,
            dry_run=args.dry_run,
            verbose=not args.quiet,
        )
        print(f"\nSUMMARY {'(DRY RUN)' if args.dry_run else '(EXECUTED)'}")
        print(f"  Renamed:  {len(results['renamed'])}")
        print(f"  Skipped:  {len(results['skipped'])}")
        print(f"  Warnings: {len(results['warnings'])}")
        print(f"  Errors:   {len(results['errors'])}")

        if results["errors"]:
            for err in results["errors"]:
                print(f"  ERROR: {err}", file=sys.stderr)
            return 1

    elif args.batch:
        rename_batch(
            source_agents_dir=args.batch,
            output_packages_dir=args.output,
            dry_run=args.dry_run,
        )

    return 0


if __name__ == "__main__":
    sys.exit(main())
