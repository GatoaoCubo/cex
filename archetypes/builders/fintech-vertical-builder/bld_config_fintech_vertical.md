---
kind: config
id: bld_config_fintech_vertical
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for fintech_vertical production
quality: 8.6
title: "Config Fintech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [fintech_vertical, builder, config]
tldr: "Production constraints for fintech vertical: naming (p01_fv_{{name}}.md), output paths (P01/), size limit 6144B. Fintech vertical KC."
domain: "fintech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_customer_segment
  - bld_config_integration_guide
  - bld_config_sales_playbook
  - bld_config_healthcare_vertical
  - bld_config_search_strategy
  - bld_config_workflow_node
  - bld_config_pricing_page
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
  - bld_config_repo_map
---

## Naming Convention
Pattern: `p01_fv_{{name}}.md`
Examples: `p01_fv_payment_gateway.md`, `p01_fv_fraud_detection.md`

## Paths
Artifacts: `/artifacts/verticals/p01_fv_{{name}}`
Configs: `/configs/p01`
Logs: `/logs/p01_fv_{{name}}`

## Limits
max_bytes: 6144
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
| Boundary | Fintech vertical KC |
| Dependencies | customer_segment, knowledge_card |
| Primary 8F function | F1_constrain |
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
| Domain | fintech vertical construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_customer_segment]] | sibling | 0.57 |
| [[bld_config_integration_guide]] | sibling | 0.54 |
| [[bld_config_sales_playbook]] | sibling | 0.54 |
| [[bld_config_healthcare_vertical]] | sibling | 0.54 |
| [[bld_config_search_strategy]] | sibling | 0.53 |
| [[bld_config_workflow_node]] | sibling | 0.53 |
| [[bld_config_pricing_page]] | sibling | 0.53 |
| [[bld_config_diff_strategy]] | sibling | 0.53 |
| [[bld_config_agent_computer_interface]] | sibling | 0.52 |
| [[bld_config_repo_map]] | sibling | 0.52 |
