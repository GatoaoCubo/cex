---
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of scraper — inventory, dependencies, and architectural position
---

# Architecture: scraper in the CEX

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, target_site, output_format, etc.) | scraper-builder | active |
| target_definition | URL patterns and page types the scraper operates on | author | active |
| selectors | CSS or XPath selectors for data extraction from DOM | author | active |
| pagination_strategy | How the scraper navigates across multiple pages (next_page, scroll, numbered) | author | active |
| rate_limiting | Request throttling and delay configuration | author | active |
| anti_bot_config | Anti-detection measures (headers, user-agent rotation, proxy) | author | active |
| output_format | Structure of extracted data (json, csv, yaml) | author | active |

## Dependency Graph

```
target_site     --scraped_by-->  scraper  --produces-->     structured_data
rag_source      --references-->  scraper  --consumed_by-->  ingestion_pipeline
scraper         --signals-->     scrape_error
```

| From | To | Type | Data |
|------|----|------|------|
| target_site (web) | scraper | data_flow | HTML/DOM content fetched for extraction |
| scraper | structured_data | produces | extracted data in specified output format |
| rag_source (P01) | scraper | dependency | source URL definition may reference scraper |
| scraper | ingestion_pipeline | consumes | pipeline receives extracted data for processing |
| scraper | scrape_error (P12) | signals | emitted on extraction failure or anti-bot block |
| parser (P05) | scraper | dependency | parser may post-process scraper output |

## Boundary Table

| scraper IS | scraper IS NOT |
|------------|---------------|
| An HTML/DOM data extractor with CSS/XPath selectors | A structured API consumer (client P04) |
| Configured with pagination and rate limiting | A bidirectional integration adapter (connector P04) |
| Produces structured data from web pages | A text extractor from LLM output (parser P05) |
| Includes anti-bot awareness and proxy support | A protocol server exposing tools (mcp_server P04) |
| Scoped to specific target sites and page types | A background process with continuous execution (daemon P04) |
| Output formatted as json, csv, or yaml | A reusable multi-phase capability (skill P04) |

## Layer Map

| Layer | Components | Purpose |
|-------|------------|---------|
| Target | target_definition, rag_source | Identify what sites and pages to scrape |
| Extraction | selectors, pagination_strategy | Navigate pages and extract data from DOM |
| Protection | rate_limiting, anti_bot_config | Throttle requests and avoid detection |
| Output | output_format, structured_data | Format and deliver extracted data |
| Integration | ingestion_pipeline, parser, scrape_error | Process output and handle failures |
