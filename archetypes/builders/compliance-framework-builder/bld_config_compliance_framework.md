---
kind: config
id: bld_config_compliance_framework
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for compliance_framework production
quality: 8.6
title: "Config Compliance Framework"
version: "1.0.0"
author: wave1_builder_gen
tags: [compliance_framework, builder, config]
tldr: "Naming, paths, limits for compliance_framework production"
domain: "compliance_framework construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_safety_policy
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_content_filter
  - bld_config_planning_strategy
  - bld_config_ab_test_config
  - bld_config_transport_config
  - bld_config_diff_strategy
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
---

## Naming Convention
Pattern: `p11_cfw_<name>_<version>.md` (e.g., `p11_cfw_compliance_policy_v1.md`, `p11_cfw_data_protection_v2.md`)

## Paths
Artifacts stored in: `/artifacts/p11/cfw/{{name}}/`
Root reference: `/compliance_frameworks/p11/`

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
| [[bld_config_safety_policy]] | sibling | 0.63 |
| [[bld_config_sales_playbook]] | sibling | 0.63 |
| [[bld_config_search_strategy]] | sibling | 0.62 |
| [[bld_config_content_filter]] | sibling | 0.62 |
| [[bld_config_planning_strategy]] | sibling | 0.62 |
| [[bld_config_ab_test_config]] | sibling | 0.60 |
| [[bld_config_transport_config]] | sibling | 0.60 |
| [[bld_config_diff_strategy]] | sibling | 0.60 |
| [[bld_config_pricing_page]] | sibling | 0.59 |
| [[bld_config_agent_computer_interface]] | sibling | 0.59 |
