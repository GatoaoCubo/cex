---
kind: config
id: bld_config_vc_credential
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for vc_credential production
quality: 8.6
title: "Config VC Credential"
version: "1.0.0"
author: n04_wave7
tags: [vc_credential, builder, config, W3C, did, p10]
tldr: "Production constraints for vc credential: naming (p10_vc_{{name}}.md), output paths (P10/), size limit 4096B. VC 2."
domain: "vc_credential construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_workflow_run_crate
  - bld_config_c2pa_manifest
  - bld_config_sales_playbook
  - bld_config_transport_config
  - bld_config_partner_listing
  - bld_config_planning_strategy
  - bld_config_visual_workflow
  - bld_config_prompt_technique
  - bld_config_pricing_page
---

## Naming Convention
Pattern: `p10_vc_{{name}}.md`
Examples: `p10_vc_agent_n03_capability.md`, `p10_vc_provenance_run_20260414.md`

## Paths
Artifacts stored in: `P10_memory/credentials/{{name}}.md`

## Limits
max_bytes: 4096
max_turns: 5
effort_level: 4

## Hooks
pre_build: validate_did_format
post_build: compile_to_yaml
on_error: null
on_quality_fail: rebuild_with_schema_fix

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | VC 2 |
| Dependencies | knowledge_card |
| Primary 8F function | F8_collaborate |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency knowledge_card not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | vc credential construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.68 |
| [[bld_config_workflow_run_crate]] | sibling | 0.68 |
| [[bld_config_c2pa_manifest]] | sibling | 0.67 |
| [[bld_config_sales_playbook]] | sibling | 0.67 |
| [[bld_config_transport_config]] | sibling | 0.65 |
| [[bld_config_partner_listing]] | sibling | 0.64 |
| [[bld_config_planning_strategy]] | sibling | 0.64 |
| [[bld_config_visual_workflow]] | sibling | 0.64 |
| [[bld_config_prompt_technique]] | sibling | 0.63 |
| [[bld_config_pricing_page]] | sibling | 0.62 |
