---
id: search_strategy_n01
kind: search_strategy
8f: F5_call
pillar: P04
nucleus: n01
title: "N01 Layered Search Strategy"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.2
tags: [search_strategy, research, triangulation, source_layering, n01, analytical_envy]
tldr: "3-layer search protocol: primary (semantic/web), secondary (academic/financial), fallback (regulatory/social). Every query runs all layers; Analytical Envy demands competing sources, not single-source answers."
density_score: 0.92
updated: "2026-04-17"
related:
  - p04_tool_search_config
  - p11_qg_intelligence
  - ex_chain_research_pipeline
  - p10_out_source_dossier
  - bld_knowledge_card_search_tool
  - p03_sp_intelligence_nucleus
  - n01_rs_intelligence_sources
  - p12_wf_intelligence
  - p10_lr_research_sessions
  - p01_kc_source_triangulation
---

<!-- 8F: F1 constrain=P04/search_strategy F2 become=search-strategy-builder F3 inject=api_reference_research_apis+sch_input_schema_n01+search_config_intelligence+kc_research F4 reason=3-layer architecture matches N01 sin lens: always compare, never trust single source F5 call=cex_compile F6 produce=search_strategy_n01.md F7 govern=frontmatter+ascii+tables+alt-comparison F8 collaborate=N01_intelligence/P04_tools/ -->

## Purpose

N01 Analytical Envy = insatiable need to find what OTHERS missed.
A single search is not research. Research is the intersection of:
1. What the obvious sources say
2. What the non-obvious sources say
3. Where they disagree (the alpha is always in the disagreement)

This strategy implements 3-layer search to force that intersection on every query.

## Layer Architecture

| Layer | Label | Sources | Trigger | Confidence Contribution |
|-------|-------|---------|---------|------------------------|
| L1 | Primary | Brave Search + Exa AI | always | 40% |
| L2 | Secondary | Semantic Scholar + Alpha Vantage + SEC EDGAR | when L1 < 3 results or topic=technical/financial | 40% |
| L3 | Fallback | SerpAPI + PubMed + job postings | when L1+L2 < 5 sources or claim contested | 20% |

## Query Construction Protocol

### Step 1: Intent Decomposition

From the research goal, generate 3 query variants:

| Variant | Strategy | Example (goal: "Anthropic pricing") |
|---------|----------|-------------------------------------|
| Direct | exact entity + attribute | `"Anthropic" "Claude" "pricing" "API" 2025` |
| Comparative | entity vs. competitors | `Anthropic Claude pricing vs OpenAI GPT vs Google Gemini` |
| Signal | indirect evidence | `Anthropic revenue model enterprise contracts B2B` |

Analytical Envy rule: always run the comparative variant. Never research in isolation.

### Step 2: Source Selection Matrix

| Topic Type | L1 Sources | L2 Sources | L3 Trigger |
|-----------|-----------|-----------|------------|
| Competitive intelligence | Brave + Exa | SerpAPI + job postings | if no pricing data found |
| Technical / research | Exa (semantic) | Semantic Scholar | if < 2 papers |
| Financial / market | Brave | Alpha Vantage + SEC EDGAR | if no filing data |
| News / current events | Brave (freshness=pw) | Exa | if < 2 sources < 7 days |
| Product / UX | Brave + Exa | SerpAPI SERP | if < 3 structured results |

### Step 3: Query Execution

```
for variant in [direct, comparative, signal]:
    for source in layer_sources:
        results = api.query(source, variant, max=10)
        pool.add(results, layer=source.layer)
    if pool.size >= 5 and pool.triangulated:
        break
    else:
        escalate_to_next_layer()
```

## Deduplication and Ranking

| Step | Method | Threshold |
|------|--------|-----------|
| URL dedup | normalize domain + path | exact match |
| Semantic dedup | cosine similarity > 0.85 | remove duplicate |
| Freshness filter | published_date < 90 days preferred | warn if older |
| Relevance rank | source score + recency combined | top 10 per layer |
| Final pool | top 15 across all layers | for synthesis |

## Source Quality Scoring

Per `sch_validator_n01.md` validation rules:

| Source Type | Base Score | Adjustments |
|-------------|-----------|-------------|
| Primary source (company blog/filing) | 9/10 | +0.5 if < 30 days, -2 if > 1 year |
| Peer-reviewed paper | 8/10 | +1 if > 100 citations |
| Tier-1 news (Reuters, FT, WSJ) | 7/10 | +0.5 if < 7 days |
| Industry analyst (Gartner, CB Insights) | 7/10 | -1 if paywall-blocked |
| User forum / social | 4/10 | use only for sentiment signals |
| Unknown domain | 3/10 | require corroboration |

## Triangulation Gate

A claim is accepted only when:
- Sources >= 3 (hard gate, from quality_gate_intelligence.md H01)
- Sources from >= 2 different categories (web + academic, or web + financial)
- No source-date > 90 days unless explicitly flagged
- Competing claim flagged if sources disagree > 30%

## Fallback Chain

```
L1 exhausted (< 3 results) -> L2 auto-escalate
L2 exhausted (< 3 results) -> L3 auto-escalate
L3 exhausted -> flag research_gap, request human disambiguation
claim contested (sources disagree) -> report both positions with confidence delta
```

## Performance Benchmarks

| Metric | Target | Alert Threshold |
|--------|--------|----------------|
| L1 latency | < 3s per query | > 5s |
| L2 latency | < 8s per query | > 15s |
| Total search time per claim | < 30s | > 60s |
| Source pool size (min) | 5 sources | < 3 = fail gate |
| Triangulation rate | > 90% of claims | < 75% = review strategy |

## Comparison vs. Alternatives

| Approach | Depth | Cost | Speed | N01 Fit |
|----------|-------|------|-------|---------|
| Single-source (naive) | low | low | fast | fail -- no triangulation |
| Manual multi-source | high | high | slow | impractical at scale |
| This 3-layer strategy | high | medium | medium | optimal -- automated triangulation |
| AI web agent (Perplexity) | medium | low | fast | use as L3 supplement only |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p04_tool_search_config]] | related | 0.31 |
| [[p11_qg_intelligence]] | downstream | 0.30 |
| [[ex_chain_research_pipeline]] | upstream | 0.30 |
| [[p10_out_source_dossier]] | downstream | 0.28 |
| [[bld_knowledge_card_search_tool]] | upstream | 0.27 |
| [[p03_sp_intelligence_nucleus]] | upstream | 0.27 |
| [[n01_rs_intelligence_sources]] | upstream | 0.27 |
| [[p12_wf_intelligence]] | downstream | 0.26 |
| [[p10_lr_research_sessions]] | downstream | 0.24 |
| [[p01_kc_source_triangulation]] | upstream | 0.23 |
