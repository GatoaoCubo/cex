---
id: p12_spawn_knowledge_engineer
kind: spawn_config
pillar: P12
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
title: "Knowledge Engineer Spawn Config"
mode: solo
agent_group: knowledge_engineer
model: opus-4-6
flags:
  - --model
  - opus-4-6
  - --reasoning-effort
  - high
mcp_config: .mcp-n04.json
timeout_seconds: 7200
prompt_inline: false
handoff_path: .cex/runtime/handoffs/n04_task.md
quality: 8.9
tags: [spawn_config, knowledge, n04, opus, rag, embedding, supabase]
tldr: "N04 Knowledge Engineer spawn on Opus 4.6 with 5 MCP servers (supabase, postgres, fetch, firecrawl, notebooklm) for full knowledge lifecycle."
domain: knowledge-management
density_score: 0.92
related:
  - agent_card_n04
  - n04_self_audit_20260408
  - p12_mission_supabase_data_layer
  - bld_collaboration_supabase_data_layer
  - bld_architecture_supabase_data_layer
  - self_audit_newpc
  - p02_nd_n04.md
  - self_audit_n04_codex_2026_04_15
  - p01_kc_supabase_data_layer_n04
  - grid_test_n04_20260407
---

# Spawn Command

```powershell
claude --model opus-4-6 --reasoning-effort high
```

## Parameters

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| `mode` | `solo` | Knowledge work requires deep context — single-owner session |
| `agent_group` | `knowledge_engineer` | Routes to N04 persona with Knowledge Gluttony lens |
| `model` | `opus-4-6` | 1M context for ingesting large document corpora |
| `timeout_seconds` | `7200` | 2h — KC creation, embedding batch, taxonomy builds are long-running |
| `mcp_config` | `.mcp-n04.json` | 5 servers: supabase, postgres, fetch, firecrawl, notebooklm |
| `prompt_inline` | `false` | Prompt loaded from agent card + ISOs, not CLI arg |

## MCP Servers Required

| Server | Critical | Used For |
|--------|----------|----------|
| supabase | Yes | Schema ops, RLS, project admin |
| postgres | Yes | Direct SQL — migrations, bulk vector inserts |
| fetch | Yes | HTTP content retrieval for KC authoring |
| firecrawl | Recommended | Bulk web crawling for knowledge ingestion |
| notebooklm | Optional | Transform KCs → audio, flashcards, quizzes |

## Environment

| Variable | Value |
|----------|-------|
| `CEX_NUCLEUS` | `N04` |
| `CEX_SIN` | `Knowledge Gluttony` |
| `CEX_DOMAIN` | `knowledge-management` |

## Pre-Flight Checklist

1. `.mcp-n04.json` exists and all 5 servers reachable
2. `.cex/runtime/handoffs/n04_task.md` exists with valid frontmatter
3. `N04_knowledge/agent_card_n04.md` loaded for capability awareness
4. `cex_skill_loader.py` can resolve builder ISOs for target kind
5. Git working tree is clean (no uncommitted changes in N04_knowledge/)

## Post-Completion

```bash
# Compile all created artifacts
python _tools/cex_compile.py N04_knowledge/ --all

# Signal completion
python -c "from _tools.signal_writer import write_signal; write_signal('n04', 'complete', 9.0)"

# Commit
git add -A && git commit -m "[N04] <description>"
```

## Boundary

Configuracao de spawn de agent_groups. NAO eh boot_config (P02, per-provider) nem env_config (P09, variaveis).


## 8F Pipeline Function

Primary function: **GOVERN**

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[agent_card_n04]] | upstream | 0.42 |
| [[n04_self_audit_20260408]] | upstream | 0.33 |
| [[p12_mission_supabase_data_layer]] | related | 0.32 |
| [[bld_collaboration_supabase_data_layer]] | related | 0.30 |
| [[bld_architecture_supabase_data_layer]] | upstream | 0.29 |
| [[self_audit_newpc]] | upstream | 0.29 |
| [[p02_nd_n04.md]] | upstream | 0.28 |
| [[self_audit_n04_codex_2026_04_15]] | upstream | 0.28 |
| [[p01_kc_supabase_data_layer_n04]] | upstream | 0.27 |
| [[grid_test_n04_20260407]] | upstream | 0.27 |
