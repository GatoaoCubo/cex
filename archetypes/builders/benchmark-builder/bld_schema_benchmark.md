---
kind: schema
id: bld_schema_benchmark
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for benchmark
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Benchmark"
version: "1.0.0"
author: n03_builder
tags: [benchmark, builder, examples]
tldr: "Golden and anti-examples for benchmark construction, demonstrating ideal structure and common pitfalls."
domain: "benchmark construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_usage_report
  - bld_schema_unit_eval
  - bld_schema_golden_test
  - bld_schema_reranker_config
  - bld_schema_smoke_eval
  - bld_schema_benchmark_suite
  - bld_schema_quickstart_guide
  - bld_schema_action_prompt
  - bld_schema_search_strategy
  - bld_schema_retriever_config
---

# Schema: benchmark
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_bm_{metric_slug}) | YES | — | Namespace compliance |
| kind | literal "benchmark" | YES | — | Type integrity |
| pillar | literal "P07" | YES | — | Pillar assignment |
| title | string "Benchmark: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| metric | string | YES | — | What is being measured (e.g., latency, throughput, cost) |
| unit | string | YES | — | Measurement unit (ms, tokens/s, USD, req/s) |
| direction | enum: lower_is_better, higher_is_better | YES | — | Optimization direction |
| baseline | number | YES | — | Current measured value |
| target | number | YES | — | Goal value |
| iterations | integer >= 10 | YES | — | Number of measurement runs |
| warmup | integer >= 1 | YES | — | Warmup runs before measurement |
| percentiles | list[integer] | YES | [50, 95, 99] | Which percentiles to report |
| environment | string | YES | — | Hardware/software description |
| domain | string | YES | — | Domain this benchmark covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| comparison_subjects | list[string] | REC | — | What entities are compared |
| statistical_test | string | REC | — | Significance test (t-test, Mann-Whitney) |
| confidence_interval | float 0.0-1.0 | REC | 0.95 | Confidence level |
| density_score | float 0.80-1.00 | REC | — | Content density |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
## ID Pattern
Regex: `^p07_bm_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Benchmark Overview` — what is measured, why, and business impact
2. `## Methodology` — how the benchmark runs (iterations, warmup, environment)
3. `## Metrics` — table: metric, unit, baseline, target, direction
4. `## Environment` — hardware, software, configuration for reproducibility
5. `## Results Template` — percentile table structure for recording results
## Constraints
- max_bytes: 4096 (body only)
- naming: p07_bm_{metric_slug}.md + .yaml
- id == filename stem
- iterations MUST be >= 10
- warmup MUST be >= 1
- percentiles MUST include at least p50 and p95
- baseline and target MUST use same unit
- direction MUST be explicit (no implicit assumptions)
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.66 |
| [[bld_schema_unit_eval]] | sibling | 0.66 |
| [[bld_schema_golden_test]] | sibling | 0.66 |
| [[bld_schema_reranker_config]] | sibling | 0.66 |
| [[bld_schema_smoke_eval]] | sibling | 0.65 |
| [[bld_schema_benchmark_suite]] | sibling | 0.65 |
| [[bld_schema_quickstart_guide]] | sibling | 0.65 |
| [[bld_schema_action_prompt]] | sibling | 0.64 |
| [[bld_schema_search_strategy]] | sibling | 0.64 |
| [[bld_schema_retriever_config]] | sibling | 0.64 |
