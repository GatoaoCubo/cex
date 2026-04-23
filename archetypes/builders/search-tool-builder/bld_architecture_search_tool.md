---
kind: architecture
id: bld_architecture_search_tool
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of search_tool — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Search Tool"
version: "1.0.0"
author: n03_builder
tags: [search_tool, builder, examples]
tldr: "Golden and anti-examples for search tool construction, demonstrating ideal structure and common pitfalls."
domain: "search tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_search_tool_builder
  - search-tool-builder
  - p11_qg_search_tool
  - bld_examples_search_tool
  - bld_collaboration_search_tool
  - bld_architecture_retriever
  - bld_instruction_search_tool
  - bld_output_template_search_tool
  - p01_kc_search_tool
  - bld_knowledge_card_search_tool
---

# Architecture: search_tool
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| provider | External search service (Tavily, Serper, etc.) | search_tool | required |
| search_type | Kind of search (web, semantic, hybrid, news) | search_tool | required |
| max_results | Maximum results per query | search_tool | required |
| result_fields | Data fields in each result | search_tool | recommended |
| date_range | Date filtering support | search_tool | optional |
| domain_filter | Domain whitelist/blacklist support | search_tool | optional |
| rate_limit | Query throttling policy | search_tool | recommended |
| cost_per_query | Per-query cost for budget tracking | search_tool | recommended |
| agent | Runtime caller that issues search queries | P02 | consumer |
| function_def | Interface wrapping search as callable function | P04 | consumer |
## Dependency Graph
```
provider     --provides-->  search_results
search_type  --constrains-> query (what kind of search)
max_results  --constrains-> results (how many returned)
result_fields --defines-->  result_structure
date_range   --filters-->   results (by time)
domain_filter --filters-->  results (by source)
rate_limit   --throttles--> queries
agent        --invokes-->   search_tool (query)
function_def --wraps-->     search_tool (as callable)
```
| From | To | Type | Data |
|------|----|------|------|
| provider | search_results | provides | External search service API |
| search_type | query | constrains | What kind of search to perform |
| max_results | results | constrains | How many results returned |
| result_fields | result_structure | defines | What data each result contains |
| rate_limit | queries | throttles | Requests per time unit |
| agent | search_tool | invokes | Query string for search |
## Boundary Table
| search_tool IS | search_tool IS NOT |
|---------------|-------------------|
| External search service integration | Local vector store search (that is retriever) |
| Returns ranked results from web/news/semantic index | File ingestion and chunking (that is document_loader) |
| Stateless query-response (no navigation) | Web navigation with DOM interaction (that is browser_tool) |
| Provider-specific API integration | Generic HTTP client (that is api_client) |
| Cost-aware with per-query pricing | Free unlimited access (always has quotas/costs) |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| provider | provider, cost_per_query | Which service and at what cost |
| query | search_type, max_results | How to search |
| filtering | date_range, domain_filter, language | Narrow results |
| results | result_fields | What comes back |
| governance | rate_limit | Throttle and protect quotas |
| consumers | agent, function_def | Runtime callers |
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Search over local embeddings | search_tool | retriever | retriever=local vector store; search_tool=external API |
| Navigate site to find data | search_tool | browser_tool | browser_tool=DOM interaction; search_tool=API query |
| Load and chunk a document | search_tool | document_loader | loader=file ingestion; search_tool=query for results |
## Decision Tree
- External web/news search API? → search_tool
- Local vector/keyword index? → retriever
- Navigate and scrape pages? → browser_tool
- Ingest files into chunks? → document_loader
## Neighbor Comparison
| Dimension | search_tool | retriever | Difference |
|---|---|---|---|
| Data source | External API (web) | Local vector store | search_tool calls remote; retriever is local |
| Cost | Per-query pricing | Free (after indexing) | search_tool has ongoing API costs |
| Freshness | Real-time web | Stale until re-indexed | search_tool always current |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_search_tool_builder]] | upstream | 0.70 |
| [[search-tool-builder]] | upstream | 0.61 |
| [[p11_qg_search_tool]] | downstream | 0.49 |
| [[bld_examples_search_tool]] | upstream | 0.49 |
| [[bld_collaboration_search_tool]] | downstream | 0.48 |
| [[bld_architecture_retriever]] | sibling | 0.46 |
| [[bld_instruction_search_tool]] | upstream | 0.45 |
| [[bld_output_template_search_tool]] | upstream | 0.45 |
| [[p01_kc_search_tool]] | upstream | 0.45 |
| [[bld_knowledge_card_search_tool]] | upstream | 0.40 |
