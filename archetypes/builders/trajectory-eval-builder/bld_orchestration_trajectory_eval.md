---
kind: collaboration
id: bld_collaboration_trajectory_eval
pillar: P12
llm_function: COLLABORATE
purpose: How trajectory_eval-builder works in crews with other builders
quality: 8.9
title: "Collaboration Trajectory Eval"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [trajectory_eval, builder, collaboration]
tldr: "How trajectory_eval-builder works in crews with other builders"
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - trajectory-eval-builder
  - kc_trajectory_eval
  - p03_sp_trajectory_eval_builder
  - bld_collaboration_agentic_rag
  - bld_instruction_trajectory_eval
  - bld_collaboration_cohort_analysis
  - bld_collaboration_memory_benchmark
  - bld_collaboration_eval_metric
  - bld_examples_trajectory_eval
  - bld_knowledge_card_trajectory_eval
---

## Crew Role  
Analyzes and evaluates trajectory data to assess performance, safety, and compliance with constraints. Generates metrics, visualizations, and feedback for iterative improvement.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| data_collector| Raw trajectory logs   | JSON/CSV    |  
| simulation_env| Simulated trajectory  | Binary log  |  
| planner       | Planned trajectory    | ROS bag     |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| visualization | Trajectory plots      | PNG/HTML    |  
| metrics_aggregator | Performance metrics | JSON      |  
| feedback_system | Evaluation reports  | Markdown    |  

## Boundary  
Does NOT handle static benchmarking (benchmark_builder), end-to-end testing (e2e_eval_builder), or raw data collection (data_collector).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[trajectory-eval-builder]] | upstream | 0.44 |
| [[kc_trajectory_eval]] | related | 0.35 |
| [[p03_sp_trajectory_eval_builder]] | upstream | 0.34 |
| [[bld_collaboration_agentic_rag]] | sibling | 0.28 |
| [[bld_instruction_trajectory_eval]] | upstream | 0.25 |
| [[bld_collaboration_cohort_analysis]] | sibling | 0.23 |
| [[bld_collaboration_memory_benchmark]] | sibling | 0.23 |
| [[bld_collaboration_eval_metric]] | sibling | 0.22 |
| [[bld_examples_trajectory_eval]] | upstream | 0.21 |
| [[bld_knowledge_card_trajectory_eval]] | upstream | 0.20 |
