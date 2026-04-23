---
kind: config
id: bld_config_safety_hazard_taxonomy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for safety_hazard_taxonomy production
quality: 8.6
title: "Config Safety Hazard Taxonomy"
version: "1.0.0"
author: n01_wave7
tags: [safety_hazard_taxonomy, builder, config, MLCommons, AILuminate]
tldr: "Naming, paths, limits for safety_hazard_taxonomy production"
domain: "safety_hazard_taxonomy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_gpai_technical_doc
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_sales_playbook
  - bld_config_ai_rmf_profile
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_diff_strategy
  - bld_config_visual_workflow
  - bld_config_agent_computer_interface
---

## Naming Convention
Pattern: `p11_sht_{{scope}}.md`
Examples: `p11_sht_ailuminate_v1_full.md`, `p11_sht_consumer_api_restricted.md`

## Paths
Artifacts stored in: `P11_governance/safety_hazard_taxonomies/`

## Limits
max_bytes: 5120
max_turns: 6
effort_level: 4

## Hooks
pre_build: validate_category_count
post_build: compile + signal_n07
on_error: null
on_quality_fail: retry_with_missing_categories

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_gpai_technical_doc]] | sibling | 0.68 |
| [[bld_config_search_strategy]] | sibling | 0.66 |
| [[bld_config_transport_config]] | sibling | 0.66 |
| [[bld_config_sales_playbook]] | sibling | 0.64 |
| [[bld_config_ai_rmf_profile]] | sibling | 0.63 |
| [[bld_config_planning_strategy]] | sibling | 0.62 |
| [[bld_config_partner_listing]] | sibling | 0.62 |
| [[bld_config_diff_strategy]] | sibling | 0.62 |
| [[bld_config_visual_workflow]] | sibling | 0.61 |
| [[bld_config_agent_computer_interface]] | sibling | 0.61 |
