---
kind: quality_gate
id: bld_eval_query_optimizer
pillar: P07
llm_function: GOVERN
purpose: Quality gate for query_optimizer artifacts
quality: null
title: "Query Optimizer Builder - Eval ISO"
version: "1.0.0"
author: n03_builder
tags: [query_optimizer, builder, quality_gate]
tldr: "Quality gate for query optimizer: validates techniques, latency budget, and fallback behavior."
domain: "query optimization"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_schema_query_optimizer
---

## Quality Gate

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match ^p01_qo_[a-z][a-z0-9_]+$ |
| H03 | kind field matches | kind is not 'query_optimizer' |
| H04 | techniques defined | techniques list empty or missing |
| H05 | quality is null | quality must be null |
| H06 | target_system defined | target_system missing or empty |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Strategy clarity | 0.20 | Pipeline order documented with rationale |
| D2 | Technique depth | 0.15 | Each technique described with parameters |
| D3 | Latency budget | 0.15 | Numeric time allocation per step |
| D4 | Re-ranking config | 0.15 | Model and counts specified (if applicable) |
| D5 | Fallback defined | 0.15 | Behavior on failure documented |
| D6 | Query type coverage | 0.10 | Handles different query patterns |
| D7 | Documentation | 0.10 | tldr captures key info |

## Actions

| Score | Action |
|-------|--------|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |

## Validation Checklist

| Check | Method | Automated |
|-------|--------|-----------|
| Frontmatter schema | cex_compile.py --validate | Yes |
| Naming convention | Regex match against p01_qo_{{name}}.md + .yaml | Yes |
| Size limit | Byte count <= 5120 | Yes |
| Density score | Token/byte ratio >= 0.85 | Yes |
| Cross-references valid | Link resolution check | Partial |

## Properties

| Property | Value |
|----------|-------|
| Kind | `eval` |
| Pillar | P07 |
| Domain | query optimizer construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
