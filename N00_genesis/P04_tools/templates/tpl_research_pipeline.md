---
id: tpl_research_pipeline
kind: cli_tool
pillar: P04
title: "Research Pipeline — STORM+CRAG+CRITIC Market Intelligence"
version: 1.0.0
created: 2026-03-31
author: research-pipeline-builder
domain: research_pipeline
quality: 9.1
tags: [research-pipeline, template, STORM, CRAG, CRITIC, multi-model]
tldr: "Template for config-driven research pipeline. 7 stages, 30+ sources, multi-model, budget-aware. Any business configures sources and gets market intelligence."
density_score: 1.0
updated: "2026-04-07"
---

# Research Pipeline — Template

## Overview
Config-driven market intelligence pipeline based on STORM (multi-perspective planning), CRAG (per-source quality gates), and CRITIC (iterative verification). 7 stages from query to verified report.

## Pipeline (7 Stages)
| Stage | Name | Pattern | Model |
|-------|------|---------|-------|
| 1 | INTENT | Classifier | Fast (regex+embed) |
| 2 | PLAN | STORM | Reasoning (Sonnet/GPT) |
| 3 | RETRIEVE | CRAG | APIs + scraping |
| 4 | RESOLVE | Entity dedup | Deterministic + embed |
| 5 | SCORE | Gartner 7-dim | Fast (Flash) |
| 6 | SYNTHESIZE | Graph-of-Thoughts | Domain-specific models |
| 7 | VERIFY | CRITIC | Thinking (o4-mini) |

## Config Schema
```yaml
identity:
  empresa: "{{COMPANY}}"
  nicho: "{{NICHE}}"
  idioma: "{{LANG}}"           # pt-BR, en, es
  pais: "{{COUNTRY}}"          # BR, US, EU

sources:
  inbound: [{{INBOUND}}]       # marketplaces / product catalogs
  outbound: [{{OUTBOUND}}]     # social / reviews / community
  search: [{{SEARCH}}]         # web search engines
  trends: [{{TRENDS}}]         # price / trend tracking
  rag: [{{RAG}}]               # internal knowledge

storm_perspectives:
  - {role: "{{ROLE}}", focus: "{{FOCUS}}"}
  # min 3, recommended 5

multi_model:
  extraction: "{{MODEL}}"      # fast: gemini-flash
  reasoning: "{{MODEL}}"       # strong: sonnet / gpt
  social: "{{MODEL}}"          # fast: gemini-flash
  critic: "{{MODEL}}"          # thinking: o4-mini

budget:
  firecrawl_monthly: {{N}}     # credit cap
  firecrawl_per_research: {{N}}
  serper_daily: {{N}}

output:
  formats: [{{FORMATS}}]       # html, pptx, json, md
  idioma: "{{LANG}}"
  template: "{{STYLE}}"        # consulting, academic, brief

quality:
  crag_min_score: {{0.0-1.0}}  # default 0.7
  critic_max_iterations: {{1-5}} # default 3
  final_min_score: {{1-10}}    # default 8.0

marketplace_schemas:            # optional: extraction fields
  {{SOURCE}}: { fields: [{{FIELDS}}] }
```

## Source Categories
| Category | Description | Examples |
|----------|------------|---------|
| Inbound | Product/listing data | mercadolivre, shopee, amazon, g2, capterra |
| Outbound | Social intelligence | youtube, reddit, reclameaqui, hackernews |
| Search | Web search engines | serper, exa, brave, tavily, gemini_search |
| Trends | Price/trend tracking | pytrends, keepa, semrush |
| RAG | Internal knowledge | local_docs, supabase_embeddings |

## Quality Gates
| Gate | Rule | Severity |
|------|------|----------|
| 7 stages present | All stages documented | HARD |
| 2+ source categories | Min inbound + search | HARD |
| CRAG threshold | 0.0-1.0 defined | HARD |
| CRITIC iterations | 1-5 defined | HARD |
| Budget caps | At least 1 cap | HARD |
| Zero secrets | Only ENV_VAR refs | HARD |
| 5+ perspectives | STORM diversity | SOFT |
| Fallback chains | Per-source fallback | SOFT |
