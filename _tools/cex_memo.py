#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""CEX Result Memoization -- SHA256 prompt hash -> cached JSON response.

Cache location: .cex/cache/memo/
TTL: 24 hours (configurable via --ttl)
Key: SHA256(prompt_string)[:32]

Usage (import):
    from cex_memo import memo_get, memo_set, memo_wrap
    cached = memo_get(prompt)
    if cached:
        return cached["response"]
    response = call_llm(prompt)
    memo_set(prompt, response, model="qwen3:14b")

Usage (CLI):
    python _tools/cex_memo.py stats             # cache stats
    python _tools/cex_memo.py get <hash>         # lookup by hash
    python _tools/cex_memo.py clear              # purge expired
    python _tools/cex_memo.py clear --all        # purge everything
"""

import argparse
import hashlib
import json
import sys
import time
from pathlib import Path
from typing import Any, Callable

ROOT = Path(__file__).resolve().parent.parent
CACHE_DIR = ROOT / ".cex" / "cache" / "memo"
DEFAULT_TTL = 86400  # 24 hours in seconds


def _ensure_dir():
    CACHE_DIR.mkdir(parents=True, exist_ok=True)


def _hash_prompt(prompt):
    """SHA256 of prompt string, truncated to 32 hex chars."""
    return hashlib.sha256(prompt.encode("utf-8")).hexdigest()[:32]


def _cache_path(key):
    """Return Path for a cache key."""
    return CACHE_DIR / ("%s.json" % key)


def memo_get(prompt: str, ttl: int = DEFAULT_TTL) -> dict[str, Any] | None:
    """Look up cached response for a prompt.

    Args:
        prompt: The prompt string to look up.
        ttl: Time-to-live in seconds (default 24h). 0 = no expiry.

    Returns:
        dict with {response, model, timestamp, hash} or None if miss/expired.
    """
    key = _hash_prompt(prompt)
    path = _cache_path(key)

    if not path.exists():
        return None

    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (json.JSONDecodeError, OSError):
        return None

    # Check TTL
    if ttl > 0:
        age = time.time() - data.get("timestamp", 0)
        if age > ttl:
            return None

    return data


def memo_set(
    prompt: str,
    response: str,
    model: str = "unknown",
    metadata: dict[str, Any] | None = None,
) -> str:
    """Cache a prompt->response pair.

    Args:
        prompt: The prompt string (used as hash key).
        response: The LLM response string.
        model: Model identifier for provenance.
        metadata: Optional dict of extra info to store.

    Returns:
        The cache key (hash string).
    """
    _ensure_dir()
    key = _hash_prompt(prompt)
    data = {
        "hash": key,
        "timestamp": time.time(),
        "model": model,
        "prompt_length": len(prompt),
        "response": response,
    }
    if metadata:
        data["metadata"] = metadata

    path = _cache_path(key)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
    return key


def memo_wrap(
    prompt: str,
    llm_fn: Callable[[str], str],
    model: str = "unknown",
    ttl: int = DEFAULT_TTL,
) -> tuple[str, bool]:
    """Memoized LLM call -- returns cached or calls llm_fn(prompt).

    Args:
        prompt: The prompt string.
        llm_fn: Callable that takes prompt and returns response string.
        model: Model identifier.
        ttl: Cache TTL in seconds.

    Returns:
        (response_string, was_cached_bool)
    """
    cached = memo_get(prompt, ttl=ttl)
    if cached:
        return cached["response"], True

    response = llm_fn(prompt)
    memo_set(prompt, response, model=model)
    return response, False


def memo_clear(all_entries: bool = False, ttl: int = DEFAULT_TTL) -> tuple[int, int]:
    """Remove expired (or all) cache entries.

    Returns:
        (removed_count, remaining_count)
    """
    if not CACHE_DIR.exists():
        return 0, 0

    removed = 0
    remaining = 0
    now = time.time()

    for f in CACHE_DIR.glob("*.json"):
        if all_entries:
            f.unlink()
            removed += 1
            continue

        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            age = now - data.get("timestamp", 0)
            if age > ttl:
                f.unlink()
                removed += 1
            else:
                remaining += 1
        except (json.JSONDecodeError, OSError):
            f.unlink()
            removed += 1

    return removed, remaining


def memo_stats() -> dict[str, int | float | None]:
    """Return cache statistics.

    Returns:
        dict with total, expired, active, total_bytes, oldest, newest.
    """
    if not CACHE_DIR.exists():
        return {"total": 0, "expired": 0, "active": 0,
                "total_bytes": 0, "oldest": None, "newest": None}

    now = time.time()
    total = 0
    expired = 0
    active = 0
    total_bytes = 0
    oldest = float("in")
    newest = 0

    for f in CACHE_DIR.glob("*.json"):
        total += 1
        total_bytes += f.stat().st_size
        try:
            data = json.loads(f.read_text(encoding="utf-8"))
            ts = data.get("timestamp", 0)
            age = now - ts
            if age > DEFAULT_TTL:
                expired += 1
            else:
                active += 1
            oldest = min(oldest, ts)
            newest = max(newest, ts)
        except (json.JSONDecodeError, OSError):
            expired += 1

    return {
        "total": total,
        "expired": expired,
        "active": active,
        "total_bytes": total_bytes,
        "oldest": oldest if oldest != float("in") else None,
        "newest": newest if newest > 0 else None,
    }


# ================================================================
# CLI
# ================================================================

def main() -> None:
    parser = argparse.ArgumentParser(description="CEX Result Memoization")
    sub = parser.add_subparsers(dest="command")

    sub.add_parser("stats", help="Show cache statistics")

    get_p = sub.add_parser("get", help="Lookup by hash")
    get_p.add_argument("hash", help="Cache key (hash prefix)")

    clear_p = sub.add_parser("clear", help="Purge expired entries")
    clear_p.add_argument("--all", action="store_true", help="Purge everything")
    clear_p.add_argument("--ttl", type=int, default=DEFAULT_TTL,
                         help="TTL in seconds (default: %d)" % DEFAULT_TTL)

    args = parser.parse_args()

    if args.command == "stats":
        s = memo_stats()
        print("CEX Memo Cache Stats")
        print("  Total entries: %d" % s["total"])
        print("  Active:        %d" % s["active"])
        print("  Expired:       %d" % s["expired"])
        print("  Total bytes:   %d" % s["total_bytes"])
        if s["oldest"]:
            import datetime
            print("  Oldest:        %s" % datetime.datetime.fromtimestamp(s["oldest"]).isoformat())
        if s["newest"]:
            import datetime
            print("  Newest:        %s" % datetime.datetime.fromtimestamp(s["newest"]).isoformat())

    elif args.command == "get":
        path = _cache_path(args.hash)
        if path.exists():
            print(path.read_text(encoding="utf-8"))
        else:
            # Try prefix match
            matches = list(CACHE_DIR.glob("%s*.json" % args.hash))
            if matches:
                print(matches[0].read_text(encoding="utf-8"))
            else:
                print("Not found: %s" % args.hash, file=sys.stderr)
                sys.exit(1)

    elif args.command == "clear":
        removed, remaining = memo_clear(all_entries=args.all, ttl=args.ttl)
        print("Removed: %d  Remaining: %d" % (removed, remaining))

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
