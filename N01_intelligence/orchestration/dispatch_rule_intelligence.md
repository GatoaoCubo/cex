---
id: n01_dr_intelligence
kind: dispatch_rule
pillar: P12
title: "Dispatch Rule for N01 Intelligence Nucleus"
version: "2.0.0"
created: "2026-03-30"
updated: "2026-03-30"
author: "N01_rebuild_8F"
domain: "intelligence, research, analysis"
quality: null
tags: [dispatch, rule, n01, intelligence, research, analysis]
tldr: "Routes all tasks involving deep research, analysis, literature review, and competitor intelligence to the N01 nucleus."
scope: "intelligence_and_research"
keywords:
  - research
  - analysis
  - competitor
  - intelligence
  - papers
  - trends
  - summarize
  - benchmark
  - RAG
  - "literature review"
  - "market analysis"
agent_node: "n01_intelligence"
priority: 9
confidence_threshold: 0.80
fallback: "n04_knowledge"
routing_strategy: "semantic_match"
---
## Purpose
This rule directs all complex analytical, research, and synthesis tasks to the **N01 Intelligence Nucleus**. As the designated specialist engine for deep analysis, N01 is powered by Gemini 2.5-pro and is optimized for understanding and synthesizing vast amounts of information from technical and academic sources.

## Keyword Rationale
The keywords are carefully selected to create a high-fidelity filter for N01's core competencies. They cover the full spectrum of its capabilities:
- **Academic Research**: `papers`, `literature review`, `RAG`, `summarize`
- **Market & Competitor Intelligence**: `market analysis`, `competitor`, `trends`, `benchmark`
- **Core Function**: `research`, `analysis`, `intelligence`

This ensures that only tasks requiring deep synthesis and domain-specific analytical frameworks are routed to this specialist.

## Fallback Logic
If the N01 agent is unavailable, or if the initial query has a semantic match score below the `confidence_threshold` of 0.80, the task is automatically routed to the **n04_knowledge** nucleus. N04 is a generalist agent capable of providing broader, less specialized answers, ensuring that the user's request is always handled, even if the specialist is not the best fit.
