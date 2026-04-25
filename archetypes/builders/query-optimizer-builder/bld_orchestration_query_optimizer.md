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
tldr: "Orchestration protocol for query optimizer: workflow integration, handoff signals, dependency management, and cross-nucleus coordination for query rewriting, expansion, and multi-hop decomposition rules for rag retrieval."
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

## Integration Points

| Point | Direction | Protocol |
|-------|-----------|----------|
| F8 COLLABORATE | outbound | signal_writer.write_signal() |
| F3 INJECT | inbound | Receives upstream artifacts via handoff |
| search_strategy | upstream | Must exist before query optimizer production |
| retriever_config | upstream | Must exist before query optimizer production |
| rag_source | upstream | Must exist before query optimizer production |

## Dependencies

| Dependency | Required | Purpose |
|-----------|----------|---------|
| search_strategy | yes | Upstream artifact for query optimizer |
| retriever_config | yes | Upstream artifact for query optimizer |
| rag_source | yes | Upstream artifact for query optimizer |

## Properties

| Property | Value |
|----------|-------|
| Kind | `orchestration` |
| Pillar | P12 |
| Domain | query optimizer construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
