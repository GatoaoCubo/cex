---
kind: config
id: bld_config_sandbox_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for sandbox_config production
quality: 8.6
title: "Config Sandbox Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [sandbox_config, builder, config]
tldr: "Production constraints for sandbox config: naming (p09_sb_{{name}}.yaml), output paths (P09/), size limit 2048B. Sandbox/isolation config."
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_transport_config
  - bld_config_search_strategy
  - bld_config_data_residency
  - bld_config_usage_quota
  - bld_config_ab_test_config
  - bld_config_sales_playbook
  - bld_config_planning_strategy
  - bld_config_sandbox_spec
  - bld_config_partner_listing
  - bld_config_diff_strategy
---

## Naming Convention  
Pattern: `p09_sb_{{name}}.yaml`  
Examples: `p09_sb_example.yaml`, `p09_sb_test.yaml`  

## Paths  
Artifacts stored in: `/sandboxes/p09/{{name}}/artifacts`  

## Limits  
max_bytes: 2048  
max_turns: 10  
effort_level: 3  

## Hooks  
pre_build: null  
post_build: null  
on_error: null  
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Sandbox/isolation config |
| Dependencies | audit_log |
| Primary 8F function | F1_constrain |
| Max artifact size | 2048 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 2048 bytes | Trim prose sections; preserve tables |
| Dependency audit_log not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | sandbox config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_transport_config]] | sibling | 0.64 |
| [[bld_config_search_strategy]] | sibling | 0.60 |
| [[bld_config_data_residency]] | sibling | 0.60 |
| [[bld_config_usage_quota]] | sibling | 0.60 |
| [[bld_config_ab_test_config]] | sibling | 0.60 |
| [[bld_config_sales_playbook]] | sibling | 0.59 |
| [[bld_config_planning_strategy]] | sibling | 0.57 |
| [[bld_config_sandbox_spec]] | sibling | 0.57 |
| [[bld_config_partner_listing]] | sibling | 0.57 |
| [[bld_config_diff_strategy]] | sibling | 0.56 |
