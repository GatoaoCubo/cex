---
kind: architecture
id: bld_architecture_benchmark
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of benchmark — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Benchmark"
version: "1.0.0"
author: n03_builder
tags: [benchmark, builder, examples]
tldr: "Golden and anti-examples for benchmark construction, demonstrating ideal structure and common pitfalls."
domain: "benchmark construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - benchmark-builder
  - p03_sp_benchmark_builder
  - p01_kc_benchmark
  - bld_collaboration_benchmark
  - p11_qg_benchmark
  - bld_instruction_benchmark
  - p10_lr_benchmark-builder
  - bld_output_template_benchmark
  - benchmark-suite-builder
  - bld_tools_benchmark
---

# Architecture: benchmark in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 22-field metadata header (id, kind, pillar, domain, metric_type, target_system, etc.) | benchmark-builder | required |
| metric_definitions | Named quantitative metrics with units (p50_latency_ms, cost_per_call_usd, throughput_rps) | author | required |
| baseline | Current measured performance values (pre-optimization reference point) | author | required |
| target | Desired performance values that define pass/fail threshold | author | required |
| methodology | Measurement protocol: iterations, warmup_runs, percentiles, environment isolation | author | required |
| environment_spec | Hardware, runtime, model version, concurrency settings required for reproducibility | author | required |
| statistical_config | Significance thresholds, variance tolerance, outlier handling rules | author | required |
| results_schema | Structure for recording raw measurement data and computed statistics | benchmark-builder | required |
## Dependency Graph
```
environment_spec  --depends-->   benchmark  --produces_for-->  scoring_rubric
boot_config       --produces-->  benchmark  --produces_for-->  quality_gate
methodology       --depends-->   benchmark  --produces_for-->  model_card
benchmark         --signals-->   comparison_report
benchmark         --produces-->  raw_results (feeds downstream consumers)
```
| From | To | Type | Data |
|------|----|------|------|
| boot_config (P02) | benchmark | data_flow | runtime configuration for the system under test |
| environment_spec | benchmark | depends | hardware and software environment for isolation |
| benchmark | scoring_rubric (P07) | produces | quantitative metrics used as evaluation input |
| benchmark | quality_gate (P11) | produces | numeric baselines and thresholds for pass/fail gates |
| benchmark | model_card (P02) | produces | performance data (latency, cost, throughput) for LLM specs |
| benchmark | comparison_report | signals | delta between baseline and target after measurement run |
| benchmark | raw_results | produces | iteration-level measurements for statistical analysis |
## Boundary Table
| benchmark IS | benchmark IS NOT |
|--------------|-----------------|
| A quantitative measurement of system performance (latency, cost, throughput) | A multi-dimensional quality evaluation (scoring_rubric) |
| Reproducible — defined methodology, isolated environment, fixed seed | A one-time correctness test (unit_eval) |
| Statistical — percentiles, warmup, significance thresholds | A pass/fail sanity check (smoke_eval) |
| The raw number source that other eval types reference | A reference example demonstrating correct output (golden_test) |
| Scoped to a specific system, model version, and environment | A full pipeline correctness test (e2e_eval) |
| Produces baselines that inform quality gates and model cards | A subjective or qualitative assessment |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Configuration | boot_config, environment_spec, statistical_config | Define the system under test and measurement conditions |
| Definition | frontmatter, metric_definitions, baseline, target | Specify what is measured and what success looks like |
| Execution | methodology (iterations, warmup, percentiles) | Protocol for running reproducible measurements |
| Collection | results_schema, raw_results | Capture iteration-level data for statistical processing |
| Distribution | scoring_rubric, quality_gate, model_card | Downstream consumers that use benchmark numbers as inputs |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[benchmark-builder]] | upstream | 0.57 |
| [[p03_sp_benchmark_builder]] | upstream | 0.47 |
| [[p01_kc_benchmark]] | upstream | 0.45 |
| [[bld_collaboration_benchmark]] | downstream | 0.45 |
| [[p11_qg_benchmark]] | downstream | 0.42 |
| [[bld_instruction_benchmark]] | upstream | 0.36 |
| [[p10_lr_benchmark-builder]] | downstream | 0.35 |
| [[bld_output_template_benchmark]] | upstream | 0.35 |
| [[benchmark-suite-builder]] | upstream | 0.33 |
| [[bld_tools_benchmark]] | upstream | 0.31 |
