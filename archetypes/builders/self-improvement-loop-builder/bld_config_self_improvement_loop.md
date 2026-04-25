---
kind: config
id: bld_config_self_improvement_loop
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for self_improvement_loop production
quality: 8.6
title: "Config Self Improvement Loop"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [self_improvement_loop, builder, config]
tldr: "Production constraints for self improvement loop: naming (p11_sil_{{name}}.md), output paths (P11/), size limit 5120B. Self-improvement loop."
domain: "self_improvement_loop construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_visual_workflow
  - bld_config_prompt_technique
  - bld_config_diff_strategy
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
  - bld_config_rbac_policy
  - bld_config_transport_config
  - bld_config_usage_quota
---

## Naming Convention
Pattern: p11_sil_{{name}}.md
Examples: p11_sil_daily_journal.md, p11_sil_weekly_review.md

## Paths
Artifacts: /opt/cex/loop/artifacts/p11_sil_{{name}}
Symlink: /opt/cex/loop/current → latest version

## Limits
max_bytes: 5120
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
| Boundary | Self-improvement loop |
| Dependencies | quality_gate, reward_signal |
| Primary 8F function | F7_govern |
| Max artifact size | 5120 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 5120 bytes | Trim prose sections; preserve tables |
| Dependency quality_gate not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | self improvement loop construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_visual_workflow]] | sibling | 0.58 |
| [[bld_config_prompt_technique]] | sibling | 0.58 |
| [[bld_config_diff_strategy]] | sibling | 0.54 |
| [[bld_config_sales_playbook]] | sibling | 0.54 |
| [[bld_config_search_strategy]] | sibling | 0.54 |
| [[bld_config_pricing_page]] | sibling | 0.54 |
| [[bld_config_agent_computer_interface]] | sibling | 0.54 |
| [[bld_config_rbac_policy]] | sibling | 0.52 |
| [[bld_config_transport_config]] | sibling | 0.52 |
| [[bld_config_usage_quota]] | sibling | 0.52 |
