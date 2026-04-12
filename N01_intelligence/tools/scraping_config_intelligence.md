---
id: p04_tool_scraping_config
kind: tool_config
pillar: P04
title: "Web Scraping Config -- N01 Intelligence"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n01_intelligence
agent_group: n01-research-analyst
domain: research-intelligence
quality: 8.9
tags: [tool-config, scraping, firecrawl, fetch, mcp, n01, rate-limits]
tldr: "Scraping rules for N01 research -- rate limits, retry policy, content extraction priorities, and domain-specific selectors for firecrawl and fetch MCP servers."
density_score: 0.93
---

## Purpose

Configures web scraping behavior for N01's two extraction MCP servers (firecrawl and fetch). Without this config, scraping is unthrottled and unfocused -- producing noisy data that wastes context window budget. This config enforces rate limits, content priorities, and domain-specific extraction rules.

## MCP Server Configs

### firecrawl (Primary Scraper)

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **max_pages_per_domain** | 10 | Prevents over-crawling; 10 pages captures site structure without exhausting rate limits |
| **request_delay_ms** | 1500 | 1.5s between requests -- respects robots.txt spirit, avoids IP blocks |
| **timeout_ms** | 15000 | 15s per page -- balances completeness vs pipeline speed |
| **max_retries** | 2 | Retry on 429/503; 3rd failure = skip (don't block pipeline) |
| **content_format** | markdown | Structured extraction to markdown -- feeds directly into 8F pipeline |
| **include_metadata** | true | Capture title, description, publish_date for freshness validation |
| **follow_links** | false | Stay on target page -- link following is separate research step |
| **extract_tables** | true | Tables contain competitive data (pricing, features, specs) |

### fetch (Fallback/Direct)

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| **max_size_bytes** | 5242880 | 5MB cap -- prevents memory issues on large PDFs |
| **timeout_ms** | 30000 | 30s for direct fetch (allows larger downloads) |
| **user_agent** | CEX-Research/1.0 | Identify as research bot -- transparency |
| **accept_types** | text/html, application/pdf, text/markdown | Only content types N01 can process |
| **ignore_robots** | true | Research exemption -- fetch is for specific URLs, not crawling |

## Domain-Specific Rules

| Domain Pattern | Action | Selector/Rule |
|----------------|--------|---------------|
| `*.linkedin.com` | Skip | Anti-scraping; use manual research instead |
| `*.github.com` | Fetch raw | Use raw.githubusercontent.com for file content |
| `*.arxiv.org` | Fetch PDF | Use /pdf/ URL variant for full papers |
| `*.statista.com` | Extract tables | Focus on data tables, skip navigation |
| `*.crunchbase.com` | Extract structured | Company profiles, funding rounds |
| `*.g1.globo.com` | Extract article | Skip ads, comments, sidebars |
| `news.*` | Extract article | Use article-body selectors, skip chrome |

## Content Extraction Priorities

For each scraped page, extract in this order (stop when context budget exhausted):

1. **Data tables** -- pricing grids, feature matrices, spec sheets (highest density)
2. **Headings + first paragraphs** -- captures structure and key claims
3. **Lists and bullet points** -- compressed information, high density
4. **Full paragraphs** -- narrative content (lowest density, only if budget allows)

## Rate Limit Recovery

| HTTP Status | Action | Wait |
|-------------|--------|------|
| 429 (Too Many Requests) | Retry with exponential backoff | 3s, 9s, skip |
| 403 (Forbidden) | Log and skip domain | N/A |
| 503 (Service Unavailable) | Retry once | 5s |
| Timeout | Log as incomplete, continue pipeline | N/A |

## Anti-Patterns

1. **Never scrape without a search context** -- firecrawl after brave-search, not standalone. Unfocused scraping wastes budget.
2. **Never follow links by default** -- link following explodes page count. Research each link as a deliberate decision.
3. **Never process >5MB files inline** -- chunk large PDFs through markitdown first.

## Validation

```bash
# Verify firecrawl MCP is responsive
npx firecrawl-mcp --health 2>&1 | grep -i "ok\|ready"

# Verify fetch MCP is responsive  
uvx mcp-server-fetch --health 2>&1 | grep -i "ok\|ready"

# Test extraction on known page
npx firecrawl-mcp scrape --url "https://example.com" --format markdown
```
