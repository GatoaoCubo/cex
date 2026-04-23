---
kind: config
id: bld_config_playground_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for playground_config production
quality: 8.6
title: "Config Playground Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [playground_config, builder, config]
tldr: "Naming, paths, limits for playground_config production"
domain: "playground_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_graph_rag_config
  - bld_config_ab_test_config
  - bld_config_sandbox_spec
  - bld_config_rl_algorithm
  - bld_config_workflow_node
  - bld_config_customer_segment
  - bld_config_transport_config
  - bld_config_data_residency
  - bld_config_usage_quota
  - bld_config_benchmark_suite
---

## Naming Convention
Pattern: `p09_pg_{{name}}.yaml`
Examples:
- p09_pg_example.yaml
- p09_pg_test.yaml

## Paths
Artifacts: `/mnt/data/cex/playgrounds/p09/{{name}}`
Logs: `/mnt/data/cex/logs/p09/{{name}}`

## Limits
- max_bytes: 4096
- max_turns: 0
- effort_level: 0

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_graph_rag_config]] | sibling | 0.59 |
| [[bld_config_ab_test_config]] | sibling | 0.58 |
| [[bld_config_sandbox_spec]] | sibling | 0.56 |
| [[bld_config_rl_algorithm]] | sibling | 0.56 |
| [[bld_config_workflow_node]] | sibling | 0.56 |
| [[bld_config_customer_segment]] | sibling | 0.54 |
| [[bld_config_transport_config]] | sibling | 0.53 |
| [[bld_config_data_residency]] | sibling | 0.53 |
| [[bld_config_usage_quota]] | sibling | 0.52 |
| [[bld_config_benchmark_suite]] | sibling | 0.51 |
