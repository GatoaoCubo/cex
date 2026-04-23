---
kind: config
id: bld_config_course_module
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for course_module production
quality: 8.6
title: "Config Course Module"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [course_module, builder, config]
tldr: "Naming, paths, limits for course_module production"
domain: "course_module construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_pricing_page
  - bld_config_partner_listing
  - bld_config_visual_workflow
  - bld_config_sales_playbook
  - bld_config_prompt_technique
  - bld_config_search_strategy
  - bld_config_integration_guide
  - bld_config_product_tour
  - bld_config_transport_config
  - bld_config_diff_strategy
---

p05_cm_{{name}}.md
Pillar: P05

## Naming Convention
Pattern: `p05_cm_{{name}}.md`
Examples: `p05_cm_intro.md`, `p05_cm_lesson1.md`

## Paths
Artifacts stored in: `/opt/cex/course_modules/p05/{{name}}.md`

## Limits
max_bytes: 8192
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
| [[bld_config_pricing_page]] | sibling | 0.61 |
| [[bld_config_partner_listing]] | sibling | 0.60 |
| [[bld_config_visual_workflow]] | sibling | 0.60 |
| [[bld_config_sales_playbook]] | sibling | 0.60 |
| [[bld_config_prompt_technique]] | sibling | 0.59 |
| [[bld_config_search_strategy]] | sibling | 0.59 |
| [[bld_config_integration_guide]] | sibling | 0.59 |
| [[bld_config_product_tour]] | sibling | 0.58 |
| [[bld_config_transport_config]] | sibling | 0.56 |
| [[bld_config_diff_strategy]] | sibling | 0.56 |
