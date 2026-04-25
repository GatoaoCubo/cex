---
kind: config
id: bld_config_bias_audit
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for bias_audit production
quality: 8.6
title: "Config Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, config]
tldr: "Production constraints for bias audit: naming (p07_ba_{{name}}.md), output paths (P07/), size limit 5120B. Fairness evaluation."
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_voice_pipeline
  - bld_config_customer_segment
  - bld_config_search_strategy
  - bld_config_usage_quota
  - bld_config_workflow_node
  - bld_config_integration_guide
  - bld_config_pricing_page
  - bld_config_experiment_tracker
  - bld_config_graph_rag_config
  - bld_config_sales_playbook
---

## Naming Convention

This ISO drives a bias audit: measuring fairness across demographic slices.
Pattern: `p07_ba_{{name}}.md`
Examples:
- `p07_ba_model_v1.md`
- `p07_ba_dataset_2023.md`

## Paths
- Base: `/artifacts/p07/bias_audit/{{name}}/`
- Outputs: `{{base}}/outputs/`
- Logs: `{{base}}/logs/`
- Temp: `{{base}}/tmp/`

## Limits
- max_bytes: 5120
- max_turns: 10
- effort_level: high

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Fairness evaluation |
| Dependencies | eval_dataset, scoring_rubric |
| Primary 8F function | F7_govern |
| Max artifact size | 5120 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 5120 bytes | Trim prose sections; preserve tables |
| Dependency eval_dataset not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | bias audit construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_voice_pipeline]] | sibling | 0.58 |
| [[bld_config_customer_segment]] | sibling | 0.49 |
| [[bld_config_search_strategy]] | sibling | 0.47 |
| [[bld_config_usage_quota]] | sibling | 0.46 |
| [[bld_config_workflow_node]] | sibling | 0.46 |
| [[bld_config_integration_guide]] | sibling | 0.46 |
| [[bld_config_pricing_page]] | sibling | 0.46 |
| [[bld_config_experiment_tracker]] | sibling | 0.46 |
| [[bld_config_graph_rag_config]] | sibling | 0.45 |
| [[bld_config_sales_playbook]] | sibling | 0.45 |
