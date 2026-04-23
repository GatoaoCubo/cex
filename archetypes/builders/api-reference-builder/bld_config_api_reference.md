---
kind: config
id: bld_config_api_reference
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for api_reference production
quality: 8.6
title: "Config Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, config]
tldr: "Naming, paths, limits for api_reference production"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_pricing_page
  - bld_config_sales_playbook
  - bld_config_diff_strategy
  - bld_config_repo_map
  - bld_config_usage_quota
  - bld_config_agent_computer_interface
  - bld_config_transport_config
  - bld_config_product_tour
  - bld_config_ab_test_config
---

## Naming Convention
Pattern: `p06_ar_<name>.md` (e.g., `p06_ar_userapi.md`, `p06_ar_payment.md`)

## Paths
`/artifacts/api_refs/p06/<name>.md`

## Limits
max_bytes: 8192 | max_turns: 20 | effort level: 3

## Hooks
pre_build: null | post_build: null | on_error: null | on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.61 |
| [[bld_config_pricing_page]] | sibling | 0.60 |
| [[bld_config_sales_playbook]] | sibling | 0.60 |
| [[bld_config_diff_strategy]] | sibling | 0.60 |
| [[bld_config_repo_map]] | sibling | 0.60 |
| [[bld_config_usage_quota]] | sibling | 0.60 |
| [[bld_config_agent_computer_interface]] | sibling | 0.59 |
| [[bld_config_transport_config]] | sibling | 0.59 |
| [[bld_config_product_tour]] | sibling | 0.59 |
| [[bld_config_ab_test_config]] | sibling | 0.59 |
