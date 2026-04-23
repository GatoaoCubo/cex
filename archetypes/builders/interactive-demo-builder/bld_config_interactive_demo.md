---
kind: config
id: bld_config_interactive_demo
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for interactive_demo production
quality: 8.6
title: "Config Interactive Demo"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [interactive_demo, builder, config]
tldr: "Naming, paths, limits for interactive_demo production"
domain: "interactive_demo construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_customer_segment
  - bld_config_integration_guide
  - bld_config_pricing_page
  - bld_config_workflow_node
  - bld_config_product_tour
  - bld_config_partner_listing
  - bld_config_search_strategy
  - bld_config_sales_playbook
  - bld_config_diff_strategy
  - bld_config_usage_quota
---

## Naming Convention
Pattern: `p05_id_{{name}}.md`
Examples: `p05_id_demo1.md`, `p05_id_userflow.md`

## Paths
Artifacts: `/artifacts/p05/demos/{{name}}`
Logs: `/logs/p05/{{name}}_build.log`

## Limits
max_bytes: 6144
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
| [[bld_config_customer_segment]] | sibling | 0.61 |
| [[bld_config_integration_guide]] | sibling | 0.60 |
| [[bld_config_pricing_page]] | sibling | 0.60 |
| [[bld_config_workflow_node]] | sibling | 0.59 |
| [[bld_config_product_tour]] | sibling | 0.58 |
| [[bld_config_partner_listing]] | sibling | 0.58 |
| [[bld_config_search_strategy]] | sibling | 0.58 |
| [[bld_config_sales_playbook]] | sibling | 0.56 |
| [[bld_config_diff_strategy]] | sibling | 0.55 |
| [[bld_config_usage_quota]] | sibling | 0.55 |
