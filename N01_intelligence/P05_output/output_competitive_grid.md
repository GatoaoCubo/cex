---
id: p10_out_competitive_grid
kind: output
pillar: P10
title: "Output: Competitive Grid"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [output, n01, competitive, grid, analysis]
tldr: "N competitors × M dimensions matrix with positioning, pricing, strengths, weaknesses."
density_score: 0.92
related:
  - p02_agent_competitor_tracker
  - p06_schema_competitive_analysis
  - p10_out_executive_summary
  - p11_qg_intelligence
  - bld_output_template_llm_judge
  - p01_rs_SOURCE_SLUG
  - p01_kc_confidence_scoring
  - n06_kc_competitive_positioning
  - p04_rp_weekly_market_intelligence_brief_output_template
  - bld_knowledge_card_competitive_matrix
---

# Output: Competitive Grid

## Template

```markdown
# Competitive Grid: {{CATEGORY}}
**Date**: {{DATE}} | **Depth**: {{DEPTH}} | **Sources**: {{SOURCE_COUNT}}

## Grid

| Dimension | {{BRAND_NAME}} | Competitor A | Competitor B | Competitor C |
|-----------|---------------|-------------|-------------|-------------|
| Positioning | | | | |
| Pricing Model | | | | |
| Price Range | | | | |
| Target Audience | | | | |
| Key Strengths | | | | |
| Key Weaknesses | | | | |
| Market Position | | | | |
| Differentiator | | | | |
| Threat Level | — | high/med/low | high/med/low | high/med/low |

## Key Findings
1. {{FINDING_1}} (confidence: {{SCORE}})
2. {{FINDING_2}} (confidence: {{SCORE}})
3. {{FINDING_3}} (confidence: {{SCORE}})

## Opportunities
- {{OPPORTUNITY_1}}
- {{OPPORTUNITY_2}}

## Sources
{{CITATIONS}}
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_agent_competitor_tracker]] | upstream | 0.31 |
| [[p06_schema_competitive_analysis]] | upstream | 0.31 |
| [[p10_out_executive_summary]] | sibling | 0.30 |
| [[p11_qg_intelligence]] | downstream | 0.24 |
| [[bld_output_template_llm_judge]] | upstream | 0.22 |
| [[p01_rs_SOURCE_SLUG]] | upstream | 0.20 |
| [[p01_kc_confidence_scoring]] | upstream | 0.20 |
| [[n06_kc_competitive_positioning]] | upstream | 0.20 |
| [[p04_rp_weekly_market_intelligence_brief_output_template]] | upstream | 0.19 |
| [[bld_knowledge_card_competitive_matrix]] | upstream | 0.18 |
