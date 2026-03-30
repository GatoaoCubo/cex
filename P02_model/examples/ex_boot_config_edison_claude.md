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
tags: [boot, claude-cli, agent_node, edison, mcp-config]
---

# builder_agent Boot Config — Claude CLI

## Boot Script (boot/edison.cmd)
```cmd
@echo off
title organization-builder_agent
set CLAUDECODE=
set organization_SATELLITE=edison
set organization_ROOT=C:\Users\PC\Documents\GitHub\organization-core
cd /d "%organization_ROOT%"
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model opus --no-chrome
set MCP=--mcp-config "%organization_ROOT%\.mcp-edison.json" --strict-mcp-config
claude %FLAGS% %MCP% "%IDENTITY%"
```

## Boot Chain (5 Layers)
1. **ENV**: CLAUDECODE= (prevent nested), organization_SATELLITE=edison
2. **BOOT SCRIPT**: Model selection (opus), MCP config, permission bypass
3. **CLAUDE.MD**: Auto-loaded, reads PRIME via agent_node env var
4. **RULES**: 10 rule files in .claude/rules/ (navigation, encoding, etc)
5. **PRIME**: `records/agent_nodes/edison/PRIME_builder_agent.md` (full identity)

## Key Design Decisions
- `set CLAUDECODE=` prevents nested Claude detection (critical for agent_node isolation)
- `--strict-mcp-config` ensures only declared MCPs are available
- Identity prompt injected as first argument (not via file)
