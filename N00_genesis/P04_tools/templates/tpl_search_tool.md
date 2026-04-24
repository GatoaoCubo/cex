---
id: p04_search_tool_NAME
kind: search_tool
8f: F5_call
pillar: P04
version: 1.0.0
title: "Template - Search Tool"
tags: [template, search, api, web, query]
tldr: "Configures a search tool for web or knowledge base queries. Defines provider, result format, rate limits, and dedup strategy."
quality: 9.0
updated: "2026-04-07"
domain: "tool integration"
author: n03_builder
created: "2026-04-07"
density_score: 0.98
related:
  - bld_examples_search_tool
  - p04_search_tavily
  - search-tool-builder
  - bld_knowledge_card_search_tool
  - p10_lr_search_tool_builder
  - model-provider-builder
  - bld_instruction_search_tool
  - bld_collaboration_model_provider
  - p11_qg_search_tool
  - p01_kc_search_tool
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
1. **No results**: Rephrase query, retry with broader terms
2. **Rate limited**: Queue + backoff (60s)
3. **Provider down**: Fallback to alternate provider
4. **Invalid query**: Return empty + validation error

## Quality Gate
1. [ ] Provider and API key configured
2. [ ] Rate limits defined
3. [ ] Result format includes title + url + snippet
4. [ ] Fallback provider configured

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `search_tool` |
| Pillar | P04 |
| Domain | tool integration |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_search_tool]] | downstream | 0.36 |
| [[p04_search_tavily]] | sibling | 0.36 |
| [[search-tool-builder]] | related | 0.35 |
| [[bld_knowledge_card_search_tool]] | upstream | 0.35 |
| [[p10_lr_search_tool_builder]] | downstream | 0.34 |
| [[model-provider-builder]] | upstream | 0.34 |
| [[bld_instruction_search_tool]] | upstream | 0.34 |
| [[bld_collaboration_model_provider]] | upstream | 0.32 |
| [[p11_qg_search_tool]] | downstream | 0.31 |
| [[p01_kc_search_tool]] | upstream | 0.31 |
