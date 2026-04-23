---
kind: config
id: bld_config_compliance_checklist
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for compliance_checklist production
quality: 8.6
title: "Config Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, config]
tldr: "Naming, paths, limits for compliance_checklist production"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_pricing_page
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
  - bld_config_repo_map
  - bld_config_usage_quota
  - bld_config_product_tour
  - bld_config_ab_test_config
  - bld_config_transport_config
---

## Naming Convention
Pattern: `p11_cc_{{name}}.md`
Examples:
- `p11_cc_example.md`
- `p11_cc_compliance.md`

## Paths
- `/artifacts/compliance_checklists/p11_cc_{{name}}.md`
- `/reports/p11_cc_{{name}}_report.json`

## Limits
- max_bytes: 6144
- max_turns: 10
- effort_level: medium

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_pricing_page]] | sibling | 0.58 |
| [[bld_config_sales_playbook]] | sibling | 0.58 |
| [[bld_config_search_strategy]] | sibling | 0.57 |
| [[bld_config_diff_strategy]] | sibling | 0.57 |
| [[bld_config_agent_computer_interface]] | sibling | 0.56 |
| [[bld_config_repo_map]] | sibling | 0.56 |
| [[bld_config_usage_quota]] | sibling | 0.56 |
| [[bld_config_product_tour]] | sibling | 0.55 |
| [[bld_config_ab_test_config]] | sibling | 0.55 |
| [[bld_config_transport_config]] | sibling | 0.54 |
