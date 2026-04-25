---
kind: config
id: bld_config_content_filter
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for content_filter production
quality: 8.6
title: "Config Content Filter"
version: "1.0.0"
author: wave1_builder_gen
tags: [content_filter, builder, config]
tldr: "Production constraints for content filter: naming (p11_cf_{{name}}.md), output paths (P11/), size limit 4096B. Content filtering pipeline."
domain: "content_filter construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_safety_policy
  - bld_config_compliance_framework
  - bld_config_sales_playbook
  - bld_config_ab_test_config
  - bld_config_transport_config
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
---

## Naming Convention

This ISO defines a content filter -- the moderation rules that gate output or input.
Pattern: `p11_cf_{{name}}.md`
Examples:
- `p11_cf_report.md`
- `p11_cf_summary.md`

## Paths
Artifacts stored in: `/artifacts/p11/{{name}}/`
Example: `/artifacts/p11/report/`

## Limits
max_bytes: 4096
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
| Boundary | Content filtering pipeline |
| Dependencies | guardrail |
| Primary 8F function | F1_constrain |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency guardrail not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | content filter construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.58 |
| [[bld_config_safety_policy]] | sibling | 0.58 |
| [[bld_config_compliance_framework]] | sibling | 0.57 |
| [[bld_config_sales_playbook]] | sibling | 0.56 |
| [[bld_config_ab_test_config]] | sibling | 0.56 |
| [[bld_config_transport_config]] | sibling | 0.56 |
| [[bld_config_planning_strategy]] | sibling | 0.56 |
| [[bld_config_partner_listing]] | sibling | 0.55 |
| [[bld_config_diff_strategy]] | sibling | 0.54 |
| [[bld_config_agent_computer_interface]] | sibling | 0.53 |
