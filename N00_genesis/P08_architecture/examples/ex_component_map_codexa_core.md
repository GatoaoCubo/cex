---
id: p08_cmap_organization_core
kind: component_map
pillar: P08
description: "Component map of organization-core repository"
scope: full_system
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.1
tags: [component-map, architecture, dependencies]
updated: "2026-04-07"
domain: "architecture"
title: "Component Map Codexa Core"
density_score: 0.92
tldr: "Defines component map for component map codexa core, with validation gates and integration points."
---

# Component Map: organization-core

## Components
| Component | Path | Depends On | Used By |
|-----------|------|-----------|---------|
| orchestrator orchestrator | boot/stella.cmd | Claude Code runtime, rules | USER |
| Agent_group boots | boot/*.cmd | claude CLI, MCP configs | orchestrator |
| Brain MCP | records/core/brain/ | Ollama, FAISS | All agent_groups |
| Quality Gate | records/core/python/quality_gate.py | git hooks | Pre-commit |
| Spawn Scripts | records/core/powershell/ | PowerShell | orchestrator |
| Signal Writer | records/core/python/signal_writer.py | filesystem | Agent_groups |
| Agent Store | records/agents/ | Brain index | Agent_groups |
| Skill Store | records/skills/ | Brain index | Agent_groups |
| Pool | records/pool/ | Brain index | Knowledge queries |
| WhatsApp Bridge | records/framework/whatsapp/ | Node.js, Groq | orchestrator |
| Handoffs | .claude/handoffs/ | filesystem | orchestrator -> Agent_groups |
| Signals | .claude/signals/ | filesystem | Agent_groups -> orchestrator |

## Data Flow
```
USER -> orchestrator -> handoffs/ -> spawn -> AGENT_GROUP -> signals/ -> orchestrator
                                           |
                                    brain_query (MCP)
                                           |
                                    Pool + Agents + Skills
```

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target
