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
related:
  - bld_collaboration_eval_framework
  - bld_collaboration_memory_benchmark
  - benchmark-suite-builder
  - bld_collaboration_llm_evaluation_scenario
  - bld_collaboration_eval_metric
  - bld_collaboration_cohort_analysis
  - bld_collaboration_reranker_config
  - bld_collaboration_reward_model
  - bld_collaboration_sso_config
  - bld_collaboration_white_label_config
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_eval_framework]] | sibling | 0.34 |
| [[bld_collaboration_memory_benchmark]] | sibling | 0.33 |
| [[benchmark-suite-builder]] | upstream | 0.31 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.26 |
| [[bld_collaboration_eval_metric]] | sibling | 0.24 |
| [[bld_collaboration_cohort_analysis]] | sibling | 0.24 |
| [[bld_collaboration_reranker_config]] | sibling | 0.24 |
| [[bld_collaboration_reward_model]] | sibling | 0.23 |
| [[bld_collaboration_sso_config]] | sibling | 0.23 |
| [[bld_collaboration_white_label_config]] | sibling | 0.23 |
