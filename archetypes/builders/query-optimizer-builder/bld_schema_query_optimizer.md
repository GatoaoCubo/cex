---
kind: schema
id: bld_schema_query_optimizer
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for query_optimizer
quality: null
title: "Query Optimizer Builder - Schema ISO"
version: "1.0.0"
author: n03_builder
tags: [query_optimizer, builder, schema]
tldr: "Schema for query optimizer artifacts -- fields, types, and constraints."
domain: "query optimization"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_output_query_optimizer
  - bld_eval_query_optimizer
---

# Schema: query_optimizer

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p01_qo_{slug}) | YES | - | Namespace compliance |
| kind | literal "query_optimizer" | YES | - | Type integrity |
| pillar | literal "P01" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| target_system | string | YES | - | Retrieval system being optimized |
| techniques | list[string] | YES | - | Optimization techniques used |
| reranker_model | string or null | REC | null | Cross-encoder for re-ranking |
| latency_budget_ms | integer | REC | - | Total optimization latency budget |
| top_n_retrieve | integer | REC | 20 | Initial retrieval count before re-ranking |
| rerank_count | integer | REC | 5 | Final results after re-ranking |
| domain | string | YES | - | Target domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "query" and "optimizer" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p01_qo_[a-z][a-z0-9_]+$`

## Body Structure (required sections)

1. `## Strategy` -- pipeline order and technique selection
2. `## Rewriting` -- query reformulation approach
3. `## Expansion` -- synonym and term expansion
4. `## Re-ranking` -- re-ranker model and configuration
5. `## Latency Budget` -- time allocation per step
6. `## Fallback` -- behavior on optimization failure

## Constraints

- naming: p01_qo_{optimizer_slug}.md
- techniques MUST be a non-empty list
- techniques values from: rewriting, expansion, decomposition, hyde, step_back, reranking
- quality: null always
