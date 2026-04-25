---
kind: config
id: bld_config_agents_md
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for agents_md production
quality: 8.6
title: "Config Agents Md"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [agents_md, builder, config]
tldr: "Production constraints for agents md: naming (p02_am_{{name}}.md), output paths (P02/), size limit 3072B. AGENTS."
domain: "agents_md construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_sales_playbook
  - bld_config_transport_config
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_diff_strategy
  - bld_config_visual_workflow
  - bld_config_customer_segment
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
---

## Naming Convention
Pattern: `p02_am_{{name}}.md`
Examples: `p02_am_acme_api.md`, `p02_am_cex_core.md`

## Paths
Artifacts stored in: `/artifacts/p02/agents_md/{{name}}.md`

## Limits
max_bytes: 3072
max_turns: 5
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | AGENTS |
| Dependencies | agent, agent_card |
| Primary 8F function | F2_become |
| Max artifact size | 3072 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 3072 bytes | Trim prose sections; preserve tables |
| Dependency agent not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | agents md construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.66 |
| [[bld_config_sales_playbook]] | sibling | 0.65 |
| [[bld_config_transport_config]] | sibling | 0.64 |
| [[bld_config_planning_strategy]] | sibling | 0.63 |
| [[bld_config_partner_listing]] | sibling | 0.63 |
| [[bld_config_diff_strategy]] | sibling | 0.62 |
| [[bld_config_visual_workflow]] | sibling | 0.61 |
| [[bld_config_customer_segment]] | sibling | 0.61 |
| [[bld_config_pricing_page]] | sibling | 0.61 |
| [[bld_config_agent_computer_interface]] | sibling | 0.61 |
