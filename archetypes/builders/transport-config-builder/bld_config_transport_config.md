---
kind: config
id: bld_config_transport_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for transport_config production
quality: 8.6
title: "Config Transport Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [transport_config, builder, config]
tldr: "Naming, paths, limits for transport_config production"
domain: "transport_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_data_residency
  - bld_config_search_strategy
  - bld_config_usage_quota
  - bld_config_ab_test_config
  - bld_config_sales_playbook
  - bld_config_sandbox_config
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
---

## Naming Convention  
Pattern: `p09_tc_<name>.yaml`  
Examples:  
- `p09_tc_ship.yaml`  
- `p09_tc_drone.yaml`  

## Paths  
Artifacts stored in: `/artifacts/p09/transport_configs/`  

## Limits  
- `max_bytes`: 2048  
- `max_turns`: 10  
- `effort_level`: 3  

## Hooks  
- `pre_build`: null  
- `post_build`: null  
- `on_error`: null  
- `on_quality_fail`: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_data_residency]] | sibling | 0.62 |
| [[bld_config_search_strategy]] | sibling | 0.62 |
| [[bld_config_usage_quota]] | sibling | 0.61 |
| [[bld_config_ab_test_config]] | sibling | 0.61 |
| [[bld_config_sales_playbook]] | sibling | 0.60 |
| [[bld_config_sandbox_config]] | sibling | 0.59 |
| [[bld_config_planning_strategy]] | sibling | 0.59 |
| [[bld_config_partner_listing]] | sibling | 0.58 |
| [[bld_config_diff_strategy]] | sibling | 0.58 |
| [[bld_config_agent_computer_interface]] | sibling | 0.57 |
