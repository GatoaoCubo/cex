#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Prompt Cache v1.0 -- Pre-compiled builder ISO cache.

Problem: cex_skill_loader.py reads 13 ISO files from disk every time a builder
is invoked. For 124 builders x 12 ISOs = 1612 file reads per full grid pass.

Solution: compile all builder ISOs into a single cached JSON file per builder.
Invalidation: if any ISO's mtime > compiled_at, rebuild that builder's cache.

Usage:
    python _tools/cex_prompt_cache.py build          # compile all builders
    python _tools/cex_prompt_cache.py build agent     # compile one builder
    python _tools/cex_prompt_cache.py get agent       # load pre-compiled prompt
    python _tools/cex_prompt_cache.py stats           # cache hit rate, staleness
    python _tools/cex_prompt_cache.py invalidate      # remove stale entries
    python _tools/cex_prompt_cache.py clean           # wipe entire cache

Exit codes: 0 = success, 1 = error, 2 = stale cache detected
"""

import argparse
import hashlib
import json
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

sys.path.insert(0, str(Path(__file__).resolve().parent))

CEX_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = CEX_ROOT / ".cex" / "cache"
BUILDERS_DIR = CEX_ROOT / "archetypes" / "builders"


def _parse_frontmatter(raw):
    """Minimal frontmatter parser -- returns (dict, body_str)."""
    if not raw.startswith("---"):
        return {}, raw
    end = raw.find("---", 3)
    if end == -1:
        return {}, raw
    fm_str = raw[3:end].strip()
    body = raw[end + 3:].strip()
    try:
        import yaml
        fm = yaml.safe_load(fm_str) or {}
    except Exception:
        fm = {}
    return fm, body


def _iso_hash(paths):
    """SHA-256 of concatenated ISO file contents (sorted by name)."""
    h = hashlib.sha256()
    for p in sorted(paths, key=lambda x: x.name):
        try:
            h.update(p.read_bytes())
        except Exception:
            pass
    return h.hexdigest()


def _max_mtime(paths):
    """Latest mtime among a list of paths."""
    mtimes = []
    for p in paths:
        try:
            mtimes.append(p.stat().st_mtime)
        except Exception:
            pass
    return max(mtimes) if mtimes else 0.0


def list_builder_kinds() -> list[str]:
    """List all available builder kinds from archetypes/builders/."""
    if not BUILDERS_DIR.exists():
        return []
    kinds = []
    for d in sorted(BUILDERS_DIR.iterdir()):
        if d.is_dir() and d.name.endswith("-builder") and d.name != "_shared":
            kinds.append(d.name.replace("-builder", ""))
    return kinds


def compile_builder(kind: str) -> dict[str, Any] | None:
    """Compile all ISOs for a builder kind into a single cache entry.

    Returns the cache dict (also written to disk).
    """
    builder_dir = BUILDERS_DIR / f"{kind}-builder"
    if not builder_dir.exists():
        return None

    iso_files = sorted(builder_dir.glob("bld_*.md"))
    if not iso_files:
        return None

    # Also gather shared skills
    shared_dir = BUILDERS_DIR / "_shared"
    shared_files = sorted(shared_dir.glob("skill_*.md")) if shared_dir.exists() else []

    all_files = iso_files + shared_files
    source_hash = _iso_hash(all_files)

    # Check if cache is current
    cache_path = CACHE_DIR / f"builder_{kind}.json"
    if cache_path.exists():
        try:
            existing = json.loads(cache_path.read_text(encoding="utf-8"))
            if existing.get("source_hash") == source_hash:
                return existing  # cache hit -- no rebuild needed
        except Exception:
            pass

    # Build prompt sections from ISOs
    prompt_sections = {}
    total_bytes = 0

    for iso_path in iso_files:
        try:
            raw = iso_path.read_text(encoding="utf-8")
            fm, body = _parse_frontmatter(raw)
            # Derive section name from filename: bld_prompt_agent.md -> prompt
            stem = iso_path.stem  # bld_prompt_agent
            # Remove bld_ prefix and _kind suffix
            section = stem
            if section.startswith("bld_"):
                section = section[4:]
            if section.endswith(f"_{kind}"):
                section = section[: -len(f"_{kind}")]

            prompt_sections[section] = {
                "content": body,
                "frontmatter": fm,
                "source_file": iso_path.name,
                "bytes": len(body.encode("utf-8")),
            }
            total_bytes += len(body.encode("utf-8"))
        except Exception as e:
            prompt_sections[iso_path.stem] = {
                "content": "",
                "frontmatter": {},
                "source_file": iso_path.name,
                "bytes": 0,
                "error": str(e),
            }

    # Add shared skills
    for skill_path in shared_files:
        try:
            raw = skill_path.read_text(encoding="utf-8")
            fm, body = _parse_frontmatter(raw)
            section = f"shared_{skill_path.stem}"
            prompt_sections[section] = {
                "content": body,
                "frontmatter": fm,
                "source_file": skill_path.name,
                "bytes": len(body.encode("utf-8")),
            }
            total_bytes += len(body.encode("utf-8"))
        except Exception:
            pass

    # Estimate tokens (~4 chars per token)
    total_tokens = total_bytes // 4

    cache_entry = {
        "kind": kind,
        "compiled_at": datetime.now(timezone.utc).isoformat(),
        "source_hash": source_hash,
        "iso_count": len(iso_files),
        "shared_count": len(shared_files),
        "prompt_sections": prompt_sections,
        "total_tokens": total_tokens,
        "total_bytes": total_bytes,
    }

    # Write cache (default=str handles date/datetime from YAML frontmatter)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache_path.write_text(
        json.dumps(cache_entry, indent=2, ensure_ascii=True, default=str),
        encoding="utf-8",
    )

    return cache_entry


def get_cached(kind: str) -> dict[str, Any] | None:
    """Load pre-compiled builder prompt from cache.

    Returns cache dict or None if not cached / stale.
    """
    cache_path = CACHE_DIR / f"builder_{kind}.json"
    if not cache_path.exists():
        return None

    try:
        entry = json.loads(cache_path.read_text(encoding="utf-8"))
    except Exception:
        return None

    # Staleness check: compare source_hash with current files
    builder_dir = BUILDERS_DIR / f"{kind}-builder"
    if not builder_dir.exists():
        return None

    iso_files = sorted(builder_dir.glob("bld_*.md"))
    shared_dir = BUILDERS_DIR / "_shared"
    shared_files = sorted(shared_dir.glob("skill_*.md")) if shared_dir.exists() else []
    current_hash = _iso_hash(iso_files + shared_files)

    if entry.get("source_hash") != current_hash:
        return None  # stale

    return entry


def get_sections(kind: str, section_names: list[str] | None = None) -> dict[str, str]:
    """Get specific prompt sections from cache.

    Args:
        kind: builder kind name
        section_names: list of section names to retrieve, or None for all

    Returns dict of section_name -> content string.
    """
    entry = get_cached(kind)
    if entry is None:
        # Try compile on the fly
        entry = compile_builder(kind)
    if entry is None:
        return {}

    sections = entry.get("prompt_sections", {})
    if section_names is None:
        return {k: v["content"] for k, v in sections.items()}

    result = {}
    for name in section_names:
        if name in sections:
            result[name] = sections[name]["content"]
    return result


# =============================================================================
# CLI Commands
# =============================================================================

def cmd_build(args: argparse.Namespace) -> int:
    """Compile builder ISOs into cache."""
    if args.kind:
        kinds = [args.kind]
    else:
        kinds = list_builder_kinds()

    if not kinds:
        print("[FAIL] No builder kinds found")
        return 1

    built = 0
    skipped = 0
    errors = 0
    start = time.time()

    for kind in kinds:
        result = compile_builder(kind)
        if result is None:
            errors += 1
            print(f"  [FAIL] {kind}")
        elif result.get("_cached"):
            skipped += 1
        else:
            built += 1
            sections = len(result.get("prompt_sections", {}))
            total_kb = result.get("total_bytes", 0) / 1024
            print(f"  [OK] {kind:30s} {sections:>3} sections  {total_kb:>6.1f} KB")

    elapsed = time.time() - start
    print()
    print("=== Cache Build Complete ===")
    print(f"Built: {built} | Skipped (current): {skipped} | Errors: {errors}")
    print(f"Time: {elapsed:.1f}s")
    print(f"Cache dir: {CACHE_DIR}")
    return 0 if errors == 0 else 1


def cmd_get(args: argparse.Namespace) -> int:
    """Load and display a cached builder prompt."""
    entry = get_cached(args.kind)
    if entry is None:
        print(f"[WARN] No valid cache for '{args.kind}' -- compiling now...")
        entry = compile_builder(args.kind)
        if entry is None:
            print(f"[FAIL] Builder '{args.kind}' not found")
            return 1

    print(f"=== {args.kind}-builder (cached) ===")
    print(f"Compiled: {entry['compiled_at']}")
    print(f"ISOs: {entry['iso_count']} | Shared: {entry['shared_count']}")
    print(f"Total: {entry['total_bytes']:,} bytes (~{entry['total_tokens']:,} tokens)")
    print()

    sections = entry.get("prompt_sections", {})
    for name, data in sections.items():
        size = data.get("bytes", 0)
        src = data.get("source_file", "?")
        print(f"  {name:35s} {size:>6,} bytes  ({src})")

    return 0


def cmd_stats(args: argparse.Namespace) -> int:
    """Show cache statistics."""
    kinds = list_builder_kinds()
    total = len(kinds)
    cached = 0
    stale = 0
    missing = 0
    total_bytes = 0
    total_tokens = 0

    for kind in kinds:
        cache_path = CACHE_DIR / f"builder_{kind}.json"
        if not cache_path.exists():
            missing += 1
            continue

        entry = get_cached(kind)
        if entry is None:
            stale += 1
        else:
            cached += 1
            total_bytes += entry.get("total_bytes", 0)
            total_tokens += entry.get("total_tokens", 0)

    hit_rate = (cached / total * 100) if total > 0 else 0.0

    print("=== CEX Prompt Cache Stats ===")
    print(f"Builder kinds:   {total:>5}")
    print(f"Cached (fresh):  {cached:>5}")
    print(f"Stale:           {stale:>5}")
    print(f"Missing:         {missing:>5}")
    print(f"Hit rate:        {hit_rate:>5.1f}%")
    print(f"Total cached:    {total_bytes / 1024:>5.0f} KB (~{total_tokens:,} tokens)")
    print(f"Cache dir:       {CACHE_DIR}")
    return 0


def cmd_invalidate(args: argparse.Namespace) -> int:
    """Remove stale cache entries."""
    if not CACHE_DIR.exists():
        print("No cache directory.")
        return 0

    removed = 0
    for cache_file in sorted(CACHE_DIR.glob("builder_*.json")):
        kind = cache_file.stem.replace("builder_", "")
        entry = get_cached(kind)
        if entry is None:
            cache_file.unlink()
            removed += 1
            print(f"  [REMOVED] {kind} (stale)")

    print(f"\nInvalidated: {removed} stale entries")
    return 0


def cmd_clean(args: argparse.Namespace) -> int:
    """Wipe entire cache."""
    if not CACHE_DIR.exists():
        print("No cache directory.")
        return 0

    count = 0
    for f in CACHE_DIR.glob("builder_*.json"):
        f.unlink()
        count += 1

    print(f"Cleaned: {count} cache files removed")
    return 0


# =============================================================================
# CLI
# =============================================================================

def main() -> None:
    parser = argparse.ArgumentParser(
        description="CEX Prompt Cache v1.0 -- Pre-compiled builder ISO cache"
    )
    sub = parser.add_subparsers(dest="command")

    p_build = sub.add_parser("build", help="Compile builder ISOs into cache")
    p_build.add_argument("kind", nargs="?", help="Specific builder kind (default: all)")

    p_get = sub.add_parser("get", help="Load cached builder prompt")
    p_get.add_argument("kind", help="Builder kind name")

    sub.add_parser("stats", help="Cache statistics")
    sub.add_parser("invalidate", help="Remove stale cache entries")
    sub.add_parser("clean", help="Wipe entire cache")

    args = parser.parse_args()

    if not args.command:
        parser.print_help()
        sys.exit(0)

    dispatch = {
        "build": cmd_build,
        "get": cmd_get,
        "stats": cmd_stats,
        "invalidate": cmd_invalidate,
        "clean": cmd_clean,
    }

    handler = dispatch.get(args.command)
    if handler is None:
        parser.print_help()
        sys.exit(0)

    sys.exit(handler(args))


if __name__ == "__main__":
    main()
