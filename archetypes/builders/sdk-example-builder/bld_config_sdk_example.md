---
kind: config
id: bld_config_sdk_example
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for sdk_example production
quality: 8.6
title: "Config Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, config]
tldr: "Production constraints for sdk example: naming (p04_sdk_{{name}}.md), output paths (P04/), size limit 5120B. SDK example."
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_diff_strategy
  - bld_config_sales_playbook
  - bld_config_transport_config
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_mcp_app_extension
  - bld_config_agent_computer_interface
  - bld_config_ab_test_config
  - bld_config_visual_workflow
---

## Naming Convention
Pattern: `p04_sdk_{{name}}`
Examples: `p04_sdk_userauth`, `p04_sdk_payment`

## Paths
Artifacts stored in: `/artifacts/sdk/P04/{{name}}`
Example: `/artifacts/sdk/P04/userauth`

## Limits
- max_bytes: 5120
- max_turns: 10
- effort_level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | SDK example |
| Dependencies | api_client, function_def |
| Primary 8F function | F6_produce |
| Max artifact size | 5120 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 5120 bytes | Trim prose sections; preserve tables |
| Dependency api_client not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | sdk example construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.65 |
| [[bld_config_diff_strategy]] | sibling | 0.60 |
| [[bld_config_sales_playbook]] | sibling | 0.59 |
| [[bld_config_transport_config]] | sibling | 0.59 |
| [[bld_config_planning_strategy]] | sibling | 0.59 |
| [[bld_config_partner_listing]] | sibling | 0.57 |
| [[bld_config_mcp_app_extension]] | sibling | 0.57 |
| [[bld_config_agent_computer_interface]] | sibling | 0.56 |
| [[bld_config_ab_test_config]] | sibling | 0.55 |
| [[bld_config_visual_workflow]] | sibling | 0.55 |
