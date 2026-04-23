---
kind: config
id: bld_config_planning_strategy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for planning_strategy production
quality: 8.6
title: "Config Planning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [planning_strategy, builder, config]
tldr: "Naming, paths, limits for planning_strategy production"
domain: "planning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_prompt_technique
  - bld_config_partner_listing
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
  - bld_config_reasoning_strategy
  - bld_config_repo_map
  - bld_config_ab_test_config
---

## Naming Convention
Pattern: `p03_ps_{{name}}.md`
Examples: `p03_ps_strategy.md`, `p03_ps_example_plan.md`

## Paths
Artifacts stored in: `/artifacts/p03/ps/{{name}}/`
Root: `/artifacts/p03/ps/`

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
| [[bld_config_sales_playbook]] | sibling | 0.66 |
| [[bld_config_search_strategy]] | sibling | 0.63 |
| [[bld_config_transport_config]] | sibling | 0.61 |
| [[bld_config_prompt_technique]] | sibling | 0.61 |
| [[bld_config_partner_listing]] | sibling | 0.60 |
| [[bld_config_diff_strategy]] | sibling | 0.59 |
| [[bld_config_agent_computer_interface]] | sibling | 0.58 |
| [[bld_config_reasoning_strategy]] | sibling | 0.58 |
| [[bld_config_repo_map]] | sibling | 0.58 |
| [[bld_config_ab_test_config]] | sibling | 0.58 |
