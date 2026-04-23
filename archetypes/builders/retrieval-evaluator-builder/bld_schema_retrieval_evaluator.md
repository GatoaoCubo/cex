---
kind: schema
id: bld_schema_retrieval_evaluator
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for retrieval_evaluator
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: null
title: "Retrieval Evaluator Builder - Schema ISO"
version: "1.0.0"
author: n03_builder
tags: [retrieval_evaluator, builder, schema]
tldr: "Schema definition for retrieval evaluator artifacts -- fields, types, constraints, and body structure."
domain: "retrieval evaluation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_output_retrieval_evaluator
  - bld_eval_retrieval_evaluator
  - bld_config_retrieval_evaluator
---

# Schema: retrieval_evaluator

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_re_{slug}) | YES | - | Namespace compliance |
| kind | literal "retrieval_evaluator" | YES | - | Type integrity |
| pillar | literal "P07" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| target_system | string | YES | - | System under evaluation |
| primary_metric | enum (ndcg, mrr, map, precision, recall) | YES | - | Main ranking metric |
| k_values | list[integer] | YES | - | Cutoff values for @k metrics |
| judgment_scale | enum (binary, graded) | YES | "binary" | Relevance judgment type |
| min_query_set_size | integer | YES | 50 | Minimum queries for stable estimates |
| baseline | string | YES | - | Reference system for comparison |
| domain | string | YES | - | Evaluation domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "retrieval" and "evaluation" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p07_re_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)

1. `## Metrics` -- primary and secondary metrics with formulas
2. `## Query Set` -- construction methodology and minimum size
3. `## Judgment Protocol` -- relevance scale and annotation guidelines
4. `## Baseline` -- reference system and expected score ranges
5. `## Thresholds` -- pass/fail/regression criteria

## Constraints

- naming: p07_re_{evaluator_slug}.md
- id == filename stem
- primary_metric MUST be one of: ndcg, mrr, map, precision, recall
- judgment_scale MUST be one of: binary, graded
- min_query_set_size MUST be >= 30
- quality: null always
- retrieval_evaluator is EVALUATION -- no retrieval logic
