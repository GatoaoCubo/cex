---
kind: config
id: bld_config_diff_strategy
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for diff_strategy production
quality: 8.6
title: "Config Diff Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [diff_strategy, builder, config]
tldr: "Production constraints for diff strategy: naming (p04_ds_{{name}}.md), output paths (P04/), size limit 4096B. Diff matching strategy."
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_agent_computer_interface
  - bld_config_sales_playbook
  - bld_config_pricing_page
  - bld_config_transport_config
  - bld_config_usage_quota
  - bld_config_ab_test_config
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_product_tour
---

## Naming Convention
Pattern: p04_ds_{{name}}.md
Examples:
- p04_ds_auth_refactor.md
- p04_ds_api_patch.md

## Paths
Artifacts: ./artifacts/p04/

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
| Boundary | Diff matching strategy |
| Dependencies | function_def |
| Primary 8F function | F6_produce |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency function_def not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | diff strategy construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.68 |
| [[bld_config_agent_computer_interface]] | sibling | 0.66 |
| [[bld_config_sales_playbook]] | sibling | 0.66 |
| [[bld_config_pricing_page]] | sibling | 0.65 |
| [[bld_config_transport_config]] | sibling | 0.64 |
| [[bld_config_usage_quota]] | sibling | 0.62 |
| [[bld_config_ab_test_config]] | sibling | 0.62 |
| [[bld_config_planning_strategy]] | sibling | 0.62 |
| [[bld_config_partner_listing]] | sibling | 0.61 |
| [[bld_config_product_tour]] | sibling | 0.61 |
