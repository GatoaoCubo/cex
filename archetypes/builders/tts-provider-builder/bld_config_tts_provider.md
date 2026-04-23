---
kind: config
id: bld_config_tts_provider
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for tts_provider production
quality: 8.6
title: "Config Tts Provider"
version: "1.0.0"
author: wave1_builder_gen
tags: [tts_provider, builder, config]
tldr: "Naming, paths, limits for tts_provider production"
domain: "tts_provider construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_usage_quota
  - bld_config_search_strategy
  - bld_config_ab_test_config
  - bld_config_transport_config
  - bld_config_pricing_page
  - bld_config_sales_playbook
  - bld_config_repo_map
  - bld_config_diff_strategy
  - bld_config_product_tour
  - bld_config_agent_computer_interface
---

## Naming Convention  
p04_tts_{{name}}.md (e.g., p04_tts_azure.md, p04_tts_google.md)  

## Paths  
/artifacts/tts/{{name}}/  
/config/tts/{{name}}.yaml  

## Limits  
max_bytes: 4096  
max_turns: 5  
effort_level: 3  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_usage_quota]] | sibling | 0.61 |
| [[bld_config_search_strategy]] | sibling | 0.61 |
| [[bld_config_ab_test_config]] | sibling | 0.61 |
| [[bld_config_transport_config]] | sibling | 0.60 |
| [[bld_config_pricing_page]] | sibling | 0.60 |
| [[bld_config_sales_playbook]] | sibling | 0.60 |
| [[bld_config_repo_map]] | sibling | 0.59 |
| [[bld_config_diff_strategy]] | sibling | 0.59 |
| [[bld_config_product_tour]] | sibling | 0.59 |
| [[bld_config_agent_computer_interface]] | sibling | 0.58 |
