---
kind: config
id: bld_config_changelog
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for changelog production
quality: 8.6
title: "Config Changelog"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, config]
tldr: "Naming, paths, limits for changelog production"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_repo_map
  - bld_config_search_strategy
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
  - bld_config_transport_config
  - bld_config_sales_playbook
  - bld_config_healthcare_vertical
  - bld_config_pricing_page
  - bld_config_usage_quota
  - bld_config_ab_test_config
---

## Naming Convention
Pattern: `p01_ch_{{name}}.md`
Examples:
- `p01_ch_release_v1.0.md`
- `p01_ch_hotfix_20231001.md`

## Paths
- Artifacts: `/artifacts/changelogs/p01/`
- Sources: `/src/pillars/p01/`

## Limits
- max_bytes: 5120
- max_turns: 10
- effort_level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_repo_map]] | sibling | 0.61 |
| [[bld_config_search_strategy]] | sibling | 0.61 |
| [[bld_config_diff_strategy]] | sibling | 0.60 |
| [[bld_config_agent_computer_interface]] | sibling | 0.59 |
| [[bld_config_transport_config]] | sibling | 0.59 |
| [[bld_config_sales_playbook]] | sibling | 0.59 |
| [[bld_config_healthcare_vertical]] | sibling | 0.59 |
| [[bld_config_pricing_page]] | sibling | 0.58 |
| [[bld_config_usage_quota]] | sibling | 0.58 |
| [[bld_config_ab_test_config]] | sibling | 0.58 |
