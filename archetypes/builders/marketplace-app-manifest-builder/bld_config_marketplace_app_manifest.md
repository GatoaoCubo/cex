---
kind: config
id: bld_config_marketplace_app_manifest
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for marketplace_app_manifest production
quality: 8.6
title: "Config Marketplace App Manifest"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [marketplace_app_manifest, builder, config]
tldr: "Production constraints for marketplace app manifest: naming (p09_mam_{{name}}.yaml), output paths (P09/), size limit 4096B. Marketplace manifest."
domain: "marketplace_app_manifest construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_ab_test_config
  - bld_config_transport_config
  - bld_config_usage_quota
  - bld_config_sales_playbook
  - bld_config_graph_rag_config
  - bld_config_search_strategy
  - bld_config_diff_strategy
  - bld_config_data_residency
  - bld_config_agent_computer_interface
  - bld_config_pricing_page
---

## Naming Convention
Pattern: `p09_mam_<app_name>.yaml`
Examples:
- `p09_mam_calendar.yaml`
- `p09_mam_notes.yaml`

## Paths
Artifacts stored in: `/mnt/cex/apps/marketplace/manifests/<app_name>/v<version>/manifest.yaml`

## Limits
max_bytes: 4096
max_turns: 20
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Marketplace manifest |
| Dependencies | agent_card, env_config |
| Primary 8F function | F5_call |
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
| Domain | marketplace app manifest construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_ab_test_config]] | sibling | 0.56 |
| [[bld_config_transport_config]] | sibling | 0.55 |
| [[bld_config_usage_quota]] | sibling | 0.53 |
| [[bld_config_sales_playbook]] | sibling | 0.51 |
| [[bld_config_graph_rag_config]] | sibling | 0.51 |
| [[bld_config_search_strategy]] | sibling | 0.51 |
| [[bld_config_diff_strategy]] | sibling | 0.50 |
| [[bld_config_data_residency]] | sibling | 0.50 |
| [[bld_config_agent_computer_interface]] | sibling | 0.50 |
| [[bld_config_pricing_page]] | sibling | 0.49 |
