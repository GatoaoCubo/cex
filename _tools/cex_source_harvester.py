#!/usr/bin/env python3
"""
cex_source_harvester.py -- Repo-Wide Source Reference Extractor

Scans CEX repo files for external source references (URLs, arXiv IDs, RFC
numbers, GitHub slugs, W3C TRs, IETF drafts, ISO/IEEE/NIST standards,
HuggingFace models, DOI references) and merges them into:
  .cex/P09_config/taxonomy_sources.yaml

Deduplicates via URL canonicalization + fuzzy Levenshtein match.
Tags each entry with the file it was harvested from.

Usage:
  python _tools/cex_source_harvester.py --dry-run
  python _tools/cex_source_harvester.py --apply
  python _tools/cex_source_harvester.py --apply --verbose
  python _tools/cex_source_harvester.py --stats
  python _tools/cex_source_harvester.py --harvest-first  (called by scout)

ASCII-only. See .claude/rules/ascii-code-rule.md.
"""

import argparse
import datetime
import os
import re
import sys
from pathlib import Path
from typing import Dict, List, Optional, Set, Tuple

# ---------------------------------------------------------------------------
# Setup
# ---------------------------------------------------------------------------

CEX_ROOT = Path(__file__).resolve().parent.parent
os.chdir(str(CEX_ROOT))

SOURCES_CONFIG = CEX_ROOT / ".cex" / "config" / "taxonomy_sources.yaml"
TODAY = datetime.date.today().isoformat()

HARVESTED_MARKER = "# ============== HARVESTED SECTION START =============="
HARVESTED_FOOTER = "# =============== HARVESTED SECTION END ==============="

# ---------------------------------------------------------------------------
# Scan targets
# ---------------------------------------------------------------------------

SCAN_TARGETS: List[Tuple[Path, str]] = [
    (CEX_ROOT / "N01_intelligence" / "research", "**/*.md"),
    (CEX_ROOT / "P01_knowledge" / "library", "**/*.md"),
    (CEX_ROOT / "_docs" / "specs", "**/*.md"),
    (CEX_ROOT / "archetypes" / "builders", "**/bld_knowledge_card_*.md"),
    (CEX_ROOT / ".claude" / "rules", "*.md"),
    (CEX_ROOT, "CLAUDE.md"),
]

# ---------------------------------------------------------------------------
# Extraction patterns (compiled once)
# ---------------------------------------------------------------------------

_PAT_URL      = re.compile(r'https?://[^\s<>"\')\]\,\|`]+')
_PAT_ARXIV_ID = re.compile(r'\barXiv:(\d{4}\.\d{4,5})\b', re.IGNORECASE)
_PAT_ARXIV_URL = re.compile(r'arxiv\.org/abs/(\d{4}\.\d{4,5})')
_PAT_RFC      = re.compile(r'\bRFC\s?(\d{3,5})\b')
_PAT_ISO      = re.compile(r'\b(ISO(?:/IEC)?\s+\d[\d-]*(?::\d{4})?)\b')
_PAT_IEEE     = re.compile(r'\b(IEEE\s+P?\d+(?:\.\d+)?)\b')
_PAT_NIST     = re.compile(r'\b(NIST\s+(?:AI|SP|IR)\s+[\d.-]+)\b')

# Skip-list: CDN, tracking, CI, local, image hosts
_SKIP_DOMAINS = frozenset([
    "shields.io", "img.shields.io", "badge.fury.io", "badgen.net",
    "travis-ci.org", "circleci.com", "codecov.io", "coveralls.io",
    "snyk.io", "dependabot.com", "pypi.org", "npmjs.com",
    "pkg.go.dev", "crates.io", "rubygems.org",
    "unsplash.com", "pexels.com", "pixabay.com", "flickr.com",
    "twitter.com", "x.com", "linkedin.com", "facebook.com",
    "instagram.com", "youtube.com", "youtu.be",
    "fonts.googleapis.com", "fonts.gstatic.com", "cdn.jsdelivr.net",
    "cdnjs.cloudflare.com", "unpkg.com",
    "localhost", "127.0.0.1", "0.0.0.0",
])

# Source types that are individual citations, not watchable feeds
_CITATION_TYPES = {"arxiv", "rfc", "doi"}


# ---------------------------------------------------------------------------
# URL utilities
# ---------------------------------------------------------------------------

def canonical_url(url: str) -> str:
    """Normalize URL for deduplication."""
    url = url.rstrip('/')
    url = re.sub(r'#.*$', '', url)
    url = re.sub(r'[?&](utm_[^&]+)', '', url)
    m = re.match(r'(https?://)([^/]+)(.*)', url)
    if m:
        url = m.group(1) + m.group(2).lower() + m.group(3)
    return url


def url_domain(url: str) -> str:
    m = re.match(r'https?://([^/]+)', url)
    return m.group(1).lower() if m else ""


def is_skip_url(url: str) -> bool:
    dom = url_domain(url)
    if not dom:
        return True
    bare = re.sub(r'^www\.', '', dom)
    return bare in _SKIP_DOMAINS or dom in _SKIP_DOMAINS


def classify_url(url: str) -> str:
    u = url.lower()
    if "github.com/" in u:
        return "github"
    if "arxiv.org/" in u:
        return "arxiv"
    if "w3.org/tr/" in u or "w3.org/groups/" in u:
        return "w3c"
    if "datatracker.ietf.org" in u or "ietf.org/rfc" in u:
        return "ietf"
    if "iso.org" in u:
        return "iso"
    if "standards.ieee.org" in u or "ieeexplore.ieee.org" in u:
        return "ieee"
    if "nist.gov" in u or "airc.nist.gov" in u:
        return "nist"
    if "huggingface.co/" in u:
        return "huggingface"
    if "doi.org/" in u:
        return "doi"
    return "website"


# ---------------------------------------------------------------------------
# Levenshtein (stdlib-only, O(m*n))
# ---------------------------------------------------------------------------

def _levenshtein(a: str, b: str) -> int:
    if len(a) < len(b):
        return _levenshtein(b, a)
    if not b:
        return len(a)
    prev = list(range(len(b) + 1))
    for ca in a:
        curr = [prev[0] + 1]
        for j, cb in enumerate(b):
            curr.append(min(prev[j + 1] + 1, curr[j] + 1, prev[j] + (0 if ca == cb else 1)))
        prev = curr
    return prev[-1]


def _fuzzy_dup(can_url: str, seen: Set[str], threshold: int = 10) -> bool:
    if can_url in seen:
        return True
    dom = url_domain(can_url)
    for ex in seen:
        if url_domain(ex) != dom:
            continue
        if _levenshtein(can_url, ex) <= threshold:
            return True
    return False


# ---------------------------------------------------------------------------
# Name / cadence / priority helpers
# ---------------------------------------------------------------------------

def _name_from_url(url: str, src_type: str) -> str:
    if src_type == "github":
        m = re.search(r'github\.com/([^/]+/[^/\s#?]+)', url)
        if m:
            return re.sub(r'[^a-z0-9-]', '-', m.group(1).lower())[:50]
    if src_type == "w3c":
        m = re.search(r'w3\.org/TR/([^/\s#?]+)', url)
        if m:
            return "w3c-" + m.group(1).lower()[:40]
    if src_type == "ietf":
        m = re.search(r'/doc/([^/\s#?]+)', url)
        if m:
            return "ietf-" + m.group(1).lower()[:40]
    if src_type == "nist":
        tail = url.rstrip('/').split('/')[-1]
        return "nist-" + re.sub(r'[^a-z0-9-]', '-', tail.lower())[:30]
    if src_type == "huggingface":
        m = re.search(r'huggingface\.co/([^/\s#?]+/[^/\s#?]+)', url)
        if m:
            return "hf-" + re.sub(r'[^a-z0-9-]', '-', m.group(1).lower())[:40]
    s = re.sub(r'^https?://(www\.)?', '', url)
    return re.sub(r'[^a-z0-9-]', '-', s.lower())[:50].strip('-')


_CADENCE = {"github": "weekly", "arxiv": "weekly", "w3c": "monthly",
            "ietf": "monthly", "website": "monthly", "huggingface": "biweekly"}

_PRIORITY = {"github": "medium", "w3c": "medium", "ietf": "medium",
             "iso": "medium", "ieee": "medium", "nist": "medium",
             "huggingface": "low", "website": "low", "doi": "low"}


# ---------------------------------------------------------------------------
# File scanner
# ---------------------------------------------------------------------------

def scan_file(path: Path) -> List[Tuple[str, str]]:
    """Return list of (url_type, canonical_url) from a file."""
    try:
        text = path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return []
    hits: List[Tuple[str, str]] = []

    # Raw URLs
    for m in _PAT_URL.finditer(text):
        raw = m.group(0).rstrip('.,;:)"\'`')
        if is_skip_url(raw):
            continue
        src_type = classify_url(raw)
        if src_type in _CITATION_TYPES:
            continue
        hits.append((src_type, canonical_url(raw)))

    return hits


# ---------------------------------------------------------------------------
# Load existing canonical URLs from the YAML
# ---------------------------------------------------------------------------

def _load_existing_canonicals() -> Set[str]:
    seen: Set[str] = set()
    if not SOURCES_CONFIG.exists():
        return seen
    text = SOURCES_CONFIG.read_text(encoding="utf-8")
    for m in re.finditer(r'\burl:\s*(\S+)', text):
        raw = m.group(1).strip('"\'')
        seen.add(canonical_url(raw))
    for m in _PAT_URL.finditer(text):
        seen.add(canonical_url(m.group(0).rstrip('.,;')))
    return seen


# ---------------------------------------------------------------------------
# Harvest orchestrator
# ---------------------------------------------------------------------------

class HarvestResult:
    def __init__(self):
        self.entries: List[dict] = []
        self.scanned = 0
        self.total_refs = 0
        self.skipped = 0


def harvest(verbose: bool = False) -> HarvestResult:
    result = HarvestResult()
    seen: Set[str] = _load_existing_canonicals()

    for base, pattern in SCAN_TARGETS:
        if not base.exists():
            continue
        if pattern == "CLAUDE.md":
            files = [base / "CLAUDE.md"] if (base / "CLAUDE.md").exists() else []
        else:
            files = list(base.glob(pattern))

        for fpath in sorted(files):
            result.scanned += 1
            rel = str(fpath.relative_to(CEX_ROOT)).replace("\\", "/")
            hits = scan_file(fpath)
            result.total_refs += len(hits)

            for src_type, can in hits:
                if _fuzzy_dup(can, seen):
                    result.skipped += 1
                    continue
                seen.add(can)
                name = _name_from_url(can, src_type)
                entry = {
                    "name": name,
                    "type": src_type,
                    "url": can,
                    "watch_paths": [],
                    "extract_patterns": [],
                    "cadence": _CADENCE.get(src_type, "monthly"),
                    "priority": _PRIORITY.get(src_type, "low"),
                    "harvested_from": rel,
                    "last_checked": TODAY,
                    "status": "active",
                }
                result.entries.append(entry)
                if verbose:
                    print(f"  [NEW] {src_type:12s} {can[:70]}")

    return result


# ---------------------------------------------------------------------------
# YAML serializer (no PyYAML dependency)
# ---------------------------------------------------------------------------

def _ys(val) -> str:
    """YAML-safe scalar serializer."""
    if val is None:
        return "null"
    s = str(val)
    if any(c in s for c in ':{}[]|>&*!,#?@`'):
        return '"' + s.replace('"', '\\"') + '"'
    return s


def _build_harvested_block(entries: List[dict]) -> str:
    lines = [
        "",
        HARVESTED_MARKER,
        "# Auto-generated by cex_source_harvester.py -- do not edit manually.",
        "# Re-run with --apply to refresh.",
        "#",
        f"# Harvest date: {TODAY}",
        f"# Entry count:  {len(entries)}",
        "# =====================================================================",
        "harvested:",
        "",
    ]
    for e in entries:
        lines.append("  - name: " + _ys(e["name"]))
        lines.append("    type: " + _ys(e["type"]))
        lines.append("    url: " + _ys(e["url"]))
        lines.append("    watch_paths: []")
        lines.append("    extract_patterns: []")
        lines.append("    cadence: " + _ys(e["cadence"]))
        lines.append("    priority: " + _ys(e["priority"]))
        lines.append("    harvested_from: " + _ys(e["harvested_from"]))
        lines.append("    last_checked: " + _ys(e["last_checked"]))
        lines.append("    status: " + _ys(e["status"]))
        lines.append("")
    lines.append(HARVESTED_FOOTER)
    return "\n".join(lines)


def apply_harvest(entries: List[dict]) -> int:
    if not entries:
        print("[OK] No new entries to add.")
        return 0
    current = SOURCES_CONFIG.read_text(encoding="utf-8") if SOURCES_CONFIG.exists() else ""
    # Strip old harvested section
    current = re.sub(
        r'\n' + re.escape(HARVESTED_MARKER) + r'.*?' + re.escape(HARVESTED_FOOTER),
        '',
        current,
        flags=re.DOTALL,
    )
    current = current.rstrip() + "\n"
    block = _build_harvested_block(entries)
    SOURCES_CONFIG.write_text(current + block, encoding="utf-8")
    return len(entries)


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main() -> None:
    parser = argparse.ArgumentParser(description="CEX Source Harvester")
    parser.add_argument("--dry-run", action="store_true", help="Preview new entries without writing")
    parser.add_argument("--apply", action="store_true", help="Merge new entries into taxonomy_sources.yaml")
    parser.add_argument("--stats", action="store_true", help="Show type breakdown only")
    parser.add_argument("--verbose", action="store_true", help="Print each new entry as found")
    parser.add_argument("--harvest-first", action="store_true", dest="harvest_first",
                        help="Run harvest+apply then exit 0 (called by scout --harvest-first)")
    args = parser.parse_args()

    print("=== CEX Source Harvester ===")
    print("Root:   " + str(CEX_ROOT))
    print("Config: " + str(SOURCES_CONFIG.relative_to(CEX_ROOT)))
    print("")

    result = harvest(verbose=args.verbose)

    print(f"Files scanned:  {result.scanned}")
    print(f"Refs found:     {result.total_refs}")
    print(f"Deduped/skip:   {result.skipped}")
    print(f"New entries:    {len(result.entries)}")

    if args.stats:
        by_type: Dict[str, int] = {}
        for e in result.entries:
            by_type[e["type"]] = by_type.get(e["type"], 0) + 1
        print("\nBreakdown:")
        for t, cnt in sorted(by_type.items(), key=lambda x: -x[1]):
            print(f"  {t:15s} {cnt}")
        return

    if args.dry_run:
        print("\n--- DRY RUN (no writes) ---")
        for e in result.entries[:25]:
            print(f"  [{e['type']:12s}] {e['url'][:72]}")
        if len(result.entries) > 25:
            print(f"  ... and {len(result.entries) - 25} more")
        return

    if args.apply or args.harvest_first:
        added = apply_harvest(result.entries)
        print(f"\n[OK] Applied {added} entries to {SOURCES_CONFIG.relative_to(CEX_ROOT)}")
        return

    print("\nRun with --dry-run to preview or --apply to write.")


if __name__ == "__main__":
    main()
