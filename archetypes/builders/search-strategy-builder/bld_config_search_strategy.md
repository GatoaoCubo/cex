---
kind: config
id: bld_config_search_strategy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for search_strategy production
quality: 8.6
title: "Config Search Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [search_strategy, builder, config]
tldr: "Naming, paths, limits for search_strategy production"
domain: "search_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_sales_playbook
  - bld_config_transport_config
  - bld_config_diff_strategy
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_visual_workflow
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
  - bld_config_prompt_technique
  - bld_config_mcp_app_extension
---

## Naming Convention
Pattern: `p04_ss_{{name}}.md`
Examples: `p04_ss_basic.md`, `p04_ss_advanced.md`

## Paths
Artifacts stored in: `/artifacts/p04/search_strategies/{{name}}`

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
| [[bld_config_sales_playbook]] | sibling | 0.66 |
| [[bld_config_transport_config]] | sibling | 0.66 |
| [[bld_config_diff_strategy]] | sibling | 0.65 |
| [[bld_config_planning_strategy]] | sibling | 0.65 |
| [[bld_config_partner_listing]] | sibling | 0.64 |
| [[bld_config_visual_workflow]] | sibling | 0.63 |
| [[bld_config_pricing_page]] | sibling | 0.62 |
| [[bld_config_agent_computer_interface]] | sibling | 0.62 |
| [[bld_config_prompt_technique]] | sibling | 0.62 |
| [[bld_config_mcp_app_extension]] | sibling | 0.62 |
