---
kind: config
id: bld_config_faq_entry
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for faq_entry production
quality: 8.6
title: "Config Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, config]
tldr: "Production constraints for faq entry: naming (p01_faq_{{name}}.md), output paths (P01/), size limit 3072B. FAQ entry."
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_api_reference
  - bld_config_repo_map
  - bld_config_visual_workflow
  - bld_config_prompt_technique
  - bld_config_diff_strategy
  - bld_config_search_strategy
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
  - bld_config_transport_config
  - bld_config_usage_quota
---

## Naming Convention
Pattern: p01_faq_<topic>_<identifier>.md
Examples:
- p01_faq_trading_limits.md
- p01_faq_support_contact.md

## Paths
/opt/cex/faq/entries/P01/

## Limits
max_bytes: 3072
max_turns: 5
effort level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | FAQ entry |
| Dependencies | knowledge_card |
| Primary 8F function | F3_inject |
| Max artifact size | 3072 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 3072 bytes | Trim prose sections; preserve tables |
| Dependency knowledge_card not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | faq entry construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_api_reference]] | sibling | 0.61 |
| [[bld_config_repo_map]] | sibling | 0.57 |
| [[bld_config_visual_workflow]] | sibling | 0.57 |
| [[bld_config_prompt_technique]] | sibling | 0.57 |
| [[bld_config_diff_strategy]] | sibling | 0.55 |
| [[bld_config_search_strategy]] | sibling | 0.55 |
| [[bld_config_pricing_page]] | sibling | 0.54 |
| [[bld_config_agent_computer_interface]] | sibling | 0.54 |
| [[bld_config_transport_config]] | sibling | 0.54 |
| [[bld_config_usage_quota]] | sibling | 0.54 |
