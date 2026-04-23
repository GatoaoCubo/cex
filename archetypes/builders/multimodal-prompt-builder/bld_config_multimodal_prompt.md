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
tldr: "Naming, paths, limits for multimodal_prompt production"
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
