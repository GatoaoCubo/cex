---
kind: config
id: bld_config_visual_workflow
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for visual_workflow production
quality: 8.6
title: "Config Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, config]
tldr: "Naming, paths, limits for visual_workflow production"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_prompt_technique
  - bld_config_search_strategy
  - bld_config_sales_playbook
  - bld_config_transport_config
  - bld_config_partner_listing
  - bld_config_planning_strategy
  - bld_config_pricing_page
  - bld_config_workflow_node
  - bld_config_diff_strategy
  - bld_config_healthcare_vertical
---

## Naming Convention
Pattern: `p12_vw_{{name}}.md`
Examples: `p12_vw_onboarding.md`, `p12_vw_data_processing.md`

## Paths
Artifacts stored in: `/opt/cex/p12/workflows/{{name}}.md`

## Limits
max_bytes: 5120
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
| [[bld_config_prompt_technique]] | sibling | 0.66 |
| [[bld_config_search_strategy]] | sibling | 0.66 |
| [[bld_config_sales_playbook]] | sibling | 0.64 |
| [[bld_config_transport_config]] | sibling | 0.64 |
| [[bld_config_partner_listing]] | sibling | 0.62 |
| [[bld_config_planning_strategy]] | sibling | 0.62 |
| [[bld_config_pricing_page]] | sibling | 0.61 |
| [[bld_config_workflow_node]] | sibling | 0.61 |
| [[bld_config_diff_strategy]] | sibling | 0.61 |
| [[bld_config_healthcare_vertical]] | sibling | 0.61 |
