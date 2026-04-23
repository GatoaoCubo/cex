---
id: ex_dispatch_rule_research
kind: dispatch_rule
pillar: P12
title: Research Task Routing
target_nucleus: N01
target_agent: research-agent
priority: 8
confidence_threshold: 0.7
fallback_agent: gateway-agent
tags: [dispatch, routing, research, orchestration, N01]
references:
  - tpl_dispatch_rule
  - ex_chain_research_pipeline
  - ex_agent_copywriter
  - ex_skill_web_scraper
tldr: "Dispatch rule: routes research intents to N01 research-agent (STORM+CRAG pipeline) with keyword+intent matching."
quality: 9.1
related:
  - n01_dr_intelligence
  - bld_collaboration_research_pipeline
  - p02_card_intelligence
  - p01_kc_dispatch_rule
  - n01_dr_research_pipeline
  - p12_dr_admin_orchestration
  - bld_examples_e2e_eval
  - research-pipeline-builder
  - bld_knowledge_card_dispatch_rule
  - p03_sp_research_pipeline_builder
---

# Research Task Routing

## Matching Logic

The dispatcher evaluates incoming intents against this rule using a two-stage match:

**Stage 1 — Keyword Match** (fast, regex-based):
```
Keywords: research, analyze, compare, benchmark, investigate, study, evaluate, survey
Pattern: /\b(research|analyz|compar|benchmark|investigat|stud|evaluat|survey)\b/i
```

**Stage 2 — Intent Classification** (LLM-based, if keyword score > 0.3):
```
Classifier input: user intent + context
Classifier output: confidence score [0, 1]
Threshold: >= 0.7 to route to research-agent
```

## Rule Configuration

| Field | Value | Description |
|-------|-------|-------------|
| Keywords | research, analyze, compare, benchmark, investigate, study, evaluate | Trigger words (any match activates Stage 2) |
| Target | `research-agent` (N01) | Gemini 2.5-pro with 1M context window |
| Priority | 8 (of 10) | Higher priority than general dispatch rules |
| Threshold | 0.7 | Minimum confidence for research routing |
| Fallback | `gateway-agent` | Routes to N07 orchestrator for manual triage |
| Pipeline | STORM + CRAG | Multi-source research with retrieval-augmented generation |

## Routing Examples

| Intent | Keyword Score | Intent Score | Route | Reason |
|--------|---------------|--------------|-------|--------|
| "Research competitors in the SaaS analytics space" | 1.0 (exact: "research") | 0.95 | research-agent | High confidence research intent |
| "Compare pricing models for AI APIs" | 1.0 (exact: "compare") | 0.88 | research-agent | Comparative analysis, clear research |
| "Analyze last quarter's sales data" | 1.0 (exact: "analyze") | 0.62 | gateway-agent | Below 0.7 — likely analytics, not research |
| "Write a blog post about trends" | 0.0 (no keywords) | — | skipped | No keyword match, rule not activated |
| "Benchmark our LLM pipeline latency" | 1.0 (exact: "benchmark") | 0.91 | research-agent | Technical benchmarking = research domain |

## Priority Resolution

When multiple dispatch rules match the same intent:

| Priority | Rule | Resolution |
|----------|------|------------|
| 10 | emergency-triage | Always wins — safety/compliance routing |
| 8 | **research** (this rule) | Wins over general and domain rules |
| 6 | marketing-copy | Only activated if research doesn't match |
| 4 | general-task | Default catch-all |
| 1 | gateway-fallback | Last resort — N07 manual triage |

**Tie-breaking**: If two rules share the same priority, the one with higher confidence score wins.

## STORM + CRAG Pipeline

When `research-agent` receives a dispatched task, it executes:

1. **STORM** (Survey of the Topic via Retrieval-Oriented Methods):
   - Generate 5-7 research questions from the intent
   - Search multiple sources (web, papers, internal docs)
   - Synthesize findings into structured outline

2. **CRAG** (Corrective Retrieval-Augmented Generation):
   - Retrieve candidate passages for each section
   - Score passage relevance (discard < 0.6)
   - Generate response with inline citations
   - Cross-check facts against retrieved sources

## Fallback Behavior

When confidence < 0.7, the intent routes to `gateway-agent` (N07 orchestrator), which:
1. Logs the unmatched intent for rule refinement
2. Presents the user with nucleus options (N01-N06)
3. Learns from the user's manual choice to improve future routing

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n01_dr_intelligence]] | sibling | 0.34 |
| [[bld_collaboration_research_pipeline]] | related | 0.34 |
| [[p02_card_intelligence]] | upstream | 0.34 |
| [[p01_kc_dispatch_rule]] | related | 0.33 |
| [[n01_dr_research_pipeline]] | sibling | 0.33 |
| [[p12_dr_admin_orchestration]] | sibling | 0.31 |
| [[bld_examples_e2e_eval]] | upstream | 0.30 |
| [[research-pipeline-builder]] | upstream | 0.29 |
| [[bld_knowledge_card_dispatch_rule]] | upstream | 0.29 |
| [[p03_sp_research_pipeline_builder]] | upstream | 0.27 |
