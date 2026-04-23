#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
CEX KC Indexer -- Embed all Knowledge Cards into Supabase pgvector.

Reads all KCs from filesystem, generates embeddings via OpenAI,
and upserts into kc_embeddings table. Skips unchanged files (by content hash).

Usage:
    python _tools/cex_kc_index.py                  # index all KCs
    python _tools/cex_kc_index.py --dry-run         # show what would be indexed
    python _tools/cex_kc_index.py --force            # re-index everything
    python _tools/cex_kc_index.py --stats            # show index stats
"""

import hashlib
import json
import os
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

# -- Load .env --------------------------------------------------------------
# Keys that should NOT be loaded into os.environ because they override
# Claude CLI subscription auth with API billing (which may have no credits).
_ENV_BLOCKLIST = {"ANTHROPIC_API_KEY", "CLAUDE_API_KEY"}

def _load_env():
    """Load .env file into os.environ (excluding blocklisted keys)."""
    env_path = ROOT / ".env"
    if env_path.exists():
        for line in env_path.read_text(encoding="utf-8").splitlines():
            line = line.strip()
            if not line or line.startswith("#") or "=" not in line:
                continue
            key, _, value = line.partition("=")
            key = key.strip()
            if key in _ENV_BLOCKLIST:
                continue
            os.environ.setdefault(key, value.strip())

_load_env()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY", "")
SUPABASE_URL = os.environ.get("SUPABASE_URL", "")
SUPABASE_KEY = os.environ.get("SUPABASE_SERVICE_ROLE_KEY", "")

EMBEDDING_MODEL = "text-embedding-3-small"  # 1536 dimensions, $0.02/1M tokens


# -- Embedding --------------------------------------------------------------

def get_embedding(text: str) -> list[float]:
    """Get embedding vector via cex_sdk OpenAIEmbedder."""
    from cex_sdk.knowledge.embedder.openai_embedder import OpenAIEmbedder
    embedder = OpenAIEmbedder(model=EMBEDDING_MODEL, api_key=OPENAI_API_KEY)
    # Truncate to ~8000 tokens (~32K chars) to stay within model limits
    text = text[:32000]
    return embedder.embed(text)


def get_embeddings_batch(texts: list[str], batch_size: int = 50) -> list[list[float]]:
    """Get embeddings for multiple texts in batches."""
    import openai
    client = openai.OpenAI(api_key=OPENAI_API_KEY)
    all_embeddings = []

    for i in range(0, len(texts), batch_size):
        batch = [t[:32000] for t in texts[i:i + batch_size]]
        response = client.embeddings.create(
            model=EMBEDDING_MODEL,
            input=batch,
        )
        all_embeddings.extend([d.embedding for d in response.data])
        if len(texts) > batch_size:
            print(f"  Embedded {min(i + batch_size, len(texts))}/{len(texts)}")

    return all_embeddings


# -- Supabase ---------------------------------------------------------------

def get_supabase():
    """Get Supabase client."""
    from supabase import create_client
    return create_client(SUPABASE_URL, SUPABASE_KEY)


def get_indexed_hashes(client) -> dict[str, str]:
    """Get {id: content_hash} for all indexed KCs."""
    try:
        result = client.table("kc_embeddings").select("id,content_hash").execute()
        return {row["id"]: row["content_hash"] for row in result.data}
    except Exception:
        return {}


# -- KC Discovery -----------------------------------------------------------

def _parse_frontmatter(content: str) -> dict:
    """Extract YAML frontmatter as dict."""
    fm_match = re.match(r"^---\n(.*?)\n---", content, re.DOTALL)
    if not fm_match:
        return {}
    try:
        import yaml
        return yaml.safe_load(fm_match.group(1)) or {}
    except Exception:
        # Fallback: regex parsing
        fm = {}
        for m in re.finditer(r"^(\w+):\s*(.+)$", fm_match.group(1), re.MULTILINE):
            fm[m.group(1)] = m.group(2).strip().strip('"\'')
        return fm


def _parse_tags(raw) -> list[str]:
    """Parse tags from various formats."""
    if isinstance(raw, list):
        return [str(t).strip() for t in raw]
    if isinstance(raw, str):
        # "[tag1, tag2]" or "tag1, tag2"
        cleaned = raw.strip("[]")
        return [t.strip().strip('"\'') for t in cleaned.split(",") if t.strip()]
    return []


def _content_hash(content: str) -> str:
    """SHA256 hash of content."""
    return hashlib.sha256(content.encode("utf-8")).hexdigest()[:16]


def discover_kcs() -> list[dict]:
    """Find all Knowledge Cards in the project."""
    kcs = []

    # Search in nucleus dirs + P01_knowledge
    search_dirs = [d for d in ROOT.iterdir() if d.is_dir() and (
        d.name.startswith("N0") or d.name.startswith("P01")
    )]

    for search_dir in search_dirs:
        for md_path in search_dir.rglob("*.md"):
            if "compiled" in str(md_path):
                continue
            try:
                content = md_path.read_text(encoding="utf-8")
                fm = _parse_frontmatter(content)
                if not fm.get("id"):
                    continue

                # Build embedding text: combine key fields for rich semantic search
                embed_text = "\n".join(filter(None, [
                    fm.get("title", ""),
                    fm.get("tldr", ""),
                    fm.get("domain", ""),
                    " ".join(_parse_tags(fm.get("tags", []))),
                    " ".join(_parse_tags(fm.get("keywords", []))),
                    # Include body (truncated) for semantic richness
                    content[content.find("---", 3) + 3:][:4000] if "---" in content[3:] else "",
                ]))

                kcs.append({
                    "id": str(fm["id"]),
                    "kind": str(fm.get("kind", "unknown")),
                    "pillar": str(fm.get("pillar", "")),
                    "domain": str(fm.get("domain", "")),
                    "title": str(fm.get("title", ""))[:200],
                    "tldr": str(fm.get("tldr", ""))[:300],
                    "tags": _parse_tags(fm.get("tags", [])),
                    "feeds_kinds": _parse_tags(fm.get("feeds_kinds", [])),
                    "file_path": str(md_path.relative_to(ROOT)),
                    "content_hash": _content_hash(content),
                    "embed_text": embed_text,
                })
            except Exception as e:
                print(f"  SKIP {md_path.name}: {e}")

    return kcs


# -- Index ------------------------------------------------------------------

def index_kcs(force: bool = False, dry_run: bool = False) -> dict:
    """Index all KCs into Supabase pgvector. Returns stats."""
    print("=" * 60)
    print("  CEX KC INDEXER -> Supabase pgvector")
    print("=" * 60)

    # Discover
    kcs = discover_kcs()
    print(f"\n  Found {len(kcs)} Knowledge Cards")

    if not kcs:
        return {"total": 0, "indexed": 0, "skipped": 0, "errors": 0}

    # Check what's already indexed
    if not dry_run:
        client = get_supabase()
        existing = get_indexed_hashes(client) if not force else {}
    else:
        existing = {}

    # Filter to only new/changed KCs
    to_index = []
    skipped = 0
    for kc in kcs:
        if kc["id"] in existing and existing[kc["id"]] == kc["content_hash"]:
            skipped += 1
            continue
        to_index.append(kc)

    print(f"  To index: {len(to_index)} (skipping {skipped} unchanged)")

    if dry_run:
        for kc in to_index[:10]:
            print(f"    + {kc['id']}: {kc['title'][:50]}")
        if len(to_index) > 10:
            print(f"    ... +{len(to_index) - 10} more")
        return {"total": len(kcs), "indexed": 0, "skipped": skipped, "errors": 0, "dry_run": True}

    if not to_index:
        print("  Nothing to index. All up to date.")
        return {"total": len(kcs), "indexed": 0, "skipped": skipped, "errors": 0}

    # Generate embeddings
    print(f"\n  Generating embeddings ({EMBEDDING_MODEL})...")
    texts = [kc["embed_text"] for kc in to_index]
    try:
        embeddings = get_embeddings_batch(texts)
    except Exception as e:
        print(f"  ERROR: Embedding failed: {e}")
        return {"total": len(kcs), "indexed": 0, "skipped": skipped, "errors": len(to_index)}

    # Estimate cost
    total_chars = sum(len(t) for t in texts)
    est_tokens = total_chars // 4
    est_cost = est_tokens * 0.02 / 1_000_000
    print(f"  Embedded {len(embeddings)} KCs (~{est_tokens:,} tokens, ~${est_cost:.4f})")

    # Upsert to Supabase
    print("\n  Upserting to Supabase...")
    errors = 0
    indexed = 0

    for kc, embedding in zip(to_index, embeddings):
        try:
            row = {
                "id": kc["id"],
                "kind": kc["kind"],
                "pillar": kc["pillar"],
                "domain": kc["domain"],
                "title": kc["title"],
                "tldr": kc["tldr"],
                "tags": kc["tags"],
                "feeds_kinds": kc["feeds_kinds"],
                "file_path": kc["file_path"],
                "content_hash": kc["content_hash"],
                "embedding": embedding,
            }
            client.table("kc_embeddings").upsert(row).execute()
            indexed += 1
        except Exception as e:
            print(f"  ERROR {kc['id']}: {e}")
            errors += 1

    print(f"\n  OK Indexed: {indexed} | Skipped: {skipped} | Errors: {errors}")

    stats = {"total": len(kcs), "indexed": indexed, "skipped": skipped, "errors": errors}
    return stats


# -- Search (used by crew_runner) -------------------------------------------

def search_kcs_by_text(query: str, top_k: int = 5, filter_kind: str = None) -> list[dict]:
    """Search KCs by semantic similarity. Returns list of matches with file_path + similarity."""
    embedding = get_embedding(query)
    client = get_supabase()

    params = {
        "query_embedding": embedding,
        "match_count": top_k,
    }
    if filter_kind:
        params["filter_kind"] = filter_kind

    try:
        result = client.rpc("search_kcs", params).execute()
        return result.data or []
    except Exception as e:
        print(f"[KC Search] Error: {e}", file=sys.stderr)
        return []


def search_kcs_by_kind(kind: str, top_k: int = 5) -> list[dict]:
    """Find KCs that feed a specific kind (via feeds_kinds field)."""
    client = get_supabase()
    try:
        result = (
            client.table("kc_embeddings")
            .select("id,kind,domain,title,tldr,file_path")
            .contains("feeds_kinds", [kind])
            .limit(top_k)
            .execute()
        )
        return result.data or []
    except Exception as e:
        print(f"[KC Search by kind] Error: {e}", file=sys.stderr)
        return []


# -- CLI --------------------------------------------------------------------

def main():
    import argparse
    parser = argparse.ArgumentParser(description="CEX KC Indexer -> Supabase pgvector")
    parser.add_argument("--dry-run", action="store_true", help="Show what would be indexed")
    parser.add_argument("--force", action="store_true", help="Re-index everything")
    parser.add_argument("--stats", action="store_true", help="Show index stats")
    parser.add_argument("--search", type=str, help="Test search query")
    parser.add_argument("--top-k", type=int, default=5, help="Number of results")
    args = parser.parse_args()

    if args.search:
        results = search_kcs_by_text(args.search, top_k=args.top_k)
        print(f"\nSearch: '{args.search}' -> {len(results)} results\n")
        for r in results:
            print(f"  {r['similarity']:.3f} | {r['kind']:<20} | {r['title'][:50]}")
            print(f"         {r['file_path']}")
        return

    if args.stats:
        client = get_supabase()
        try:
            result = client.table("kc_embeddings").select("id,kind", count="exact").execute()
            print(f"\nIndexed KCs: {result.count}")
            kinds = {}
            for r in result.data:
                kinds[r["kind"]] = kinds.get(r["kind"], 0) + 1
            for k, v in sorted(kinds.items(), key=lambda x: -x[1]):
                print(f"  {k}: {v}")
        except Exception as e:
            print(f"Error: {e}")
        return

    stats = index_kcs(force=args.force, dry_run=args.dry_run)
    print(f"\nDone. {json.dumps(stats)}")


if __name__ == "__main__":
    main()
