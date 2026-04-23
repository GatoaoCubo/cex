---
kind: knowledge_card
id: bld_knowledge_card_search_tool
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for search_tool production — web and semantic search integration
sources: Tavily docs, Serper docs, Brave Search API, Exa docs, Google Grounding API
quality: 9.1
title: "Knowledge Card Search Tool"
version: "1.0.0"
author: n03_builder
tags: [search_tool, builder, examples]
tldr: "Golden and anti-examples for search tool construction, demonstrating ideal structure and common pitfalls."
domain: "search tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - search-tool-builder
  - p10_lr_search_tool_builder
  - p03_sp_search_tool_builder
  - bld_examples_search_tool
  - bld_instruction_search_tool
  - bld_collaboration_search_tool
  - p04_search_tavily
  - p01_kc_search_tool
  - p04_search_tool_NAME
  - bld_config_search_tool
---

# Domain Knowledge: search_tool
## Executive Summary
Search tools connect LLM agents to external search services, returning ranked results for queries. They are the primary way agents access current information beyond their training data. Each provider offers different strengths: Tavily for AI-optimized clean text, Serper for Google SERP data, Exa for neural/semantic search, Brave for privacy-focused results.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P04 (tools) |
| llm_function | CALL (invocable) |
| Search types | web, semantic, hybrid, news, images |
| Result fields | title, url, snippet (minimum), score, content (optional) |
| Auth | API key via environment variable (NEVER hardcoded) |
| Cost model | Per-query pricing varies by provider |
## Provider Comparison
| Provider | Type | Cost | Strengths | Best For |
|----------|------|------|-----------|----------|
| Tavily | AI-optimized | ~$0.005/query | Clean text, LLM-ready | AI agent search |
| Serper | Google SERP | ~$0.001/query | Google results, structured | General web search |
| Perplexity | AI search | ~$0.005/query | Citations, summaries | Research queries |
| Brave | Web search | free tier + paid | Privacy, no tracking | Privacy-conscious |
| Exa | Neural search | ~$0.01/query | Semantic similarity | Content discovery |
| Google | Grounding | varies | Official Google, fresh | Gemini integration |
## Patterns
- **Provider selection**: match provider to use case — Tavily for AI agents, Serper for SERP, Exa for similarity
- **Max results tuning**: 3-5 for quick lookups, 10-20 for research, 1 for fact-checking
- **Result enrichment**: some providers return full content (Tavily), others just snippets (Serper)
- **Cost awareness**: always document cost_per_query — agents may issue many searches per task
| Pattern | Example | When to use |
|---------|---------|-------------|
| Quick lookup | max_results: 3, web search | Simple fact-checking |
| Deep research | max_results: 20, hybrid search | Comprehensive topic research |
| Content discovery | Exa, semantic search | Finding similar content |
| News monitoring | news search, date filter | Recent events tracking |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No provider specified | "Search" is meaningless without knowing which service |
| Hardcoded API keys | Security vulnerability — use env vars |
| No max_results limit | Unbounded results waste tokens and money |
| No rate limit awareness | Quota exhaustion, HTTP 429 errors |
| Confusing with retriever | search_tool = external; retriever = local vector store |
| No cost tracking | Agent issues 100 queries, bill surprises follow |
## Application
1. Choose provider based on use case and budget
2. Define search type (web, semantic, hybrid, news)
3. Set max_results with sensible default (10)
4. Document result fields returned by provider
5. Document filtering options (date, domain, language)
6. Document cost per query and rate limits
7. Store API key in env var, reference in artifact
## References
- Tavily: tavily.com documentation
- Serper: serper.dev documentation
- Brave: brave.com/search/api documentation
- Exa: exa.ai documentation
- Perplexity: perplexity.ai API documentation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[search-tool-builder]] | downstream | 0.58 |
| [[p10_lr_search_tool_builder]] | downstream | 0.56 |
| [[p03_sp_search_tool_builder]] | downstream | 0.52 |
| [[bld_examples_search_tool]] | downstream | 0.50 |
| [[bld_instruction_search_tool]] | downstream | 0.50 |
| [[bld_collaboration_search_tool]] | downstream | 0.48 |
| [[p04_search_tavily]] | downstream | 0.46 |
| [[p01_kc_search_tool]] | sibling | 0.45 |
| [[p04_search_tool_NAME]] | downstream | 0.40 |
| [[bld_config_search_tool]] | downstream | 0.38 |
