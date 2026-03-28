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
`page.goto(url, { waitUntil: 'networkidle' })`
Navigates to product URL and waits for network idle.
Params: url (string, required), waitUntil (load|networkidle|domcontentloaded, default: networkidle)
### wait
`page.waitForSelector(selector, { timeout: 10000 })`
Waits for product container to appear before extraction.
Selector: `[data-testid="product-container"]` (data_attr, primary)
Fallback: `.product-main` (css)
### extract
Extracts product fields from DOM.
Fields:
- name: `[data-testid="product-title"]` (data_attr) | `h1.title` (css fallback)
- price: `[data-testid="price-current"]` (data_attr) | `.price span` (css fallback)
- rating: `[aria-label*="rating"]` (aria) | `.stars-value` (css fallback)
- seller: `[data-testid="seller-name"]` (data_attr) | `.seller-link` (css fallback)
Returns: JSON object with all fields; null for unavailable fields.
### screenshot
`page.screenshot({ path: output_path, fullPage: false })`
Captures viewport screenshot on extraction failure for debugging.
Params: fullPage (boolean, default: false), path (string, required)
## Selectors
Priority order: data_attr > aria > css > xpath
1. data_attr (`[data-testid="*"]`): most stable, survives CSS refactors
2. aria (`[aria-label="*"]`): accessible elements, resilient to visual redesigns
3. css (`.class`, `#id`): fast but fragile to class name changes
4. xpath (`//div[@class="*"]`): structural fallback when CSS and data attrs absent
Fallback rule: if primary selector returns null, try next in priority chain before failing.
## Output Format
Primary: json
Schema per extract action:
```json
{
  "url": "string",
  "name": "string | null",
  "price": "number | null",
  "currency": "string | null",
  "rating": "number | null",
  "seller": "string | null",
  "available": "boolean",
  "screenshot_path": "string | null"
}
```
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_browser_ pattern (H02 pass)
- kind: browser_tool (H04 pass)
- engine declared: playwright (H06 pass)
- actions list matches ## Actions section names (H07 pass)
- selectors with fallback chain (S04 pass)
- output_format: json with schema (S05 pass)
- timeout defined: 30000ms (H09 pass)
- stealth and user_agent documented (S06 pass)
- tldr: 119 chars <= 160 (S01 pass)
- tags: 5 items, includes "browser_tool" (S02 pass)
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
