#!/usr/bin/env python3
"""Fix frontmatter: add kind+id to all builder .md files missing them.

Usage:
    python fix_frontmatter.py --dry-run   # Report only
    python fix_frontmatter.py --fix       # Apply changes
"""

import re
import sys
from pathlib import Path

CEX_ROOT = Path(__file__).resolve().parent.parent
BUILDERS_DIR = CEX_ROOT / "archetypes" / "builders"


def derive_topic_from_dir(dirpath: Path) -> str | None:
    """Extract builder topic from directory name.

    'action-prompt-builder' -> 'action_prompt'
    '_builder-builder'      -> 'builder'
    'builders' (root)       -> None
    """
    dirname = dirpath.name
    if dirname == "builders":
        return None
    topic = dirname
    if topic.endswith("-builder"):
        topic = topic[:-8]
    topic = topic.lstrip("_").replace("-", "_")
    return topic


def derive_kind_and_id(filepath: Path) -> tuple[str, str]:
    """Derive kind and id from file path.

    For bld_{iso_type}_{topic}.md in {topic}-builder/:
      id   = filename stem  (e.g. bld_architecture_action_prompt)
      kind = iso_type        (e.g. architecture)
    """
    stem = filepath.stem
    file_id = stem
    topic = derive_topic_from_dir(filepath.parent)

    if topic is None:
        # Root-level file (e.g. bld_norms.md)
        kind = stem[4:] if stem.startswith("bld_") else stem
        return kind, file_id

    prefix = "bld_"
    suffix = f"_{topic}"

    if stem.startswith(prefix) and stem.endswith(suffix) and len(stem) > len(prefix) + len(suffix):
        kind = stem[len(prefix) : -len(suffix)]
    elif stem.startswith(prefix):
        kind = stem[len(prefix) :]
    else:
        kind = stem

    return kind, file_id


def strip_backtick_wrapper(lines: list[str]) -> tuple[list[str], bool]:
    """Remove ```yaml / ``` wrapper around frontmatter if present."""
    if not lines or not lines[0].startswith("```"):
        return lines, False

    new_lines = lines[1:]  # drop opening ```yaml

    # Find the ``` that sits right after the closing ---
    for i in range(1, len(new_lines)):
        if new_lines[i].strip() == "```" and i > 0 and new_lines[i - 1].strip() == "---":
            new_lines.pop(i)
            break

    return new_lines, True


def inject_fields(
    lines: list[str], kind: str, file_id: str, need_kind: bool, need_id: bool
) -> list[str]:
    """Insert kind/id after the opening --- of existing frontmatter."""
    if lines[0].strip() != "---":
        return lines

    insert = []
    if need_kind:
        insert.append(f"kind: {kind}")
    if need_id:
        insert.append(f"id: {file_id}")

    return lines[:1] + insert + lines[1:]


def create_frontmatter(lines: list[str], kind: str, file_id: str) -> list[str]:
    """Wrap content with a minimal frontmatter block."""
    header = ["---", f"kind: {kind}", f"id: {file_id}", "---", ""]
    return header + lines


def process_file(filepath: Path, dry_run: bool) -> str:
    """Process one file. Returns status: ok | fixed | skip | error."""
    if filepath.name == "README.md":
        return "skip"

    content = filepath.read_text(encoding="utf-8")
    lines = content.split("\n")

    has_kind = bool(re.search(r"^kind:", content, re.MULTILINE))
    has_id = bool(re.search(r"^id:", content, re.MULTILINE))

    if has_kind and has_id:
        return "ok"

    kind, file_id = derive_kind_and_id(filepath)
    modified = False

    # Step 1: strip backtick wrapper if present
    lines, stripped = strip_backtick_wrapper(lines)
    if stripped:
        modified = True

    # Step 2a: has frontmatter -> inject fields
    if lines and lines[0].strip() == "---":
        lines = inject_fields(lines, kind, file_id, need_kind=not has_kind, need_id=not has_id)
        modified = True

    # Step 2b: no frontmatter -> create minimal
    elif lines and lines[0].strip() != "---":
        lines = create_frontmatter(lines, kind, file_id)
        modified = True

    if modified:
        if not dry_run:
            filepath.write_text("\n".join(lines), encoding="utf-8")
        return "fixed"

    return "error"


def main():
    dry_run = "--dry-run" in sys.argv
    fix = "--fix" in sys.argv

    if not dry_run and not fix:
        print("Usage: python fix_frontmatter.py [--dry-run | --fix]")
        sys.exit(1)

    mode = "DRY RUN" if dry_run else "FIX"
    print(f"=== {mode} MODE ===\n")

    stats = {"ok": 0, "fixed": 0, "error": 0, "skip": 0}
    fixed_files = []
    error_files = []

    for md_file in sorted(BUILDERS_DIR.rglob("*.md")):
        try:
            status = process_file(md_file, dry_run)
            stats[status] += 1
            rel = md_file.relative_to(BUILDERS_DIR)
            if status == "fixed":
                fixed_files.append(str(rel))
            elif status == "error":
                error_files.append(str(rel))
        except Exception as e:
            stats["error"] += 1
            error_files.append(f"{md_file.relative_to(BUILDERS_DIR)}: {e}")

    total = sum(stats.values())
    print("Results:")
    print(f"  Already OK:  {stats['ok']}")
    label = "Would fix" if dry_run else "Fixed"
    print(f"  {label}:     {stats['fixed']}")
    print(f"  Errors:      {stats['error']}")
    print(f"  Skipped:     {stats['skip']}")
    print(f"  Total files: {total}")

    if fixed_files:
        print(f"\n{label} {len(fixed_files)} files:")
        for f in fixed_files[:30]:
            print(f"  {f}")
        if len(fixed_files) > 30:
            print(f"  ... and {len(fixed_files) - 30} more")

    if error_files:
        print(f"\nErrors ({len(error_files)}):")
        for e in error_files:
            print(f"  {e}")

    if dry_run and stats["fixed"] == 0 and stats["error"] == 0:
        print("\nAll files have kind+id. No fixes needed.")


if __name__ == "__main__":
    main()
