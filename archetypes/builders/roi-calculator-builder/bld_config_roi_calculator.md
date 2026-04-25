---
kind: config
id: bld_config_roi_calculator
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for roi_calculator production
quality: 8.6
title: "Config Roi Calculator"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [roi_calculator, builder, config]
tldr: "Production constraints for roi calculator: naming (p11_roi_{{name}}.yaml), output paths (P11/), size limit 4096B. ROI calc."
domain: "roi_calculator construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_ab_test_config
  - bld_config_usage_quota
  - bld_config_customer_segment
  - bld_config_safety_policy
  - bld_config_transport_config
  - bld_config_content_filter
  - bld_config_compliance_framework
  - bld_config_integration_guide
  - bld_config_data_residency
  - bld_config_sales_playbook
---

## Naming Convention
Pattern: `p11_roi_{{name}}.yaml`
Examples: `p11_roi_projectA.yaml`, `p11_roi_q4_2023.yaml`

## Paths
Artifacts: `/artifacts/roi/p11/{{name}}/output.yaml`
Logs: `/artifacts/roi/p11/{{name}}/logs/`

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
| Boundary | ROI calc |
| Dependencies | customer_segment, eval_metric |
| Primary 8F function | F6_produce |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency customer_segment not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | roi calculator construction |
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
| [[bld_config_usage_quota]] | sibling | 0.52 |
| [[bld_config_customer_segment]] | sibling | 0.52 |
| [[bld_config_safety_policy]] | sibling | 0.51 |
| [[bld_config_transport_config]] | sibling | 0.51 |
| [[bld_config_content_filter]] | sibling | 0.50 |
| [[bld_config_compliance_framework]] | sibling | 0.50 |
| [[bld_config_integration_guide]] | sibling | 0.50 |
| [[bld_config_data_residency]] | sibling | 0.50 |
| [[bld_config_sales_playbook]] | sibling | 0.50 |
