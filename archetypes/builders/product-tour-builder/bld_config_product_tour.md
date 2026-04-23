---
kind: config
id: bld_config_product_tour
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for product_tour production
quality: 8.6
title: "Config Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, config]
tldr: "Naming, paths, limits for product_tour production"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_pricing_page
  - bld_config_search_strategy
  - bld_config_partner_listing
  - bld_config_sales_playbook
  - bld_config_diff_strategy
  - bld_config_repo_map
  - bld_config_usage_quota
  - bld_config_agent_computer_interface
  - bld_config_transport_config
  - bld_config_ab_test_config
---

## Naming Convention
Pattern: p05_pt_{{name}}.md
Examples: p05_pt_onboarding.md, p05_pt_feature_x.md

## Paths
/artifacts/p05/product_tours/{{name}}.md

## Limits
max_bytes: 5120
max_turns: 0
effort_level: 0

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_pricing_page]] | sibling | 0.67 |
| [[bld_config_search_strategy]] | sibling | 0.66 |
| [[bld_config_partner_listing]] | sibling | 0.65 |
| [[bld_config_sales_playbook]] | sibling | 0.64 |
| [[bld_config_diff_strategy]] | sibling | 0.64 |
| [[bld_config_repo_map]] | sibling | 0.64 |
| [[bld_config_usage_quota]] | sibling | 0.64 |
| [[bld_config_agent_computer_interface]] | sibling | 0.63 |
| [[bld_config_transport_config]] | sibling | 0.63 |
| [[bld_config_ab_test_config]] | sibling | 0.63 |
