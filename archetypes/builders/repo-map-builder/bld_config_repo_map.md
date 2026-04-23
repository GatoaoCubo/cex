---
kind: config
id: bld_config_repo_map
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for repo_map production
quality: 8.6
title: "Config Repo Map"
version: "1.0.0"
author: wave1_builder_gen
tags: [repo_map, builder, config]
tldr: "Naming, paths, limits for repo_map production"
domain: "repo_map construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_pricing_page
  - bld_config_usage_quota
  - bld_config_sales_playbook
  - bld_config_product_tour
  - bld_config_diff_strategy
  - bld_config_planning_strategy
  - bld_config_ab_test_config
  - bld_config_agent_computer_interface
  - bld_config_transport_config
---

## Naming Convention  
Pattern: `p01_rm_{{name}}.md`  
Examples:  
- `p01_rm_projectA.md`  
- `p01_rm_dataScience.md`  

## Paths  
- Root: `/repo_maps/`  
- Per Pillar: `/repo_maps/P01/{{name}}/`  

## Limits  
- max_bytes: 5120  
- max_turns: 10  
- effort_level: 3  

## Hooks  
- pre_build: null  
- post_build: null  
- on_error: null  
- on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.62 |
| [[bld_config_pricing_page]] | sibling | 0.62 |
| [[bld_config_usage_quota]] | sibling | 0.61 |
| [[bld_config_sales_playbook]] | sibling | 0.61 |
| [[bld_config_product_tour]] | sibling | 0.61 |
| [[bld_config_diff_strategy]] | sibling | 0.60 |
| [[bld_config_planning_strategy]] | sibling | 0.60 |
| [[bld_config_ab_test_config]] | sibling | 0.60 |
| [[bld_config_agent_computer_interface]] | sibling | 0.60 |
| [[bld_config_transport_config]] | sibling | 0.60 |
