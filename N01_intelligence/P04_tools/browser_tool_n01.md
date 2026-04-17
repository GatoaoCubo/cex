---
id: browser_tool_n01
kind: browser_tool
pillar: P04
nucleus: n01
title: "N01 Competitive Intelligence Browser Tool"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [browser_tool, web_scraping, competitive_intelligence, playwright, n01]
tldr: "Playwright-based browser tool for N01 JS-heavy source extraction: competitor pricing pages, LinkedIn job postings, dynamic product catalogs, app stores. Falls back to requests+BeautifulSoup for static pages."
density_score: 0.89
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P04/browser_tool F2 become=browser-tool-builder F3 inject=document_loader_n01+search_strategy_n01+api_reference_research_apis F4 reason=competitor pricing pages and job postings are JS-heavy, require browser rendering F5 call=cex_compile F6 produce=browser_tool_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P04_tools/ -->

## Purpose

Static HTTP fetching fails on 40%+ of modern competitor pages (JS-rendered).
N01 Analytical Envy demands data from ALL sources, including JS-heavy pages.
This tool provides authenticated, headless browser access for intelligence gathering.

## Target Page Categories

| Category | Example Sites | Why JS-Rendered | Intelligence Value |
|----------|--------------|-----------------|-------------------|
| Competitor pricing | linear.app/pricing, notion.so/pricing | React SPA | H competitive data |
| Job postings | linkedin.com/jobs, greenhouse.io | AJAX pagination | H strategic intent |
| Product changelogs | product updates, release notes | dynamic loading | M feature tracking |
| App store listings | ProductHunt, G2, Capterra | review widgets | M social proof data |
| SaaS dashboards | any authenticated trial | full React | H feature matrix |
| Financial charts | macrotrends.net | Canvas/SVG | L (prefer API) |

## Tool Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Engine | Playwright (Chromium) | widest JS compatibility |
| Headless | true (default) | no UI needed |
| User-agent | Chrome/120 on Windows | lowest bot-detection rate |
| Viewport | 1920x1080 | ensures full page render |
| Timeout | 30s page load, 10s selector | balance coverage vs speed |
| Screenshot | on failure only | reduces storage |
| Cookie persistence | per-domain session cache | avoids repeated CAPTCHAs |

## Extraction Patterns

### Pricing Page Pattern

```
navigate(url)
wait_for_selector(".pricing, [data-testid='pricing'], #pricing")
scroll_to_bottom()  # load lazy content
extract_table(".pricing-table, .plan-comparison")
  or
extract_text_blocks(".price, .plan-name, .plan-features")
```

### Job Postings Pattern

```
navigate(linkedin_jobs_url)
wait_for_selector(".job-card-list")
scroll_auto(iterations=5, delay=2s)
extract_all(".job-card-container")
  -> title, company, location, date_posted, description
```

### Generic Content Pattern

```
navigate(url)
wait_for_load_state("networkidle")
extract("article, main, .content, [role='main']")
filter_out("nav, header, footer, aside, .cookie-banner")
```

## Anti-Bot Handling

| Detection | Mitigation |
|-----------|-----------|
| IP rate limit | rotate via residential proxy pool (optional) |
| CAPTCHA | log + skip + flag for human |
| Cloudflare 403 | 30s delay + retry with fresh session |
| Cookie wall | accept first-party cookies automatically |
| Login required | use saved session token if available |

## Output Schema

Outputs normalized DocumentChunks (see `document_loader_n01.md`):

| Field | Source |
|-------|--------|
| `chunk_id` | `{domain}_{timestamp}` |
| `source_url` | input URL |
| `source_type` | `html` |
| `content` | extracted text |
| `extraction_confidence` | selector match quality (0-1) |

## Rate Limiting

| Target Type | Delay | Max Sessions |
|-------------|-------|-------------|
| Competitor site | 3-5s between pages | 1 concurrent |
| Job aggregator | 2s between requests | 2 concurrent |
| Public news | 1s | 3 concurrent |

## Comparison vs. Alternatives

| Tool | JS Support | Cost | N01 Fit |
|------|-----------|------|---------|
| requests + BS4 | none | free | static pages only |
| This (Playwright) | full | free (local) | primary for JS pages |
| Firecrawl MCP | full | API cost | use as fallback |
| Selenium | full | slow | deprecated by Playwright |

## Integration

```
search_strategy_n01 -> URL marked "JS-heavy"
  -> browser_tool_n01 -> DocumentChunks
    -> document_loader_n01 (merge) -> research_pipeline_n01
```
