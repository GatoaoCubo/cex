#!/usr/bin/env python3
"""cex_web_fetch.py: Fetch URL content for N01 research.

Minimal HTTP GET with HTML->text extraction. No JS rendering.
For N01 leverage: live web research + arxiv + citation sources.

Usage:
    python _tools/cex_web_fetch.py https://arxiv.org/abs/1706.03762
    python _tools/cex_web_fetch.py --arxiv 1706.03762
"""
from __future__ import annotations

import argparse
import re
import sys
from urllib import parse, request


def fetch(url: str, timeout: int = 20) -> str:
    req = request.Request(url, headers={"User-Agent": "CEX-N01/1.0"})
    with request.urlopen(req, timeout=timeout) as resp:
        ct = resp.headers.get("Content-Type", "")
        body = resp.read()
    enc = "utf-8"
    m = re.search(r"charset=([\w-]+)", ct)
    if m:
        enc = m.group(1)
    return body.decode(enc, errors="replace")


def html_to_text(html: str) -> str:
    html = re.sub(r"<script[^>]*>.*?</script>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<style[^>]*>.*?</style>", "", html, flags=re.DOTALL | re.IGNORECASE)
    html = re.sub(r"<[^>]+>", " ", html)
    html = re.sub(r"\s+", " ", html)
    return html.strip()


def arxiv_url(arxiv_id: str) -> str:
    return f"https://export.arxiv.org/abs/{parse.quote(arxiv_id)}"


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("url", nargs="?", help="URL to fetch")
    p.add_argument("--arxiv", help="arxiv ID (e.g. 1706.03762)")
    p.add_argument("--max-bytes", type=int, default=20000)
    p.add_argument("--raw", action="store_true", help="skip HTML->text")
    args = p.parse_args()

    url = args.url
    if args.arxiv:
        url = arxiv_url(args.arxiv)
    if not url:
        p.error("provide url or --arxiv")

    try:
        html = fetch(url)
    except Exception as e:
        print(f"ERROR: {e}", file=sys.stderr)
        return 1

    text = html if args.raw else html_to_text(html)
    if len(text) > args.max_bytes:
        text = text[:args.max_bytes] + f"\n... [truncated, {len(text)} total bytes]"
    print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
