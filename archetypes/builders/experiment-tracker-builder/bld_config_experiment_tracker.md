---
kind: config
id: bld_config_experiment_tracker
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for experiment_tracker production
quality: 8.6
title: "Config Experiment Tracker"
version: "1.0.0"
author: wave1_builder_gen
tags: [experiment_tracker, builder, config]
tldr: "Naming, paths, limits for experiment_tracker production"
domain: "experiment_tracker construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_diff_strategy
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_repo_map
  - bld_config_usage_quota
  - bld_config_product_tour
  - bld_config_ab_test_config
---

## Naming Convention
Pattern: p07_et_{{name}}.md
Examples: p07_et_baseline.md, p07_et_v1_test.md

## Paths
Artifacts: ./outputs/p07/experiments/

## Limits
max_bytes: 4096
max_turns: 15
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_diff_strategy]] | sibling | 0.66 |
| [[bld_config_pricing_page]] | sibling | 0.65 |
| [[bld_config_agent_computer_interface]] | sibling | 0.65 |
| [[bld_config_sales_playbook]] | sibling | 0.65 |
| [[bld_config_search_strategy]] | sibling | 0.64 |
| [[bld_config_transport_config]] | sibling | 0.62 |
| [[bld_config_repo_map]] | sibling | 0.62 |
| [[bld_config_usage_quota]] | sibling | 0.62 |
| [[bld_config_product_tour]] | sibling | 0.61 |
| [[bld_config_ab_test_config]] | sibling | 0.61 |
