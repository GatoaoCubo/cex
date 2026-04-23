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
related:
  - bld_examples_diagram
  - p01_rs_brain_faiss_index
  - p09_path_organization_repos
  - p11_gr_stella_dispatch
  - p08_diag_agent_group_grid
  - bld_tools_spawn_config
  - p10_bi_organization_brain
  - p08_sat_edison
  - bld_examples_instruction
  - p12_crew_agent_group_grid
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_diagram]] | related | 0.37 |
| [[p01_rs_brain_faiss_index]] | related | 0.37 |
| [[p09_path_organization_repos]] | downstream | 0.28 |
| [[p11_gr_stella_dispatch]] | downstream | 0.28 |
| [[p08_diag_agent_group_grid]] | related | 0.28 |
| [[bld_tools_spawn_config]] | upstream | 0.27 |
| [[p10_bi_organization_brain]] | downstream | 0.26 |
| [[p08_sat_edison]] | related | 0.25 |
| [[bld_examples_instruction]] | upstream | 0.25 |
| [[p12_crew_agent_group_grid]] | downstream | 0.25 |
