#!/usr/bin/env python3
"""W3: Wikilink sweep -- populate related: frontmatter + Related Artifacts section.

Scans all .md files in the repo with frontmatter, uses cex_retriever TF-IDF to
find top-N similar artifacts, writes related: field and ## Related Artifacts table.

Usage:
    python _tools/cex_wikilink.py --sweep --dry-run        # preview changes
    python _tools/cex_wikilink.py --sweep --apply          # write all changes
    python _tools/cex_wikilink.py --file path/to/x.md --apply
    python _tools/cex_wikilink.py --stats                  # count eligible files
    python _tools/cex_wikilink.py --rebuild-index          # rebuild retriever first
"""

import argparse
import re
import sys
from pathlib import Path

import yaml

CEX_ROOT = Path(__file__).resolve().parent.parent

sys.path.insert(0, str(CEX_ROOT / "_tools"))
from cex_retriever import find_similar, load_index

SKIP_DIRS = {
    ".git", ".obsidian", "__pycache__", "node_modules",
    "compiled", ".cex", "_docs",
}

# Minimum TF-IDF cosine similarity to include as related
DEFAULT_MIN_SCORE = 0.15
DEFAULT_MAX_REFS = 10

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)", re.DOTALL)

RELATED_TABLE_HEADER = """
## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
"""


def _classify_relationship(src_kind: str, tgt_kind: str, tgt_pillar: str, src_pillar: str) -> str:
    """Simple heuristic relationship classification."""
    if src_kind and tgt_kind and src_kind == tgt_kind:
        return "sibling"
    # Pillar ordering: upstream is lower pillar number (P01 feeds P02, etc.)
    try:
        src_p = int(src_pillar[1:]) if src_pillar and src_pillar[0] == "P" else 0
        tgt_p = int(tgt_pillar[1:]) if tgt_pillar and tgt_pillar[0] == "P" else 0
        if src_p > tgt_p > 0:
            return "upstream"
        if tgt_p > src_p > 0:
            return "downstream"
    except (ValueError, IndexError):
        pass
    return "related"


def collect_md_files(root: Path) -> list[Path]:
    """Collect all .md files eligible for wikilink sweep."""
    result = []
    for p in root.rglob("*.md"):
        parts = set(p.parts)
        if any(s in parts for s in SKIP_DIRS):
            continue
        # Skip files without frontmatter (cheap check: starts with ---)
        try:
            head = p.read_text(encoding="utf-8", errors="ignore")[:4]
            if head != "---\n":
                continue
        except (OSError, PermissionError):
            continue
        result.append(p)
    return sorted(result)


def parse_file(path: Path) -> tuple[dict, str] | None:
    """Parse frontmatter + body. Returns (meta, body) or None if no frontmatter."""
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None

    m = FRONTMATTER_RE.match(text)
    if not m:
        return None

    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except yaml.YAMLError:
        return None

    body = m.group(2)
    return meta, body


def build_related_list(
    meta: dict,
    body: str,
    index: dict,
    min_score: float,
    max_refs: int,
    self_id: str,
) -> list[dict]:
    """Find related artifacts using TF-IDF retriever."""
    query = body[:4000]  # Use first 4K chars of body as query
    if not query.strip():
        # Fall back to tldr + title from frontmatter
        query = " ".join(filter(None, [
            str(meta.get("title", "")),
            str(meta.get("tldr", "")),
            str(meta.get("domain", "")),
        ]))

    if not query.strip():
        return []

    results = find_similar(
        query=query,
        index=index,
        top_k=max_refs + 5,  # Get extra to compensate for self-filter
        min_score=min_score,
    )

    # Filter self and dedupe
    seen = set()
    filtered = []
    for r in results:
        rid = r.get("id", "")
        if not rid or rid == self_id or rid in seen:
            continue
        seen.add(rid)
        filtered.append(r)
        if len(filtered) >= max_refs:
            break

    return filtered


def format_related_table(related: list[dict], src_kind: str, src_pillar: str) -> str:
    """Build ## Related Artifacts markdown table."""
    rows = []
    for r in related:
        rid = r.get("id", "")
        kind = r.get("kind", "")
        pillar = r.get("pillar", "")
        score = r.get("score", 0)
        rel = _classify_relationship(src_kind, kind, pillar, src_pillar)
        rows.append(f"| [[{rid}]] | {rel} | {score:.2f} |")

    return RELATED_TABLE_HEADER + "\n".join(rows) + "\n"


def wire_file(
    path: Path,
    index: dict,
    min_score: float,
    max_refs: int,
    apply: bool,
    force: bool = False,
) -> str:
    """Process a single file. Returns status: 'changed', 'skipped', 'no_results', 'error'."""
    parsed = parse_file(path)
    if parsed is None:
        return "error"

    meta, body = parsed
    self_id = str(meta.get("id", ""))
    src_kind = str(meta.get("kind", ""))
    src_pillar = str(meta.get("pillar", ""))

    # Skip if already has populated related: (unless --force)
    existing_related = meta.get("related", [])
    if existing_related and not force:
        return "skipped"

    related = build_related_list(meta, body, index, min_score, max_refs, self_id)
    if not related:
        return "no_results"

    related_ids = [r["id"] for r in related]

    # Rebuild frontmatter with related: field inserted
    try:
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return "error"

    m = FRONTMATTER_RE.match(text)
    if not m:
        return "error"

    fm_text = m.group(1)
    body_text = m.group(2)

    # Update related: in frontmatter YAML text (simple string manipulation)
    # Remove any existing related: lines
    fm_lines = fm_text.split("\n")
    new_fm_lines = []
    i = 0
    while i < len(fm_lines):
        line = fm_lines[i]
        if line.startswith("related:"):
            # Skip existing related block (multi-line list)
            i += 1
            while i < len(fm_lines) and fm_lines[i].startswith("  - "):
                i += 1
            continue
        new_fm_lines.append(line)
        i += 1

    # Build new related: block
    related_yaml = "related:\n" + "".join(f"  - {rid}\n" for rid in related_ids)
    new_fm_text = "\n".join(new_fm_lines).rstrip() + "\n" + related_yaml.rstrip()

    # Update or append ## Related Artifacts section in body
    if "## Related Artifacts" in body_text:
        # Replace existing section
        body_updated = re.sub(
            r"## Related Artifacts\n[\s\S]*?(?=\n## |\Z)",
            format_related_table(related, src_kind, src_pillar),
            body_text,
            count=1,
        )
    else:
        body_updated = body_text.rstrip() + "\n" + format_related_table(related, src_kind, src_pillar)

    new_content = f"---\n{new_fm_text}\n---\n{body_updated}"

    if apply:
        try:
            path.write_text(new_content, encoding="utf-8")
        except (OSError, PermissionError) as e:
            return f"error:{e}"

    return "changed"


def rebuild_index() -> None:
    """Rebuild the retriever index."""
    import subprocess
    print("[W3] Rebuilding retriever index...")
    result = subprocess.run(
        [sys.executable, str(CEX_ROOT / "_tools" / "cex_retriever.py"), "--build"],
        capture_output=True, text=True,
    )
    if result.returncode == 0:
        print("[W3] Index rebuilt successfully.")
    else:
        print(f"[W3] Index rebuild failed: {result.stderr[:200]}")


def main() -> None:
    parser = argparse.ArgumentParser(description="W3: Wikilink sweep for CEX repo")
    parser.add_argument("--sweep", action="store_true", help="Process all eligible .md files")
    parser.add_argument("--file", help="Process a single file")
    parser.add_argument("--dry-run", action="store_true", help="Preview changes (default)")
    parser.add_argument("--apply", action="store_true", help="Write changes")
    parser.add_argument("--stats", action="store_true", help="Count eligible files, no processing")
    parser.add_argument("--force", action="store_true", help="Overwrite existing related: fields")
    parser.add_argument("--rebuild-index", action="store_true", help="Rebuild retriever index first")
    parser.add_argument("--min-score", type=float, default=DEFAULT_MIN_SCORE,
                        help=f"Min similarity threshold (default: {DEFAULT_MIN_SCORE})")
    parser.add_argument("--max-refs", type=int, default=DEFAULT_MAX_REFS,
                        help=f"Max related refs per artifact (default: {DEFAULT_MAX_REFS})")
    args = parser.parse_args()

    if args.rebuild_index:
        rebuild_index()

    if args.stats:
        files = collect_md_files(CEX_ROOT)
        print(f"[W3] Eligible .md files: {len(files)}")
        return

    mode = "APPLY" if args.apply else "DRY-RUN"
    print(f"[W3] cex_wikilink.py -- {mode}")
    print("[W3] Loading retriever index...")

    index = load_index()
    if not index:
        print("[W3] ERROR: No retriever index found. Run with --rebuild-index first.")
        sys.exit(1)

    print(f"[W3] Index loaded: {index.get('n_docs', 0)} documents")

    # Collect target files
    if args.file:
        files = [Path(args.file).resolve()]
    elif args.sweep:
        files = collect_md_files(CEX_ROOT)
    else:
        parser.print_help()
        sys.exit(1)

    print(f"[W3] Processing {len(files)} files (min_score={args.min_score}, max_refs={args.max_refs})")

    changed = 0
    skipped = 0
    no_results = 0
    errors = 0

    for i, path in enumerate(files):
        status = wire_file(
            path, index, args.min_score, args.max_refs,
            apply=args.apply, force=args.force,
        )
        if status == "changed":
            changed += 1
            rel = path.relative_to(CEX_ROOT)
            print(f"  [+] {rel}")
        elif status == "skipped":
            skipped += 1
        elif status == "no_results":
            no_results += 1
        elif status.startswith("error"):
            errors += 1

        # Progress every 100 files
        if (i + 1) % 100 == 0:
            print(f"  ... {i+1}/{len(files)} processed")

    print()
    print(f"[W3] Summary ({mode}):")
    print(f"     changed:    {changed}")
    print(f"     skipped:    {skipped} (already have related:)")
    print(f"     no_results: {no_results} (retriever found nothing)")
    print(f"     errors:     {errors}")
    print(f"     total:      {len(files)}")

    if not args.apply and changed > 0:
        print()
        print("[W3] Re-run with --apply to write changes.")


if __name__ == "__main__":
    main()
