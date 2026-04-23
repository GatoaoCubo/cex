---
kind: config
id: bld_config_action_paradigm
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for action_paradigm production
quality: 8.8
title: "Config Action Paradigm"
version: "1.0.0"
author: wave1_builder_gen
tags: [action_paradigm, builder, config]
tldr: "Naming, paths, limits for action_paradigm production"
domain: "action_paradigm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_voice_pipeline
  - bld_config_collaboration_pattern
  - bld_config_search_strategy
  - bld_config_diff_strategy
  - bld_config_thinking_config
  - bld_config_transport_config
  - bld_config_stt_provider
  - bld_config_ab_test_config
  - bld_config_sales_playbook
  - bld_config_repo_map
---

## Naming Convention
Pattern: p04_act_<name> (lowercase alphanumeric, underscores allowed)
Examples: p04_act_data_flow, p04_act_error_handler

## Paths
Base: /artifacts/p04/actions/
Per-action: /artifacts/p04/actions/<name>/

## Limits
max_bytes: 4096
max_turns: 10
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | action_paradigm construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_voice_pipeline]] | sibling | 0.55 |
| [[bld_config_collaboration_pattern]] | sibling | 0.54 |
| [[bld_config_search_strategy]] | sibling | 0.51 |
| [[bld_config_diff_strategy]] | sibling | 0.50 |
| [[bld_config_thinking_config]] | sibling | 0.49 |
| [[bld_config_transport_config]] | sibling | 0.49 |
| [[bld_config_stt_provider]] | sibling | 0.47 |
| [[bld_config_ab_test_config]] | sibling | 0.47 |
| [[bld_config_sales_playbook]] | sibling | 0.47 |
| [[bld_config_repo_map]] | sibling | 0.47 |
