---
kind: config
id: bld_config_workflow_node
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for workflow_node production
quality: 8.6
title: "Config Workflow Node"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [workflow_node, builder, config]
tldr: "Naming, paths, limits for workflow_node production"
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_rl_algorithm
  - bld_config_ab_test_config
  - bld_config_search_strategy
  - bld_config_customer_segment
  - bld_config_graph_rag_config
  - bld_config_visual_workflow
  - bld_config_eval_framework
  - bld_config_sales_playbook
  - bld_config_pricing_page
  - bld_config_diff_strategy
---

## Naming Convention
Pattern: `p12_wn_{{name}}.md`
Examples: `p12_wn_data_processing.md`, `p12_wn_user_auth.md`

## Paths
Artifacts: `/mnt/artifacts/p12/workflow_nodes/{{name}}/`
Logs: `/var/log/p12/workflow_nodes/{{name}}/`

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
| [[bld_config_rl_algorithm]] | sibling | 0.62 |
| [[bld_config_ab_test_config]] | sibling | 0.61 |
| [[bld_config_search_strategy]] | sibling | 0.59 |
| [[bld_config_customer_segment]] | sibling | 0.58 |
| [[bld_config_graph_rag_config]] | sibling | 0.58 |
| [[bld_config_visual_workflow]] | sibling | 0.58 |
| [[bld_config_eval_framework]] | sibling | 0.58 |
| [[bld_config_sales_playbook]] | sibling | 0.58 |
| [[bld_config_pricing_page]] | sibling | 0.57 |
| [[bld_config_diff_strategy]] | sibling | 0.57 |
