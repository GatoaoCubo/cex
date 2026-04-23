---
kind: collaboration
id: bld_collaboration_eval_metric
pillar: P12
llm_function: COLLABORATE
purpose: How eval_metric-builder works in crews with other builders
quality: 8.9
title: "Collaboration Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, collaboration]
tldr: "How eval_metric-builder works in crews with other builders"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_reranker_config
  - eval-metric-builder
  - bld_collaboration_cohort_analysis
  - bld_collaboration_reward_model
  - bld_collaboration_memory_benchmark
  - bld_collaboration_visual_workflow
  - bld_collaboration_sso_config
  - bld_collaboration_ab_test_config
  - bld_collaboration_sandbox_spec
  - bld_collaboration_response_format
---

## Crew Role  
Defines and structures individual evaluation metrics, specifying calculation logic, input requirements, and output formats for quantitative assessment.  

## Receives From  
| Builder        | What                  | Format         |  
|----------------|-----------------------|----------------|  
| Data Provider  | Dataset samples       | Parquet/CSV    |  
| Metric Specifier | Metric configuration | JSON schema    |  
| Domain Expert  | Business rules        | Natural language |  

## Produces For  
| Builder        | What                  | Format         |  
|----------------|-----------------------|----------------|  
| Metric Validator | Metric definition   | JSON/YAML      |  
| Calculation Engine | Script            | Python         |  
| Documentation Team | Technical spec    | Markdown       |  
| Validation Team | Test cases          | CSV/JSON       |  

## Boundary  
Does NOT handle composite metrics (benchmark_suite builder), qualitative rubrics (scoring_rubric builder), or data collection (data_provider).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_reranker_config]] | sibling | 0.32 |
| [[eval-metric-builder]] | upstream | 0.29 |
| [[bld_collaboration_cohort_analysis]] | sibling | 0.28 |
| [[bld_collaboration_reward_model]] | sibling | 0.28 |
| [[bld_collaboration_memory_benchmark]] | sibling | 0.28 |
| [[bld_collaboration_visual_workflow]] | sibling | 0.28 |
| [[bld_collaboration_sso_config]] | sibling | 0.27 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.27 |
| [[bld_collaboration_sandbox_spec]] | sibling | 0.26 |
| [[bld_collaboration_response_format]] | sibling | 0.26 |
