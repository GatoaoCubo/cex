---
id: p12_wf_intelligence
kind: workflow
8f: F8_collaborate
pillar: P12
title: "N01 Workflow — Research Pipeline"
version: 4.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
step_count: 8
quality: 9.1
tags: [workflow, n01, research, pipeline, triangulation]
tldr: "8-step research pipeline: brief→scope→search→triangulate→synthesize→format→validate→deliver."
density_score: 0.93
related:
  - ex_chain_research_pipeline
  - p06_schema_research_depth
  - p10_lr_research_sessions
  - p06_schema_research_brief
  - p11_qg_intelligence
  - p10_out_research_brief
  - p03_sp_intelligence_nucleus
  - p10_out_source_dossier
  - p03_sp_n01_intelligence
  - p07_rubric_intelligence
---

# N01 Workflow — Research Pipeline

## Pipeline

```
BRIEF → SCOPE → SEARCH → TRIANGULATE → SYNTHESIZE → FORMAT → VALIDATE → DELIVER
```

| Step | Action | Input | Output | Tool |
|------|--------|-------|--------|------|
| 1 | Receive research brief | User/nucleus request | Classified brief | cex_intent.py |
| 2 | Scope research | Brief + brand context | Depth level (L1/L2/L3), source plan | research_depth_levels.md |
| 3 | Search sources | Scope + queries | Raw findings (10-50 sources) | fetch MCP, markitdown MCP |
| 4 | Triangulate | Raw findings | Verified claims (3+ sources each) | source_quality_contract.md |
| 5 | Synthesize | Verified claims | Structured analysis | System prompt rules 7-10 |
| 6 | Format | Analysis | Output template filled | output_*.md templates |
| 7 | Validate | Formatted output | Quality check (freshness, citations) | quality_gate_intelligence.md |
| 8 | Deliver | Validated output | Signal + handoff | signal_writer.py |

## Research Depth Levels

| Level | Time | Sources | Output |
|-------|------|---------|--------|
| L1 Scan | 5 min | 3-5 web | Quick snapshot, bullet points |
| L2 Analysis | 15 min | 10-20 mixed | Structured report with grids |
| L3 Deep-Dive | 30+ min | 20-50 multi-type | Full dossier with projections |

## Anti-Patterns

| Never Do | Why | Instead |
|----------|-----|---------|
| Search before scoping | Wastes time on irrelevant sources | Always classify brief depth (L1/L2/L3) first |
| Single-source claims | Creates unverified intelligence | Require 3+ sources per claim minimum |
| Skip triangulation | Amplifies misinformation | Cross-verify every finding before synthesis |
| Mix raw data with analysis | Confuses facts with interpretation | Separate findings (Step 4) from synthesis (Step 5) |
| Deliver without freshness check | Provides outdated intelligence | Validate recency in Step 7 quality gate |

## Decision Points

| Step | Scenario | Decision | Action |
|------|----------|----------|--------|
| 2 | Brief too vague ("research competitors") | Scope clarification needed | Use GDP to get specific verticals, regions, metrics |
| 2 | Time constraint vs depth requested | L3 brief but 10min available | Negotiate down to L2 or extend timeline |
| 3 | Paywall sources blocking research | Premium content inaccessible | Shift to academic papers, company reports, public filings |
| 4 | <3 sources found for key claim | Triangulation impossible | Flag as "single-source claim" and note confidence level |
| 4 | Sources contradict each other | Conflicting information | Present both views with source attribution |
| 6 | Multiple output formats requested | Format selection unclear | Use research_brief template unless specifically requested |
| 7 | Sources >6 months old | Freshness gate failure | Re-search with date filters or flag as historical analysis |
| 8 | Handoff target unclear | Delivery ambiguity | Signal N07 and await routing instructions |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[ex_chain_research_pipeline]] | upstream | 0.35 |
| [[p06_schema_research_depth]] | upstream | 0.35 |
| [[p10_lr_research_sessions]] | upstream | 0.33 |
| [[p06_schema_research_brief]] | upstream | 0.32 |
| [[p11_qg_intelligence]] | upstream | 0.31 |
| [[p10_out_research_brief]] | upstream | 0.31 |
| [[p03_sp_intelligence_nucleus]] | upstream | 0.30 |
| [[p10_out_source_dossier]] | upstream | 0.28 |
| [[p03_sp_n01_intelligence]] | upstream | 0.28 |
| [[p07_rubric_intelligence]] | upstream | 0.24 |
