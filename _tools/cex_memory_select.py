#!/usr/bin/env python3
"""CEX Memory Selector — LLM-powered relevant memory retrieval.

Selects top-K most relevant builder memories for a given query using
an LLM (sonnet) as selector. Falls back to keyword matching when LLM
is unavailable.

Inspired by Claude Code's SELECT_MEMORIES_SYSTEM_PROMPT pattern.

Usage:
    python cex_memory_select.py --query "create agent for sales" --builder agent-builder
    python cex_memory_select.py --query "improve quality gates" --all --top-k 5
"""

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
import time
from dataclasses import dataclass, field
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

sys.path.insert(0, str(Path(__file__).resolve().parent))
from cex_memory import MemoryHeader, scan_all_memories, scan_builder_memories
from cex_shared import parse_frontmatter

# --- T06: Memory age integration ---
try:
    from cex_memory_age import memory_age_days, memory_freshness_caveat, format_recalled_memory
    _HAS_MEMORY_AGE = True
except ImportError:
    _HAS_MEMORY_AGE = False

CEX_ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = CEX_ROOT / ".cex" / "temp" / "memory_cache"
CACHE_TTL_SECONDS = 300  # 5 minutes

# LLM selector model — sonnet is sufficient, 4x cheaper than opus
LLM_MODEL = "claude-sonnet-4-6"
LLM_MAX_TOKENS = 1024


# ---------------------------------------------------------------------------
# Data Types
# ---------------------------------------------------------------------------


@dataclass
class SelectedMemory:
    """A memory selected as relevant, with full content loaded."""

    path: str
    content: str
    type: str
    confidence: float
    builder_id: str


# ---------------------------------------------------------------------------
# Cache
# ---------------------------------------------------------------------------


def _cache_key(query: str, builder_id: str | None) -> str:
    """Generate cache key from query + builder scope."""
    raw = f"{query}::{builder_id or 'all'}"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


def _read_cache(key: str) -> list[dict] | None:
    """Read cached selection result if still fresh."""
    cache_file = CACHE_DIR / f"{key}.json"
    if not cache_file.exists():
        return None
    try:
        data = json.loads(cache_file.read_text(encoding="utf-8"))
        if time.time() - data.get("timestamp", 0) < CACHE_TTL_SECONDS:
            return data.get("selections")
    except (json.JSONDecodeError, OSError):
        pass
    return None


def _write_cache(key: str, selections: list[dict]):
    """Write selection result to cache."""
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    data = {"timestamp": time.time(), "selections": selections}
    try:
        (CACHE_DIR / f"{key}.json").write_text(
            json.dumps(data, ensure_ascii=False), encoding="utf-8"
        )
    except OSError:
        pass


# ---------------------------------------------------------------------------
# LLM Selector
# ---------------------------------------------------------------------------


SELECT_PROMPT_TEMPLATE = """You are a memory selector for a software build system.
Given a user query and a list of builder memories (observations from past builds),
select up to {top_k} memories that are CLEARLY useful for this query.

Rules:
- Only select memories that are directly relevant to the query
- If unsure, do NOT include the memory
- Return an empty list if no memories apply
- Return ONLY a JSON array of indices (0-based) of selected memories

## User Query
{query}

## Available Memories
{memories_block}

## Response
Return a JSON array of selected indices. Example: [0, 3, 7]
If none are relevant, return: []
"""


def _format_memories_block(headers: list[MemoryHeader]) -> str:
    """Format memory headers for LLM prompt."""
    lines = []
    for i, h in enumerate(headers):
        lines.append(
            f"[{i}] builder={h.builder_id} type={h.type} "
            f"conf={h.confidence:.2f} outcome={h.outcome}\n"
            f"    {h.observation_preview}"
        )
    return "\n".join(lines)


def _select_via_llm(
    query: str, headers: list[MemoryHeader], top_k: int = 5
) -> list[int]:
    """Use LLM (sonnet) to select relevant memory indices."""
    prompt = SELECT_PROMPT_TEMPLATE.format(
        top_k=top_k,
        query=query,
        memories_block=_format_memories_block(headers),
    )

    try:
        import subprocess
        result = subprocess.run(
            ["claude", "-p", "--model", LLM_MODEL, "--no-chrome"],
            input=prompt, capture_output=True, text=True,
            timeout=30, encoding="utf-8",
        )
        if result.returncode == 0:
            text = result.stdout.strip()
            # Parse JSON array from response
            match = re.search(r"\[[\d\s,]*\]", text)
            if match:
                indices = json.loads(match.group(0))
                valid = [i for i in indices if isinstance(i, int) and 0 <= i < len(headers)]
                return valid[:top_k]
    except FileNotFoundError:
        pass  # claude CLI not available, fall through to keyword
    except Exception as e:
        print(f"WARN: LLM selector failed: {e}. Falling back to keyword.", file=sys.stderr)

    return []  # Empty = trigger fallback


# ---------------------------------------------------------------------------
# Keyword Fallback Selector
# ---------------------------------------------------------------------------


def _select_via_keywords(
    query: str, headers: list[MemoryHeader], top_k: int = 5
) -> list[int]:
    """Fallback: select memories by keyword overlap with query."""
    query_words = set(re.findall(r"\w{3,}", query.lower()))
    if not query_words:
        return []

    scored = []
    for i, h in enumerate(headers):
        text = f"{h.observation_preview} {h.type} {h.builder_id}".lower()
        mem_words = set(re.findall(r"\w{3,}", text))
        overlap = len(query_words & mem_words)
        if overlap > 0:
            # Score = overlap count * confidence
            score = overlap * h.confidence
            # --- T06: Age penalty (D3: linear decay over 1yr) ---
            if _HAS_MEMORY_AGE and hasattr(h, "path") and h.path:
                try:
                    age = memory_age_days(os.path.getmtime(h.path))
                    age_penalty = max(0.5, 1.0 - (age / 365))
                    score *= age_penalty
                except Exception:
                    pass
            scored.append((i, score))

    scored.sort(key=lambda x: -x[1])
    return [i for i, _ in scored[:top_k]]


# ---------------------------------------------------------------------------
# Main Selection Function
# ---------------------------------------------------------------------------


def select_relevant_memories(
    query: str,
    memories: list[MemoryHeader] | None = None,
    builder_id: str | None = None,
    top_k: int = 5,
    use_cache: bool = True,
) -> list[SelectedMemory]:
    """Select top-K relevant memories for a query using LLM + fallback.

    Args:
        query: Natural language query/intent.
        memories: Pre-scanned memory headers. If None, scans automatically.
        builder_id: If set, only scan this builder's memories.
        top_k: Maximum memories to return.
        use_cache: Whether to use result caching (5min TTL).

    Returns:
        List of SelectedMemory with full content loaded.
    """
    # Check cache
    cache_key = _cache_key(query, builder_id)
    if use_cache:
        cached = _read_cache(cache_key)
        if cached is not None:
            return [SelectedMemory(**c) for c in cached]

    # Scan memories if not provided
    if memories is None:
        if builder_id:
            memories = scan_builder_memories(builder_id)
        else:
            memories = scan_all_memories()

    if not memories:
        return []

    # Try LLM selector first
    selected_indices = _select_via_llm(query, memories, top_k)

    # Fallback to keyword if LLM returned nothing
    if not selected_indices:
        selected_indices = _select_via_keywords(query, memories, top_k)

    if not selected_indices:
        return []

    # Load full content for selected memories
    results = []
    for idx in selected_indices:
        h = memories[idx]
        full_path = CEX_ROOT / h.path
        content = ""
        try:
            if full_path.exists():
                content = full_path.read_text(encoding="utf-8")
        except (OSError, UnicodeDecodeError):
            content = h.observation_preview  # Fallback to preview

        results.append(SelectedMemory(
            path=h.path,
            content=content,
            type=h.type,
            confidence=h.confidence,
            builder_id=h.builder_id,
        ))

    # Cache results
    if use_cache:
        cache_data = [
            {"path": m.path, "content": m.content, "type": m.type,
             "confidence": m.confidence, "builder_id": m.builder_id}
            for m in results
        ]
        _write_cache(cache_key, cache_data)

    return results


# ---------------------------------------------------------------------------
# Format for Prompt Injection
# ---------------------------------------------------------------------------


def format_memory_injection(memories: list[SelectedMemory], total_observations: int = 0) -> str:
    """Format selected memories as a prompt section for builder injection.

    Returns a markdown block ready to inject into builder context.
    """
    if not memories:
        return ""

    lines = [f"## Builder Memory (top-{len(memories)} relevant from {total_observations} observations)"]
    for i, m in enumerate(memories, 1):
        # Extract observation preview from frontmatter
        fm = parse_frontmatter(m.content) if m.content.startswith("---") else None
        obs = ""
        if fm:
            obs = fm.get("observation", "")[:80]
        if not obs:
            obs = m.content[:80] if m.content else "(empty)"
        outcome = fm.get("outcome", "UNKNOWN") if fm else "UNKNOWN"
        lines.append(
            f"{i}. [type={m.type}, conf={m.confidence:.2f}] {obs} ({outcome})"
        )
    lines.append("")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------


def main():
    parser = argparse.ArgumentParser(description="CEX Memory Selector — LLM-powered retrieval")
    parser.add_argument("--query", "-q", required=True, help="Query/intent to match memories against")
    parser.add_argument("--builder", "-b", help="Specific builder ID (default: search all)")
    parser.add_argument("--all", action="store_true", help="Search all builder memories")
    parser.add_argument("--top-k", type=int, default=5, help="Max memories to select (default: 5)")
    parser.add_argument("--no-cache", action="store_true", help="Bypass cache")
    parser.add_argument("--format", choices=["json", "inject", "text"], default="text",
                        help="Output format")
    args = parser.parse_args()

    builder_id = args.builder if not args.all else None

    results = select_relevant_memories(
        query=args.query,
        builder_id=builder_id,
        top_k=args.top_k,
        use_cache=not args.no_cache,
    )

    if args.format == "json":
        out = [{"path": m.path, "type": m.type, "confidence": m.confidence,
                "builder_id": m.builder_id} for m in results]
        print(json.dumps(out, ensure_ascii=False, indent=2))
    elif args.format == "inject":
        print(format_memory_injection(results))
    else:
        print(f"\n=== Memory Selection ({len(results)} selected) ===")
        for m in results:
            print(f"  [{m.type:10s} conf={m.confidence:.2f}] {m.path}")
        if not results:
            print("  (no relevant memories found)")


if __name__ == "__main__":
    main()
