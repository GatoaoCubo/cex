---
id: p10_out_swot_analysis
kind: output
8f: F6_produce
pillar: P10
title: "Output: SWOT Analysis"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [output, n01, swot, strategic, analysis]
tldr: "4-quadrant SWOT with actionable implications per item."
density_score: 0.91
related:
  - p06_schema_competitive_analysis
  - p10_out_competitive_grid
  - p10_lr_context_doc_builder
---

# Output: SWOT Analysis

## Template
```markdown
# SWOT: {{BRAND_NAME}} in {{CATEGORY}}
**Date**: {{DATE}} | **Sources**: {{COUNT}}

## Matrix

| | Helpful | Harmful |
|---|---------|---------|
| **Internal** | **Strengths** | **Weaknesses** |
| | S1: {{ITEM}} | W1: {{ITEM}} |
| | S2: {{ITEM}} | W2: {{ITEM}} |
| | S3: {{ITEM}} | W3: {{ITEM}} |
| **External** | **Opportunities** | **Threats** |
| | O1: {{ITEM}} | T1: {{ITEM}} |
| | O2: {{ITEM}} | T2: {{ITEM}} |
| | O3: {{ITEM}} | T3: {{ITEM}} |

## Strategic Implications
- **SO** (use strengths for opportunities): {{STRATEGY}}
- **WO** (fix weaknesses to capture opportunities): {{STRATEGY}}
- **ST** (use strengths to counter threats): {{STRATEGY}}
- **WT** (minimize weaknesses, avoid threats): {{STRATEGY}}
```

## Example Analysis

| | Helpful | Harmful |
|---|---------|---------|
| **Internal** | **Strengths** | **Weaknesses** |
| | S1: 50K email subscribers | W1: No mobile app |
| | S2: 15 years domain expertise | W2: Limited social media presence |
| | S3: High customer retention (85%) | W3: Small dev team (3 people) |
| **External** | **Opportunities** | **Threats** |
| | O1: AI integration trend | T1: New funded competitor launched |
| | O2: Remote work adoption | T2: Economic downturn affecting budgets |
| | O3: Partnership with Platform X | T3: Regulatory changes in EU |

**Strategic Implications**:
- **SO**: Leverage email list to promote AI-powered features for remote teams
- **WO**: Build mobile app to capture mobile-first opportunities
- **ST**: Use retention rates as differentiator against new competitors
- **WT**: Focus on core market, delay expansion until economy stabilizes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_competitive_analysis]] | upstream | 0.22 |
| [[p10_out_competitive_grid]] | sibling | 0.20 |
| [[p10_lr_context_doc_builder]] | related | 0.18 |
