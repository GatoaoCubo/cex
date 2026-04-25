---
kind: config
id: bld_config_judge_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for judge_config production
quality: 8.6
title: "Config Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, config]
tldr: "Production constraints for judge config: naming (p07_jc_{{name}}.md), output paths (P07/), size limit 4096B. Judge config."
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_ab_test_config
  - bld_config_rl_algorithm
  - bld_config_workflow_node
  - bld_config_search_strategy
  - bld_config_eval_framework
  - bld_config_sales_playbook
  - bld_config_pricing_page
  - bld_config_reward_model
  - bld_config_transport_config
  - bld_config_diff_strategy
---

## Naming Convention
Pattern: `p07_jc_{{name}}.md`
Examples: `p07_jc_initial.md`, `p07_jc_final.md`

## Paths
Artifacts: `/mnt/artifacts/p07/{{name}}/`
Judge config: `/mnt/configs/judge/p07_jc_{{name}}.md`

## Limits
max_bytes: 4096
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Judge config |
| Dependencies | content_filter, audit_log |
| Primary 8F function | F7_govern |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency content_filter not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | judge config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_ab_test_config]] | sibling | 0.63 |
| [[bld_config_rl_algorithm]] | sibling | 0.61 |
| [[bld_config_workflow_node]] | sibling | 0.60 |
| [[bld_config_search_strategy]] | sibling | 0.57 |
| [[bld_config_eval_framework]] | sibling | 0.57 |
| [[bld_config_sales_playbook]] | sibling | 0.55 |
| [[bld_config_pricing_page]] | sibling | 0.55 |
| [[bld_config_reward_model]] | sibling | 0.55 |
| [[bld_config_transport_config]] | sibling | 0.55 |
| [[bld_config_diff_strategy]] | sibling | 0.55 |
