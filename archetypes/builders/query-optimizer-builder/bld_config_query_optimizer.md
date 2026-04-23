---
kind: config
id: bld_config_query_optimizer
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions and constraints for query_optimizer
quality: null
title: "Query Optimizer Builder - Config ISO"
version: "1.0.0"
author: n03_builder
tags: [query_optimizer, builder, config]
tldr: "Production config for query optimizer: naming, paths, and constraints."
domain: "query optimization"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_schema_query_optimizer
---

# Config: query_optimizer Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | p01_qo_{optimizer_slug}.md | p01_qo_rag_hybrid_v1.md |
| Builder directory | kebab-case | query-optimizer-builder/ |
| Frontmatter fields | snake_case | latency_budget_ms, reranker_model |

## File Paths

1. Output: P01_knowledge/examples/p01_qo_{slug}.md
2. Compiled: P01_knowledge/compiled/p01_qo_{slug}.yaml

## Size Limits

1. Body: max 2048 bytes
2. Density: >= 0.85

## Technique Reference

| Technique | Latency Cost | Precision Impact | When to Use |
|-----------|-------------|-----------------|-------------|
| rewriting | 200-500ms | High | Ambiguous queries |
| expansion | 50-100ms | Medium | Vocabulary mismatch |
| decomposition | 300-800ms | High | Multi-part questions |
| hyde | 500-1000ms | Very high | Semantic gap |
| reranking | 100-300ms | Very high | Precision-critical |
