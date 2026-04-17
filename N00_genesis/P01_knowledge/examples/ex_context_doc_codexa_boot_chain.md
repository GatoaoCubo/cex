---
id: p01_ctx_organization_boot_chain
kind: context_doc
pillar: P01
domain: architecture
scope: boot_initialization
quality: 9.0
title: "Context Doc Codexa Boot Chain"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for knowledge, demonstrating ideal structure and common pitfalls."
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Context: organization Boot Chain

## Scope
Sequencia deterministica de 8 camadas que inicializa qualquer sessao organization, de variavel de ambiente ate execucao de tarefa.

## Current State
```
L0 ENV        .env (API keys) + organization_AGENT_GROUP env var
L1 BOOT       boot/{sat}.cmd — set CLAUDECODE= | model | MCP config
L2 CLAUDE.MD  Auto-loaded — "read PRIME_{SAT}.md"
L3 RULES      .claude/rules/ (10 files: nav, encoding, agent_group)
L4 PRIME      records/agent_groups/{sat}/PRIME_{SAT}.md (identity)
L5 MENTAL     records/agent_groups/{sat}/mental_model.yaml (deep state)
L6 HANDOFF    .claude/handoffs/{sat}_*.md (dispatch queue)
L7 EXECUTION  Agent -> Skill -> Sub-agents -> Quality Gate
```

## Operational Context
1. **Deterministic**: same env = same boot state, always
2. **Fractal**: each layer references the next via path pointers
3. **Identity-first**: agent_group knows WHO before WHAT
4. **Fail-safe**: missing layer = graceful fallback to general session

| Layer | Token Cost | Mandatory |
|-------|-----------|-----------|
| L0-L1 | 0 | yes (env + script) |
| L2 CLAUDE.md | ~2K | yes |
| L3 rules | ~8K | yes (auto-loaded) |
| L4 PRIME | ~3K | yes (agent_groups) |
| L5 mental | ~2K | recommended |
| L6 handoff | ~1K | if dispatched |

## Decision Notes
1. `set CLAUDECODE=` prevents nested Claude detection (critical for isolation)
2. `--strict-mcp-config` ensures only declared MCPs available per agent_group
3. Total boot context: ~15K tokens (98% reduction from v3.6 monolithic load)

Source: `records/framework/docs/META_BOOTSTRAP.md`
