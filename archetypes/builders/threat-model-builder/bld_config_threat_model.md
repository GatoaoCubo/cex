---
kind: config
id: bld_config_threat_model
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for threat_model production
quality: 8.6
title: "Config Threat Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [threat_model, builder, config]
tldr: "Naming, paths, limits for threat_model production"
domain: "threat_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_diff_strategy
  - bld_config_safety_policy
  - bld_config_content_filter
  - bld_config_compliance_framework
  - bld_config_pricing_page
  - bld_config_planning_strategy
  - bld_config_agent_computer_interface
---

## Naming Convention  

This ISO records a threat model: the assets worth protecting and the attacker profiles that target them.
Pattern: `p11_tm_{{name}}.md`  
Examples: `p11_tm_webapp.md`, `p11_tm_api.md`  

## Paths  
Artifacts stored in: `/artifacts/p11/{{name}}/`  

## Limits  
max_bytes: 5120  
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
| [[bld_config_sales_playbook]] | sibling | 0.60 |
| [[bld_config_search_strategy]] | sibling | 0.60 |
| [[bld_config_transport_config]] | sibling | 0.58 |
| [[bld_config_diff_strategy]] | sibling | 0.57 |
| [[bld_config_safety_policy]] | sibling | 0.57 |
| [[bld_config_content_filter]] | sibling | 0.57 |
| [[bld_config_compliance_framework]] | sibling | 0.57 |
| [[bld_config_pricing_page]] | sibling | 0.57 |
| [[bld_config_planning_strategy]] | sibling | 0.57 |
| [[bld_config_agent_computer_interface]] | sibling | 0.57 |
