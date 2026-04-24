---
id: p06_schema_research_depth
kind: schema
8f: F1_constrain
pillar: P06
title: "Research Depth Levels"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [schema, n01, depth, levels, scope]
tldr: "3 research depth levels: L1 Scan (5min, 3-5 sources), L2 Analysis (15min, 10-20), L3 Deep-Dive (30min+, 20-50)."
density_score: 0.92
related:
  - p12_wf_intelligence
  - p07_rubric_intelligence
  - p10_out_research_brief
  - p03_sp_intelligence_nucleus
  - p11_qg_intelligence
  - n01_agent_intelligence
  - p10_out_source_dossier
  - p03_pt_intelligence_analysis
  - p08_ac_intelligence
  - p07_sr_intel_research
---

# Research Depth Levels

| Level | Name | Time | Sources | Output | When |
|-------|------|------|---------|--------|------|
| L1 | Scan | 5 min | 3-5 web | Bullet-point snapshot | Quick check, context for other tasks |
| L2 | Analysis | 15 min | 10-20 mixed | Structured report with grids | Standard research request |
| L3 | Deep-Dive | 30+ min | 20-50 multi-type | Full dossier with projections | Strategic decisions, market entry |

## L1 Scan Spec
- Sources: web only (first page results)
- Output: 5-10 bullet points
- Citations: inline URLs
- Confidence: label but don't deep-verify

## L2 Analysis Spec
- Sources: web + industry + 1 academic if available
- Output: sections with tables/grids
- Citations: full citation format
- Triangulation: 2+ sources per claim

## L3 Deep-Dive Spec
- Sources: web + academic + industry + government + social
- Output: multi-section report with executive summary
- Citations: full with reliability scores
- Triangulation: 3+ sources per claim
- Includes: trend analysis, projections, risk assessment

## Examples

**L1 Scan: "AI coding tools market"**
• GitHub Copilot dominates with 1M+ users (github.com/features/copilot)
• New entrants: Cursor, Replit, CodeT5+ gaining traction
• Pricing: $10-20/month subscription model standard
• Main use case: code completion, not full generation

**L2 Analysis: "AI coding tools competitive landscape"**
*Executive Summary*: Market consolidating around 3 tiers...
*Market Size*: $2.3B projected by 2025 (Gartner, IDC)
*Player Matrix*: [table with features vs. competitors]
*Adoption Barriers*: Security concerns (67% enterprises), accuracy gaps

**L3 Deep-Dive: "Strategic positioning in AI coding tools"**
*Executive Summary + Risk Assessment*
*Market Analysis*: 15-page section with trend projections
*Competitive Intelligence*: Patent analysis, funding rounds, team moves
*Strategic Recommendations*: 3 market entry scenarios with ROI models

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_intelligence]] | downstream | 0.31 |
| [[p07_rubric_intelligence]] | downstream | 0.31 |
| [[p10_out_research_brief]] | downstream | 0.27 |
| [[p03_sp_intelligence_nucleus]] | upstream | 0.27 |
| [[p11_qg_intelligence]] | downstream | 0.26 |
| [[n01_agent_intelligence]] | upstream | 0.25 |
| [[p10_out_source_dossier]] | downstream | 0.24 |
| [[p03_pt_intelligence_analysis]] | upstream | 0.24 |
| [[p08_ac_intelligence]] | downstream | 0.23 |
| [[p07_sr_intel_research]] | downstream | 0.23 |
