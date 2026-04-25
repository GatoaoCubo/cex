---
kind: config
id: bld_config_integration_guide
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for integration_guide production
quality: 8.6
title: "Config Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, config]
tldr: "Production constraints for integration guide: naming (p05_ig_{{name}}.md), output paths (P05/), size limit 8192B. Integration guide."
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_pricing_page
  - bld_config_partner_listing
  - bld_config_transport_config
  - bld_config_diff_strategy
  - bld_config_planning_strategy
  - bld_config_agent_computer_interface
  - bld_config_product_tour
  - bld_config_customer_segment
---

p05_ig_integration_guide.md
## Naming Convention
Pattern: `p05_ig_<name>.md`
Examples: `p05_ig_integration_guide.md`, `p05_ig_api_v2.md`

## Paths
Artifacts stored in: `/artifacts/p05/ig/{{name}}/`
Subdirectories: `docs/`, `logs/`, `metadata/`

## Limits
max_bytes: 8192
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
| Boundary | Integration guide |
| Dependencies | api_reference, knowledge_card |
| Primary 8F function | F6_produce |
| Max artifact size | 8192 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 8192 bytes | Trim prose sections; preserve tables |
| Dependency api_reference not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | integration guide construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_sales_playbook]] | sibling | 0.65 |
| [[bld_config_search_strategy]] | sibling | 0.64 |
| [[bld_config_pricing_page]] | sibling | 0.63 |
| [[bld_config_partner_listing]] | sibling | 0.63 |
| [[bld_config_transport_config]] | sibling | 0.62 |
| [[bld_config_diff_strategy]] | sibling | 0.62 |
| [[bld_config_planning_strategy]] | sibling | 0.61 |
| [[bld_config_agent_computer_interface]] | sibling | 0.61 |
| [[bld_config_product_tour]] | sibling | 0.60 |
| [[bld_config_customer_segment]] | sibling | 0.60 |
