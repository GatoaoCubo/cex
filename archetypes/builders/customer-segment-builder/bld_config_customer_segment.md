---
kind: config
id: bld_config_customer_segment
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for customer_segment production
quality: 8.6
title: "Config Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, config]
tldr: "Naming, paths, limits for customer_segment production"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_rl_algorithm
  - bld_config_search_strategy
  - bld_config_workflow_node
  - bld_config_integration_guide
  - bld_config_sales_playbook
  - bld_config_pricing_page
  - bld_config_interactive_demo
  - bld_config_diff_strategy
  - bld_config_usage_quota
  - bld_config_ab_test_config
---

## Naming Convention
Pattern: `p02_cs_{{name}}`
Examples: `p02_cs_high_value`, `p02_cs_churn_risk`

## Paths
Artifacts: `/data/segments/p02/{{name}}/artifacts`
Logs: `/logs/p02/{{name}}`

## Limits
max_bytes: 4096
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
| [[bld_config_rl_algorithm]] | sibling | 0.59 |
| [[bld_config_search_strategy]] | sibling | 0.58 |
| [[bld_config_workflow_node]] | sibling | 0.58 |
| [[bld_config_integration_guide]] | sibling | 0.57 |
| [[bld_config_sales_playbook]] | sibling | 0.57 |
| [[bld_config_pricing_page]] | sibling | 0.56 |
| [[bld_config_interactive_demo]] | sibling | 0.56 |
| [[bld_config_diff_strategy]] | sibling | 0.56 |
| [[bld_config_usage_quota]] | sibling | 0.56 |
| [[bld_config_ab_test_config]] | sibling | 0.55 |
