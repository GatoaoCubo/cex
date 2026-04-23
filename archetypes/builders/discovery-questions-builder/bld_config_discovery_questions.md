---
kind: config
id: bld_config_discovery_questions
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for discovery_questions production
quality: 8.6
title: "Config Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, config]
tldr: "Naming, paths, limits for discovery_questions production"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_repo_map
  - bld_config_search_strategy
  - bld_config_pricing_page
  - bld_config_sales_playbook
  - bld_config_diff_strategy
  - bld_config_healthcare_vertical
  - bld_config_usage_quota
  - bld_config_agent_computer_interface
  - bld_config_transport_config
  - bld_config_product_tour
---

## Naming Convention
Pattern: `p01_dq_<name>.md` (e.g., `p01_dq_customer.md`, `p01_dq_product.md`)

## Paths
`/artifacts/p01/discovery_questions/{{name}}.md`
`/templates/p01/dq_template.md`

## Limits
- max_bytes: 4096
- max_turns: 5
- effort_level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_repo_map]] | sibling | 0.64 |
| [[bld_config_search_strategy]] | sibling | 0.62 |
| [[bld_config_pricing_page]] | sibling | 0.61 |
| [[bld_config_sales_playbook]] | sibling | 0.60 |
| [[bld_config_diff_strategy]] | sibling | 0.60 |
| [[bld_config_healthcare_vertical]] | sibling | 0.60 |
| [[bld_config_usage_quota]] | sibling | 0.60 |
| [[bld_config_agent_computer_interface]] | sibling | 0.60 |
| [[bld_config_transport_config]] | sibling | 0.59 |
| [[bld_config_product_tour]] | sibling | 0.59 |
