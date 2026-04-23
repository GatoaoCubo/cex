---
kind: config
id: bld_config_agent_profile
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for agent_profile production
quality: 8.6
title: "Config Agent Profile"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_profile, builder, config]
tldr: "Naming, paths, limits for agent_profile production"
domain: "agent_profile construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_sales_playbook
  - bld_config_customer_segment
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
  - bld_config_healthcare_vertical
  - bld_config_visual_workflow
---

## Naming Convention
Pattern: `p02_ap_{{name}}.md`
Examples: `p02_ap_john.md`, `p02_ap_sarah.md`

## Paths
Artifacts stored in: `/artifacts/p02/profiles/`
Example path: `/artifacts/p02/profiles/john.md`

## Limits
max_bytes: 4096
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.60 |
| [[bld_config_transport_config]] | sibling | 0.59 |
| [[bld_config_sales_playbook]] | sibling | 0.58 |
| [[bld_config_customer_segment]] | sibling | 0.58 |
| [[bld_config_planning_strategy]] | sibling | 0.58 |
| [[bld_config_partner_listing]] | sibling | 0.56 |
| [[bld_config_diff_strategy]] | sibling | 0.56 |
| [[bld_config_agent_computer_interface]] | sibling | 0.56 |
| [[bld_config_healthcare_vertical]] | sibling | 0.54 |
| [[bld_config_visual_workflow]] | sibling | 0.54 |
