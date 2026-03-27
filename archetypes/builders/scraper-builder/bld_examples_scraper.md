---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of scraper artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: scraper-builder

## Golden Example

INPUT: "Create scraper for extracting product data from an e-commerce marketplace"

OUTPUT:
```yaml
---
id: p04_scraper_marketplace_products
kind: scraper
pillar: P04
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "EDISON"
name: "Marketplace Product Scraper"
target: "https://marketplace.example.com/search"
selectors:
  - product_title
  - price
  - rating
  - seller_name
  - image_url
output_format: json
quality: null
tags: [scraper, marketplace, products, P04]
tldr: "Marketplace product scraper: 5 fields, CSS selectors, cursor pagination, JSON output"
description: "Extracts product title, price, rating, seller, and image from marketplace search results"
pagination: next_page
rate_limit: "2 req/s, 1s delay between pages"
anti_bot: basic
proxy: true
scheduling: "daily 06:00 UTC"
validation: ["price > 0", "title non-empty", "rating 0-5"]
freshness: "24h"
---
```

## Overview
Extracts product listing data from marketplace search results pages.
Used by research agents for competitive analysis and price monitoring.

## Selectors

### product_title
Selector: `h2.product-title` (CSS)
Type: string
Rule: strip whitespace, max 200 chars, decode HTML entities

### price
Selector: `span.price-value` (CSS)
Type: float
Rule: extract numeric value, remove currency symbol, parse decimal

### rating
Selector: `div.rating-stars::attr(data-score)` (CSS)
Type: float
Rule: value 0.0-5.0, null if no reviews

### seller_name
Selector: `a.seller-link` (CSS)
Type: string
Rule: text content, strip whitespace

### image_url
Selector: `img.product-image::attr(src)` (CSS)
Type: url
Rule: absolute URL, prefer high-res variant

## Pagination & Rate Limiting
Pagination: next_page — follow `a.next-page` link until absent
Rate limit: 2 requests/second, 1s delay between page transitions
Anti-bot: basic (rotate User-Agent, respect robots.txt)
Proxy: required (rotate per 50 requests)

## Output
Format: JSON array of {product_title, price, rating, seller_name, image_url}
Validation: price > 0, title non-empty, rating in 0-5 range
Freshness: data stale after 24h, re-scrape daily

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_scraper_ pattern (H02 pass)
- kind: scraper (H04 pass)
- 19+ required+recommended fields present (H06 pass)
- body has all 4 sections: Overview, Selectors, Pagination & Rate Limiting, Output (H07 pass)
- selectors list matches ## Selectors field names exactly (S03 pass)
- Each selector has CSS/XPath, type, extraction rule (S06 pass)
- tldr: 78 chars <= 160 (S01 pass)
- tags: 4 items, includes "scraper" (S02 pass)
- pagination and rate_limit defined (S04 pass)

## Anti-Example

INPUT: "Create scraper for news headlines"

BAD OUTPUT:
```yaml
---
id: news-scraper
kind: web_scraper
pillar: tools
name: News Scraper
selectors: [title, link]
quality: 8.0
tags: [news]
---
```

Scrapes news headlines.

## Selectors
title: gets the title
link: gets the link

FAILURES:
1. id: "news-scraper" has hyphens and no `p04_scraper_` prefix -> H02 FAIL
2. kind: "web_scraper" not "scraper" -> H04 FAIL
3. pillar: "tools" not "P04" -> H06 FAIL
4. quality: 8.0 (not null) -> H05 FAIL
5. Missing fields: target, output_format, version, created, updated, author, tldr -> H06 FAIL
6. tags: only 1 item, missing "scraper" -> S02 FAIL
7. Body missing ## Pagination & Rate Limiting, ## Output sections -> H07 FAIL
8. Selector entries have no CSS/XPath, type, or extraction rule -> S06 FAIL
9. No target URL — cannot know where to scrape -> H06 FAIL
10. No output_format — consumer cannot parse results -> H06 FAIL
