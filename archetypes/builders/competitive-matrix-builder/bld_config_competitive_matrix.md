---
kind: config
id: bld_config_competitive_matrix
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for competitive_matrix production
quality: 8.6
title: "Config Competitive Matrix"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [competitive_matrix, builder, config]
tldr: "Naming, paths, limits for competitive_matrix production"
domain: "competitive_matrix construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_usage_quota
  - bld_config_repo_map
  - bld_config_sales_playbook
  - bld_config_diff_strategy
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
  - bld_config_transport_config
  - bld_config_ab_test_config
  - bld_config_planning_strategy
---

## Naming Convention (competitive matrix artifacts)
Pattern: p01_cm_{{name}}.md (e.g., p01_cm_market_analysis.md) for competitive matrix outputs

## Paths
/artifacts/p01/cm/{{name}}.md

## Limits
max_bytes: 5120
max_turns: 3
effort_level: high

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.59 |
| [[bld_config_usage_quota]] | sibling | 0.57 |
| [[bld_config_repo_map]] | sibling | 0.57 |
| [[bld_config_sales_playbook]] | sibling | 0.57 |
| [[bld_config_diff_strategy]] | sibling | 0.57 |
| [[bld_config_pricing_page]] | sibling | 0.56 |
| [[bld_config_agent_computer_interface]] | sibling | 0.56 |
| [[bld_config_transport_config]] | sibling | 0.56 |
| [[bld_config_ab_test_config]] | sibling | 0.56 |
| [[bld_config_planning_strategy]] | sibling | 0.56 |
