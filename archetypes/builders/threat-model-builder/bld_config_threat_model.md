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
tldr: "Production constraints for threat model: naming (p11_tm_{{name}}.md), output paths (P11/), size limit 5120B. Threat/risk assessment."
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

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Threat/risk assessment |
| Dependencies | safety_policy, knowledge_card |
| Primary 8F function | F4_reason |
| Max artifact size | 5120 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 5120 bytes | Trim prose sections; preserve tables |
| Dependency safety_policy not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | threat model construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

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
