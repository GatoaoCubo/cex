---
kind: config
id: bld_config_subscription_tier
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for subscription_tier production
quality: 8.6
title: "Config Subscription Tier"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [subscription_tier, builder, config]
tldr: "Naming, paths, limits for subscription_tier production"
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_usage_quota
  - bld_config_ab_test_config
  - bld_config_customer_segment
  - bld_config_transport_config
  - bld_config_roi_calculator
  - bld_config_search_strategy
  - bld_config_workflow_node
  - bld_config_data_residency
  - bld_config_integration_guide
  - bld_config_sales_playbook
---

## Naming Convention
Pattern: `p11_st_{{name}}.yaml`
Examples: `p11_st_bronze.yaml`, `p11_st_premium.yaml`

## Paths
Artifacts: `/artifacts/subscription_tiers/p11_st_{{name}}.yaml`
Logs: `/logs/build/p11_st_{{name}}`

## Limits
max_bytes: 3072
max_turns: 150
effort_level: high

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_usage_quota]] | sibling | 0.54 |
| [[bld_config_ab_test_config]] | sibling | 0.53 |
| [[bld_config_customer_segment]] | sibling | 0.53 |
| [[bld_config_transport_config]] | sibling | 0.51 |
| [[bld_config_roi_calculator]] | sibling | 0.50 |
| [[bld_config_search_strategy]] | sibling | 0.50 |
| [[bld_config_workflow_node]] | sibling | 0.50 |
| [[bld_config_data_residency]] | sibling | 0.49 |
| [[bld_config_integration_guide]] | sibling | 0.49 |
| [[bld_config_sales_playbook]] | sibling | 0.48 |
