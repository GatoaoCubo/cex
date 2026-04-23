---
id: p06_schema_competitive_analysis
kind: schema
pillar: P06
title: "Competitive Analysis Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [schema, n01, competitive, grid, analysis]
tldr: "Competitor grid schema: N competitors × M dimensions. Required: name, positioning, pricing, strengths, weaknesses, market share estimate."
density_score: 0.92
when_to_use: "Market entry, product positioning, pricing strategy, investment decisions, feature prioritization"
related:
  - bld_schema_competitive_matrix
  - n06_schema_brand_config
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - bld_schema_tagline
  - p10_out_competitive_grid
  - bld_schema_training_method
  - bld_schema_enum_def
  - p02_agent_competitor_tracker
  - bld_schema_model_architecture
---

# Competitive Analysis Contract

## Grid Structure
```
Competitors (rows) × Dimensions (columns) = Competitive Grid
```

## Required Dimensions

| Dimension | Type | Description |
|-----------|------|-------------|
| name | string | Company/product name |
| positioning | string | 1-sentence market position |
| pricing_model | enum: free\|freemium\|subscription\|one-time\|enterprise | How they charge |
| price_range | string | Price range in relevant currency |
| strengths | list[string] | Top 3 competitive advantages |
| weaknesses | list[string] | Top 3 vulnerabilities |
| market_share_est | enum: leader\|major\|mid\|niche\|emerging | Estimated position |
| target_audience | string | Primary audience |

## Optional Dimensions
| Dimension | Type |
|-----------|------|
| founded | int (year) |
| funding | string |
| tech_stack | list[string] |
| key_features | list[string] |
| differentiator | string |
| threat_level | enum: high\|medium\|low |

## Usage Guidelines

**When to use:**
- Market entry planning: validate market size and competitive landscape
- Product positioning: identify differentiation opportunities
- Pricing strategy: benchmark against competitor pricing models
- Investment decisions: assess competitive threats and market dynamics
- Feature prioritization: analyze competitor strengths/weaknesses for roadmap planning

**When NOT to use:**
- Internal strategy discussions (use strategy_canvas instead)
- Customer research (use user_research_report)
- Technical architecture decisions (use tech_stack_comparison)

**Anti-patterns:**
- ❌ Including 20+ competitors (focus on top 5-8 direct competitors)
- ❌ Outdated data (refresh every 6 months minimum)
- ❌ Missing pricing intel (critical for positioning decisions)
- ❌ Subjective strength/weakness assessments (use customer feedback data)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_competitive_matrix]] | sibling | 0.37 |
| [[n06_schema_brand_config]] | related | 0.36 |
| [[bld_schema_model_registry]] | sibling | 0.35 |
| [[bld_schema_experiment_tracker]] | sibling | 0.31 |
| [[bld_schema_tagline]] | sibling | 0.30 |
| [[p10_out_competitive_grid]] | downstream | 0.30 |
| [[bld_schema_training_method]] | sibling | 0.30 |
| [[bld_schema_enum_def]] | sibling | 0.26 |
| [[p02_agent_competitor_tracker]] | upstream | 0.26 |
| [[bld_schema_model_architecture]] | sibling | 0.26 |
