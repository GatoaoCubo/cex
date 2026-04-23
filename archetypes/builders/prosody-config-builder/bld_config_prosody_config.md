---
kind: config
id: bld_config_prosody_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for prosody_config production
quality: 8.6
title: "Config Prosody Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [prosody_config, builder, config]
tldr: "Naming, paths, limits for prosody_config production"
domain: "prosody_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_transport_config
  - bld_config_data_residency
  - bld_config_sso_config
  - bld_config_usage_quota
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_visual_workflow
  - bld_config_ab_test_config
  - bld_config_prompt_technique
  - bld_config_diff_strategy
---

## Naming Convention  
Pattern: `p09_prs_<name>.yaml`  
Examples: `p09_prs_user1.yaml`, `p09_prs_serviceA.yaml`  

## Paths  
Artifacts stored in: `/opt/prosody/configs/p09/`  

## Limits  
max_bytes: 2048  
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
| [[bld_config_transport_config]] | sibling | 0.64 |
| [[bld_config_data_residency]] | sibling | 0.61 |
| [[bld_config_sso_config]] | sibling | 0.60 |
| [[bld_config_usage_quota]] | sibling | 0.60 |
| [[bld_config_sales_playbook]] | sibling | 0.60 |
| [[bld_config_search_strategy]] | sibling | 0.59 |
| [[bld_config_visual_workflow]] | sibling | 0.59 |
| [[bld_config_ab_test_config]] | sibling | 0.59 |
| [[bld_config_prompt_technique]] | sibling | 0.59 |
| [[bld_config_diff_strategy]] | sibling | 0.58 |
