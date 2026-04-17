#!/usr/bin/env python3
"""cex_social_publisher.py: Multi-platform social content formatter for N02.

Takes raw copy and outputs platform-sized variants (Twitter/X, LinkedIn, Instagram).
No network calls - produces the content for manual posting or webhook dispatch.

Usage:
    python _tools/cex_social_publisher.py --input draft.md --platforms x,linkedin
    echo "launch day" | python _tools/cex_social_publisher.py --stdin
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

PLATFORM_LIMITS = {
    "x": 280,
    "twitter": 280,
    "linkedin": 3000,
    "instagram": 2200,
    "threads": 500,
    "bluesky": 300,
    "mastodon": 500,
}


def extract_hashtags(text: str) -> list[str]:
    return re.findall(r"#\w+", text)


def format_for_platform(copy: str, platform: str) -> dict:
    limit = PLATFORM_LIMITS.get(platform, 1000)
    body = copy.strip()
    hashtags = extract_hashtags(body)

    if platform in ("x", "twitter", "bluesky", "threads", "mastodon"):
        if len(body) > limit:
            body = body[:limit - 3] + "..."
    elif platform == "linkedin":
        paragraphs = [p.strip() for p in body.split("\n\n") if p.strip()]
        body = "\n\n".join(paragraphs)
        if len(body) > limit:
            body = body[:limit - 3] + "..."
    elif platform == "instagram":
        body = body.replace("\n\n", "\n.\n.\n.\n")
        if len(body) > limit:
            body = body[:limit - 3] + "..."

    return {
        "platform": platform,
        "char_count": len(body),
        "limit": limit,
        "fits": len(body) <= limit,
        "hashtags": hashtags,
        "content": body,
    }


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--input", help="path to draft .md")
    p.add_argument("--stdin", action="store_true")
    p.add_argument("--platforms", default="x,linkedin,instagram")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()

    if args.stdin:
        copy = sys.stdin.read()
    elif args.input:
        copy = Path(args.input).read_text(encoding="utf-8")
    else:
        p.error("provide --input or --stdin")

    platforms = [x.strip() for x in args.platforms.split(",") if x.strip()]
    results = [format_for_platform(copy, plat) for plat in platforms]

    if args.json:
        print(json.dumps(results, indent=2))
    else:
        for r in results:
            print(f"=== {r['platform'].upper()} ({r['char_count']}/{r['limit']}) {'OK' if r['fits'] else 'OVERFLOW'} ===")
            print(r["content"])
            if r["hashtags"]:
                print(f"[hashtags: {' '.join(r['hashtags'])}]")
            print()
    return 0


if __name__ == "__main__":
    sys.exit(main())
