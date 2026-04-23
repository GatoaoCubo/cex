---
kind: config
id: bld_config_data_residency
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for data_residency production
quality: 8.6
title: "Config Data Residency"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [data_residency, builder, config]
tldr: "Naming, paths, limits for data_residency production"
domain: "data_residency construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_transport_config
  - bld_config_ab_test_config
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_usage_quota
  - bld_config_sandbox_config
  - bld_config_planning_strategy
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
  - bld_config_partner_listing
---

## Naming Convention
Pattern: `p09_dr_<project_name>.yaml`
Examples: `p09_dr_customer_data.yaml`, `p09_dr_inventory.yaml`

## Paths
Artifacts stored in:
`/artifacts/pillar/P09/{{name}}/build`
`/artifacts/pillar/P09/{{name}}/output`

## Limits
max_bytes: 3072
max_turns: 50
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_transport_config]] | sibling | 0.60 |
| [[bld_config_ab_test_config]] | sibling | 0.56 |
| [[bld_config_sales_playbook]] | sibling | 0.55 |
| [[bld_config_search_strategy]] | sibling | 0.55 |
| [[bld_config_usage_quota]] | sibling | 0.54 |
| [[bld_config_sandbox_config]] | sibling | 0.54 |
| [[bld_config_planning_strategy]] | sibling | 0.53 |
| [[bld_config_diff_strategy]] | sibling | 0.53 |
| [[bld_config_agent_computer_interface]] | sibling | 0.52 |
| [[bld_config_partner_listing]] | sibling | 0.52 |
