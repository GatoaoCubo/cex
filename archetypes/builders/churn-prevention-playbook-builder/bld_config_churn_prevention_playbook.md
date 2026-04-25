---
kind: config
id: bld_config_churn_prevention_playbook
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for churn_prevention_playbook production
quality: 8.6
title: "Config Churn Prevention Playbook"
version: "1.0.0"
author: n05_wave6
tags: [churn_prevention_playbook, builder, config]
tldr: "Production constraints for churn prevention playbook: naming (p03_cpp_{{name}}.md), output paths (P03/), size limit 6144B. Churn playbook."
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_sales_playbook
  - bld_config_visual_workflow
  - bld_config_prompt_technique
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_healthcare_vertical
  - bld_config_diff_strategy
  - bld_config_ab_test_config
---

## Naming Convention
Pattern: `p03_cpp_{{name}}.md`
Examples: `p03_cpp_enterprise_red_zone.md`, `p03_cpp_smb_winback_90d.md`

## Paths
Artifacts stored in: `P03_prompt/playbooks/churn/`

## Limits
max_bytes: 6144
max_turns: 6
effort_level: 4

## Hooks
pre_build: load health_score_model from Gainsight config
post_build: compile + signal N06 with win-back offer parameters
on_error: log to `.cex/runtime/signals/churn_error.json`
on_quality_fail: rebuild -- enforce save script objection handlers

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Churn playbook |
| Dependencies | customer_segment, cohort_analysis |
| Primary 8F function | F6_produce |
| Max artifact size | 6144 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 6144 bytes | Trim prose sections; preserve tables |
| Dependency customer_segment not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | churn prevention playbook construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.47 |
| [[bld_config_transport_config]] | sibling | 0.47 |
| [[bld_config_sales_playbook]] | sibling | 0.46 |
| [[bld_config_visual_workflow]] | sibling | 0.45 |
| [[bld_config_prompt_technique]] | sibling | 0.45 |
| [[bld_config_planning_strategy]] | sibling | 0.44 |
| [[bld_config_partner_listing]] | sibling | 0.44 |
| [[bld_config_healthcare_vertical]] | sibling | 0.44 |
| [[bld_config_diff_strategy]] | sibling | 0.43 |
| [[bld_config_ab_test_config]] | sibling | 0.43 |
