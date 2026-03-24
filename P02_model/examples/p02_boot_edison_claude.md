---
id: p02_boot_edison_claude
type: boot_config
lp: P02
provider: claude
identity: "EDISON[BUILD]"
constraints:
  - dangerously-skip-permissions
  - bypassPermissions
  - no-chrome
tools:
  - codexa-brain (stdio, hybrid search)
  - context7 (npx, external docs)
  - github (http, copilot MCP)
version: 1.0.0
created: 2026-03-24
author: STELLA
domain: orchestration
quality: 9.0
tags: [boot, claude-cli, satellite, edison, mcp-config]
---

# EDISON Boot Config — Claude CLI

## Boot Script (boot/edison.cmd)
```cmd
@echo off
title CODEXA-EDISON
set CLAUDECODE=
set CODEXA_SATELLITE=edison
set CODEXA_ROOT=C:\Users\PC\Documents\GitHub\codexa-core
cd /d "%CODEXA_ROOT%"
set FLAGS=--dangerously-skip-permissions --permission-mode bypassPermissions --model opus --no-chrome
set MCP=--mcp-config "%CODEXA_ROOT%\.mcp-edison.json" --strict-mcp-config
claude %FLAGS% %MCP% "%IDENTITY%"
```

## Boot Chain (5 Layers)
1. **ENV**: CLAUDECODE= (prevent nested), CODEXA_SATELLITE=edison
2. **BOOT SCRIPT**: Model selection (opus), MCP config, permission bypass
3. **CLAUDE.MD**: Auto-loaded, reads PRIME via satellite env var
4. **RULES**: 10 rule files in .claude/rules/ (navigation, encoding, etc)
5. **PRIME**: `records/satellites/edison/PRIME_EDISON.md` (full identity)

## Key Design Decisions
- `set CLAUDECODE=` prevents nested Claude detection (critical for satellite isolation)
- `--strict-mcp-config` ensures only declared MCPs are available
- Identity prompt injected as first argument (not via file)
