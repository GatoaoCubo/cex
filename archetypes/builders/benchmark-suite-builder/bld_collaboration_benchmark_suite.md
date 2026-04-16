---
kind: collaboration
id: bld_collaboration_benchmark_suite
pillar: P12
llm_function: COLLABORATE
purpose: How benchmark_suite-builder works in crews with other builders
quality: 8.9
title: "Collaboration Benchmark Suite"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [benchmark_suite, builder, collaboration]
tldr: "How benchmark_suite-builder works in crews with other builders"
domain: "benchmark_suite construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Coordinates integration of multiple benchmarks into cohesive suites, ensuring consistency, versioning, and dependency management across components.  

## Receives From  
| Builder | What | Format |  
|---|---|---|  
| Benchmark Author | Individual benchmarks | YAML |  
| Config Manager | Configuration parameters | JSON |  
| Data Provider | Datasets | CSV |  

## Produces For  
| Builder | What | Format |  
|---|---|---|  
| Suite Validator | Benchmark suite | JSON |  
| QA Team | Validation report | Markdown |  
| Dev Team | Dependency graph | DOT |  

## Boundary  
Does NOT execute benchmarks (Benchmark Runner handles execution), analyze results (Eval Framework handles analysis), or manage user requests (User Interface handles direct interactions).
