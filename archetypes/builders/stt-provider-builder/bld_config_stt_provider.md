---
kind: config
id: bld_config_stt_provider
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for stt_provider production
quality: 8.6
title: "Config Stt Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [stt_provider, builder, config]
tldr: "Naming, paths, limits for stt_provider production"
domain: "stt_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_integration_guide
  - bld_config_search_strategy
  - bld_config_diff_strategy
  - bld_config_sales_playbook
  - bld_config_pricing_page
  - bld_config_customer_segment
  - bld_config_agent_computer_interface
  - bld_config_workflow_node
  - bld_config_usage_quota
  - bld_config_ab_test_config
---

## Naming Convention  
Pattern: `p04_stt_{{name}}.md`  
Examples: `p04_stt_azure.md`, `p04_stt_google.md`  
{{name}}: lowercase, alphanumeric, hyphens allowed  

## Paths  
Artifacts: `/artifacts/p04/stt/{{name}}/`  
Subdirectories: `models/`, `logs/`, `tests/`  

## Limits  
max_bytes: 4096  
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
| [[bld_config_integration_guide]] | sibling | 0.60 |
| [[bld_config_search_strategy]] | sibling | 0.59 |
| [[bld_config_diff_strategy]] | sibling | 0.59 |
| [[bld_config_sales_playbook]] | sibling | 0.58 |
| [[bld_config_pricing_page]] | sibling | 0.57 |
| [[bld_config_customer_segment]] | sibling | 0.57 |
| [[bld_config_agent_computer_interface]] | sibling | 0.57 |
| [[bld_config_workflow_node]] | sibling | 0.55 |
| [[bld_config_usage_quota]] | sibling | 0.55 |
| [[bld_config_ab_test_config]] | sibling | 0.55 |
