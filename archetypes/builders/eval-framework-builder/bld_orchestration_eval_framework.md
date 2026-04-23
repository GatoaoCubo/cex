---
kind: collaboration
id: bld_collaboration_eval_framework
pillar: P12
llm_function: COLLABORATE
purpose: How eval_framework-builder works in crews with other builders
quality: 8.9
title: "Collaboration Eval Framework"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_framework, builder, collaboration]
tldr: "How eval_framework-builder works in crews with other builders"
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_benchmark_suite
  - eval-framework-builder
  - bld_collaboration_eval_metric
  - bld_collaboration_llm_evaluation_scenario
  - bld_collaboration_memory_benchmark
  - benchmark-suite-builder
  - bld_collaboration_ab_test_config
  - bld_collaboration_dataset_card
  - bld_collaboration_sandbox_spec
  - kc_eval_framework
---

## Crew Role  
Designs and implements evaluation framework infrastructure, enabling modular integration of metrics, benchmarks, and execution pipelines. Acts as a central coordination layer for evaluation processes.  

## Receives From  
| Builder         | What                  | Format      |  
|------------------|-----------------------|-------------|  
| Config Manager   | Framework config specs| YAML        |  
| Benchmark Suite  | Integration requests  | API         |  
| Eval Metric      | Metric registration   | JSON        |  
| Data Engineer    | Data schema definitions| Avro        |  

## Produces For  
| Builder         | What                  | Format      |  
|------------------|-----------------------|-------------|  
| Benchmark Suite  | Framework API         | Python      |  
| Eval Metric      | Documentation spec    | Markdown    |  
| Test Engineer    | Validation test suite | pytest      |  
| UI/UX Team       | Framework UI spec     | Figma       |  

## Boundary  
Does NOT collect benchmarks (handled by benchmark_suite) or define individual metrics (handled by eval_metric). Does NOT curate datasets (handled by data_engineer). Does NOT handle deployment or CI/CD (handled by devops).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_benchmark_suite]] | sibling | 0.39 |
| [[eval-framework-builder]] | upstream | 0.34 |
| [[bld_collaboration_eval_metric]] | sibling | 0.34 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.32 |
| [[bld_collaboration_memory_benchmark]] | sibling | 0.31 |
| [[benchmark-suite-builder]] | upstream | 0.28 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.28 |
| [[bld_collaboration_dataset_card]] | sibling | 0.27 |
| [[bld_collaboration_sandbox_spec]] | sibling | 0.26 |
| [[kc_eval_framework]] | upstream | 0.26 |
