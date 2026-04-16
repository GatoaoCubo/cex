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
tldr: "Naming, paths, limits for mcp_app_extension production"
domain: "mcp_app_extension construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
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
