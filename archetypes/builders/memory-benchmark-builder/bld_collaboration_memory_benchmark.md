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
