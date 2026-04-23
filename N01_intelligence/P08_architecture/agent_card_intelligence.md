---
id: p02_card_intelligence
kind: agent_card
pillar: P02
title: "N01 Research Analyst — Agent Card"
version: 4.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [agent_card, n01, research, analyst, routing]
tldr: "Research Analyst routing card — 12 capabilities, hybrid provider, input/output contracts, inter-nucleus handoffs."
density_score: 0.93
related:
  - n01_dr_intelligence
  - n01_dr_research_pipeline
  - ex_dispatch_rule_research
  - bld_collaboration_research_pipeline
  - n01_agent_intelligence
  - agent_card_n01
  - p12_dr_intelligence
  - dispatch
  - p03_sp_intelligence_nucleus
  - p10_out_research_brief
---

# N01 Research Analyst — Agent Card

## Routing
- **Priority**: 8 (high — research often precedes other nuclei)
- **Keywords**: research, competitor, market, trend, analyze, benchmark, compare, investigate, SWOT, pricing, who, what's happening, industry
- **Dispatch**: `bash _spawn/dispatch.sh solo n01 "task"`

## Provider
| Mode | Provider | When |
|------|----------|------|
| Search | Gemini 2.5 Pro | Web grounding, large docs |
| Analysis | Claude | Deep synthesis, nuance |
| Fallback | Either | Rate limit on primary |

## Capabilities Map

| Capability | Input | Output Template |
|-----------|-------|-----------------|
| Competitive Grid | competitors list + dimensions | output_competitive_grid.md |
| Market Snapshot | category + geography | output_market_snapshot.md |
| Trend Report | domain + timeframe | output_trend_report.md |
| Source Dossier | topic + depth level | output_source_dossier.md |
| SWOT | company/product | output_swot_analysis.md |
| Benchmark | products + criteria | output_benchmark_report.md |
| Executive Summary | any research output | output_executive_summary.md |

## Anti-Patterns (Route AWAY)

| Don't Use For | Route To Instead | Why |
|---------------|------------------|-----|
| "Write marketing copy for X" | N02 | Creative writing, not research |
| "Build me a landing page" | N03 | Artifact creation, not analysis |
| "Debug this code" | N05 | Technical operations |
| "Create a knowledge card" | N04 | Knowledge management |
| "Set up pricing for course" | N06 | Commercial strategy |

## Inter-Nucleus Handoffs

| From | To N01 | What |
|------|--------|------|
| N06 | Competitor research request | "Research these 5 competitors" |
| N07 | Mission decomposition | "Research phase of /plan" |
| N02 | Design benchmark | "Find UI patterns in category X" |

| From N01 | To | What |
|----------|-----|------|
| Research complete | N06 | Competitive positioning data |
| Trend report | N04 | New KC material |
| Benchmark | N02 | Design reference data |

## Composable Crews

| Crew | Process | Roles | Purpose |
|------|---------|-------|---------|
| competitive_intelligence | sequential | 3 (analyst, synthesizer, validator) | Peer-reviewed competitive intelligence brief with source verification |
| deep_research | sequential | 4 (scout, analyst, fact_checker, writer) | Comprehensive fact-validated research report with confidence scoring |
| trend_analysis | sequential | 3 (scanner, pattern_detector, brief_writer) | Emerging trend detection with temporal signal clustering and momentum scores |
| source_verification | sequential | 3 (harvester, cross_checker, confidence_scorer) | Standalone source validation layer -- reusable across any artifact |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_dr_intelligence]] | downstream | 0.40 |
| [[n01_dr_research_pipeline]] | downstream | 0.39 |
| [[ex_dispatch_rule_research]] | downstream | 0.37 |
| [[bld_collaboration_research_pipeline]] | downstream | 0.35 |
| [[n01_agent_intelligence]] | related | 0.34 |
| [[agent_card_n01]] | related | 0.34 |
| [[p12_dr_intelligence]] | downstream | 0.32 |
| [[dispatch]] | downstream | 0.32 |
| [[p03_sp_intelligence_nucleus]] | downstream | 0.31 |
| [[p10_out_research_brief]] | downstream | 0.31 |
