---
kind: schema
id: bld_schema_memory_benchmark
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for memory_benchmark
quality: 9.1
title: "Schema Memory Benchmark"
version: "1.1.0"
author: n05_operations
tags: [memory_benchmark, builder, schema]
tldr: "Formal schema for AI agent memory benchmark artifacts"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_search_strategy
  - bld_schema_playground_config
---

## Frontmatter Fields

### Required

| Field          | Type   | Required | Default | Notes                                          |
|----------------|--------|----------|---------|------------------------------------------------|
| id             | string | yes      |         | Must match ID Pattern below                    |
| kind           | string | yes      |         | Fixed: "memory_benchmark"                      |
| pillar         | string | yes      |         | Fixed: "P07"                                   |
| title          | string | yes      |         | Human-readable benchmark name                  |
| version        | string | yes      | "1.0.0" | Semantic versioning                            |
| created        | date   | yes      |         | ISO 8601                                       |
| updated        | date   | yes      |         | ISO 8601                                       |
| author         | string | yes      |         | Primary contributor                            |
| domain         | string | yes      |         | Application domain (e.g., "multi-turn recall") |
| quality        | null   | yes      | null    | Never self-score; peer review assigns          |
| tags           | list   | yes      | []      | Keywords for categorization                    |
| tldr           | string | yes      |         | One-sentence summary                           |
| memory_type    | string | yes      |         | "in_context" | "external_store" | "hybrid"     |
| eval_distance  | string | yes      |         | Turn/token range tested (e.g., "5-100 turns")  |

### Recommended

| Field           | Type   | Notes                                          |
|-----------------|--------|------------------------------------------------|
| reference_bench | string | Established benchmark this extends (LOCOMO...) |
| metric_count    | number | Number of distinct metrics defined             |
| dataset         | string | Source dataset for test conversations          |

## ID Pattern

^p07_mb_[a-z][a-z0-9_]+.md$

## Body Structure

1. **Overview**
   - Purpose, scope, and target AI memory system type.
2. **Metrics**
   - Each metric: name, formula, scale (0-1 or 0-100), primary tool.
3. **Test Protocol**
   - Conversation generation, fact planting depth, query turn distance.
4. **Reference Benchmarks**
   - Alignment with LOCOMO, LongMemEval, MemGPT, MT-Bench-101, or equivalent.
5. **Evaluation Criteria**
   - Pass/fail thresholds, comparison baseline, hallucination budget.
6. **Notes**
   - Caveats, scope limitations, known failure modes.

## Constraints

- ID must conform to: ^p07_mb_[a-z][a-z0-9_]+.md$
- All required fields must be present and non-null
- version must follow semantic versioning
- memory_type must be one of: in_context, external_store, hybrid
- File size must not exceed 5120 bytes
- quality field must be assigned by peer review only
- NO hardware memory fields (capacity_mb, dram_latency, bandwidth_gbps, ecc_rate)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_benchmark_suite]] | sibling | 0.75 |
| [[bld_schema_usage_report]] | sibling | 0.72 |
| [[bld_schema_reranker_config]] | sibling | 0.71 |
| [[bld_schema_sandbox_config]] | sibling | 0.68 |
| [[bld_schema_dataset_card]] | sibling | 0.68 |
| [[bld_schema_integration_guide]] | sibling | 0.68 |
| [[bld_schema_quickstart_guide]] | sibling | 0.68 |
| [[bld_schema_pitch_deck]] | sibling | 0.68 |
| [[bld_schema_search_strategy]] | sibling | 0.67 |
| [[bld_schema_playground_config]] | sibling | 0.66 |
