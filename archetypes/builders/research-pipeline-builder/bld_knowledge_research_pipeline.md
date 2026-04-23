---
kind: knowledge_card
id: bld_knowledge_card_research_pipeline
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for research pipeline design — STORM, CRAG, CRITIC patterns
sources: Stanford STORM paper, CRAG paper (Yan et al 2024), CRITIC paper (Gou et al 2024), CODEXA production system (13908 lines)
quality: 9.1
title: "Knowledge Card Research Pipeline"
version: "1.0.0"
author: n03_builder
tags: [research_pipeline, builder, examples]
tldr: "Golden and anti-examples for research pipeline construction, demonstrating ideal structure and common pitfalls."
domain: "research pipeline construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_research_pipeline_builder
  - p02_agent_research_pipeline_intelligence
  - p01_kc_research_pipeline
  - n01_kc_research_methods
  - bld_instruction_research_pipeline
  - research-pipeline-builder
  - n01_tool_research_pipeline
  - p10_lr_research-pipeline-builder
  - tpl_research_pipeline
  - bld_architecture_research_pipeline
---

# Domain Knowledge: research_pipeline

## Executive Summary
A research pipeline is a config-driven system that collects, scores, synthesizes, and verifies market intelligence from 30+ sources. Built on three academic patterns: **STORM** (multi-perspective query planning from Stanford), **CRAG** (Corrective RAG with per-source quality gates), and **CRITIC** (iterative self-verification with thinking models). The CEX research-pipeline-builder distills a 13,908-line production system into a reusable 7-stage pattern.

## The 3 Core Patterns

### STORM (Survey of Topic via Retrieval and Organization of Multi-perspective)
- **Paper**: Stanford/UW 2024 — generates Wikipedia-quality articles from scratch
- **CEX adaptation**: generate 5 expert perspectives per research query, each decomposed into 5-7 atomic sub-questions. This multiplies retrieval coverage 25-35x vs single-query.
- **Why it works**: single-angle research misses competitor blind spots, buyer pain points, and market trends. STORM's multi-perspective approach covers all angles systematically.

### CRAG (Corrective Retrieval-Augmented Generation)
- **Paper**: Yan et al 2024 — evaluates retrieval quality before using it
- **CEX adaptation**: every retrieved result gets a quality score (0.0-1.0). Below threshold (default 0.7) → trigger fallback source or discard. Prevents low-quality data from polluting synthesis.
- **Quality dimensions**: relevance, recency, completeness, trustworthiness.

### CRITIC (Self-Correcting with Tool-Interactive Critique)
- **Paper**: Gou et al 2024 — LLM verifies own output, correct with tools
- **CEX adaptation**: Stage 7 uses a thinking model (o4-mini) to verify synthesis against source data. Catches hallucinations, numerical errors, contradictions. Max 3 iterations — diminishing returns after that.

## 7-Stage Pipeline
| Stage | Name | Model | Input | Output |
|-------|------|-------|-------|--------|
| 1 | INTENT | Fast classifier | User query | domain, verb, complexity, route |
| 2 | PLAN (STORM) | Reasoning model | Intent + perspectives | 25-35 sub-questions |
| 3 | RETRIEVE (CRAG) | APIs + scraping | Sub-questions | Scored results (≥0.7) |
| 4 | RESOLVE | Deterministic | Raw results | Deduplicated entities |
| 5 | SCORE | Fast model | Entities | Gartner 7-dim scored listings |
| 6 | SYNTHESIZE (GoT) | Domain models | Scored data | Structured analysis |
| 7 | VERIFY (CRITIC) | Thinking model | Synthesis + sources | Verified report |

## Anti-Patterns
| Anti-Pattern | Why It Fails |
|-------------|-------------|
| Single-query retrieval | Misses 80% of relevant data (no perspective diversity) |
| No quality gate on retrieval | Garbage in → garbage out; CRAG prevents this |
| Single-model synthesis | Different domains need different models; Flash for extraction, GPT for reasoning |
| No verification step | 15-20% of LLM synthesis contains hallucinations; CRITIC catches them |
| Unlimited scraping budget | Firecrawl/Serper credits drain fast; budget caps are essential |
| Hardcoded source list | Every niche needs different sources; config must be flexible |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_research_pipeline_builder]] | downstream | 0.54 |
| [[p02_agent_research_pipeline_intelligence]] | downstream | 0.48 |
| [[p01_kc_research_pipeline]] | sibling | 0.45 |
| [[n01_kc_research_methods]] | sibling | 0.44 |
| [[bld_instruction_research_pipeline]] | downstream | 0.41 |
| [[research-pipeline-builder]] | downstream | 0.39 |
| [[n01_tool_research_pipeline]] | downstream | 0.38 |
| [[p10_lr_research-pipeline-builder]] | downstream | 0.38 |
| [[tpl_research_pipeline]] | downstream | 0.36 |
| [[bld_architecture_research_pipeline]] | downstream | 0.33 |
