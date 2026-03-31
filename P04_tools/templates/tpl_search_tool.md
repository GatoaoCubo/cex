---
id: p04_search_tool_NAME
kind: search_tool
pillar: P04
version: 1.0.0
title: "Template - Search Tool"
tags: [template, search, api, web, query]
tldr: "Configures a search tool for web or knowledge base queries. Defines provider, result format, rate limits, and dedup strategy."
quality: null
---

# Search Tool: [NAME]

## Purpose
Enables agents to search external sources (web, docs, databases) and return structured results.

## Configuration
```yaml
provider: [google | bing | searxng | tavily]
api_key: "[API_KEY]"
max_results: [5 | 10 | 20]
safe_search: [strict | moderate | off]
language: [en | pt-BR | auto]
region: [us | br | auto]
```

## Capabilities

| Provider | Results/min | Cost | Quality |
|---|---|---|---|
| Google | 100 | USD 5/1K | Best relevance |
| Bing | 1000 | USD 3/1K | Good + news |
| SearXNG | unlimited | Free | Self-hosted, variable |
| Tavily | 1000 | Free tier | AI-optimized snippets |

## Error Handling
- **No results**: Rephrase query, retry with broader terms
- **Rate limited**: Queue + backoff (60s)
- **Provider down**: Fallback to alternate provider
- **Invalid query**: Return empty + validation error

## Quality Gate
- [ ] Provider and API key configured
- [ ] Rate limits defined
- [ ] Result format includes title + url + snippet
- [ ] Fallback provider configured
