---
kind: config
id: bld_config_gpai_technical_doc
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for gpai_technical_doc production
quality: 8.6
title: "Config GPAI Technical Doc"
version: "1.0.0"
author: n01_wave7
tags: [gpai_technical_doc, builder, config, GPAI, EU-AI-Act, Annex-IV]
tldr: "Production constraints for gpai technical doc: naming (p11_gpai_{{model}}.md), output paths (P11/), size limit 5120B. GPAI provider technical documentation per EU-AI-Act Article-53 and Annex-IV."
domain: "gpai_technical_doc construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_sales_playbook
  - bld_config_safety_hazard_taxonomy
  - bld_config_ai_rmf_profile
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_diff_strategy
  - bld_config_visual_workflow
  - bld_config_agent_computer_interface
---

## Naming Convention
Pattern: `p11_gpai_{{model}}.md`
Examples: `p11_gpai_acmellm_v2_1.md`, `p11_gpai_company_foundation_model_v1.md`

## Paths
Artifacts stored in: `P11_governance/gpai_technical_docs/`

## Limits
max_bytes: 5120
max_turns: 8
effort_level: 5

## Hooks
pre_build: validate_annex_iv_fields
post_build: compile + signal_n07
on_error: null
on_quality_fail: retry_with_field_checklist

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | GPAI provider technical documentation per EU-AI-Act Article-53 and Annex-IV |
| Dependencies | ai_rmf_profile, knowledge_card |
| Primary 8F function | F7_govern |
| Max artifact size | 5120 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 5120 bytes | Trim prose sections; preserve tables |
| Dependency ai_rmf_profile not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | gpai technical doc construction |
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
| [[bld_config_transport_config]] | sibling | 0.67 |
| [[bld_config_sales_playbook]] | sibling | 0.66 |
| [[bld_config_safety_hazard_taxonomy]] | sibling | 0.65 |
| [[bld_config_ai_rmf_profile]] | sibling | 0.64 |
| [[bld_config_planning_strategy]] | sibling | 0.64 |
| [[bld_config_partner_listing]] | sibling | 0.64 |
| [[bld_config_diff_strategy]] | sibling | 0.63 |
| [[bld_config_visual_workflow]] | sibling | 0.63 |
| [[bld_config_agent_computer_interface]] | sibling | 0.63 |
