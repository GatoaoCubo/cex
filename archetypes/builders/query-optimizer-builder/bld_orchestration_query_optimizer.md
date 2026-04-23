---
kind: collaboration
id: bld_orchestration_query_optimizer
pillar: P12
llm_function: COLLABORATE
purpose: How query-optimizer-builder works in crews
quality: null
title: "Query Optimizer Builder - Orchestration ISO"
version: "1.0.0"
author: n03_builder
tags: [query_optimizer, builder, collaboration]
tldr: "Crew collaboration protocol for query optimizer builder."
domain: "query optimization"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_query_optimizer
---

# Collaboration: query-optimizer-builder

## My Role in Crews

I am a SPECIALIST. I answer: "how to optimize queries for better retrieval?"
I do not configure indexes. I do not build retrieval engines.

## Crew Compositions

### Crew: "RAG Pipeline Optimization"
```
1. query-optimizer-builder -> "query transformation pipeline"
2. embedding-config-builder -> "embedding model configuration"
3. retrieval-evaluator-builder -> "retrieval quality measurement"
```

## Handoff Protocol

### I Receive
- seeds: target retrieval system, query patterns, latency requirements

### I Produce
- query_optimizer artifact (.md with YAML frontmatter)

### I Signal
- signal: complete (with quality score)

## Builders I Depend On

| Builder | Why |
|---------|-----|
| embedding-config-builder | Embedding-aware query rewriting needs model specs |

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| retrieval-evaluator-builder | Evaluates optimized query effectiveness |
