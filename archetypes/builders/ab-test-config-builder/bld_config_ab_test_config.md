---
kind: config
id: bld_config_ab_test_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for ab_test_config production
quality: 8.6
title: "Config Ab Test Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ab_test_config, builder, config]
tldr: "Production constraints for ab test config: naming (p11_abt_{{name}}.yaml), output paths (P11/), size limit 4096B. A/B test spec."
domain: "ab_test_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_usage_quota
  - bld_config_transport_config
  - bld_config_search_strategy
  - bld_config_workflow_node
  - bld_config_data_residency
  - bld_config_graph_rag_config
  - bld_config_diff_strategy
  - bld_config_sales_playbook
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
---

## Naming Convention
Pattern: `p11_abt_{{name}}.yaml`
Examples: `p11_abt_feature_flag.yaml`, `p11_abt_button_color.yaml`

## Paths
Artifacts: `/mnt/artifacts/pillar/P11/ab_tests/{{name}}.yaml`

## Limits
max_bytes: 4096
max_turns: 100
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | A/B test spec |
| Dependencies | feature_flag, eval_metric |
| Primary 8F function | F1_constrain |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency feature_flag not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | ab test config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_usage_quota]] | sibling | 0.59 |
| [[bld_config_transport_config]] | sibling | 0.57 |
| [[bld_config_search_strategy]] | sibling | 0.54 |
| [[bld_config_workflow_node]] | sibling | 0.54 |
| [[bld_config_data_residency]] | sibling | 0.53 |
| [[bld_config_graph_rag_config]] | sibling | 0.53 |
| [[bld_config_diff_strategy]] | sibling | 0.53 |
| [[bld_config_sales_playbook]] | sibling | 0.53 |
| [[bld_config_pricing_page]] | sibling | 0.52 |
| [[bld_config_agent_computer_interface]] | sibling | 0.52 |
