---
kind: config
id: bld_config_eval_framework
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for eval_framework production
quality: 8.6
title: "Config Eval Framework"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_framework, builder, config]
tldr: "Production constraints for eval framework: naming (p07_efw_{{name}}.md), output paths (P07/), size limit 5120B. Eval framework."
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_workflow_node
  - bld_config_rl_algorithm
  - bld_config_ab_test_config
  - bld_config_search_strategy
  - bld_config_customer_segment
  - bld_config_graph_rag_config
  - bld_config_sales_playbook
  - bld_config_pricing_page
  - bld_config_benchmark_suite
  - bld_config_diff_strategy
---

## Naming Convention
Pattern: `p07_efw_{{name}}.md`
Examples: `p07_efw_chatbot.md`, `p07_efw_summarizer.md`

## Paths
Artifacts: `/mnt/artifacts/p07/efw/{{name}}`
Logs: `/var/log/eval_framework/p07/{{name}}`

## Limits
max_bytes: 5120
max_turns: 20
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Eval framework |
| Dependencies | eval_metric, scoring_rubric |
| Primary 8F function | F7_govern |
| Max artifact size | 5120 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 5120 bytes | Trim prose sections; preserve tables |
| Dependency eval_metric not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | eval framework construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_workflow_node]] | sibling | 0.65 |
| [[bld_config_rl_algorithm]] | sibling | 0.61 |
| [[bld_config_ab_test_config]] | sibling | 0.60 |
| [[bld_config_search_strategy]] | sibling | 0.59 |
| [[bld_config_customer_segment]] | sibling | 0.58 |
| [[bld_config_graph_rag_config]] | sibling | 0.58 |
| [[bld_config_sales_playbook]] | sibling | 0.57 |
| [[bld_config_pricing_page]] | sibling | 0.57 |
| [[bld_config_benchmark_suite]] | sibling | 0.57 |
| [[bld_config_diff_strategy]] | sibling | 0.56 |
