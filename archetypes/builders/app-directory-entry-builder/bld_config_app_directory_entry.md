---
kind: config
id: bld_config_app_directory_entry
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for app_directory_entry production
quality: 8.7
title: "Config App Directory Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [app_directory_entry, builder, config]
tldr: "Production constraints for app directory entry: naming (p05_ade_{{name}}.md), output paths (P05/), size limit 4096B. App directory entry."
domain: "app_directory_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_mcp_app_extension
  - bld_config_sales_playbook
  - bld_config_partner_listing
  - bld_config_search_strategy
  - bld_config_integration_guide
  - bld_config_transport_config
  - bld_config_planning_strategy
  - bld_config_pricing_page
  - bld_config_safety_policy
  - bld_config_data_residency
---

## Naming Convention  
Pattern: `p05_ade_{{name}}.md`  
Examples: `p05_ade_user_profile.md`, `p05_ade_transaction_log.md`  

## Paths  
Artifacts stored in: `/artifacts/p05/ade/{{name}}.md`  
Example: `/artifacts/p05/ade/user_profile.md`  

## Limits  
max_bytes: 4096  
max_turns: 5  
effort_level: medium  

## Hooks  
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain Scope
This config applies to app directory entry artifacts. Each app directory entry artifact is stored under the app directory path with the ade prefix, scoping all entry files to the app directory namespace.

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | App directory entry |
| Dependencies | agent_card, knowledge_card |
| Primary 8F function | F8_collaborate |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency agent_card not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | app directory entry construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_mcp_app_extension]] | sibling | 0.46 |
| [[bld_config_sales_playbook]] | sibling | 0.46 |
| [[bld_config_partner_listing]] | sibling | 0.46 |
| [[bld_config_search_strategy]] | sibling | 0.45 |
| [[bld_config_integration_guide]] | sibling | 0.45 |
| [[bld_config_transport_config]] | sibling | 0.45 |
| [[bld_config_planning_strategy]] | sibling | 0.44 |
| [[bld_config_pricing_page]] | sibling | 0.43 |
| [[bld_config_safety_policy]] | sibling | 0.43 |
| [[bld_config_data_residency]] | sibling | 0.42 |
