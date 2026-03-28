---
kind: knowledge_card
id: bld_knowledge_card_scraper
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for scraper production — atomic searchable facts
sources: scraper-builder MANIFEST.md + SCHEMA.md, web scraping best practices, selector patterns
---

# Domain Knowledge: scraper
## Executive Summary
Scrapers are web data extraction artifacts that define the contract for collecting structured data from HTML/DOM pages — target site, selectors (CSS/XPath/JSON-LD), pagination strategy, rate limiting, and output format. Each scraper is read-only (never modifies the source) and converts unstructured web content into structured output. They differ from clients (which consume structured APIs), connectors (which integrate bidirectionally), parsers (which extract from local text/LLM output), and MCP servers (which expose tools via protocol) by targeting remote web pages with DOM-based extraction.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools/infrastructure) |
| Kind | `scraper` (exact literal) |
| ID pattern | `p04_scraper_{slug}` |
| Required frontmatter | 14 fields |
| Quality gates | HARD + SOFT (per QUALITY_GATES.md) |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Selector strategies | CSS, XPath, JSON-LD |
| Pagination types | next_page, infinite_scroll, numbered, none |
| Output formats | json, csv, yaml |
## Patterns
| Pattern | Application |
|---------|-------------|
| JSON-LD first | Try structured data extraction before DOM selectors |
| CSS over XPath | Prefer CSS for readability; XPath for complex traversal |
| Politeness delay | 1-2s between requests; avoid IP bans |
| Max concurrent | 1-3 concurrent requests; respect server load |
| robots.txt compliance | Always check before scraping; legal requirement |
| Retry on 429 | Backoff 30-60s on rate limit responses |
| Output normalization | Clean whitespace, normalize encoding, deduplicate |
### Anti-Bot Awareness Levels
| Level | Techniques | Complexity |
|-------|-----------|-----------|
| none | Direct fetch | Trivial |
| basic | User-Agent rotation, cookies | Low |
| cloudflare | JS challenge, TLS fingerprint | Medium |
| captcha | CAPTCHA solving service | High |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No rate limiting | IP bans; site degradation; legal risk |
| Ignoring robots.txt | Legal compliance violation |
| XPath for simple selections | Unnecessarily complex; use CSS |
| No pagination strategy | Only gets first page; misses most data |
| No output format specified | Consumers cannot parse undefined format |
| Scraper that modifies source | Scrapers are read-only; side effects are wrong |
| No anti-bot awareness declared | Fails silently on protected sites |
## Application
1. Identify target site and data to extract
2. Check robots.txt and legal compliance
3. Choose selector strategy: try JSON-LD first, then CSS, then XPath
4. Define all selectors with field name and extraction pattern
5. Set pagination strategy (next_page/infinite_scroll/numbered/none)
6. Configure rate limiting: delay, max concurrent, retry policy
7. Specify output format (json/csv/yaml) and normalization rules
8. Validate: all HARD + SOFT gates, body <= 4096 bytes
## References
- scraper-builder SCHEMA.md v1.0.0
- Web scraping best practices (politeness, robots.txt)
- CSS Selectors Level 4 (W3C)
- Schema.org JSON-LD structured data
