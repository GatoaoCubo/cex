---
id: crew_command
kind: instruction
pillar: P12
description: "Manage composable multi-role crews: list, show, run"
quality: null
title: "/crew"
version: "1.0.0"
author: n07_orchestrator
tags: [crew, orchestration, wave8, atemporal]
tldr: "List, inspect, or run composable multi-role crews with handoffs."
domain: "CEX system"
created: "2026-04-23"
density_score: 0.90
related:
  - composable-crew
  - p12_wf_orchestration_pipeline
  - crew_template
  - role_assignment
  - team_charter
---

# /crew — Composable Crew Management

## Usage

| Invocation | What it does |
|------------|-------------|
| `/crew list` | List all registered crew templates |
| `/crew show <name>` | Inspect resolved plan (roles, topology, agents) |
| `/crew run <name>` | Dry-run: generate prompts under `.cex/runtime/crews/` |
| `/crew run <name> --execute` | Real execution with LLM calls + artifact production |

## How it works

```bash
python _tools/cex_crew.py list
python _tools/cex_crew.py show product_launch
python _tools/cex_crew.py run product_launch \
    --charter N02_marketing/crews/team_charter_launch_demo.md
python _tools/cex_crew.py run product_launch \
    --charter N02_marketing/crews/team_charter_launch_demo.md --execute
```

## When to use crews vs other dispatch modes

| Scenario | Use |
|----------|-----|
| 1 artifact, 1 kind | `/build` (solo builder) |
| N artifacts in parallel, independent | `/grid` (parallel dispatch) |
| 1 coherent deliverable requiring N roles with handoffs | `/crew` |
| N parallel builders of the same kind | `dispatch.sh swarm` |

## The 5 WAVE8 primitives

| Kind | Pillar | Purpose |
|------|--------|---------|
| `crew_template` | P12 | Reusable recipe: roles + topology + handoff protocol |
| `role_assignment` | P02 | Binds role_name to agent_id with goal/tools |
| `capability_registry` | P08 | Index of all spawnable agents |
| `team_charter` | P12 | Mission contract: budget, deadline, quality gate |
| `nucleus_def` | P02 | Machine-readable nucleus identity |

## Topology

| Process | When |
|---------|------|
| `sequential` | Each role depends on the prior role's output |
| `hierarchical` | Manager coordinates workers (5+ roles) |
| `consensus` | All roles work in parallel, vote on final output |

See `.claude/rules/composable-crew.md` for full protocol.
