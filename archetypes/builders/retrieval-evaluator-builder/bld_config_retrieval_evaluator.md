---
kind: config
id: bld_config_retrieval_evaluator
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
quality: null
title: "Retrieval Evaluator Builder - Config ISO"
version: "1.0.0"
author: n03_builder
tags: [retrieval_evaluator, builder, config]
tldr: "Production config for retrieval evaluator: naming, paths, size limits, and operational constraints."
domain: "retrieval evaluation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_schema_retrieval_evaluator
  - bld_architecture_retrieval_evaluator
---

# Config: retrieval_evaluator Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | p07_re_{evaluator_slug}.md | p07_re_rag_retrieval_v1.md |
| Builder directory | kebab-case | retrieval-evaluator-builder/ |
| Frontmatter fields | snake_case | primary_metric, k_values |

Rule: id MUST equal filename stem.

## File Paths

1. Output: P07_evals/examples/p07_re_{evaluator_slug}.md
2. Compiled: P07_evals/compiled/p07_re_{evaluator_slug}.yaml

## Size Limits

1. Body: max 2048 bytes
2. Total: ~3000 bytes including frontmatter
3. Density: >= 0.85

## Metric Enum

| Metric | Use Case | Position-Aware |
|--------|----------|----------------|
| ndcg | Graded relevance, ranked list | Yes |
| mrr | Single-answer, first hit | Yes |
| map | Binary relevance, full list | Yes |
| precision | Top-k accuracy | Partially |
| recall | Coverage of relevant docs | No |

## Standard k Values

| Use Case | Recommended k Values |
|----------|---------------------|
| QA / navigational | [1, 3, 5] |
| Document search | [5, 10, 20] |
| Recommendation | [10, 20, 50] |
