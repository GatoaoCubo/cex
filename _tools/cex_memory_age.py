#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Memory Aging -- human-readable freshness + staleness caveats.

Pattern: OpenClaude memdir/memoryAge.ts
Adapted for CEX builder memory recall.

Key insight from OpenClaude: "Models are poor at date arithmetic --
a raw ISO timestamp doesn't trigger staleness reasoning the way
'47 days ago' does."

Usage:
    from cex_memory_age import memory_age_label, memory_freshness_caveat
    
    label = memory_age_label(mtime)           # "47 days ago"
    caveat = memory_freshness_caveat(mtime)   # "[WARN] This memory is..."
"""

import time


def memory_age_days(mtime: float) -> int:
    """Days elapsed since mtime. Floor-rounded. 0 = today.
    
    Negative inputs (future mtime, clock skew) clamp to 0.
    """
    return max(0, int((time.time() - mtime) / 86400))


def memory_age_label(mtime: float) -> str:
    """Human-readable age: 'today', 'yesterday', '47 days ago'.
    
    Models understand relative time better than ISO timestamps.
    """
    days = memory_age_days(mtime)
    if days == 0:
        return "today"
    if days == 1:
        return "yesterday"
    return f"{days} days ago"


def memory_freshness_caveat(mtime: float) -> str:
    """Staleness warning for memories >1 day old. Empty string for fresh.
    
    Motivated by user reports of stale code-state memories being asserted
    as fact -- the citation makes stale claims sound authoritative, not less.
    
    Returns empty string for today/yesterday (warning = noise for fresh).
    """
    days = memory_age_days(mtime)
    if days <= 1:
        return ""
    return (
        f"[STALE] This memory is {days} days old. "
        "It is a point-in-time observation, not live state. "
        "Claims about file paths, function names, or code behavior "
        "may be outdated. Verify against current code before asserting as fact."
    )


def memory_freshness_tag(mtime: float) -> str:
    """Short tag for manifest display: 'fresh', 'recent', 'stale'."""
    days = memory_age_days(mtime)
    if days <= 1:
        return "fresh"
    if days <= 7:
        return "recent"
    if days <= 30:
        return "aging"
    return "stale"


def format_memory_manifest(memories: list[dict]) -> str:
    """Format memory headers as a selectable manifest for LLM recall.
    
    Each entry: - [type] filename (age): description
    
    This format is designed to be parsed by an LLM selector
    that picks top-K relevant memories for the current task.
    
    Args:
        memories: List of dicts with keys:
            filename, type (optional), mtime, description (optional)
    
    Returns:
        Formatted manifest string, one line per memory.
    """
    lines = []
    for m in memories:
        tag = f"[{m['type']}] " if m.get("type") else ""
        age = memory_age_label(m.get("mtime", 0))
        freshness = memory_freshness_tag(m.get("mtime", 0))
        desc = m.get("description", "")
        
        line = f"- {tag}{m['filename']} ({age}, {freshness})"
        if desc:
            line += f": {desc}"
        lines.append(line)
    
    return "\n".join(lines)


def format_recalled_memory(content: str, mtime: float, filename: str = "") -> str:
    """Format a recalled memory with freshness context.
    
    For memories >1 day old, prepend staleness caveat.
    For all memories, add the age label.
    """
    header = f"## Memory: {filename}" if filename else "## Recalled Memory"
    age = memory_age_label(mtime)
    caveat = memory_freshness_caveat(mtime)
    
    parts = [f"{header} (last updated: {age})"]
    if caveat:
        parts.append(f"\n> {caveat}\n")  # noqa: RUF001
    parts.append(content)
    
    return "\n".join(parts)


if __name__ == "__main__":
    # Quick demo
    pass
    
    print("=== Memory Age Demo ===\n")
    
    now = time.time()
    test_times = [
        ("Just now", now),
        ("Yesterday", now - 86400),
        ("3 days ago", now - 86400 * 3),
        ("2 weeks ago", now - 86400 * 14),
        ("2 months ago", now - 86400 * 60),
    ]
    
    for label, mtime in test_times:
        age = memory_age_label(mtime)
        tag = memory_freshness_tag(mtime)
        caveat = memory_freshness_caveat(mtime)
        print(f"  {label:15s} -> age='{age}', tag={tag}")
        if caveat:
            print(f"                   caveat: {caveat[:60]}...")
    
    print("\n=== Manifest Demo ===\n")
    demo_memories = [
        {"filename": "user_prefs.md", "type": "user", "mtime": now - 3600, "description": "Prefers concise output"},
        {"filename": "api_gotcha.md", "type": "feedback", "mtime": now - 86400 * 5, "description": "API returns 500 on empty body"},
        {"filename": "sprint_goal.md", "type": "project", "mtime": now - 86400 * 30, "description": "Q2 sprint: auth rewrite"},
        {"filename": "linear_board.md", "type": "reference", "mtime": now - 86400 * 2, "description": "Bug tracker in Linear/INGEST"},
    ]
    print(format_memory_manifest(demo_memories))
