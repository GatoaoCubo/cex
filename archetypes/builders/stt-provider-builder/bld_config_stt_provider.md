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
tldr: "Production constraints for stt provider: naming (p04_stt_{{name}}.md), output paths (P04/), size limit 4096B. STT provider integration."
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

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | STT provider integration |
| Dependencies | api_client |
| Primary 8F function | F6_produce |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency api_client not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | stt provider construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

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
