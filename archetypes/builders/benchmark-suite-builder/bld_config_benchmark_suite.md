---
kind: config
id: bld_config_benchmark_suite
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for benchmark_suite production
quality: 8.6
title: "Config Benchmark Suite"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [benchmark_suite, builder, config]
tldr: "Naming, paths, limits for benchmark_suite production"
domain: "benchmark_suite construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_reward_model
  - bld_config_eval_framework
  - bld_config_rl_algorithm
  - bld_config_playground_config
  - bld_config_workflow_node
  - bld_config_ab_test_config
  - bld_config_memory_benchmark
  - bld_config_customer_segment
  - bld_config_graph_rag_config
  - bld_config_sandbox_spec
---

## Naming Convention
Pattern: `p07_bs_{{name}}.md`
Examples: `p07_bs_chat_completion.md`, `p07_bs_code_generation.md`
Note: `{{name}}` replaced by benchmark-specific identifier; pillar (P07) prefix enforced.

## Paths
Artifacts: `/mnt/data/benchmarks/p07/{{name}}/artifacts`
Logs: `/mnt/data/benchmarks/p07/{{name}}/logs`
Outputs: `/mnt/data/benchmarks/p07/{{name}}/outputs`

## Limits
max_bytes: 5120
max_turns: 20
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_reward_model]] | sibling | 0.57 |
| [[bld_config_eval_framework]] | sibling | 0.54 |
| [[bld_config_rl_algorithm]] | sibling | 0.52 |
| [[bld_config_playground_config]] | sibling | 0.51 |
| [[bld_config_workflow_node]] | sibling | 0.50 |
| [[bld_config_ab_test_config]] | sibling | 0.48 |
| [[bld_config_memory_benchmark]] | sibling | 0.46 |
| [[bld_config_customer_segment]] | sibling | 0.46 |
| [[bld_config_graph_rag_config]] | sibling | 0.45 |
| [[bld_config_sandbox_spec]] | sibling | 0.43 |
