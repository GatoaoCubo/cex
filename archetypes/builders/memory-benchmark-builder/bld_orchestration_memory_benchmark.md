---
kind: collaboration
id: bld_collaboration_memory_benchmark
pillar: P12
llm_function: COLLABORATE
purpose: How memory_benchmark-builder works in crews with other builders
quality: 8.9
title: "Collaboration Memory Benchmark"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_benchmark, builder, collaboration]
tldr: "How memory_benchmark-builder works in crews with other builders"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_memory_scope
  - bld_collaboration_benchmark_suite
  - memory-benchmark-builder
  - bld_collaboration_memory_type
  - benchmark-suite-builder
  - bld_collaboration_eval_metric
  - bld_manifest_memory_type
  - memory-scope-builder
  - bld_collaboration_sandbox_config
  - bld_collaboration_llm_evaluation_scenario
---

## Crew Role  
Generates and validates memory-specific benchmark tests, ensuring alignment with evaluation criteria and data integrity.  

## Receives From  
| Builder       | What                  | Format  |  
|---------------|-----------------------|---------|  
| scenario_gen | Test scenarios        | JSON    |  
| config_mgr    | Memory config params  | YAML    |  
| data_prov     | Synthetic memory data | CSV     |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| eval_suite    | Memory benchmark suite| JSON        |  
| report_gen    | Evaluation report     | Markdown    |  
| metrics_agg   | Performance metrics   | Parquet     |  

## Boundary  
Does NOT handle system architecture design (memory_architecture) or general-purpose benchmarks (benchmark_suite).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_memory_scope]] | sibling | 0.33 |
| [[bld_collaboration_benchmark_suite]] | sibling | 0.33 |
| [[memory-benchmark-builder]] | upstream | 0.32 |
| [[bld_collaboration_memory_type]] | sibling | 0.31 |
| [[benchmark-suite-builder]] | upstream | 0.29 |
| [[bld_collaboration_eval_metric]] | sibling | 0.29 |
| [[bld_manifest_memory_type]] | upstream | 0.29 |
| [[memory-scope-builder]] | upstream | 0.29 |
| [[bld_collaboration_sandbox_config]] | sibling | 0.26 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.26 |
