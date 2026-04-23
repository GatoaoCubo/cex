---
kind: config
id: bld_config_sales_playbook
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for sales_playbook production
quality: 8.6
title: "Config Sales Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sales_playbook, builder, config]
tldr: "Naming, paths, limits for sales_playbook production"
domain: "sales_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_planning_strategy
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_diff_strategy
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
  - bld_config_prompt_technique
  - bld_config_partner_listing
  - bld_config_integration_guide
  - bld_config_visual_workflow
---

## Naming Convention
Pattern: `p03_sp_{{name}}.md`
Examples: `p03_sp_onboarding.md`, `p03_sp_retention.md`

## Paths
Artifacts stored in: `/artifacts/sales_playbooks/p03/{{name}}.md`

## Limits
max_bytes: 8192
max_turns: 5
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_planning_strategy]] | sibling | 0.68 |
| [[bld_config_search_strategy]] | sibling | 0.67 |
| [[bld_config_transport_config]] | sibling | 0.65 |
| [[bld_config_diff_strategy]] | sibling | 0.64 |
| [[bld_config_pricing_page]] | sibling | 0.64 |
| [[bld_config_agent_computer_interface]] | sibling | 0.64 |
| [[bld_config_prompt_technique]] | sibling | 0.64 |
| [[bld_config_partner_listing]] | sibling | 0.63 |
| [[bld_config_integration_guide]] | sibling | 0.63 |
| [[bld_config_visual_workflow]] | sibling | 0.62 |
