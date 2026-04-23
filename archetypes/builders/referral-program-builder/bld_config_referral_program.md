---
kind: config
id: bld_config_referral_program
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for referral_program production
quality: 8.6
title: "Config Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, config]
tldr: "Naming, paths, limits for referral_program production"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_ab_test_config
  - bld_config_usage_quota
  - bld_config_transport_config
  - bld_config_pricing_page
  - bld_config_diff_strategy
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_agent_computer_interface
  - bld_config_data_residency
  - bld_config_repo_map
---

## Naming Convention
Pattern: `p11_rp_{{name}}.yaml`
Examples: `p11_rp_referral_program.yaml`, `p11_rp_loyalty.yaml`

## Paths
`/artifacts/referral_programs/p11_rp_{{name}}.yaml`
`/src/pillars/P11/configs/referral_programs/`

## Limits
max_bytes: 4096
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
| [[bld_config_ab_test_config]] | sibling | 0.58 |
| [[bld_config_usage_quota]] | sibling | 0.57 |
| [[bld_config_transport_config]] | sibling | 0.55 |
| [[bld_config_pricing_page]] | sibling | 0.53 |
| [[bld_config_diff_strategy]] | sibling | 0.52 |
| [[bld_config_sales_playbook]] | sibling | 0.52 |
| [[bld_config_search_strategy]] | sibling | 0.52 |
| [[bld_config_agent_computer_interface]] | sibling | 0.52 |
| [[bld_config_data_residency]] | sibling | 0.51 |
| [[bld_config_repo_map]] | sibling | 0.50 |
