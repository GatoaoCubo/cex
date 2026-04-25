---
kind: config
id: bld_config_partner_listing
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for partner_listing production
quality: 8.6
title: "Config Partner Listing"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [partner_listing, builder, config]
tldr: "Production constraints for partner listing: naming (p05_pl_{{name}}.md), output paths (P05/), size limit 4096B. Partner listing."
domain: "partner_listing construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_sales_playbook
  - bld_config_transport_config
  - bld_config_pricing_page
  - bld_config_planning_strategy
  - bld_config_integration_guide
  - bld_config_product_tour
  - bld_config_diff_strategy
  - bld_config_visual_workflow
  - bld_config_agent_computer_interface
---

## Naming Convention
Pattern: `p05_pl_{{name}}.md`
Examples: `p05_pl_partnerA.md`, `p05_pl_sponsorX.md`

## Paths
Artifacts stored in: `/artifacts/p05/partner_listings/{{name}}.md`

## Limits
max_bytes: 4096
max_turns: 5
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Partner listing |
| Dependencies | knowledge_card, agent_card |
| Primary 8F function | F8_collaborate |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency knowledge_card not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | partner listing construction |
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
| [[bld_config_sales_playbook]] | sibling | 0.66 |
| [[bld_config_transport_config]] | sibling | 0.66 |
| [[bld_config_pricing_page]] | sibling | 0.65 |
| [[bld_config_planning_strategy]] | sibling | 0.65 |
| [[bld_config_integration_guide]] | sibling | 0.64 |
| [[bld_config_product_tour]] | sibling | 0.63 |
| [[bld_config_diff_strategy]] | sibling | 0.63 |
| [[bld_config_visual_workflow]] | sibling | 0.63 |
| [[bld_config_agent_computer_interface]] | sibling | 0.62 |
