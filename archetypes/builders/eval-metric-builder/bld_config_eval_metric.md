---
kind: config
id: bld_config_eval_metric
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for eval_metric production
quality: 8.6
title: "Config Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, config]
tldr: "Naming, paths, limits for eval_metric production"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_ab_test_config
  - bld_config_eval_framework
  - bld_config_workflow_node
  - bld_config_reward_model
  - bld_config_rl_algorithm
  - bld_config_benchmark_suite
  - bld_config_diff_strategy
  - bld_config_search_strategy
  - bld_config_agent_computer_interface
  - bld_config_transport_config
---

## Naming Convention
Pattern: `p07_em_<metric_name>`
Examples:
- p07_em_accuracy
- p07_em_f1_score

## Paths
Artifacts: `/mnt/artifacts/p07/em/<metric_name>/`
Checksum: `/mnt/checksums/p07/em/<metric_name>.sha256`
Note: Use POSIX-compliant paths only

## Limits
max_bytes: 4096
max_turns: 100
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_ab_test_config]] | sibling | 0.57 |
| [[bld_config_eval_framework]] | sibling | 0.54 |
| [[bld_config_workflow_node]] | sibling | 0.53 |
| [[bld_config_reward_model]] | sibling | 0.53 |
| [[bld_config_rl_algorithm]] | sibling | 0.53 |
| [[bld_config_benchmark_suite]] | sibling | 0.52 |
| [[bld_config_diff_strategy]] | sibling | 0.52 |
| [[bld_config_search_strategy]] | sibling | 0.52 |
| [[bld_config_agent_computer_interface]] | sibling | 0.51 |
| [[bld_config_transport_config]] | sibling | 0.51 |
