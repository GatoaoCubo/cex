---
kind: config
id: bld_config_trajectory_eval
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for trajectory_eval production
quality: 8.6
title: "Config Trajectory Eval"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [trajectory_eval, builder, config]
tldr: "Naming, paths, limits for trajectory_eval production"
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_customer_segment
  - bld_config_agent_computer_interface
  - bld_config_diff_strategy
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_integration_guide
  - bld_config_graph_rag_config
  - bld_config_sales_playbook
  - bld_config_workflow_node
  - bld_config_pricing_page
---

## Naming Convention
Pattern: `p07_te_<agent>_<task_slug>`
Examples: `p07_te_gpt4o_webArena_045`, `p07_te_claude_swebench_12`
Scope: trajectory_eval artifacts for LLM agent step-level path analysis

## Paths
Artifacts: `P07_evaluation/trajectory_eval/`
Logs: `.cex/runtime/logs/trajectory_eval/`

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
| [[bld_config_customer_segment]] | sibling | 0.51 |
| [[bld_config_agent_computer_interface]] | sibling | 0.51 |
| [[bld_config_diff_strategy]] | sibling | 0.50 |
| [[bld_config_search_strategy]] | sibling | 0.50 |
| [[bld_config_transport_config]] | sibling | 0.49 |
| [[bld_config_integration_guide]] | sibling | 0.49 |
| [[bld_config_graph_rag_config]] | sibling | 0.49 |
| [[bld_config_sales_playbook]] | sibling | 0.48 |
| [[bld_config_workflow_node]] | sibling | 0.48 |
| [[bld_config_pricing_page]] | sibling | 0.48 |
