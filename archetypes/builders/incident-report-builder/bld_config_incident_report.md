---
kind: config
id: bld_config_incident_report
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for incident_report production
quality: 8.6
title: "Config Incident Report"
version: "1.1.0"
author: n05_ops
tags: [incident_report, builder, config]
tldr: "Production constraints for incident report: naming (p11_ir_{{name}}.md), output paths (P11/), size limit 5120B. Incident post-mortem."
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_transport_config
  - bld_config_diff_strategy
  - bld_config_planning_strategy
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
  - bld_config_partner_listing
  - bld_config_integration_guide
  - bld_config_visual_workflow
---

## Naming Convention
Pattern: `p11_ir_{{name}}.md` (e.g., `p11_ir_inc001.md`). {{name}} replaced with incident identifier. ASCII-only, lowercase.

## Paths
Artifacts stored in `/artifacts/incident_reports/`.

## Limits
max_bytes: 8192
max_turns: 5
effort_level: medium

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Incident post-mortem |
| Dependencies | audit_log, knowledge_card |
| Primary 8F function | F8_collaborate |
| Max artifact size | 5120 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 5120 bytes | Trim prose sections; preserve tables |
| Dependency audit_log not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | incident report construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_sales_playbook]] | sibling | 0.64 |
| [[bld_config_search_strategy]] | sibling | 0.64 |
| [[bld_config_transport_config]] | sibling | 0.61 |
| [[bld_config_diff_strategy]] | sibling | 0.61 |
| [[bld_config_planning_strategy]] | sibling | 0.60 |
| [[bld_config_pricing_page]] | sibling | 0.60 |
| [[bld_config_agent_computer_interface]] | sibling | 0.60 |
| [[bld_config_partner_listing]] | sibling | 0.60 |
| [[bld_config_integration_guide]] | sibling | 0.59 |
| [[bld_config_visual_workflow]] | sibling | 0.58 |
