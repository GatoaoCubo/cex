---
kind: instruction
id: bld_instruction_benchmark
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for benchmark
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Benchmark"
version: "1.0.0"
author: n03_builder
tags: [benchmark, builder, examples]
tldr: "Golden and anti-examples for benchmark construction, demonstrating ideal structure and common pitfalls."
domain: "benchmark construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_benchmark_builder
  - p11_qg_benchmark
  - bld_instruction_golden_test
  - bld_instruction_agent
  - bld_instruction_boot_config
  - bld_output_template_benchmark
  - benchmark-builder
  - bld_instruction_retriever_config
  - bld_instruction_action_prompt
  - bld_instruction_output_validator
---

# Instructions: How to Produce a benchmark
## Phase 1: RESEARCH
1. Identify the target system or component being measured
2. Define metrics: for each metric specify name, unit (ms, req/s, USD, tokens), and direction (lower_is_better or higher_is_better). Include latency percentiles (p50, p95, p99), throughput, cost, and quality score as applicable
3. Establish baseline: gather current measured values from logs, monitoring, or prior runs — never estimate
4. Set targets: derive from SLA requirements, competitor data, or explicit improvement goals — must be numeric
5. Define methodology: number of iterations (minimum 10), warmup runs (minimum 1), statistical significance approach, and percentile calculation method
6. Document environment spec: hardware (CPU, RAM, disk), OS, runtime versions, config settings — sufficient to reproduce
7. Search for existing benchmarks covering the same system and metric (avoid duplicates)
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — template to fill
3. Fill frontmatter: all 22 required fields (quality: null, never self-score)
4. Write Setup section: environment dependencies, fixtures, and initialization steps
5. Write Methodology section: iterations count, warmup runs, percentile list, significance threshold, and measurement protocol
6. Write Metrics section: table with columns for metric name, unit, baseline value, target value, and direction
7. Write Execution section: exact commands needed to reproduce the benchmark run
8. Write Results Template section: pre-formatted table structure for recording p50/p95/p99 outcomes
9. Keep body <= 8192 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md manually
2. HARD gate: id matches `p07_bench_` pattern
3. HARD gate: kind == benchmark
4. HARD gate: quality == null
5. HARD gate: each metric has a unit specified
6. HARD gate: baseline and target are numeric and share the same unit
7. HARD gate: methodology specifies iterations count
8. HARD gate: percentiles include at least p50 and p95
9. Cross-check: is this measuring quantitative performance, not correctness? (correctness belongs in eval artifacts)
10. Cross-check: is this measuring performance, not defining pass/fail criteria? (criteria belong in scoring rubrics)
11. If score < 8.0: revise before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify benchmark
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
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
| [[p03_sp_benchmark_builder]] | related | 0.44 |
| [[p11_qg_benchmark]] | downstream | 0.43 |
| [[bld_instruction_golden_test]] | sibling | 0.42 |
| [[bld_instruction_agent]] | sibling | 0.37 |
| [[bld_instruction_boot_config]] | sibling | 0.37 |
| [[bld_output_template_benchmark]] | downstream | 0.35 |
| [[benchmark-builder]] | downstream | 0.35 |
| [[bld_instruction_retriever_config]] | sibling | 0.35 |
| [[bld_instruction_action_prompt]] | sibling | 0.34 |
| [[bld_instruction_output_validator]] | sibling | 0.34 |
