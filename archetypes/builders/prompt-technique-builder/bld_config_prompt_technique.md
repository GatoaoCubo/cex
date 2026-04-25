---
kind: config
id: bld_config_prompt_technique
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for prompt_technique production
quality: 8.6
title: "Config Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, config]
tldr: "Production constraints for prompt technique: naming (p03_pt_{{name}}.md), output paths (P03/), size limit 4096B. Prompt technique."
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_visual_workflow
  - bld_config_sales_playbook
  - bld_config_search_strategy
  - bld_config_planning_strategy
  - bld_config_transport_config
  - bld_config_partner_listing
  - bld_config_pricing_page
  - bld_config_diff_strategy
  - bld_config_healthcare_vertical
  - bld_config_repo_map
---

## Naming Convention
Pattern: `p03_pt_{{name}}.md`
Examples:
- `p03_pt_summarization.md`
- `p03_pt_qa.md`

## Paths
Artifacts stored in: `/opt/cex/techniques/p03/{{name}}.md`

## Limits
- max_bytes: 4096
- max_turns: 5
- effort_level: 3

## Hooks
- pre_build: null
- post_build: null
- on_error: null
- on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Prompt technique |
| Dependencies | prompt_template |
| Primary 8F function | F6_produce |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency prompt_template not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | prompt technique construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_visual_workflow]] | sibling | 0.67 |
| [[bld_config_sales_playbook]] | sibling | 0.67 |
| [[bld_config_search_strategy]] | sibling | 0.66 |
| [[bld_config_planning_strategy]] | sibling | 0.66 |
| [[bld_config_transport_config]] | sibling | 0.64 |
| [[bld_config_partner_listing]] | sibling | 0.62 |
| [[bld_config_pricing_page]] | sibling | 0.61 |
| [[bld_config_diff_strategy]] | sibling | 0.61 |
| [[bld_config_healthcare_vertical]] | sibling | 0.61 |
| [[bld_config_repo_map]] | sibling | 0.61 |
