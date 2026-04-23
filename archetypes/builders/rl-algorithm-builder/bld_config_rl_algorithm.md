---
kind: config
id: bld_config_rl_algorithm
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for rl_algorithm production
quality: 8.6
title: "Config Rl Algorithm"
version: "1.0.0"
author: wave1_builder_gen
tags: [rl_algorithm, builder, config]
tldr: "Naming, paths, limits for rl_algorithm production"
domain: "rl_algorithm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_workflow_node
  - bld_config_customer_segment
  - bld_config_ab_test_config
  - bld_config_reward_model
  - bld_config_eval_framework
  - bld_config_graph_rag_config
  - bld_config_playground_config
  - bld_config_search_strategy
  - bld_config_sales_playbook
  - bld_config_pricing_page
---

## Naming Convention
Pattern: `p02_rla_{{name}}.md`
Examples: `p02_rla_dqn.md`, `p02_rla_ppo.md`

## Paths
Artifacts: `/mnt/artifacts/p02/rla/{{name}}`
Logs: `/var/log/rla/{{name}}`
Checkpoints: `/mnt/models/p02/rla/{{name}}`

## Limits
max_bytes: 5120
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
| [[bld_config_workflow_node]] | sibling | 0.64 |
| [[bld_config_customer_segment]] | sibling | 0.61 |
| [[bld_config_ab_test_config]] | sibling | 0.60 |
| [[bld_config_reward_model]] | sibling | 0.58 |
| [[bld_config_eval_framework]] | sibling | 0.57 |
| [[bld_config_graph_rag_config]] | sibling | 0.57 |
| [[bld_config_playground_config]] | sibling | 0.56 |
| [[bld_config_search_strategy]] | sibling | 0.55 |
| [[bld_config_sales_playbook]] | sibling | 0.53 |
| [[bld_config_pricing_page]] | sibling | 0.53 |
