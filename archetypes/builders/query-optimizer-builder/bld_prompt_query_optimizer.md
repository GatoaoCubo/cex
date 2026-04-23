---
kind: instruction
id: bld_prompt_query_optimizer
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for query_optimizer
quality: null
title: "Query Optimizer Builder - Prompt ISO"
version: "1.0.0"
author: n03_builder
tags: [query_optimizer, builder, instruction]
tldr: "Production instructions for query optimizer artifacts."
domain: "query optimization"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_query_optimizer
  - bld_schema_query_optimizer
---

# Instructions: How to Produce a query_optimizer

## Phase 1: RESEARCH

1. Identify the retrieval system this optimizer serves (dense, sparse, hybrid)
2. Analyze common query patterns: short vs long, simple vs complex, domain-specific
3. Select optimization techniques: rewriting, expansion, decomposition, HyDE, re-ranking
4. Define latency budget: how much additional time per query is acceptable
5. Identify re-ranking model if applicable (cross-encoder, LLM-based)
6. Check existing query_optimizer artifacts to avoid duplication

## Phase 2: COMPOSE

1. Read SCHEMA -- source of truth for all fields
2. Fill all frontmatter fields; set quality: null
3. Write Strategy section: selected techniques and their order in the pipeline
4. Write Rewriting section: LLM prompt for query reformulation
5. Write Expansion section: synonym sources, expansion limits
6. Write Re-ranking section: model, top-N retrieval count, re-rank count
7. Write Latency Budget section: time allocation per optimization step
8. Write Fallback section: behavior when optimization fails

## Phase 3: VALIDATE

1. Check HARD gates: YAML parses, id matches, kind correct
2. Verify at least one optimization technique defined
3. Verify latency budget specified with numeric targets
4. Verify fallback behavior documented
5. Cross-check: this is QUERY OPTIMIZATION, not retrieval logic or index config
