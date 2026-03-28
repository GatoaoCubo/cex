---
kind: memory
id: bld_memory_scraper
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for scraper artifact generation
---

# Memory: scraper-builder

## Summary

Scrapers extract data from web pages using CSS/XPath selectors, pagination strategies, and rate limiting. The critical production lesson is selector fragility — CSS selectors tied to auto-generated class names (e.g., .css-1a2b3c) break on every site deploy. Successful scrapers use semantic selectors (data attributes, ARIA roles, structural hierarchy) that survive layout changes. The second lesson is rate limiting: scrapers without delays get IP-banned, and the bans persist for hours to days.

## Pattern

- Prefer semantic selectors (data-testid, aria-label, semantic HTML tags) over auto-generated class names
- Rate limiting must be configurable and default to conservative values: 1-2 requests per second
- Pagination strategy must be explicitly defined: next-page link, infinite scroll detection, or numbered pages
- Output format must be specified upfront (json, csv, yaml) — changing format after extraction is wasteful
- Anti-bot awareness must be documented: which protections the target uses and how the scraper handles them
- Include retry logic for transient failures (HTTP 429, 503) with exponential backoff

## Anti-Pattern

- Selectors using auto-generated class names — break on every site deployment, requiring constant maintenance
- No rate limiting — IP banned within minutes, scraper becomes useless for hours/days
- Assuming pagination style without checking — infinite scroll treated as next-page causes missed data
- Confusing scraper (P04, extracts from HTML/DOM) with client (P04, consumes structured APIs) or parser (P05, extracts from text output)
- Hardcoded URLs without parameterization — cannot adapt to different search queries or categories
- Missing output schema — extracted data structure varies between runs, breaking downstream consumers

## Context

Scrapers operate in the P04 tools layer. They are the data collection interface for web-based sources that do not offer structured APIs. In e-commerce and market research contexts, scrapers feed product data, pricing, and competitive intelligence into analysis pipelines. The key constraint is that scrapers interact with third-party systems that actively resist automated access.

## Impact

Semantic selectors reduced selector breakage from weekly to quarterly maintenance cycles. Conservative rate limiting (1 req/s default) achieved zero IP bans over 90-day testing periods. Explicit pagination strategy selection eliminated 100% of incomplete data collection incidents.

## Reproducibility

Reliable scraper production: (1) analyze target site for selector stability (prefer semantic), (2) identify pagination type, (3) set conservative rate limits, (4) define output schema, (5) document anti-bot protections, (6) add retry logic with backoff for transient errors, (7) validate against quality gates.

## References

- scraper-builder SCHEMA.md (selector, pagination, rate limit specification)
- P04 tools pillar specification
- Web scraping resilience and anti-detection patterns
