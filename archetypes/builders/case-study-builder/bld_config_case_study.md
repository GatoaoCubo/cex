---
kind: config
id: bld_config_case_study
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for case_study production
quality: 8.6
title: "Config Case Study"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, config]
tldr: "Production constraints for case study: naming (p05_cs_{{name}}.md), output paths (P05/), size limit 6144B. Case study."
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_integration_guide
  - bld_config_pricing_page
  - bld_config_partner_listing
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_visual_workflow
  - bld_config_prompt_technique
  - bld_config_product_tour
  - bld_config_transport_config
  - bld_config_diff_strategy
---

p05_cs_{{name}}.md
Pillar: P05
Max bytes: 6144

## Naming Convention
Pattern: `p05_cs_<study_name>.md`
Examples:
- `p05_cs_marketing.md`
- `p05_cs_technology.md`

## Paths
Artifacts stored in: `/opt/cex/artifacts/p05/{{name}}/`
Subdirectories: `docs/`, `data/`, `outputs/`

## Limits
- max_bytes: 6144
- max_turns: 5
- effort_level: medium

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Case study |
| Dependencies | knowledge_card, customer_segment |
| Primary 8F function | F4_reason |
| Max artifact size | 6144 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 6144 bytes | Trim prose sections; preserve tables |
| Dependency knowledge_card not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | case study construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_integration_guide]] | sibling | 0.63 |
| [[bld_config_pricing_page]] | sibling | 0.59 |
| [[bld_config_partner_listing]] | sibling | 0.58 |
| [[bld_config_sales_playbook]] | sibling | 0.58 |
| [[bld_config_search_strategy]] | sibling | 0.58 |
| [[bld_config_visual_workflow]] | sibling | 0.57 |
| [[bld_config_prompt_technique]] | sibling | 0.57 |
| [[bld_config_product_tour]] | sibling | 0.56 |
| [[bld_config_transport_config]] | sibling | 0.56 |
| [[bld_config_diff_strategy]] | sibling | 0.55 |
