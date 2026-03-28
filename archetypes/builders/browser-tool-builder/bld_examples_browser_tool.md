---
kind: examples
id: bld_examples_browser_tool
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of browser_tool artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: browser-tool-builder
## Golden Example
INPUT: "Create browser tool for scraping product listings from a marketplace"
OUTPUT:
```yaml
id: p04_browser_marketplace_scraper
kind: browser_tool
pillar: P04
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "EDISON"
name: "Marketplace Product Scraper"
engine: playwright
actions: [navigate, wait, extract, screenshot]
selectors: [css, xpath, data_attr]
output_format: json
headless: true
viewport: "1280x720"
timeout: 30000
javascript: true
cookies: false
stealth: true
quality: null
tags: [browser_tool, marketplace, scraper, playwright, P04]
tldr: "Playwright scraper for marketplace product listings: navigate, wait for load, extract structured data, screenshot on failure"
description: "Extracts product name, price, rating, and seller from marketplace listing pages using CSS and data-attribute selectors"
user_agent: "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
```
## Overview
Extracts structured product data (name, price, rating, seller, availability) from marketplace
listing pages. Used by price-monitoring pipelines and competitive analysis agents.
Triggers on a list of product URLs; returns one JSON object per URL.
## Engine
Engine: Playwright (chromium). Headless: true. Viewport: 1280x720.
Timeout: 30000ms per action. JavaScript: enabled (required for dynamic content).
Stealth: true — randomized user_agent, navigator.webdriver = false.
## Actions
### navigate
Navigates to URL, waits for networkidle. Params: url (required), waitUntil.
### wait
Waits for product container. Selector: `[data-testid="product-container"]` / `.product-main`.
### extract
Extracts name/price/rating/seller via data_attr with css fallback. Returns JSON; null for missing.
### screenshot
Captures viewport on failure. Params: fullPage (bool), path (string).
## Selectors
Priority: data_attr > aria > css > xpath. Fallback: try next if null.
## Output
```json
{"url":"string","name":"string|null","price":"number|null","rating":"number|null","seller":"string|null","available":"boolean"}
```
WHY GOLDEN: H01-H10 all pass (valid YAML, id pattern, kind, quality:null, all fields, enums, timeout). Soft: selectors w/fallback (S04), output schema (S05), stealth (S06), tldr 119ch (S01), 5 tags (S02). Score ~9.2.
## Anti-Example
INPUT: "Create browser tool for extracting prices"
BAD OUTPUT:
```yaml
id: price-scraper
kind: scraper
pillar: tools
name: Price Tool
engine: browser
actions: [scrape]
quality: 8.5
tags: [scrape]
```
Gets prices from pages.
FAILURES:
1. id: "price-scraper" has hyphens and no `p04_browser_` prefix -> H02 FAIL
2. kind: "scraper" not "browser_tool" -> H04 FAIL
3. pillar: "tools" not "P04" -> H06 FAIL
4. engine: "browser" is not a recognized engine value -> H06 FAIL
5. quality: 8.5 (not null) -> H05 FAIL
6. actions: ["scrape"] is not a valid action enum value -> H07 FAIL
7. Missing fields: selectors, output_format, version, created, updated, author, tldr, timeout -> H06 FAIL
8. tags: only 1 item, missing "browser_tool" -> S02 FAIL
9. Body missing ## Engine, ## Actions, ## Selectors, ## Output Format sections -> H08 FAIL
10. No selector strategy documented — caller cannot know how elements are targeted -> S04 FAIL
