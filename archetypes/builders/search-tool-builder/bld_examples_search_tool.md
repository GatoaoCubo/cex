---
kind: examples
id: bld_examples_search_tool
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of search_tool artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: search-tool-builder
## Golden Example
INPUT: "Create search tool for Tavily AI-optimized web search"
OUTPUT:
```yaml
id: p04_search_tavily_web
kind: search_tool
pillar: P04
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
name: "Tavily Web Search"
provider: "tavily"
search_type: web
max_results: 10
result_fields:
  - title
  - url
  - content
  - score
date_range: true
domain_filter: true
language: ["en", "pt", "es"]
cost_per_query: "~$0.005"
rate_limit: "100/min"
quality: null
tags: [search_tool, tavily, web-search, ai-optimized, P04]
tldr: "Tavily AI web search: 10 results, clean text content, date/domain filters, $0.005/query"
description: "AI-optimized web search via Tavily API returning clean text results for LLM consumption"
```
## Overview
AI-optimized web search via Tavily API. Returns clean, LLM-ready text content instead of raw HTML.
Use when agent needs current web information with high-quality, pre-processed text results.
## Query
### Parameters
- `query` (string, required): natural language search query
- `max_results` (integer, optional, default: 10): results to return (1-20)
- `search_type` (enum, optional): "web" (default) or "news"
### Filtering
- Date range: supported — filter by recency (day, week, month, year)
- Domain filter: supported — include/exclude specific domains
- Language: en, pt, es supported
## Results
### Structure
Each result contains:
- `title` (string): page title
- `url` (string): source URL
- `content` (string): cleaned text content (not raw HTML)
- `score` (float): relevance score 0-1
### Ranking
Results ranked by Tavily relevance algorithm optimized for LLM consumption.
### Pagination
No cursor-based pagetion — adjust max_results parameter.
## Provider
- API: api.tavily.com/search
- Auth: env var `TAVILY_API_KEY` (NEVER hardcode)
- Rate limit: 100 requests/minute
- Cost: ~$0.005 per query ($5/1000 queries)
- Free tier: 1000 queries/month free
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p04_search_ pattern (H02 pass)
- kind: search_tool (H04 pass)
- provider: "tavily" specified (H06 pass)
- max_results: 10 >= 1 (H07 pass)
- result_fields documented (H08 pass)
- Body has all 4 sections: Overview, Query, Results, Provider (H10 pass)
- cost_per_query documented (S04 pass)
- rate_limit documented (S05 pass)
- No API keys in artifact (S07 pass)
## Anti-Example
INPUT: "Create search tool"
BAD OUTPUT:
```yaml
id: search
kind: tool
name: Search
api_key: sk-abc123xyz
quality: 7.5
tags: [search]
```
Searches the web.
FAILURES:
1. id: "search" has no `p04_search_` prefix -> H02 FAIL
2. kind: "tool" not "search_tool" -> H04 FAIL
3. quality: 7.5 (not null) -> H05 FAIL
4. Missing fields: provider, search_type, max_results -> H06 FAIL
5. api_key hardcoded (security violation) -> S07 FAIL
6. tags: only 1 item, missing "search_tool" -> S02 FAIL
7. Body missing Query, Results, Provider sections -> H10 FAIL
8. No result_fields documented -> H08 FAIL
9. No rate_limit or cost awareness -> S04, S05 FAIL
10. No filtering options documented -> S06 FAIL
