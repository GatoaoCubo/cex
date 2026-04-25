---
kind: config
id: bld_config_mcp_app_extension
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for mcp_app_extension production
quality: 8.6
title: "Config MCP App Extension"
version: "1.0.0"
author: wave7_n03_dev_manifests
tags: [mcp_app_extension, builder, config]
tldr: "Production constraints for mcp app extension: naming (p04_mae_{{name}}.md), output paths (P04/), size limit 4096B. MCP Apps Extension app."
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_config_search_strategy
  - bld_config_sales_playbook
  - bld_config_transport_config
  - bld_config_diff_strategy
  - bld_config_planning_strategy
  - bld_config_partner_listing
  - bld_config_visual_workflow
  - bld_config_pricing_page
  - bld_config_agent_computer_interface
  - bld_config_prompt_technique
---

## Naming Convention
Pattern: `p04_mae_{{name}}.md`
Examples: `p04_mae_figma_design_inspector.md`, `p04_mae_notion_workspace_ui.md`

## Paths
Artifacts stored in: `/artifacts/p04/mcp_app_extensions/{{name}}.md`

## Limits
max_bytes: 4096
max_turns: 6
effort_level: 4

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null

## Domain-Specific Constraints

| Constraint | Value |
|-----------|-------|
| Boundary | MCP Apps Extension app |
| Dependencies | mcp_server, api_client |
| Primary 8F function | F5_call |
| Max artifact size | 4096 bytes |

## Edge Cases

| Scenario | Handling |
|----------|---------|
| Missing required frontmatter field | Fail H01 gate; return to F6 |
| ID collision with existing artifact | Append version suffix (_v2) |
| Body exceeds 4096 bytes | Trim prose sections; preserve tables |
| Dependency mcp_server not found | Warn; proceed with defaults |

## Properties

| Property | Value |
|----------|-------|
| Kind | `config` |
| Pillar | P09 |
| Domain | mcp app extension construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_search_strategy]] | sibling | 0.69 |
| [[bld_config_sales_playbook]] | sibling | 0.65 |
| [[bld_config_transport_config]] | sibling | 0.65 |
| [[bld_config_diff_strategy]] | sibling | 0.64 |
| [[bld_config_planning_strategy]] | sibling | 0.64 |
| [[bld_config_partner_listing]] | sibling | 0.63 |
| [[bld_config_visual_workflow]] | sibling | 0.62 |
| [[bld_config_pricing_page]] | sibling | 0.62 |
| [[bld_config_agent_computer_interface]] | sibling | 0.62 |
| [[bld_config_prompt_technique]] | sibling | 0.62 |
