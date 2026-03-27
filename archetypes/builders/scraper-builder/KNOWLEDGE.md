---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for scraper production
sources: Web scraping best practices, selector patterns, real scraper examples
---

# Domain Knowledge: scraper

## Foundational Concept
A scraper artifact defines the EXTRACTION CONTRACT for web data collection.
It specifies which site to target, which selectors to use, how to paginate,
and what format to output. Scrapers extract UNSTRUCTURED data from HTML/DOM
and produce STRUCTURED output. They are read-only: they never modify the source.

## Selector Strategies

| Strategy | Syntax | When |
|----------|--------|------|
| CSS | `div.class > span` | Simple, readable, most common |
| XPath | `//div[@class="x"]/span` | Complex traversal, attribute matching |
| JSON-LD | `script[type="application/ld+json"]` | Structured data embedded in page |

Rule: prefer CSS for readability. Use XPath for complex traversal. Try JSON-LD first.

## Pagination Patterns

| Strategy | Detection | Example |
|----------|-----------|---------|
| next_page | `a.next` or `rel="next"` link | Most e-commerce, forums |
| infinite_scroll | Scroll + AJAX request interception | Social media, modern SPAs |
| numbered | URL pattern `?page=N` or `/page/N` | Blogs, search results |
| none | Single page or API-backed | Dashboards, detail pages |

## Rate Limiting Best Practices

| Practice | Value | Why |
|----------|-------|-----|
| Politeness delay | 1-2s between requests | Avoid IP bans |
| Concurrent requests | 1-3 max | Server load respect |
| robots.txt | Always check | Legal compliance |
| Retry on 429 | Backoff 30-60s | Rate limit recovery |

## Anti-Bot Awareness

| Level | Techniques | Complexity |
|-------|-----------|-----------|
| none | Direct fetch | Trivial |
| basic | User-Agent rotation, cookies | Low |
| cloudflare | JS challenge, TLS fingerprint | Medium |
| captcha | CAPTCHA solving service | High |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT scraper |
|------|------------|---------------------|
| client | Consumes structured API (JSON/XML) | Scraper extracts from HTML/DOM |
| connector | Bidirectional service integration | Scraper is read-only extraction |
| parser | Extracts from LLM/text output | Scraper extracts from web pages |
| cli_tool | Processes local input | Scraper accesses remote web |
