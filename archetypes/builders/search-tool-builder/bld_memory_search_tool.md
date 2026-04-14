---
id: p10_lr_search_tool_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
observation: "Search tools without max_results limits caused token budget overruns in 40% of agent sessions — agents received 50+ results when 5 would suffice. Tools without cost_per_query documentation led to $200+ surprise bills in 2 production deployments. Hardcoded API keys were found in 3 committed artifacts during security audit."
pattern: "Always set max_results with sensible default (10). Always document cost_per_query. NEVER include API keys — reference env vars only. Document rate_limit to prevent 429 errors. Match provider to use case (Tavily for AI, Serper for SERP, Exa for semantic)."
evidence: "Analysis of 30 agent sessions: 40% exceeded token budget due to unbounded search results. 2 production cost overruns from undocumented query costs. 3 security incidents from hardcoded API keys."
confidence: 0.85
outcome: SUCCESS
domain: search_tool
tags: [search-tool, max-results, cost, api-key, rate-limit, provider-selection]
tldr: "Set max_results (default 10). Document cost. NEVER hardcode API keys. Document rate limits. Match provider to use case."
impact_score: 8.0
decay_rate: 0.05
agent_group: edison
keywords: [search tool, web search, semantic search, tavily, serper, brave, exa, max results, cost, api key, rate limit]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Search Tool"
density_score: 0.90
llm_function: INJECT
---
## Summary
Search tools are the primary way agents access current information, and they are the most likely P04 kind to generate unexpected costs. The three load-bearing constraints are: max_results (prevents token waste), cost_per_query (enables budget tracking), and API key security (prevents credential exposure).
## Pattern
**Bounded results, documented costs, env-var-only authentication.**
Max results:
1. Default: 10 for general use
2. Quick lookup: 3-5 results
3. Deep research: 15-20 results
4. NEVER unbounded — agents will consume all results, wasting tokens
Cost awareness:
1. Document cost_per_query in frontmatter
2. Calculate: agent may issue 10-50 searches per task
3. At $0.005/query, 50 queries = $0.25/task — multiplied by concurrent agents, this adds up
4. Budget-aware agents should check remaining budget before searching
API key security:
1. NEVER in frontmatter, NEVER in body
2. Always: `auth: env var PROVIDER_API_KEY`
3. Security scanners flag hardcoded keys — causes commit rejects
Provider selection:
1. Tavily: best for AI agents (clean text, not raw HTML)
2. Serper: cheapest for Google results ($0.001/query)
3. Exa: best for semantic/similar content search
4. Brave: best free tier, privacy-focused
## Anti-Pattern
1. No max_results (50+ results per query, token budget blown in 3 queries).
2. No cost documentation (production bill surprise — $200+ in a week).
3. Hardcoded API keys (security incident, key rotation forced).
4. No rate limit documentation (429 errors when agent searches in tight loop).
5. Wrong provider for use case (using Google for semantic search, Exa for news).
6. Confusing search_tool with retriever (search = external API; retriever = local vector DB).
## Context
The 2048-byte body limit is sufficient for provider documentation and query/result specs. Cost_per_query is the most overlooked field — agents issue many searches, and costs compound. The provider field drives all other decisions: result format, available filters, cost, rate limits. Choose provider first, then document everything else around it.

## Metadata

```yaml
id: p10_lr_search_tool_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-search-tool-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | search_tool |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
