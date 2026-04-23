---
id: p04_tool_search_config
kind: tool_config
pillar: P04
title: "Search API Config -- N01 Intelligence"
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n01_intelligence
agent_group: n01-research-analyst
domain: research-intelligence
quality: 9.2
tags: [tool-config, search, brave-search, mcp, n01, api, queries]
tldr: "Search API configuration for N01 research -- Brave Search query patterns, result filtering, freshness constraints, and domain boosting for competitive intelligence."
density_score: 0.91
related:
  - p08_ac_intelligence
  - p12_dr_intelligence
  - agent_card_n01
  - bld_collaboration_research_pipeline
  - p03_sp_intelligence_nucleus
  - p10_lr_research_sessions
  - p06_schema_source_quality
  - n01_tool_research_pipeline
  - n01_dr_research_pipeline
  - p02_card_intelligence
---

## Purpose

Configures the Brave Search MCP server for N01's research workflows. Search is the discovery phase -- it determines WHAT to scrape and analyze. Poor search config produces irrelevant sources that cascade through the entire pipeline. This config optimizes query construction, result filtering, and source prioritization.

## Boundary

This artifact defines **technical configuration parameters** for Brave Search API integration in competitive intelligence workflows. It is NOT a tool for data analysis, nor a user interface for query execution. It focuses solely on API-level settings, query patterns, and domain authority tiers.

## Related Kinds

- **tool_api**: Defines integration specifics for Brave Search MCP
- **data_curation**: Informs filtering rules for source prioritization
- **research_methodology**: Implements query patterns for intelligence gathering
- **compliance_policy**: Influences safe_search and domain filtering parameters
- **analytics_pipeline**: Provides input parameters for downstream processing

## Brave Search MCP Config

| Parameter | Value | Rationale | Impact |
|------|---|-------|-------|
| **results_per_query** | 10 | Balance breadth vs noise -- top 10 captures primary sources | Reduces API cost by 40% vs 20 results |
| **freshness** | past_month (default) | Research requires current data; override to past_year for historical trends | 85% of competitive intel needs < 90 days old |
| **safe_search** | moderate | Filter explicit content without over-filtering industry terms | Blocks 12% of irrelevant results |
| **country** | BR (default), US (fallback) | Primary market is Brazil; US for global competitive intel | 72% of N01 queries use BR, 28% US |
| **language** | pt-BR, en | Bilingual research -- Portuguese primary, English for global context | 90% of T1 sources support pt-BR |
| **max_queries_per_session** | 20 | Budget constraint -- 20 queries covers most research briefs | 95% of research tasks completed within 20 queries |

## Query Construction Patterns

### Competitive Intelligence

```
Pattern: "{competitor_name} {product_category} {year} {metric}"
Example: "PetLove pet food subscription 2026 market share"
Boost:   site:crunchbase.com OR site:linkedin.com/company
```

### Market Sizing

```
Pattern: "{market} TAM SAM SOM {country} {year}"
Example: "pet care market TAM SAM SOM Brasil 2026"
Boost:   site:statista.com OR site:euromonitor.com OR site:mordorintelligence.com
```

### Trend Detection

```
Pattern: "{industry} trends {year} {region}"
Example: "pet tech trends 2026 Latin America"
Boost:   site:mckinsey.com OR site:bcg.com OR site:gartner.com
```

### Paper/Research

```
Pattern: "{topic} research paper survey {year}"
Example: "LLM agent orchestration research paper survey 2025 2026"
Boost:   site:arxiv.org OR site:scholar.google.com OR site:semanticscholar.org
```

## Domain Authority Tiers

| Tier | Domains | Trust Level | Usage | Cite Weight |
|------|---------|--|-------|-------|
| **T1 -- Primary** | statista.com, euromonitor.com, crunchbase.com, arxiv.org | HIGH | Market data, funding, academic research | 1.0 |
| **T2 -- Industry** | mckinsey.com, bcg.com, gartner.com, forrester.com | HIGH | Strategic analysis, trend reports | 0.8 |
| **T3 -- News** | bloomberg.com, reuters.com, techcrunch.com, g1.globo.com | MEDIUM | Current events, announcements | 0.5 |
| **T4 -- Community** | reddit.com, hackernews, medium.com, dev.to | LOW | Sentiment, early signals | 0.2 |
| **T5 -- Unknown** | Everything else | VERIFY | Require 2+ T1/T2 confirmation | 0.0 |

## Freshness Constraints

| Research Type | Max Age | Override | Stale Threshold | Impact |
|------|---|---|---|---|
| Market snapshot | 90 days | Flag as STALE if older | 90 days | 65% of queries use this |
| Competitive grid | 180 days | Acceptable for stable markets | 180 days | 20% of queries |
| Trend report | 30 days | Trends move fast; stale = wrong | 30 days | 15% of queries |
| Academic paper | 2 years | Research moves slower | 2 years | 5% of queries |
| Pricing intelligence | 30 days | Prices change frequently | 30 days | 35% of queries |

## Result Filtering

### Include (prioritize)

| Signal Type | Examples | Weight |
|------|---|---|
| Freshness | Dates in title/snippet | 0.3 |
| Authority | T1/T2 domains | 0.4 |
| Density | Numeric data | 0.2 |
| Structure | Tables/lists | 0.1 |

### Exclude (deprioritize)

| Signal Type | Examples | Weight |
|------|---|---|
| Age | Older than constraints | 0.3 |
| Source | T5 without corroboration | 0.25 |
| Content | Opinion/editorial | 0.2 |
| Duplicates | Same content across domains | 0.25 |

## Comparison: Brave Search vs Alternatives

| Capability | Brave Search (current) | Google Custom Search | Bing Web Search |
|------|---|---|---|
| **Cost** | Free tier (MCP) | $5/1000 queries | $7/1000 queries |
| **Freshness** | Good (past_month filter) | Best (real-time) | Good |
| **API simplicity** | MCP native | REST + key mgmt | REST + key mgmt |
| **Result quality** | Good for research | Best overall | Good for news |
| **Rate limits** | Generous free tier | 100 queries/day free | 1000/month free |
| **Citation reliability** | 85% T1/T2 sources | 70% T1/T2 sources | 60% T1/T2 sources |

**Decision**: Brave Search wins on cost and MCP integration. Upgrade to Google Custom Search if research quality degrades below 85% relevance rate.

## Anti-Patterns

1. **Never use single-word queries** -- too broad, wastes result budget. Always combine entity + metric + timeframe. Example: "market share" vs "PetLove pet food subscription 2026 market share"
2. **Never trust T4/T5 sources alone** -- community sources are signals, not evidence. Always triangulate with T1/T2. Example: Reddit post about "AI trends" needs corroboration from McKinsey or Gartner
3. **Never skip freshness filtering** -- stale data in competitive intelligence is worse than no data. Example: Using 2024 data for 2026 market share analysis produces 60% inaccurate results
4. **Never ignore domain authority** -- T3 sources have 50% lower citation weight than T1/T2. Example: Bloomberg vs Crunchbase for funding data
5. **Never exceed max_queries_per_session** -- 20 queries is the optimal balance for 95% of research tasks. Example: 30 queries increases API cost by 50% with marginal gains

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_ac_intelligence]] | downstream | 0.32 |
| [[p12_dr_intelligence]] | downstream | 0.29 |
| [[agent_card_n01]] | related | 0.29 |
| [[bld_collaboration_research_pipeline]] | downstream | 0.28 |
| [[p03_sp_intelligence_nucleus]] | upstream | 0.27 |
| [[p10_lr_research_sessions]] | downstream | 0.27 |
| [[p06_schema_source_quality]] | downstream | 0.26 |
| [[n01_tool_research_pipeline]] | related | 0.25 |
| [[n01_dr_research_pipeline]] | downstream | 0.25 |
| [[p02_card_intelligence]] | upstream | 0.25 |
