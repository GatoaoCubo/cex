---
kind: config
id: bld_config_enterprise_sla
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for enterprise_sla production
quality: 8.6
title: "Config Enterprise Sla"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [enterprise_sla, builder, config]
tldr: "Naming, paths, limits for enterprise_sla production"
domain: "enterprise_sla construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_api_reference
  - bld_config_pricing_page
  - bld_config_sales_playbook
  - bld_config_diff_strategy
  - bld_config_search_strategy
  - bld_config_agent_computer_interface
  - bld_config_ab_test_config
  - bld_config_repo_map
  - bld_config_usage_quota
  - bld_config_safety_policy
---

## Naming Convention
Pattern: `p11_sla_{{name}}.md`
Examples: `p11_sla_annual_review.md`, `p11_sla_q4_2023.md`

## Paths
/artifacts/enterprise/sla/P11/{{name}}

## Limits
max_bytes: 6144
max_turns: 5
effort level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_api_reference]] | sibling | 0.64 |
| [[bld_config_pricing_page]] | sibling | 0.60 |
| [[bld_config_sales_playbook]] | sibling | 0.60 |
| [[bld_config_diff_strategy]] | sibling | 0.60 |
| [[bld_config_search_strategy]] | sibling | 0.59 |
| [[bld_config_agent_computer_interface]] | sibling | 0.59 |
| [[bld_config_ab_test_config]] | sibling | 0.59 |
| [[bld_config_repo_map]] | sibling | 0.57 |
| [[bld_config_usage_quota]] | sibling | 0.57 |
| [[bld_config_safety_policy]] | sibling | 0.57 |
