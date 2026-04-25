---
kind: config
id: bld_config_compliance_checklist
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for compliance_checklist production
quality: 8.6
title: "Config Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, config]
tldr: "Production constraints for compliance checklist: naming (p11_cc_{{name}}.md), output paths (P11/), size limit 6144B. Audit checklist."
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_pricing_page
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
  - bld_config_repo_map
  - bld_config_usage_quota
  - bld_config_product_tour
  - bld_config_ab_test_config
  - bld_config_transport_config
---

## Naming Convention
Pattern: `p11_cc_{{name}}.md`
Examples:
- `p11_cc_example.md`
- `p11_cc_compliance.md`

## Paths
- `/artifacts/compliance_checklists/p11_cc_{{name}}.md`
- `/reports/p11_cc_{{name}}_report.json`

## Limits
- max_bytes: 6144
- max_turns: 10
- effort_level: medium

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Audit checklist |
| Dependencies | quality_gate, knowledge_card |
| Primary 8F function | F1_constrain |
| Max artifact size | 6144 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 6144 bytes | Trim prose sections; preserve tables |
| Dependency quality_gate not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | compliance checklist construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_pricing_page]] | sibling | 0.58 |
| [[bld_config_sales_playbook]] | sibling | 0.58 |
| [[bld_config_search_strategy]] | sibling | 0.57 |
| [[bld_config_diff_strategy]] | sibling | 0.57 |
| [[bld_config_agent_computer_interface]] | sibling | 0.56 |
| [[bld_config_repo_map]] | sibling | 0.56 |
| [[bld_config_usage_quota]] | sibling | 0.56 |
| [[bld_config_product_tour]] | sibling | 0.55 |
| [[bld_config_ab_test_config]] | sibling | 0.55 |
| [[bld_config_transport_config]] | sibling | 0.54 |
