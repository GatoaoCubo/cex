---
kind: config
id: bld_config_content_filter
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for content_filter production
quality: 8.6
title: "Config Content Filter"
version: "1.0.0"
author: wave1_builder_gen
tags: [content_filter, builder, config]
tldr: "Naming, paths, limits for content_filter production"
domain: "content_filter construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_safety_policy
  - bld_config_compliance_framework
  - bld_config_sales_playbook
  - bld_config_ab_test_config
  - bld_config_transport_config
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
---

## Naming Convention

This ISO defines a content filter -- the moderation rules that gate output or input.
Pattern: `p11_cf_{{name}}.md`
Examples:
- `p11_cf_report.md`
- `p11_cf_summary.md`

## Paths
Artifacts stored in: `/artifacts/p11/{{name}}/`
Example: `/artifacts/p11/report/`

## Limits
max_bytes: 4096
max_turns: 5
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.58 |
| [[bld_config_safety_policy]] | sibling | 0.58 |
| [[bld_config_compliance_framework]] | sibling | 0.57 |
| [[bld_config_sales_playbook]] | sibling | 0.56 |
| [[bld_config_ab_test_config]] | sibling | 0.56 |
| [[bld_config_transport_config]] | sibling | 0.56 |
| [[bld_config_planning_strategy]] | sibling | 0.56 |
| [[bld_config_partner_listing]] | sibling | 0.55 |
| [[bld_config_diff_strategy]] | sibling | 0.54 |
| [[bld_config_agent_computer_interface]] | sibling | 0.53 |
