---
kind: config
id: bld_config_model_registry
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for model_registry production
quality: 8.6
title: "Config Model Registry"
version: "1.0.0"
author: wave1_builder_gen
tags: [model_registry, builder, config]
tldr: "Production constraints for model registry: naming (p10_mr_{{name}}.md), output paths (P10/), size limit 4096B. Model registry."
domain: "model_registry construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_diff_strategy
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_repo_map
  - bld_config_usage_quota
  - bld_config_product_tour
  - bld_config_ab_test_config
---

## Naming Convention
Pattern: p10_mr_{name}
Examples: p10_mr_gpt4, p10_mr_claude_sonnet

## Paths
Artifacts: P10_memory/registry/

## Limits
max_bytes: 4096
max_turns: 5
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Model registry |
| Dependencies | model_card, model_provider |
| Primary 8F function | F2_become |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency model_card not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | model registry construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_diff_strategy]] | sibling | 0.66 |
| [[bld_config_pricing_page]] | sibling | 0.66 |
| [[bld_config_agent_computer_interface]] | sibling | 0.66 |
| [[bld_config_sales_playbook]] | sibling | 0.66 |
| [[bld_config_search_strategy]] | sibling | 0.65 |
| [[bld_config_transport_config]] | sibling | 0.63 |
| [[bld_config_repo_map]] | sibling | 0.63 |
| [[bld_config_usage_quota]] | sibling | 0.63 |
| [[bld_config_product_tour]] | sibling | 0.62 |
| [[bld_config_ab_test_config]] | sibling | 0.62 |
