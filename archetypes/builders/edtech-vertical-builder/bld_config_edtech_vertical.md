---
kind: config
id: bld_config_edtech_vertical
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for edtech_vertical production
quality: 8.6
title: "Config Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, config]
tldr: "Naming, paths, limits for edtech_vertical production"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_pricing_page
  - bld_config_diff_strategy
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_agent_computer_interface
  - bld_config_healthcare_vertical
  - bld_config_repo_map
  - bld_config_usage_quota
  - bld_config_transport_config
  - bld_config_product_tour
---

## Naming Convention
Pattern: p01_etv_{{name}}.md
Examples: p01_etv_math.md, p01_etv_science.md

## Paths
/cex/verticals/p01_etv_{{name}}/artifacts/

## Limits
max_bytes: 6144
max_turns: 5
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_pricing_page]] | sibling | 0.63 |
| [[bld_config_diff_strategy]] | sibling | 0.62 |
| [[bld_config_sales_playbook]] | sibling | 0.62 |
| [[bld_config_search_strategy]] | sibling | 0.62 |
| [[bld_config_agent_computer_interface]] | sibling | 0.62 |
| [[bld_config_healthcare_vertical]] | sibling | 0.62 |
| [[bld_config_repo_map]] | sibling | 0.60 |
| [[bld_config_usage_quota]] | sibling | 0.60 |
| [[bld_config_transport_config]] | sibling | 0.60 |
| [[bld_config_product_tour]] | sibling | 0.59 |
