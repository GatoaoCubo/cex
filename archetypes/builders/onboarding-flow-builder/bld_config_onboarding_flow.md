---
kind: config
id: bld_config_onboarding_flow
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for onboarding_flow production
quality: 8.6
title: "Config Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, config]
tldr: "Production constraints for onboarding flow: naming (p05_of_{{name}}.md), output paths (P05/), size limit 5120B. Activation flow."
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_pricing_page
  - bld_config_visual_workflow
  - bld_config_prompt_technique
  - bld_config_product_tour
  - bld_config_course_module
  - bld_config_partner_listing
  - bld_config_user_journey
  - bld_config_integration_guide
  - bld_config_case_study
  - bld_config_rbac_policy
---

p05_of_{{name}}.md
Pillar: P05

## Naming Convention
Pattern: p05_of_{{name}}.md
Examples: p05_of_user_onboarding.md, p05_of_payment_setup.md

## Paths
/opt/cex/flows/p05/{{name}}
Example: /opt/cex/flows/p05/user_onboarding

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
| Boundary | Activation flow |
| Dependencies | user_journey, knowledge_card |
| Primary 8F function | F6_produce |
| Max artifact size | 5120 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 5120 bytes | Trim prose sections; preserve tables |
| Dependency user_journey not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | onboarding flow construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_pricing_page]] | sibling | 0.56 |
| [[bld_config_visual_workflow]] | sibling | 0.54 |
| [[bld_config_prompt_technique]] | sibling | 0.54 |
| [[bld_config_product_tour]] | sibling | 0.53 |
| [[bld_config_course_module]] | sibling | 0.52 |
| [[bld_config_partner_listing]] | sibling | 0.52 |
| [[bld_config_user_journey]] | sibling | 0.51 |
| [[bld_config_integration_guide]] | sibling | 0.51 |
| [[bld_config_case_study]] | sibling | 0.51 |
| [[bld_config_rbac_policy]] | sibling | 0.50 |
