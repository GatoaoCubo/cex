---
kind: config
id: bld_config_memory_benchmark
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for memory_benchmark production
quality: 8.6
title: "Config Memory Benchmark"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [memory_benchmark, builder, config]
tldr: "Naming, paths, limits for memory_benchmark production"
domain: "memory_benchmark construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_eval_framework
  - bld_config_workflow_node
  - bld_config_rl_algorithm
  - bld_config_ab_test_config
  - bld_config_graph_rag_config
  - bld_config_search_strategy
  - bld_config_customer_segment
  - bld_config_diff_strategy
  - bld_config_sales_playbook
  - bld_config_pricing_page
---

p07_mb_{{name}}.md
## Naming Convention
Pattern: `p07_mb_{{name}}.md`
Examples: `p07_mb_memory_test.md`, `p07_mb_cache_check.md`

## Paths
Artifacts: `/mnt/artifacts/p07/memory_benchmarks/`
Logs: `/var/log/p07/memory_benchmark-builder/`

## Limits
max_bytes: 5120
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_eval_framework]] | sibling | 0.63 |
| [[bld_config_workflow_node]] | sibling | 0.63 |
| [[bld_config_rl_algorithm]] | sibling | 0.59 |
| [[bld_config_ab_test_config]] | sibling | 0.59 |
| [[bld_config_graph_rag_config]] | sibling | 0.58 |
| [[bld_config_search_strategy]] | sibling | 0.57 |
| [[bld_config_customer_segment]] | sibling | 0.56 |
| [[bld_config_diff_strategy]] | sibling | 0.56 |
| [[bld_config_sales_playbook]] | sibling | 0.56 |
| [[bld_config_pricing_page]] | sibling | 0.55 |
