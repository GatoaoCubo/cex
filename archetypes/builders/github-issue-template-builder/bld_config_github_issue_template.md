---
kind: config
id: bld_config_github_issue_template
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for github_issue_template production
quality: 8.6
title: "Config Github Issue Template"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [github_issue_template, builder, config]
tldr: "Production constraints for github issue template: naming (p05_git_{{name}}.md), output paths (P05/), size limit 3072B. Issue template."
domain: "github_issue_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_pricing_page
  - bld_config_product_tour
  - bld_config_partner_listing
  - bld_config_sales_playbook
  - bld_config_integration_guide
  - bld_config_search_strategy
  - bld_config_diff_strategy
  - bld_config_agent_computer_interface
  - bld_config_repo_map
  - bld_config_usage_quota
---

p05_git_{{name}}.md
## Naming Convention
Pattern: p05_git_{{name}}.md
Examples: p05_git_feature_request.md, p05_git_bug_report.md

## Paths
/artifacts/github_issue_templates/p05/
/built/issues/p05/{{name}}.md

## Limits
max_bytes: 3072
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
| Boundary | Issue template |
| Dependencies | knowledge_card |
| Primary 8F function | F8_collaborate |
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
| Domain | github issue template construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_pricing_page]] | sibling | 0.63 |
| [[bld_config_product_tour]] | sibling | 0.60 |
| [[bld_config_partner_listing]] | sibling | 0.59 |
| [[bld_config_sales_playbook]] | sibling | 0.58 |
| [[bld_config_integration_guide]] | sibling | 0.58 |
| [[bld_config_search_strategy]] | sibling | 0.58 |
| [[bld_config_diff_strategy]] | sibling | 0.58 |
| [[bld_config_agent_computer_interface]] | sibling | 0.57 |
| [[bld_config_repo_map]] | sibling | 0.56 |
| [[bld_config_usage_quota]] | sibling | 0.56 |
