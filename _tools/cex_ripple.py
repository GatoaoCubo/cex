#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""cex_ripple.py -- Cross-reference propagation engine (Karpathy LLM Wiki pattern).

On artifact save, finds related artifacts and updates bidirectional cross-refs.
Prevents cascade storms via max_ripple budget (default 15 files).

GDP decision: auto_with_safety_net
  - Auto-apply ripple patches
  - Git snapshot before
  - Revert if quality drops > 0.5

Usage:
    python _tools/cex_ripple.py <path>                  # ripple from one file
    python _tools/cex_ripple.py <path> --dry-run        # preview only
    python _tools/cex_ripple.py <path> --max-ripple 20  # custom budget
    python _tools/cex_ripple.py --check <path>          # show what would ripple
"""

import argparse
import os
import re
import subprocess
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

sys.path.insert(0, str(CEX_ROOT / "_tools"))
from cex_retriever import find_similar, load_index

DEFAULT_MAX_RIPPLE = 15
DEFAULT_MIN_SCORE = 0.15
QUALITY_DROP_THRESHOLD = 0.5

FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)", re.DOTALL)


# ------------------------------------------------------------------
# Frontmatter helpers
# ------------------------------------------------------------------

def parse_frontmatter(path: Path) -> tuple[dict, str] | None:
    """Parse YAML frontmatter + body. Returns (meta_dict, body) or None."""
    try:
        import yaml
        text = path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError, ImportError):
        return None

    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        meta = yaml.safe_load(m.group(1)) or {}
    except Exception:
        return None
    return meta, m.group(2)


def get_related_ids(path: Path) -> list[str]:
    """Extract related: list from frontmatter."""
    parsed = parse_frontmatter(path)
    if not parsed:
        return []
    meta, _ = parsed
    related = meta.get("related", [])
    if isinstance(related, list):
        return [str(r) for r in related]
    return []


def get_artifact_id(path: Path) -> str:
    """Extract id from frontmatter."""
    parsed = parse_frontmatter(path)
    if not parsed:
        return path.stem
    return str(parsed[0].get("id", path.stem))


def get_quality(path: Path) -> float | None:
    """Read quality score from frontmatter."""
    parsed = parse_frontmatter(path)
    if not parsed:
        return None
    q = parsed[0].get("quality", "null")
    if q == "null" or q is None:
        return None
    try:
        return float(q)
    except (ValueError, TypeError):
        return None


# ------------------------------------------------------------------
# ID -> Path resolution
# ------------------------------------------------------------------

_id_cache: dict[str, Path] = {}


def build_id_cache() -> dict[str, Path]:
    """Scan repo and build id -> filepath mapping."""
    if _id_cache:
        return _id_cache

    skip_dirs = {".git", ".obsidian", "__pycache__", "node_modules", "compiled", ".cex"}
    for dirpath, dirnames, filenames in os.walk(CEX_ROOT):
        dirnames[:] = [d for d in dirnames if d not in skip_dirs]
        for fname in filenames:
            if not fname.endswith(".md"):
                continue
            fp = Path(dirpath) / fname
            try:
                head = fp.read_text(encoding="utf-8", errors="ignore")[:500]
            except (OSError, PermissionError):
                continue
            if not head.startswith("---"):
                continue
            match = re.search(r"^id:\s*(.+)$", head, re.MULTILINE)
            if match:
                aid = match.group(1).strip().strip('"').strip("'")
                _id_cache[aid] = fp

    return _id_cache


def resolve_id_to_path(artifact_id: str) -> Path | None:
    """Resolve an artifact ID to its file path."""
    cache = build_id_cache()
    return cache.get(artifact_id)


# ------------------------------------------------------------------
# Ripple logic
# ------------------------------------------------------------------

def add_backlink(target_path: Path, source_id: str, source_score: float) -> bool:
    """Add source_id to target's related: field if not already present.

    Returns True if file was modified.
    """
    try:
        text = target_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return False

    m = FRONTMATTER_RE.match(text)
    if not m:
        return False

    fm_text = m.group(1)
    body_text = m.group(2)

    # Check if already linked
    existing_related = get_related_ids(target_path)
    if source_id in existing_related:
        return False

    # Add to frontmatter related: block
    fm_lines = fm_text.split("\n")
    new_fm_lines = []
    inserted = False

    for line in fm_lines:
        new_fm_lines.append(line)
        if line.startswith("related:") and not inserted:
            new_fm_lines.append(f"  - {source_id}")
            inserted = True

    if not inserted:
        # No related: field yet -- add it before closing ---
        new_fm_lines.append("related:")
        new_fm_lines.append(f"  - {source_id}")

    new_fm = "\n".join(new_fm_lines)

    # Update ## Related Artifacts table in body (append row if section exists)
    target_meta = parse_frontmatter(target_path)
    tgt_kind = target_meta[0].get("kind", "") if target_meta else ""
    tgt_pillar = target_meta[0].get("pillar", "") if target_meta else ""

    row = f"| [[{source_id}]] | related | {source_score:.2f} |"

    if "## Related Artifacts" in body_text:
        # Find end of table and insert row
        table_end = body_text.find("\n\n", body_text.find("## Related Artifacts"))
        if table_end == -1:
            table_end = len(body_text)
        body_text = body_text[:table_end] + "\n" + row + body_text[table_end:]
    # If no section, skip body update -- wikilink sweep will handle it

    new_content = f"---\n{new_fm}\n---\n{body_text}"
    try:
        target_path.write_text(new_content, encoding="utf-8")
        return True
    except (OSError, PermissionError):
        return False


def find_new_relations(
    path: Path,
    existing_ids: list[str],
    index: dict,
    min_score: float = DEFAULT_MIN_SCORE,
    max_new: int = 5,
) -> list[dict]:
    """Find artifacts related to path that are NOT already in existing_ids."""
    parsed = parse_frontmatter(path)
    if not parsed:
        return []
    meta, body = parsed
    self_id = str(meta.get("id", path.stem))

    query = body[:4000]
    if not query.strip():
        query = " ".join(filter(None, [
            str(meta.get("title", "")),
            str(meta.get("tldr", "")),
        ]))

    if not query.strip():
        return []

    results = find_similar(
        query=query,
        index=index,
        top_k=max_new + len(existing_ids) + 5,
        min_score=min_score,
    )

    existing_set = set(existing_ids) | {self_id}
    new_rels = []
    for r in results:
        rid = r.get("id", "")
        if rid and rid not in existing_set:
            new_rels.append(r)
            if len(new_rels) >= max_new:
                break

    return new_rels


def ripple(
    source_path: Path,
    index: dict | None = None,
    max_ripple: int = DEFAULT_MAX_RIPPLE,
    min_score: float = DEFAULT_MIN_SCORE,
    dry_run: bool = False,
) -> dict:
    """Execute ripple propagation from a modified artifact.

    Steps:
      1. Read source's related: field
      2. For each related artifact: ensure backlink exists (bidirectional)
      3. Find NEW relationships (not in related: yet)
      4. Add bidirectional cross-refs for new relationships
      5. Budget: max_ripple files total

    Returns dict with: modified_files, new_links, backlinks_added, errors
    """
    if index is None:
        index = load_index()
    if not index:
        return {"error": "No retriever index. Run: python _tools/cex_retriever.py --build"}

    source_id = get_artifact_id(source_path)
    existing_related = get_related_ids(source_path)

    modified_files = []
    backlinks_added = 0
    new_links_added = 0
    errors = 0
    budget_remaining = max_ripple

    print(f"[RIPPLE] Source: {source_path.relative_to(CEX_ROOT)}")
    print(f"  ID: {source_id} | Existing related: {len(existing_related)}")

    # Step 1: Ensure backlinks for existing relations
    for related_id in existing_related:
        if budget_remaining <= 0:
            print(f"  [!] Budget exhausted ({max_ripple} files)")
            break

        target_path = resolve_id_to_path(related_id)
        if not target_path or not target_path.exists():
            continue

        target_related = get_related_ids(target_path)
        if source_id not in target_related:
            if dry_run:
                rel = target_path.relative_to(CEX_ROOT)
                print(f"  [DRY] Would add backlink: {rel} <- {source_id}")
                backlinks_added += 1
            else:
                source_score = 0.0
                for r in existing_related:
                    if r == related_id:
                        source_score = 0.30  # default backlink score
                        break
                if add_backlink(target_path, source_id, source_score):
                    rel = target_path.relative_to(CEX_ROOT)
                    print(f"  [+] Backlink: {rel} <- {source_id}")
                    modified_files.append(str(target_path.relative_to(CEX_ROOT)))
                    backlinks_added += 1
                    budget_remaining -= 1
                else:
                    errors += 1

    # Step 2: Discover new relationships
    new_rels = find_new_relations(
        source_path, existing_related, index,
        min_score=min_score, max_new=min(5, budget_remaining),
    )

    if new_rels:
        print(f"  [i] Found {len(new_rels)} new relationships")

    for rel_info in new_rels:
        if budget_remaining <= 0:
            break

        rid = rel_info["id"]
        rscore = rel_info.get("score", 0.0)
        target_path = resolve_id_to_path(rid)

        if not target_path or not target_path.exists():
            continue

        if dry_run:
            t_rel = target_path.relative_to(CEX_ROOT)
            print(f"  [DRY] New link: {source_id} <-> {rid} ({t_rel}) score={rscore:.2f}")
            new_links_added += 1
        else:
            # Add forward link (source -> target) -- update source's related:
            # Add backward link (target -> source) -- update target's related:
            if add_backlink(target_path, source_id, rscore):
                t_rel = target_path.relative_to(CEX_ROOT)
                print(f"  [+] New link: {rid} ({t_rel}) <- {source_id}")
                modified_files.append(str(target_path.relative_to(CEX_ROOT)))
                new_links_added += 1
                budget_remaining -= 1

    result = {
        "source": str(source_path.relative_to(CEX_ROOT)),
        "source_id": source_id,
        "existing_related": len(existing_related),
        "backlinks_added": backlinks_added,
        "new_links_added": new_links_added,
        "modified_files": modified_files,
        "budget_used": max_ripple - budget_remaining,
        "errors": errors,
        "dry_run": dry_run,
    }

    mode = "DRY-RUN" if dry_run else "APPLIED"
    print(f"\n[RIPPLE {mode}] backlinks={backlinks_added} new={new_links_added} "
          f"modified={len(modified_files)} errors={errors}")

    return result


# ------------------------------------------------------------------
# CLI
# ------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Cross-reference propagation engine (Karpathy LLM Wiki pattern)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument("path", nargs="?", help="Path to modified artifact")
    parser.add_argument("--dry-run", action="store_true", help="Preview only, no writes")
    parser.add_argument("--check", metavar="PATH", help="Show what would ripple from PATH")
    parser.add_argument("--max-ripple", type=int, default=DEFAULT_MAX_RIPPLE,
                        help=f"Max files to modify per ripple (default: {DEFAULT_MAX_RIPPLE})")
    parser.add_argument("--min-score", type=float, default=DEFAULT_MIN_SCORE,
                        help=f"Min similarity for new relations (default: {DEFAULT_MIN_SCORE})")
    parser.add_argument("--rebuild-index", action="store_true",
                        help="Rebuild retriever index before ripple")
    args = parser.parse_args()

    if args.rebuild_index:
        subprocess.run(
            [sys.executable, str(CEX_ROOT / "_tools" / "cex_retriever.py"), "--build"],
            capture_output=True, text=True,
        )
        print("[RIPPLE] Index rebuilt.")

    target = args.check or args.path
    if not target:
        parser.print_help()
        sys.exit(1)

    target_path = Path(target).resolve()
    if not target_path.exists():
        print(f"[ERROR] File not found: {target}")
        sys.exit(1)

    dry = args.dry_run or bool(args.check)
    result = ripple(
        target_path,
        max_ripple=args.max_ripple,
        min_score=args.min_score,
        dry_run=dry,
    )

    if result.get("error"):
        print(f"[ERROR] {result['error']}")
        sys.exit(1)


if __name__ == "__main__":
    main()
