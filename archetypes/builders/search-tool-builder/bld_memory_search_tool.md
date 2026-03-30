---
id: p10_lr_search_tool_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: edison
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
agent_node: edison
keywords: [search tool, web search, semantic search, tavily, serper, brave, exa, max results, cost, api key, rate limit]
---

## Summary
Search tools are the primary way agents access current information, and they are the most likely P04 kind to generate unexpected costs. The three load-bearing constraints are: max_results (prevents token waste), cost_per_query (enables budget tracking), and API key security (prevents credential exposure).
## Pattern
**Bounded results, documented costs, env-var-only authentication.**
Max results:
- Default: 10 for general use
- Quick lookup: 3-5 results
- Deep research: 15-20 results
- NEVER unbounded — agents will consume all results, wasting tokens
Cost awareness:
- Document cost_per_query in frontmatter
- Calculate: agent may issue 10-50 searches per task
- At $0.005/query, 50 queries = $0.25/task — multiplied by concurrent agents, this adds up
- Budget-aware agents should check remaining budget before searching
API key security:
- NEVER in frontmatter, NEVER in body
- Always: `auth: env var PROVIDER_API_KEY`
- Security scanners flag hardcoded keys — causes commit rejects
Provider selection:
- Tavily: best for AI agents (clean text, not raw HTML)
- Serper: cheapest for Google results ($0.001/query)
- Exa: best for semantic/similar content search
- Brave: best free tier, privacy-focused
## Anti-Pattern
- No max_results (50+ results per query, token budget blown in 3 queries).
- No cost documentation (production bill surprise — $200+ in a week).
- Hardcoded API keys (security incident, key rotation forced).
- No rate limit documentation (429 errors when agent searches in tight loop).
- Wrong provider for use case (using Google for semantic search, Exa for news).
- Confusing search_tool with retriever (search = external API; retriever = local vector DB).
## Context
The 2048-byte body limit is sufficient for provider documentation and query/result specs. Cost_per_query is the most overlooked field — agents issue many searches, and costs compound. The provider field drives all other decisions: result format, available filters, cost, rate limits. Choose provider first, then document everything else around it.
