---
id: kc_market_sizing_methodology
kind: knowledge_card
pillar: P01
nucleus: n01
title: "Market Sizing Methodology: TAM/SAM/SOM and Beyond"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: market-analysis
quality: 9.2
tags: [market_sizing, TAM_SAM_SOM, bottom_up, top_down, market_analysis, n01]
tldr: "Comprehensive market sizing methodology: top-down (analyst reports) vs. bottom-up (unit economics), TAM/SAM/SOM definitions and calculations, common errors, and calibration against known benchmarks."
density_score: 0.91
updated: "2026-04-17"
related:
  - p10_out_market_snapshot
  - bld_knowledge_card_pitch_deck
  - n01_agent_intelligence
  - bld_knowledge_card_analyst_briefing
  - p03_sp_analyst_briefing_builder
  - p03_sp_intelligence_nucleus
  - p04_tool_search_config
  - bld_collaboration_analyst_briefing
  - bld_instruction_analyst_briefing
  - p10_out_research_brief
---

<!-- 8F: F1 constrain=P01/knowledge_card F2 become=knowledge-card-builder F3 inject=kc_competitive_intelligence_methods+reasoning_strategy_n01 F4 reason=market sizing is the most common N01 task after competitive analysis; this KC grounds every sizing exercise in methodology F5 call=cex_compile F6 produce=kc_market_sizing_methodology.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P01_knowledge/ -->

## Core Concepts

| Term | Definition | Equation |
|------|-----------|---------|
| TAM | Total Addressable Market -- total revenue opportunity if 100% market share | potential_customers * ARPU |
| SAM | Serviceable Addressable Market -- portion TAM reachable with current model | TAM * (reachable_segment_pct) |
| SOM | Serviceable Obtainable Market -- realistic capture in 3-5 years | SAM * market_share_estimate |

Hierarchy: TAM > SAM > SOM always. SOM < 25% of SAM is typical for emerging players.

## Sizing Methodologies

### Top-Down (Analyst-Driven)

| Step | Action | Source |
|------|--------|--------|
| 1 | Find analyst market estimate | Gartner, IDC, CB Insights, Statista |
| 2 | Apply segment filter (geography, vertical, tier) | company-specific criteria |
| 3 | Verify with 2nd analyst source | compare, note discrepancy |
| 4 | Apply growth rate to current year | CAGR from analyst + cross-check |

**Error rate**: top-down estimates often overstate by 2-3x (analysts incentivized for large TAMs).
**Calibration**: always divide analyst TAM by 3 as reality check.

### Bottom-Up (Unit Economics)

| Step | Action | Data Needed |
|------|--------|------------|
| 1 | Define customer unit | ICP definition |
| 2 | Estimate total units (potential customers) | population data, LinkedIn, census |
| 3 | Estimate ARPU (average revenue per unit) | pricing * conversion assumption |
| 4 | TAM = units * ARPU | calculate |
| 5 | SAM = filter by segment (geography, size, etc.) | apply filters |
| 6 | SOM = SAM * realistic_market_share | historical market share for analogues |

**Bottom-up is more reliable** for early-stage markets where analyst data is sparse or inaccurate.

### Triangulation (Recommended)

Run BOTH methods. If they agree within 50%: use average. If they diverge > 50%: investigate why.

Common divergence causes:
- Different ICP definitions
- Different ARPU assumptions (analyst uses enterprise, bottom-up uses SMB)
- Market definition mismatch (adjacent markets included or excluded)

## Market Growth Models

| Model | Formula | Use Case |
|-------|---------|---------|
| CAGR | (end/start)^(1/years) - 1 | stable growth market |
| S-curve | logistic function | adoption-stage markets |
| Linear | constant absolute growth | mature, saturated markets |
| Viral coefficient | R0 = viral_factor * conversion | virality-driven growth |

Choosing correctly matters: applying CAGR to an S-curve market gives dramatically wrong projections.

## Common Errors

| Error | Type | Consequence | Fix |
|-------|------|------------|-----|
| Confusing TAM/SAM/SOM | definitional | inflated SOM | use definitions above, verify SAM < TAM |
| Citing one analyst | single-source | biased estimate | triangulate 2+ analysts |
| Ignoring churn | omission | overstated growth | include net growth (new - churned) |
| Static ARPU | assumption | wrong in growing markets | model ARPU change over time |
| Bottom-up overcounting | double-counting | inflated TAM | deduplicate customer units |

## Calibration: Known Market Sizes (2025)

| Market | Analyst Estimate | Bottom-Up Cross-Check | N01 Assessment |
|--------|-----------------|----------------------|---------------|
| Global AI software | $150-200B (IDC) | n/a (too broad) | plausible |
| GenAI APIs | $10-15B | plausible (10M devs * $1-1.5K ARPU) | plausible |
| AI code assistants | $2-4B | ~2B (5M users * $400 ARPU) | plausible |
| Enterprise LLM licensing | $5-8B | $7B (100K enterprises * $70K avg) | plausible |

Use these as sanity checks for analogous market sizing exercises.

## N01 Sizing Protocol

```
1. Identify market definition (scope, geography, segment)
2. Run top-down: find 2 analyst estimates
3. Run bottom-up: ICP count * ARPU
4. Triangulate: compare, explain discrepancy
5. Apply growth model (CAGR or S-curve)
6. Output: TAM / SAM / SOM table with confidence + sources
```

Confidence targets:
- TAM: 0.6-0.75 (market definitions differ)
- SAM: 0.70-0.85 (better defined)
- SOM: 0.50-0.65 (highly assumption-dependent)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_out_market_snapshot]] | downstream | 0.47 |
| [[bld_knowledge_card_pitch_deck]] | sibling | 0.23 |
| [[n01_agent_intelligence]] | downstream | 0.22 |
| [[bld_knowledge_card_analyst_briefing]] | sibling | 0.22 |
| [[p03_sp_analyst_briefing_builder]] | downstream | 0.22 |
| [[p03_sp_intelligence_nucleus]] | downstream | 0.21 |
| [[p04_tool_search_config]] | downstream | 0.20 |
| [[bld_collaboration_analyst_briefing]] | downstream | 0.20 |
| [[bld_instruction_analyst_briefing]] | downstream | 0.20 |
| [[p10_out_research_brief]] | downstream | 0.19 |
