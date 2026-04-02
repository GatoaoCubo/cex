---
id: p12_wf_intelligence
kind: workflow
pillar: P12
title: "N01 Workflow — Research Pipeline"
version: 4.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
step_count: 8
quality: 8.7
tags: [workflow, n01, research, pipeline, triangulation]
tldr: "8-step research pipeline: brief→scope→search→triangulate→synthesize→format→validate→deliver."
density_score: 0.93
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
- Step 2 scope too broad → narrow with user via GDP
- Step 4 triangulation fails (<3 sources) → flag as "low confidence"
- Step 7 freshness fail → re-search with date filters