#!/usr/bin/env python3
"""cex_janitor.py: CRUD for repo pollution. List/inspect/delete junk.

Categories (6):
  pycache      - all __pycache__ dirs (regen'd on next run)
  empty_files  - 0-byte files
  stub_md      - .md files under 200B (frontmatter-only, no body)
  stale_runtime- .cex/runtime/{signals,handoffs,out} older than N days
  empty_dirs   - directories with no files (recursive)
  orphan_json  - .json in compiled/ without matching .md source

Usage:
  python _tools/cex_janitor.py scan                        # list all categories
  python _tools/cex_janitor.py scan --category pycache     # single category
  python _tools/cex_janitor.py inspect stub_md             # show file list + sizes
  python _tools/cex_janitor.py rm pycache --dry-run        # preview delete
  python _tools/cex_janitor.py rm pycache --yes            # actually delete
  python _tools/cex_janitor.py rm stale_runtime --days 7 --yes
  python _tools/cex_janitor.py rm all --yes                # nuke everything junk
"""
from __future__ import annotations

import argparse
import shutil
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
EXCLUDE_DIRS = {".git", ".venv_litellm", "node_modules", ".cex/runtime/out/archive"}
DEFAULT_STALE_DAYS = 7
STUB_MD_MAX_BYTES = 200


def is_excluded(p: Path) -> bool:
    """Return whether a path lives under an excluded directory."""
    rel = p.relative_to(ROOT).as_posix()
    return any(rel == d or rel.startswith(d + "/") for d in EXCLUDE_DIRS)


def find_pycache() -> list[Path]:
    """Find Python bytecode cache directories outside excluded paths."""
    return [p for p in ROOT.rglob("__pycache__") if p.is_dir() and not is_excluded(p)]


PRESERVE_EMPTY = {".gitkeep", ".keep", ".gitignore", "__init__.py"}


def find_empty_files() -> list[Path]:
    """Find empty files that are not explicitly preserved."""
    hits = []
    for p in ROOT.rglob("*"):
        if not p.is_file() or is_excluded(p):
            continue
        if p.name in PRESERVE_EMPTY:
            continue
        try:
            if p.stat().st_size == 0:
                hits.append(p)
        except OSError:
            continue
    return hits


def find_stub_md() -> list[Path]:
    """Find very small markdown files that contain only frontmatter stubs."""
    hits = []
    for p in ROOT.rglob("*.md"):
        if not p.is_file() or is_excluded(p):
            continue
        try:
            size = p.stat().st_size
            if size == 0 or size > STUB_MD_MAX_BYTES:
                continue
            txt = p.read_text(encoding="utf-8", errors="replace")
            # frontmatter only = starts with --- and has second ---, nothing meaningful after
            if txt.startswith("---"):
                parts = txt.split("---", 2)
                body = parts[2].strip() if len(parts) > 2 else ""
                if len(body) < 20:
                    hits.append(p)
        except OSError:
            continue
    return hits


def find_stale_runtime(days: int = DEFAULT_STALE_DAYS) -> list[Path]:
    """Find runtime artifacts older than the configured age threshold."""
    cutoff = time.time() - (days * 86400)
    hits = []
    for sub in ("signals", "handoffs", "out"):
        d = ROOT / ".cex" / "runtime" / sub
        if not d.exists():
            continue
        for p in d.rglob("*"):
            if not p.is_file() or is_excluded(p):
                continue
            try:
                if p.stat().st_mtime < cutoff:
                    hits.append(p)
            except OSError:
                continue
    return hits


def find_empty_dirs() -> list[Path]:
    """Find empty directories, walking deepest paths first."""
    hits = []
    for p in sorted(ROOT.rglob("*"), key=lambda x: -len(x.parts)):
        if not p.is_dir() or is_excluded(p) or p == ROOT:
            continue
        try:
            if not any(p.iterdir()):
                hits.append(p)
        except OSError:
            continue
    return hits


def find_orphan_json() -> list[Path]:
    """Find compiled JSON artifacts that no longer have a markdown sibling."""
    hits = []
    for p in ROOT.rglob("compiled/**/*.json"):
        if is_excluded(p):
            continue
        # sibling .md with same stem?
        md = p.with_suffix(".md")
        if not md.exists():
            hits.append(p)
    return hits


CATEGORIES = {
    "pycache":       find_pycache,
    "empty_files":   find_empty_files,
    "stub_md":       find_stub_md,
    "stale_runtime": find_stale_runtime,
    "empty_dirs":    find_empty_dirs,
    "orphan_json":   find_orphan_json,
}


def path_size(p: Path) -> int:
    """Measure the size of one file or the recursive size of one directory."""
    try:
        if p.is_file():
            return p.stat().st_size
        if p.is_dir():
            return sum(f.stat().st_size for f in p.rglob("*") if f.is_file())
    except OSError:
        pass
    return 0


def human(n: int) -> str:
    """Format a byte count with binary size suffixes."""
    for unit in ("B", "K", "M", "G"):
        if n < 1024:
            return f"{n:.1f}{unit}"
        n /= 1024
    return f"{n:.1f}T"


def cmd_scan(args) -> int:
    """Print per-category janitor totals."""
    cats = [args.category] if args.category else list(CATEGORIES)
    total_size = 0
    total_count = 0
    print(f"{'CATEGORY':<16} {'COUNT':>7} {'SIZE':>10}")
    print("-" * 36)
    for cat in cats:
        items = CATEGORIES[cat]() if cat != "stale_runtime" else find_stale_runtime(args.days)
        size = sum(path_size(p) for p in items)
        print(f"{cat:<16} {len(items):>7} {human(size):>10}")
        total_size += size
        total_count += len(items)
    print("-" * 36)
    print(f"{'TOTAL':<16} {total_count:>7} {human(total_size):>10}")
    return 0


def cmd_inspect(args) -> int:
    """List matching janitor targets for one category."""
    if args.category == "stale_runtime":
        items = find_stale_runtime(args.days)
    else:
        items = CATEGORIES[args.category]()
    for p in items[: args.limit]:
        rel = p.relative_to(ROOT).as_posix()
        print(f"  {human(path_size(p)):>8}  {rel}")
    if len(items) > args.limit:
        print(f"  ... +{len(items) - args.limit} more")
    print(f"\n{len(items)} item(s) in '{args.category}'")
    return 0


def cmd_rm(args) -> int:
    """Delete janitor targets after dry-run and confirmation checks."""
    if args.category == "all":
        cats = list(CATEGORIES)
    else:
        cats = [args.category]

    to_delete: list[Path] = []
    for cat in cats:
        items = find_stale_runtime(args.days) if cat == "stale_runtime" else CATEGORIES[cat]()
        to_delete.extend(items)

    total_size = sum(path_size(p) for p in to_delete)
    print(f"Would delete: {len(to_delete)} item(s), {human(total_size)}")

    if args.dry_run:
        for p in to_delete[:20]:
            print(f"  - {p.relative_to(ROOT).as_posix()}")
        if len(to_delete) > 20:
            print(f"  ... +{len(to_delete) - 20} more")
        print("\n[DRY-RUN] nothing deleted. Re-run with --yes to execute.")
        return 0

    if not args.yes:
        print("Refusing to delete without --yes flag.", file=sys.stderr)
        return 1

    deleted = 0
    failed = 0
    for p in to_delete:
        try:
            if p.is_dir():
                shutil.rmtree(p)
            else:
                p.unlink()
            deleted += 1
        except OSError as e:
            print(f"  FAIL: {p.relative_to(ROOT).as_posix()}: {e}", file=sys.stderr)
            failed += 1

    print(f"Deleted: {deleted}/{len(to_delete)} ({human(total_size)} freed, {failed} failed)")
    return 0 if failed == 0 else 2


def main() -> int:
    """Dispatch janitor subcommands from the CLI."""
    p = argparse.ArgumentParser()
    sub = p.add_subparsers(dest="cmd", required=True)

    s = sub.add_parser("scan", help="summary by category")
    s.add_argument("--category", choices=list(CATEGORIES))
    s.add_argument("--days", type=int, default=DEFAULT_STALE_DAYS)
    s.set_defaults(fn=cmd_scan)

    i = sub.add_parser("inspect", help="list items in one category")
    i.add_argument("category", choices=list(CATEGORIES))
    i.add_argument("--limit", type=int, default=50)
    i.add_argument("--days", type=int, default=DEFAULT_STALE_DAYS)
    i.set_defaults(fn=cmd_inspect)

    r = sub.add_parser("rm", help="delete items in one category (or 'all')")
    r.add_argument("category", choices=list(CATEGORIES) + ["all"])
    r.add_argument("--dry-run", action="store_true")
    r.add_argument("--yes", action="store_true")
    r.add_argument("--days", type=int, default=DEFAULT_STALE_DAYS)
    r.set_defaults(fn=cmd_rm)

    args = p.parse_args()
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
