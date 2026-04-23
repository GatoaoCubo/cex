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
tldr: "Naming, paths, limits for cohort_analysis production"
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
