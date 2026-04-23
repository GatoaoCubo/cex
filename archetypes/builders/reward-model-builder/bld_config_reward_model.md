---
kind: config
id: bld_config_reward_model
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for reward_model production
quality: 8.6
title: "Config Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, config]
tldr: "Naming, paths, limits for reward_model production"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_rl_algorithm
  - bld_config_benchmark_suite
  - bld_config_eval_framework
  - bld_config_workflow_node
  - bld_config_ab_test_config
  - bld_config_playground_config
  - bld_config_graph_rag_config
  - bld_config_memory_benchmark
  - bld_config_customer_segment
  - bld_config_judge_config
---

## Naming Convention
p07_rwm_<model_name>_<timestamp> (e.g., p07_rwm_rlhf_v1_20231005)

## Paths
- Models: `/mnt/artifacts/p07/rwm/{{name}}/models/`
- Logs: `/mnt/artifacts/p07/rwm/{{name}}/logs/`
- Checkpoints: `/mnt/artifacts/p07/rwm/{{name}}/checkpoints/`

## Limits
- max_bytes: 5120
- max_turns: 20
- effort_level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_rl_algorithm]] | sibling | 0.68 |
| [[bld_config_benchmark_suite]] | sibling | 0.65 |
| [[bld_config_eval_framework]] | sibling | 0.60 |
| [[bld_config_workflow_node]] | sibling | 0.58 |
| [[bld_config_ab_test_config]] | sibling | 0.56 |
| [[bld_config_playground_config]] | sibling | 0.56 |
| [[bld_config_graph_rag_config]] | sibling | 0.52 |
| [[bld_config_memory_benchmark]] | sibling | 0.52 |
| [[bld_config_customer_segment]] | sibling | 0.51 |
| [[bld_config_judge_config]] | sibling | 0.50 |
