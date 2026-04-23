---
kind: config
id: bld_config_graph_rag_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for graph_rag_config production
quality: 8.6
title: "Config Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, config]
tldr: "Naming, paths, limits for graph_rag_config production"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_ab_test_config
  - bld_config_workflow_node
  - bld_config_usage_quota
  - bld_config_transport_config
  - bld_config_playground_config
  - bld_config_rl_algorithm
  - bld_config_search_strategy
  - bld_config_diff_strategy
  - bld_config_customer_segment
  - bld_config_agent_computer_interface
---

## Naming Convention
Pattern: `p01_grc_<name>.yaml`
Examples: `p01_grc_knowledge.yaml`, `p01_grc_finance.yaml`

## Paths
Artifacts: `/mnt/cex/data/artifacts/rag_configs/`
Logs: `/var/log/cex/rag_builder/`
Cache: `/tmp/cex/rag_cache/`

## Limits
max_bytes: 4096
max_turns: 5
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_ab_test_config]] | sibling | 0.58 |
| [[bld_config_workflow_node]] | sibling | 0.56 |
| [[bld_config_usage_quota]] | sibling | 0.54 |
| [[bld_config_transport_config]] | sibling | 0.54 |
| [[bld_config_playground_config]] | sibling | 0.54 |
| [[bld_config_rl_algorithm]] | sibling | 0.52 |
| [[bld_config_search_strategy]] | sibling | 0.52 |
| [[bld_config_diff_strategy]] | sibling | 0.51 |
| [[bld_config_customer_segment]] | sibling | 0.50 |
| [[bld_config_agent_computer_interface]] | sibling | 0.50 |
