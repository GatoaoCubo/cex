#!/usr/bin/env python
# -*- coding: ascii -*-
"""
Content Pipeline Seeder -- GATO3
================================
Parses N02's editorial content (26 blog posts + 91 IG posts from 13 week files)
and seeds Supabase content_items + content_schedule tables.

Tables (see 20260410220003_content_pipeline_clean.sql):
  - content_items: core content with title, slug, body, category, status
  - content_schedule: per-platform scheduling with date/time
  - content_media: media attachments (not seeded here -- manual upload)
  - content_sources: reference sources (not seeded here)

Usage:
    python seed_content_pipeline.py                  # Seed all content
    python seed_content_pipeline.py --dry-run        # Parse and preview, no DB writes
    python seed_content_pipeline.py --count          # Show counts only
    python seed_content_pipeline.py --clear          # Clear tables and reseed
    python seed_content_pipeline.py --blogs-only     # Seed only blog posts
    python seed_content_pipeline.py --ig-only        # Seed only Instagram posts

Requires: requests, pyyaml
Environment: SUPABASE_URL, SUPABASE_SERVICE_ROLE_KEY (or codexa-core/.env)
"""
import os
import re
import sys
import json
import argparse
from pathlib import Path
from datetime import datetime

sys.stdout.reconfigure(encoding="utf-8")

try:
    import yaml
except ImportError:
    print("[FAIL] PyYAML required. Install: pip install pyyaml")
    sys.exit(1)

try:
    import requests
except ImportError:
    print("[FAIL] requests required. Install: pip install requests")
    sys.exit(1)


# ---------------------------------------------------------------------------
# Configuration
# ---------------------------------------------------------------------------

CEX_ROOT = Path(__file__).resolve().parent.parent.parent
BLOG_DIR = CEX_ROOT / "N02_marketing" / "content_pipeline" / "blog"
IG_DIR = CEX_ROOT / "N02_marketing" / "content_pipeline" / "instagram"

SUPABASE_URL = os.getenv(
    "SUPABASE_URL", "https://fuuguegkqnpzrrhwymgw.supabase.co"
)
SUPABASE_KEY = os.getenv(
    "SUPABASE_SERVICE_ROLE_KEY", os.getenv("SUPABASE_SERVICE_KEY", "")
)

# Fallback: read from codexa-core .env
if not SUPABASE_KEY:
    codexa_env = CEX_ROOT.parent / "codexa-core" / ".env"
    if codexa_env.exists():
        with open(codexa_env, encoding="utf-8") as f:
            for line in f:
                if line.startswith("SUPABASE_SERVICE_ROLE_KEY="):
                    SUPABASE_KEY = line.split("=", 1)[1].strip()
                    break


def _headers():
    return {
        "apikey": SUPABASE_KEY,
        "Authorization": "Bearer %s" % SUPABASE_KEY,
        "Content-Type": "application/json",
        "Prefer": "return=representation",
    }


# ---------------------------------------------------------------------------
# Content type and category mapping
# ---------------------------------------------------------------------------

CONTENT_TYPE_MAP = {
    "carrossel": "instagram_carrossel",
    "feed carrossel": "instagram_carrossel",
    "carrossel infografico": "instagram_carrossel",
    "reel": "instagram_reel",
    "feed single": "instagram_feed",
    "single": "instagram_feed",
    "single image": "instagram_feed",
    "feed infografico": "instagram_feed",
    "infografico": "instagram_feed",
    "story": "instagram_story",
}

CATEGORY_MAP = {
    "educativo": "educativo",
    "meme": "meme_humor",
    "meme/humor": "meme_humor",
    "humor": "meme_humor",
    "produto": "produto",
    "product": "produto",
    "seasonal": "seasonal",
    "engagement": "educativo",
}


def map_content_type(format_str):
    """Map IG format string to content_type enum value.

    Handles compound formats like 'Story Quiz', 'Reel 30s', 'Carrossel comparativo'.
    Uses keyword matching after exact-match fails.
    """
    key = format_str.strip().lower()
    # Strip duration suffixes like "30s", "15s", "60s", "90s"
    key = re.sub(r"\s*\d+s$", "", key)

    # Exact match first
    if key in CONTENT_TYPE_MAP:
        return CONTENT_TYPE_MAP[key]

    # Keyword-based fallback (order matters: most specific first)
    if "story" in key:
        return "instagram_story"
    if "reel" in key:
        return "instagram_reel"
    if "carrossel" in key:
        return "instagram_carrossel"

    return "instagram_feed"


def map_category(category_str):
    """Map category string to DB enum value."""
    key = category_str.strip().lower()
    return CATEGORY_MAP.get(key, "educativo")


def slugify(text, max_len=60):
    """Generate URL-safe slug from text. ASCII-safe."""
    # Transliterate common Portuguese chars
    replacements = [
        ("\u00e3", "a"), ("\u00e1", "a"), ("\u00e2", "a"), ("\u00e0", "a"),
        ("\u00e9", "e"), ("\u00ea", "e"), ("\u00ed", "i"), ("\u00f3", "o"),
        ("\u00f4", "o"), ("\u00f5", "o"), ("\u00fa", "u"), ("\u00fc", "u"),
        ("\u00e7", "c"), ("\u00f1", "n"),
        ("\u00c3", "a"), ("\u00c1", "a"), ("\u00c9", "e"), ("\u00cd", "i"),
        ("\u00d3", "o"), ("\u00da", "u"), ("\u00c7", "c"),
    ]
    s = text.lower()
    for old, new in replacements:
        s = s.replace(old, new)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    s = s.strip("-")
    if len(s) > max_len:
        s = s[:max_len].rstrip("-")
    return s


# ---------------------------------------------------------------------------
# Blog parser
# ---------------------------------------------------------------------------

def parse_blog_file(filepath):
    """Parse a blog markdown file into a content_items dict."""
    text = filepath.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) < 3:
        print("  [WARN] Skipping %s: no frontmatter found" % filepath.name)
        return None

    try:
        fm = yaml.safe_load(parts[1])
    except yaml.YAMLError as exc:
        print("  [WARN] YAML error in %s: %s" % (filepath.name, exc))
        return None

    if not fm or not isinstance(fm, dict):
        return None

    body = parts[2].strip()
    slug = fm.get("slug", slugify(fm.get("title", filepath.stem)))

    return {
        "title": fm.get("title", ""),
        "slug": slug,
        "content_type": "blog_post",
        "category": map_category(fm.get("category", "educativo")),
        "status": "draft",
        "body_markdown": body,
        "target_platform": "blog",
        "product_refs": fm.get("product_refs", []) or [],
        "source_kc_id": fm.get("id", ""),
        "scheduled_date": str(fm.get("scheduled_date", "")) or None,
        "seo_title": fm.get("seo_title", ""),
        "seo_description": fm.get("seo_description", ""),
        "seo_keywords": fm.get("seo_keywords", []) or [],
        "_week": fm.get("week"),
        "_blog_number": fm.get("blog_number"),
        "_source_file": filepath.name,
    }


def parse_all_blogs():
    """Parse all blog files from N02_marketing/content_pipeline/blog/."""
    if not BLOG_DIR.exists():
        print("[WARN] Blog directory not found: %s" % BLOG_DIR)
        return []

    items = []
    for filepath in sorted(BLOG_DIR.glob("blog_*.md")):
        item = parse_blog_file(filepath)
        if item:
            items.append(item)

    return items


# ---------------------------------------------------------------------------
# Instagram parser
# ---------------------------------------------------------------------------

def parse_ig_post_fields(section_text):
    """Extract structured fields from an IG post section.

    Fields are in format: - **Field Name**: value (possibly multiline)
    """
    fields = {}
    pattern = r"- \*\*(.+?)\*\*:\s*"
    markers = list(re.finditer(pattern, section_text))

    for i, match in enumerate(markers):
        field_name = match.group(1).strip().lower().replace(" ", "_")
        start = match.end()
        end = markers[i + 1].start() if i + 1 < len(markers) else len(section_text)
        value = section_text[start:end].strip()
        # Remove trailing --- separators
        value = re.sub(r"\n---\s*$", "", value).strip()
        fields[field_name] = value

    return fields


def parse_ig_post(section_text, week_num, post_num):
    """Parse a single IG post section into a content_items dict.

    Returns None for blog reference posts (handled by blog parser).
    Handles two header formats:
      ### Post N -- Day DD/Mon Format (Category)
      ### Story -- Day DD/Mon Format (Category)
    """
    # Try standard Post header first, then Story header
    header_match = re.search(
        r"###\s+(?:Post\s+\d+|Story)\s+.+?\s+\d+/\w+\s+(.+?)\s+\((.+?)\)",
        section_text
    )
    if not header_match:
        return None

    format_str = header_match.group(1).strip()
    category_str = header_match.group(2).strip()

    # If header starts with "### Story", force content_type to story
    is_story_header = bool(re.match(r"###\s+Story\b", section_text.strip()))

    # Skip blog reference posts
    if "blog" in format_str.lower():
        return None

    # Skip if it's just a cross-reference
    if "> See:" in section_text and "**Caption**" not in section_text:
        return None

    if is_story_header:
        content_type = "instagram_story"
    else:
        content_type = map_content_type(format_str)
    category = map_category(category_str)

    fields = parse_ig_post_fields(section_text)

    if not fields:
        return None

    # Extract caption (primary content)
    caption = fields.get("caption", "")

    # Generate title from first line of caption
    title_line = caption.split("\n")[0].strip() if caption else ""
    if len(title_line) > 120:
        title_line = title_line[:117] + "..."

    # Generate slug
    slug = "ig-w%02d-p%02d-%s" % (week_num, post_num, slugify(title_line, 40))

    # Parse hashtags into array
    hashtags_raw = fields.get("hashtags", "")
    hashtags = [
        tag.strip() for tag in re.findall(r"#\S+", hashtags_raw)
    ] if hashtags_raw else []

    # Parse product refs
    product_raw = fields.get("product_ref", "")
    product_refs = [
        p.strip() for p in product_raw.split(",") if p.strip()
    ] if product_raw else []

    # Parse scheduled date/time
    scheduled_raw = fields.get("scheduled", "")
    scheduled_date = None
    scheduled_time = "10:00"
    if scheduled_raw:
        # Format: "2026-04-15 07:00 BRT"
        date_match = re.match(r"(\d{4}-\d{2}-\d{2})\s+(\d{2}:\d{2})", scheduled_raw)
        if date_match:
            scheduled_date = date_match.group(1)
            scheduled_time = date_match.group(2)

    return {
        "title": title_line or "IG Week %d Post %d" % (week_num, post_num),
        "slug": slug,
        "content_type": content_type,
        "category": category,
        "status": "draft",
        "caption": caption,
        "alt_text": fields.get("alt_text", ""),
        "hashtags": hashtags,
        "target_platform": "instagram",
        "content_pillar": category_str,
        "product_refs": product_refs,
        "scheduled_date": scheduled_date,
        "seo_title": None,
        "seo_description": None,
        "seo_keywords": None,
        "_scheduled_time": scheduled_time,
        "_week": week_num,
        "_post_num": post_num,
        "_source_file": "week_%02d.md" % week_num,
    }


def parse_ig_week(filepath):
    """Parse all IG posts from a week markdown file."""
    text = filepath.read_text(encoding="utf-8")

    # Extract week number from frontmatter
    fm_match = re.search(r"^week:\s*(\d+)", text, re.MULTILINE)
    week_num = int(fm_match.group(1)) if fm_match else 0

    if week_num == 0:
        # Fallback: extract from filename
        num_match = re.search(r"week_(\d+)", filepath.stem)
        week_num = int(num_match.group(1)) if num_match else 0

    # Split into post sections by ### Post or ### Story headers
    sections = re.split(r"(?=###\s+(?:Post\s+\d+|Story)\b)", text)

    items = []
    post_counter = 0
    for section in sections:
        if not section.strip():
            continue
        if "### Post" not in section and "### Story" not in section:
            continue
        post_counter += 1
        item = parse_ig_post(section, week_num, post_counter)
        if item:
            items.append(item)

    return items


def parse_all_ig():
    """Parse all IG week files from N02_marketing/content_pipeline/instagram/."""
    if not IG_DIR.exists():
        print("[WARN] Instagram directory not found: %s" % IG_DIR)
        return []

    items = []
    for filepath in sorted(IG_DIR.glob("week_*.md")):
        week_items = parse_ig_week(filepath)
        items.extend(week_items)

    return items


# ---------------------------------------------------------------------------
# Supabase operations
# ---------------------------------------------------------------------------

def clear_tables():
    """Delete all rows from content_schedule and content_items (cascade)."""
    print("[>>] Clearing content_schedule...")
    r1 = requests.delete(
        "%s/rest/v1/content_schedule?id=not.is.null" % SUPABASE_URL,
        headers=_headers(),
    )
    print("  Status: %d" % r1.status_code)

    print("[>>] Clearing content_items...")
    r2 = requests.delete(
        "%s/rest/v1/content_items?id=not.is.null" % SUPABASE_URL,
        headers=_headers(),
    )
    print("  Status: %d" % r2.status_code)

    return r1.ok and r2.ok


def insert_content_items(items, dry_run=False):
    """Insert content items into Supabase. Returns list of (item, uuid) tuples."""
    results = []

    for item in items:
        # Build payload matching content_items schema
        payload = {
            "title": item["title"],
            "slug": item["slug"],
            "content_type": item["content_type"],
            "category": item["category"],
            "status": item["status"],
            "body_markdown": item.get("body_markdown"),
            "caption": item.get("caption"),
            "alt_text": item.get("alt_text"),
            "hashtags": item.get("hashtags"),
            "target_platform": item["target_platform"],
            "content_pillar": item.get("content_pillar"),
            "product_refs": item.get("product_refs"),
            "source_kc_id": item.get("source_kc_id"),
            "scheduled_date": item.get("scheduled_date"),
            "seo_title": item.get("seo_title"),
            "seo_description": item.get("seo_description"),
            "seo_keywords": item.get("seo_keywords"),
            "created_by": "cex_n03_seed",
        }

        # Remove None values
        payload = {k: v for k, v in payload.items() if v is not None}

        if dry_run:
            print("  [DRY] %s | %s | %s | %s" % (
                item["content_type"].ljust(22),
                item["category"].ljust(12),
                (item.get("scheduled_date") or "no-date").ljust(12),
                item["title"][:60],
            ))
            results.append((item, "dry-run-uuid"))
            continue

        resp = requests.post(
            "%s/rest/v1/content_items" % SUPABASE_URL,
            headers=_headers(),
            json=payload,
        )

        if resp.ok:
            data = resp.json()
            item_id = data[0]["id"] if data else None
            results.append((item, item_id))
            print("  [OK] %s -> %s" % (item["slug"], item_id))
        else:
            print("  [FAIL] %s -> %d %s" % (
                item["slug"], resp.status_code, resp.text[:200]
            ))
            results.append((item, None))

    return results


def insert_content_schedule(item_results, dry_run=False):
    """Insert schedule entries for items that have scheduled dates."""
    count = 0

    for item, item_id in item_results:
        if not item.get("scheduled_date") or not item_id:
            continue
        if item_id == "dry-run-uuid":
            count += 1
            continue

        platform = "blog" if item["content_type"] == "blog_post" else "instagram"
        scheduled_time = item.get("_scheduled_time", "10:00")

        payload = {
            "content_item_id": item_id,
            "scheduled_date": item["scheduled_date"],
            "scheduled_time": scheduled_time,
            "platform": platform,
            "status": "pending",
        }

        resp = requests.post(
            "%s/rest/v1/content_schedule" % SUPABASE_URL,
            headers=_headers(),
            json=payload,
        )

        if resp.ok:
            count += 1
        else:
            print("  [FAIL] schedule %s -> %d %s" % (
                item["slug"], resp.status_code, resp.text[:200]
            ))

    return count


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------

def print_summary(blogs, ig_posts):
    """Print a summary of parsed content."""
    total = len(blogs) + len(ig_posts)

    print("\n=== Content Pipeline Summary ===")
    print("Blog posts:      %d" % len(blogs))
    print("Instagram posts: %d" % len(ig_posts))
    print("Total:           %d" % total)
    print("")

    # Category breakdown
    categories = {}
    for item in blogs + ig_posts:
        cat = item["category"]
        categories[cat] = categories.get(cat, 0) + 1

    print("Category breakdown:")
    for cat, count in sorted(categories.items()):
        pct = (count / total * 100) if total else 0
        print("  %-14s %3d (%4.1f%%)" % (cat, count, pct))

    # Content type breakdown
    print("")
    types = {}
    for item in blogs + ig_posts:
        ct = item["content_type"]
        types[ct] = types.get(ct, 0) + 1

    print("Content type breakdown:")
    for ct, count in sorted(types.items()):
        print("  %-24s %3d" % (ct, count))

    # Week distribution
    print("")
    weeks = {}
    for item in blogs + ig_posts:
        w = item.get("_week", "?")
        weeks[w] = weeks.get(w, 0) + 1

    print("Weekly distribution:")
    for w in sorted(weeks.keys(), key=lambda x: int(x) if str(x).isdigit() else 99):
        print("  Week %2s: %2d items" % (w, weeks[w]))

    print("================================\n")


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(
        description="Seed GATO3 content pipeline into Supabase"
    )
    parser.add_argument(
        "--dry-run", action="store_true",
        help="Parse and preview without writing to DB"
    )
    parser.add_argument(
        "--count", action="store_true",
        help="Show counts only, no DB operations"
    )
    parser.add_argument(
        "--clear", action="store_true",
        help="Clear existing content before seeding"
    )
    parser.add_argument(
        "--blogs-only", action="store_true",
        help="Seed only blog posts"
    )
    parser.add_argument(
        "--ig-only", action="store_true",
        help="Seed only Instagram posts"
    )
    args = parser.parse_args()

    print("=== GATO3 Content Pipeline Seeder ===")
    print("CEX root: %s" % CEX_ROOT)
    print("Blog dir: %s (exists: %s)" % (BLOG_DIR, BLOG_DIR.exists()))
    print("IG dir:   %s (exists: %s)" % (IG_DIR, IG_DIR.exists()))
    print("")

    # Parse content
    blogs = [] if args.ig_only else parse_all_blogs()
    ig_posts = [] if args.blogs_only else parse_all_ig()

    print("[OK] Parsed %d blog posts" % len(blogs))
    print("[OK] Parsed %d Instagram posts" % len(ig_posts))

    print_summary(blogs, ig_posts)

    if args.count:
        return

    # Validate connection
    if not args.dry_run:
        if not SUPABASE_KEY:
            print("[FAIL] No SUPABASE_SERVICE_ROLE_KEY found.")
            print("  Set env var or place in codexa-core/.env")
            sys.exit(1)

        print("[i] Supabase URL: %s" % SUPABASE_URL)
        print("[i] Key loaded: %s...%s" % (SUPABASE_KEY[:8], SUPABASE_KEY[-4:]))

    # Clear if requested
    if args.clear and not args.dry_run:
        print("\n[>>] Clearing existing content...")
        if not clear_tables():
            print("[FAIL] Could not clear tables. Aborting.")
            sys.exit(1)
        print("[OK] Tables cleared.\n")

    # Insert content items
    all_items = blogs + ig_posts
    if not all_items:
        print("[WARN] No content to seed.")
        return

    mode_label = "DRY RUN" if args.dry_run else "LIVE"
    print("[>>] Inserting %d content items (%s)...\n" % (len(all_items), mode_label))

    results = insert_content_items(all_items, dry_run=args.dry_run)

    succeeded = sum(1 for _, uid in results if uid is not None)
    failed = sum(1 for _, uid in results if uid is None)

    print("\n[OK] Content items: %d inserted, %d failed" % (succeeded, failed))

    # Insert schedule entries
    print("[>>] Creating schedule entries...")
    sched_count = insert_content_schedule(results, dry_run=args.dry_run)
    print("[OK] Schedule entries: %d created" % sched_count)

    print("\n=== Seeding complete ===")
    if args.dry_run:
        print("[i] This was a dry run. No data was written to Supabase.")
        print("[i] Run without --dry-run to seed for real.")


if __name__ == "__main__":
    main()
