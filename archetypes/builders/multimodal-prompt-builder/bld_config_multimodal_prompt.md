---
kind: config
id: bld_config_multimodal_prompt
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for multimodal_prompt production
quality: 8.6
title: "Config Multimodal Prompt"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [multimodal_prompt, builder, config]
tldr: "Production constraints for multimodal prompt: naming (p03_mmp_{{name}}.md), output paths (P03/), size limit 4096B. Multimodal prompt."
domain: "multimodal_prompt construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_graph_rag_config
  - bld_config_planning_strategy
  - bld_config_workflow_node
  - bld_config_sales_playbook
  - bld_config_ab_test_config
  - bld_config_prompt_technique
  - bld_config_diff_strategy
  - bld_config_search_strategy
  - bld_config_rl_algorithm
  - bld_config_agent_computer_interface
---

## Naming Convention
Pattern: p03_mmp_<project>_<module>.md
Examples: p03_mmp_cex_core.md, p03_mmp_ai_vision.md

## Paths
Artifacts: /mnt/data/cex/p03/mmp/<project>/artifacts
Logs: /var/log/cex/p03/mmp/<project>

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
| Boundary | Multimodal prompt |
| Dependencies | prompt_template |
| Primary 8F function | F6_produce |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency prompt_template not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | multimodal prompt construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_graph_rag_config]] | sibling | 0.57 |
| [[bld_config_planning_strategy]] | sibling | 0.54 |
| [[bld_config_workflow_node]] | sibling | 0.53 |
| [[bld_config_sales_playbook]] | sibling | 0.52 |
| [[bld_config_ab_test_config]] | sibling | 0.51 |
| [[bld_config_prompt_technique]] | sibling | 0.50 |
| [[bld_config_diff_strategy]] | sibling | 0.50 |
| [[bld_config_search_strategy]] | sibling | 0.50 |
| [[bld_config_rl_algorithm]] | sibling | 0.50 |
| [[bld_config_agent_computer_interface]] | sibling | 0.49 |
