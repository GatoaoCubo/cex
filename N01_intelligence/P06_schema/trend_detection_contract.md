---
id: p06_schema_trend_detection
kind: schema
8f: F1_constrain
pillar: P06
title: "Trend Detection Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [schema, n01, trend, detection, momentum]
tldr: "Trend signal schema: name, category, momentum (rising/stable/declining), confidence, evidence count, timeframe, impact assessment."
density_score: 0.92
related:
  - p10_out_trend_report
  - p11_qg_intelligence
  - p01_kc_confidence_scoring
  - p03_sp_intelligence_nucleus
  - p06_schema_research_depth
  - p06_schema_competitive_analysis
  - p10_out_source_dossier
  - bld_schema_reasoning_trace
  - p07_eval_research_outputs
  - p12_wf_weekly_fashion_content
---

# Trend Detection Contract

## Trend Signal

| Field | Type | Description |
|-------|------|-------------|
| name | string | Trend name |
| category | enum: tech\|market\|regulatory\|consumer\|competitive | Trend type |
| momentum | enum: rising\|stable\|declining | Direction |
| confidence | float 0-1 | Based on evidence count + source quality |
| evidence_count | int | Number of supporting data points |
| timeframe | string | Observation window ("Q1 2026", "last 6 months") |
| impact | enum: high\|medium\|low | Potential impact on user's business |
| sources | list[SourceQualityCard] | Supporting sources |
| so_what | string | Actionable implication for user's business |

## Confidence Mapping
| Evidence | Source Quality | Confidence |
|----------|--------------|------------|
| 5+ points | 3+ high authority | >= 0.90 |
| 3-4 points | 2+ medium+ | 0.70-0.89 |
| 1-2 points | any | < 0.70 |

## Usage Guidelines

**When to use:**
- Tracking industry shifts that could affect business strategy
- Monitoring competitive landscape changes
- Identifying emerging technologies or market opportunities
- Quarterly business review trend analysis

**Anti-patterns:**
- Single-source trend identification (confidence < 0.70)
- Mixing different timeframes in one analysis
- Treating declining trends as automatically negative
- Ignoring regulatory trends for compliance-heavy industries

**Examples:**
- Rising: "AI code generation" (tech, 0.95 confidence, 8 sources)
- Stable: "Remote work adoption" (market, 0.80 confidence, 5 sources)
- Declining: "Traditional retail expansion" (market, 0.85 confidence, 6 sources)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_out_trend_report]] | downstream | 0.43 |
| [[p11_qg_intelligence]] | downstream | 0.29 |
| [[p01_kc_confidence_scoring]] | upstream | 0.26 |
| [[p03_sp_intelligence_nucleus]] | upstream | 0.24 |
| [[p06_schema_research_depth]] | sibling | 0.23 |
| [[p06_schema_competitive_analysis]] | sibling | 0.22 |
| [[p10_out_source_dossier]] | downstream | 0.21 |
| [[bld_schema_reasoning_trace]] | sibling | 0.21 |
| [[p07_eval_research_outputs]] | downstream | 0.21 |
| [[p12_wf_weekly_fashion_content]] | downstream | 0.20 |
