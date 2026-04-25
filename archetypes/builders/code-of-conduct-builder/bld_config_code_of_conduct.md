---
kind: config
id: bld_config_code_of_conduct
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for code_of_conduct production
quality: 8.6
title: "Config Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, config]
tldr: "Production constraints for code of conduct: naming (p05_coc_{{name}}.md), output paths (P05/), size limit 4096B. Code of conduct."
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_config_search_strategy
  - bld_config_sales_playbook
  - bld_config_transport_config
  - bld_config_visual_workflow
  - bld_config_prompt_technique
  - bld_config_partner_listing
  - bld_config_planning_strategy
  - bld_config_healthcare_vertical
  - bld_config_integration_guide
  - bld_config_safety_policy
---

## Naming Convention
Pattern: `p05_coc_{{name}}.md`
Examples: `p05_coc_myproject.md`, `p05_coc_openwidget.md`, `p05_coc_foundation.md`

## Paths
Artifacts stored in: `P05_output/community/{{name}}/CODE_OF_CONDUCT.md`
Builder ISOs stored in: `archetypes/builders/code-of-conduct-builder/`

## Limits
max_bytes: 4096
max_turns: 4
effort_level: 2

## Hooks
pre_build: null
post_build: python _tools/cex_compile.py {path}
on_error: log to .cex/runtime/signals/
on_quality_fail: retry F6 PRODUCE once, then escalate to N07

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | Code of conduct |
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
| Domain | code of conduct construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.51 |
| [[bld_config_sales_playbook]] | sibling | 0.49 |
| [[bld_config_transport_config]] | sibling | 0.49 |
| [[bld_config_visual_workflow]] | sibling | 0.48 |
| [[bld_config_prompt_technique]] | sibling | 0.48 |
| [[bld_config_partner_listing]] | sibling | 0.48 |
| [[bld_config_planning_strategy]] | sibling | 0.48 |
| [[bld_config_healthcare_vertical]] | sibling | 0.47 |
| [[bld_config_integration_guide]] | sibling | 0.46 |
| [[bld_config_safety_policy]] | sibling | 0.45 |
