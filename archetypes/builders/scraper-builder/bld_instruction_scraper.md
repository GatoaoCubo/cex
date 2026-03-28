---
id: p03_ins_scraper_builder
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Scraper Builder Instructions
target: scraper-builder agent
phases_count: 4
prerequisites:
  - Target URL or domain is provided (non-empty string)
  - At least one data field to extract is identified (e.g. "product title", "price")
  - Output format preference is stated (json, csv, or yaml)
  - Site is publicly accessible unless authentication is explicitly stated
validation_method: checklist
domain: scraper
quality: null
tags: [instruction, scraper, web-extraction, data, P04]
idempotent: true
atomic: false
rollback: Delete generated scraper artifact and restart from Phase 1
dependencies: []
logging: true
tldr: Build a scraper artifact defining target site, CSS/XPath selectors, pagination strategy, rate limits, anti-bot config, and output format.
density_score: 0.89
---

## Context
The scraper-builder produces `scraper` artifacts — specifications for web data extractors
that collect information from HTML/DOM pages. A scraper artifact defines the target site,
selectors for each data field, pagination strategy, rate limiting, anti-bot awareness, and
output format.
**Input contract**:
- `{{target_url}}`: base URL to scrape (e.g. `https://example.com/products`)
- `{{fields_list}}`: comma-separated fields to extract (e.g. `title, price, sku, image_url`)
- `{{output_format}}`: one of `json`, `csv`, `yaml`
- `{{pagination_type}}`: one of `next_page`, `infinite_scroll`, `numbered`, `none`
- `{{rate_limit_rps}}`: requests per second (float, e.g. `0.5` means 1 request every 2s)
**Output contract**: A single `scraper` YAML artifact with frontmatter, selector map,
pagination config, rate limit and anti-bot settings, and output format specification.
**Boundaries**:
- Scraper extracts from HTML/DOM only.
- Consuming structured APIs is a client artifact (not scraper).
- Bidirectional data sync is a connector artifact.
- Extracting structured data from LLM output text is a parser artifact.
- This builder produces the specification — not the runtime extraction code.
## Phases
### Phase 1: Analyze Target Site Structure
**Primary action**: Characterize the target site and determine the scraping approach
before writing any selectors.
```
INPUT: target_url, fields_list
1. Parse target_url:
   site_profile = {
     domain: extracted domain from URL,
     path_pattern: URL template if paginated (?page=N, /page/N),
     likely_spa: true if site uses JavaScript-heavy rendering, else false,
     has_auth_wall: false (default; flag if user states login required)
   }
2. Classify page type:
   if path suggests listing of multiple items -> page_type = "listing"
   if path suggests single item detail        -> page_type = "detail"
   if path suggests search results            -> page_type = "search_results"
   else                                       -> page_type = "generic"
3. For each field in fields_list:
   field_profile = {
     name: field.strip(),
     selector_strategy: "css" (default) | "xpath" (for nested/conditional),
     expected_type: "text" | "attribute" | "number" | "url",
     nullable: false  # set true if field may be absent on some pages
   }
4. Assess anti-bot level for target domain:
   known_providers = [cloudflare, akamai, datadome, perimeter-x]
   anti_bot_level = "none" | "basic" | "advanced"
OUTPUT: site_profile{}, page_type, field_profiles[], anti_bot_level
```
Verification: `field_profiles` count matches `fields_list` count. `page_type` is set.
### Phase 2: Define Selectors
**Primary action**: Write the CSS or XPath selector for each data field, including
fallbacks for nullable fields.
```
INPUT: field_profiles[], page_type, site_profile
1. Selector construction rules:
   PREFER: attribute-based selectors (data-*, id=) over positional ones
   AVOID:  positional selectors like nth-child(3) unless no alternative exists
   PREFER: specific class names over generic tag names
2. For each field in field_profiles:
   if expected_type == "text":      selector extracts textContent
   if expected_type == "attribute": selector uses attr() — "img::attr(src)" or @src
   if expected_type == "number":    selector extracts text; note strip regex [\d.,]+
   if expected_type == "url":       selector uses ::attr(href) or ::attr(src)
   if field.nullable == true:
     fallback_selector = simpler alternative or null
   else:
     fallback_selector = null
3. Container selector:
   if page_type == "listing":
     define container_selector wrapping each item (e.g. ".product-card")
     all field selectors are relative to this container
   else:
     selectors are absolute from document root
4. Selector confidence:
   "stable":   based on id or data-* attribute
   "fragile":  based on class names that may change on redesign
   "unknown":  cannot determine without live DOM inspection
OUTPUT: selector_map{field_name: {primary, fallback, confidence}},
        container_selector (if listing page)
```
Verification: every field has a `primary` selector. `container_selector` defined when
`page_type` is `listing`.
### Phase 3: Configure Pagination, Rate Limit, and Anti-Bot
**Primary action**: Specify multi-page navigation, rate limiting, and anti-bot handling.
```
INPUT: pagination_type, rate_limit_rps, anti_bot_level, site_profile
1. Pagination:
   "next_page":       {selector: "a[rel='next']", max_pages: 50,
                       stop_condition: "no next link found"}
   "numbered":        {url_template: site_profile.path_pattern or "?page={{n}}",
                       start: 1, max_pages: 50}
   "infinite_scroll": {scroll_pause_ms: 1500, max_scrolls: 20,
                       stop_condition: "no new items after scroll"}
   "none":            {type: "none"}
2. Rate limit:
   rate_limit = {
     requests_per_second: {{rate_limit_rps}},
     jitter_ms: round(1000 / rate_limit_rps * 0.2),  # 20% random variation
     retry_on_429: true,
     retry_backoff_seconds: [5, 15, 60],
     max_retries: 3
   }
3. Anti-bot:
   "none":     {user_agent_rotation: false, proxy_rotation: false}
