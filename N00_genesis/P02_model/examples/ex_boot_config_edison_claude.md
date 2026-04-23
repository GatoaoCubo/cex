---
id: p02_boot_edison_claude
kind: boot_config
pillar: P02
provider: claude
identity: "builder_agent[BUILD]"
constraints:
  - dangerously-skip-permissions
  - bypassPermissions
  - no-chrome
tools:
  - organization-brain (stdio, hybrid search)
  - context7 (npx, external docs)
  - github (http, copilot MCP)
version: 1.0.0
created: 2026-03-24
author: orchestrator
domain: orchestration
quality: 9.0
tags: [boot, claude-cli, agent_group, edison, mcp-config]
updated: "2026-04-07"
title: "Boot Config Edison Claude"
density_score: 0.92
tldr: "Defines boot config for boot config edison claude, with validation gates and integration points."
related:
  - p01_ctx_organization_boot_chain
  - boot-config-builder
  - bld_examples_boot_config
  - bld_knowledge_card_boot_config
  - p01_kc_boot_config
  - p07_bm_agent_group_boot_time
  - bld_config_spawn_config
  - bld_memory_agent_card
  - p01_kc_mcp_server
  - bld_collaboration_boot_config
---

# builder_agent Boot Config — Claude CLI

## Boot Script (boot/edison.cmd)
```cmd
@echo off
title organization-builder_agent
set CLAUDECODE=
set organization_AGENT_GROUP=edison
set organization_ROOT=C:\Users\PC\Documents\GitHub\organization-core
cd /d "%organization_ROOT%"
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model opus --no-chrome
set MCP=--mcp-config "%organization_ROOT%\.mcp-edison.json" --strict-mcp-config
claude %FLAGS% %MCP% "%IDENTITY%"
```

## Boot Chain (5 Layers)
1. **ENV**: CLAUDECODE= (prevent nested), organization_AGENT_GROUP=edison
2. **BOOT SCRIPT**: Model selection (opus), MCP config, permission bypass
3. **CLAUDE.MD**: Auto-loaded, reads PRIME via agent_group env var
4. **RULES**: 10 rule files in .claude/rules/ (navigation, encoding, etc)
5. **PRIME**: `records/agent_groups/edison/PRIME_builder_agent.md` (full identity)

## Key Design Decisions
1. `set CLAUDECODE=` prevents nested Claude detection (critical for agent_group isolation)
2. `--strict-mcp-config` ensures only declared MCPs are available
3. Identity prompt injected as first argument (not via file)

## Properties

| Property | Value |
|----------|-------|
| Kind | `boot_config` |
| Pillar | P02 |
| Domain | orchestration |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_ctx_organization_boot_chain]] | related | 0.41 |
| [[boot-config-builder]] | related | 0.35 |
| [[bld_examples_boot_config]] | downstream | 0.33 |
| [[bld_knowledge_card_boot_config]] | upstream | 0.31 |
| [[p01_kc_boot_config]] | related | 0.31 |
| [[p07_bm_agent_group_boot_time]] | downstream | 0.30 |
| [[bld_config_spawn_config]] | downstream | 0.28 |
| [[bld_memory_agent_card]] | downstream | 0.27 |
| [[p01_kc_mcp_server]] | upstream | 0.27 |
| [[bld_collaboration_boot_config]] | downstream | 0.26 |
