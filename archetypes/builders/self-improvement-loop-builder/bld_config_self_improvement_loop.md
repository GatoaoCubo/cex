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
tldr: "Naming, paths, limits for self_improvement_loop production"
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
