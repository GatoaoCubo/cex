---
kind: config
id: bld_config_usage_quota
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for usage_quota production
quality: 8.6
title: "Config Usage Quota"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_quota, builder, config]
tldr: "Naming, paths, limits for usage_quota production"
domain: "usage_quota construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_ab_test_config
  - bld_config_transport_config
  - bld_config_search_strategy
  - bld_config_pricing_page
  - bld_config_sales_playbook
  - bld_config_diff_strategy
  - bld_config_repo_map
  - bld_config_vad_config
  - bld_config_agent_computer_interface
  - bld_config_product_tour
---

## Naming Convention
Pattern: p09_uq_{{name}}.yaml
Examples:
- p09_uq_example.yaml
- p09_uq_another.yaml

## Paths
/artifacts/usage_quotas/{{name}}.yaml

## Limits
max_bytes: 3072
max_turns: 0
effort_level: high

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_ab_test_config]] | sibling | 0.59 |
| [[bld_config_transport_config]] | sibling | 0.58 |
| [[bld_config_search_strategy]] | sibling | 0.55 |
| [[bld_config_pricing_page]] | sibling | 0.54 |
| [[bld_config_sales_playbook]] | sibling | 0.54 |
| [[bld_config_diff_strategy]] | sibling | 0.54 |
| [[bld_config_repo_map]] | sibling | 0.54 |
| [[bld_config_vad_config]] | sibling | 0.53 |
| [[bld_config_agent_computer_interface]] | sibling | 0.53 |
| [[bld_config_product_tour]] | sibling | 0.53 |
