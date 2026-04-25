---
kind: config
id: bld_config_collaboration_pattern
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for collaboration_pattern production
quality: 8.8
title: "Config Collaboration Pattern"
version: "1.0.0"
author: wave1_builder_gen
tags: [collaboration_pattern, builder, config]
tldr: "Production constraints for collaboration pattern: naming (p12_collab_{{name}}.md), output paths (P12/), size limit 5120B. Coordination pattern."
domain: "collaboration_pattern construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_action_paradigm
  - bld_config_thinking_config
  - bld_config_pricing_page
  - bld_config_transport_config
  - bld_config_diff_strategy
  - bld_config_sales_playbook
  - bld_config_voice_pipeline
  - bld_config_search_strategy
  - bld_config_agent_computer_interface
  - bld_config_data_residency
---

## Naming Convention
Pattern: p12_collab_{{name}}.md
Examples: p12_collab_projectA.md, p12_collab_featureX.md

## Paths
/artifacts/p12/collab/{{name}}/

## Limits
- max_bytes: 5120
- max_turns: 10
- effort_level: medium

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | collaboration_pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Coordination pattern |
| Dependencies | workflow, agent_card |
| Primary 8F function | F8_collaborate |
| Max artifact size | 5120 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 5120 bytes | Trim prose sections; preserve tables |
| Dependency workflow not found | Warn; proceed with defaults |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_action_paradigm]] | sibling | 0.54 |
| [[bld_config_thinking_config]] | sibling | 0.53 |
| [[bld_config_pricing_page]] | sibling | 0.53 |
| [[bld_config_transport_config]] | sibling | 0.53 |
| [[bld_config_diff_strategy]] | sibling | 0.52 |
| [[bld_config_sales_playbook]] | sibling | 0.52 |
| [[bld_config_voice_pipeline]] | sibling | 0.52 |
| [[bld_config_search_strategy]] | sibling | 0.52 |
| [[bld_config_agent_computer_interface]] | sibling | 0.52 |
| [[bld_config_data_residency]] | sibling | 0.51 |
