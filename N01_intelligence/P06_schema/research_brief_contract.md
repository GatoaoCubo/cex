---
id: p06_schema_research_brief
kind: schema
8f: F1_constrain
pillar: P06
title: "Research Brief Contract"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
tags: [schema, n01, research, brief, input-contract]
tldr: "Input contract for N01 research requests: question, scope, depth level, source preferences, deadline, brand context."
density_score: 0.93
related:
  - p10_out_research_brief
  - p12_wf_intelligence
  - p06_is_quality_audit
  - bld_schema_research_pipeline
  - bld_examples_handoff_protocol
  - p02_card_intelligence
  - bld_schema_model_registry
  - p06_schema_competitive_analysis
  - n06_schema_brand_config
  - p06_schema_research_depth
---

# Research Brief Contract

## Required Fields

| Field | Type | Description |
|-------|------|-------------|
| question | string | The research question (1-3 sentences) |
| depth | enum: L1\|L2\|L3 | L1=scan (5min), L2=analysis (15min), L3=deep-dive (30min+) |
| output_format | enum | Which output template to use |

## Optional Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| scope | string | null | Geographic, temporal, or domain constraints |
| competitors | list[string] | [] | Specific competitors to include |
| sources_preferred | list[string] | [] | Preferred source types: web, academic, industry, govt |
| sources_excluded | list[string] | [] | Sources to avoid |
| deadline | datetime | null | When results needed |
| brand_context | boolean | true | Inject brand_config.yaml context |
| language | enum | pt-BR | Output language |
| max_sources | int | 20 | Cap on sources to analyze |

## Usage Guidelines

**Use this contract when:**
- Dispatching research to N01 nucleus
- Need structured intelligence output
- Research has multiple constraints/preferences
- Want consistent research deliverables

**Don't use when:**
- Quick factual lookup (use direct query)
- Research is exploratory without clear question
- Output format is flexible/undefined

**Anti-patterns:**
- Vague questions ("research AI trends")
- Contradictory constraints (L1 depth + 50 sources)
- Missing output_format specification

## Example
```yaml
question: "Who are the top 5 competitors in AI agent frameworks for SMBs in Brazil?"
depth: L2
output_format: output_competitive_grid
competitors: [CrewAI, LangChain, AutoGen, Semantic Kernel]
scope: "Brazil, 2024-2026"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_out_research_brief]] | downstream | 0.33 |
| [[p12_wf_intelligence]] | downstream | 0.27 |
| [[p06_is_quality_audit]] | related | 0.26 |
| [[bld_schema_research_pipeline]] | sibling | 0.24 |
| [[bld_examples_handoff_protocol]] | downstream | 0.24 |
| [[p02_card_intelligence]] | upstream | 0.24 |
| [[bld_schema_model_registry]] | sibling | 0.24 |
| [[p06_schema_competitive_analysis]] | sibling | 0.24 |
| [[n06_schema_brand_config]] | related | 0.24 |
| [[p06_schema_research_depth]] | sibling | 0.24 |
