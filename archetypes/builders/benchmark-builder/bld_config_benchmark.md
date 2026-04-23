---
kind: config
id: bld_config_benchmark
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for benchmark production
pattern: CONFIG restricts SCHEMA, never contradicts
effort: high
max_turns: 25
disallowed_tools: []
fork_context: fork
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Benchmark"
version: "1.0.0"
author: n03_builder
tags: [benchmark, builder, examples]
tldr: "Golden and anti-examples for benchmark construction, demonstrating ideal structure and common pitfalls."
domain: "benchmark construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_retriever_config
  - bld_config_quality_gate
  - bld_config_validation_schema
  - bld_output_template_benchmark
  - bld_config_memory_scope
  - benchmark-builder
  - bld_schema_benchmark
  - bld_tools_benchmark
  - bld_config_prompt_version
  - bld_config_scoring_rubric
---
# Config: benchmark Production Rules
## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p07_bm_{metric_slug}.md | p07_bm_ttft_sonnet4.md |
| Builder dir | kebab-case | benchmark-builder/ |
| Fields | snake_case | comparison_subjects, statistical_test |
| Metric slugs | lowercase_underscores | ttft, tps, cost_per_1m_input |
Rule: id MUST equal filename stem.
## File Paths
1. Output: cex/P07_evals/examples/p07_bm_{metric_slug}.md
2. Compiled: cex/P07_evals/compiled/p07_bm_{metric_slug}.yaml
## Size Limits (aligned with SCHEMA)
1. Body: max 4096 bytes
2. Density: >= 0.80
3. Metrics table: >= 1 row (no upper limit)
## Measurement Policy
1. iterations >= 10 (prefer >= 30 for statistical significance)
2. warmup >= 1 (prefer >= 5 for JIT/caching warmup)
3. Percentiles MUST include p50 + p95 (p75 and p99 recommended)
4. No dimension below p50 (median is minimum granularity)
5. Baseline MUST be measured, not estimated or assumed

## Metadata

```yaml
id: bld_config_benchmark
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-config-benchmark.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | benchmark construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_retriever_config]] | sibling | 0.38 |
| [[bld_config_quality_gate]] | sibling | 0.38 |
| [[bld_config_validation_schema]] | sibling | 0.37 |
| [[bld_output_template_benchmark]] | upstream | 0.36 |
| [[bld_config_memory_scope]] | sibling | 0.35 |
| [[benchmark-builder]] | upstream | 0.35 |
| [[bld_schema_benchmark]] | upstream | 0.35 |
| [[bld_tools_benchmark]] | upstream | 0.34 |
| [[bld_config_prompt_version]] | sibling | 0.34 |
| [[bld_config_scoring_rubric]] | sibling | 0.33 |
