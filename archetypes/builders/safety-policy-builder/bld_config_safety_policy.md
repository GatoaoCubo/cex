---
kind: config
id: bld_config_safety_policy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for safety_policy production
quality: 8.6
title: "Config Safety Policy"
version: "1.0.0"
author: wave1_builder_gen
tags: [safety_policy, builder, config]
tldr: "Naming, paths, limits for safety_policy production"
domain: "safety_policy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_sales_playbook
  - bld_config_compliance_framework
  - bld_config_search_strategy
  - bld_config_content_filter
  - bld_config_ab_test_config
  - bld_config_transport_config
  - bld_config_planning_strategy
  - bld_config_diff_strategy
  - bld_config_partner_listing
  - bld_config_pricing_page
---

## Naming Convention
Pattern: `p11_sp_{{name}}.md`
Examples: `p11_sp_data.md`, `p11_sp_network.md`

## Paths
Artifacts stored in: `/artifacts/p11/sp/{{name}}/`
Config file path: `/artifacts/p11/sp/{{name}}/safety_policy.md`

## Limits
max_bytes: 5120
max_turns: 10
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_sales_playbook]] | sibling | 0.61 |
| [[bld_config_compliance_framework]] | sibling | 0.61 |
| [[bld_config_search_strategy]] | sibling | 0.61 |
| [[bld_config_content_filter]] | sibling | 0.61 |
| [[bld_config_ab_test_config]] | sibling | 0.60 |
| [[bld_config_transport_config]] | sibling | 0.59 |
| [[bld_config_planning_strategy]] | sibling | 0.58 |
| [[bld_config_diff_strategy]] | sibling | 0.58 |
| [[bld_config_partner_listing]] | sibling | 0.57 |
| [[bld_config_pricing_page]] | sibling | 0.57 |
