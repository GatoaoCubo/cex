---
kind: config
id: bld_config_cohort_analysis
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for cohort_analysis production
quality: 8.6
title: "Config Cohort Analysis"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [cohort_analysis, builder, config]
tldr: "Production constraints for cohort analysis: naming (p07_ca_{{name}}.yaml), output paths (P07/), size limit 3072B. Cohort analytics."
domain: "cohort_analysis construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_customer_segment
  - bld_config_usage_quota
  - bld_config_ab_test_config
  - bld_config_transport_config
  - bld_config_roi_calculator
  - bld_config_integration_guide
  - bld_config_eval_framework
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_workflow_node
---

## Naming Convention
Pattern: `p07_ca_{{name}}.yaml`
Examples: `p07_ca_demographics.yaml`, `p07_ca_treatment.yaml`

## Paths
Artifacts: `/artifacts/p07/cohort_analysis/{{name}}/`
Logs: `/logs/p07/cohort_analysis/{{name}}/`

## Limits
max_bytes: 3072
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
| Boundary | Cohort analytics |
| Dependencies | eval_dataset, customer_segment |
| Primary 8F function | F4_reason |
| Max artifact size | 3072 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 3072 bytes | Trim prose sections; preserve tables |
| Dependency eval_dataset not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | cohort analysis construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_customer_segment]] | sibling | 0.56 |
| [[bld_config_usage_quota]] | sibling | 0.55 |
| [[bld_config_ab_test_config]] | sibling | 0.55 |
| [[bld_config_transport_config]] | sibling | 0.53 |
| [[bld_config_roi_calculator]] | sibling | 0.53 |
| [[bld_config_integration_guide]] | sibling | 0.53 |
| [[bld_config_eval_framework]] | sibling | 0.53 |
| [[bld_config_sales_playbook]] | sibling | 0.53 |
| [[bld_config_search_strategy]] | sibling | 0.53 |
| [[bld_config_workflow_node]] | sibling | 0.53 |
