---
id: p02_nd_n07.md
kind: nucleus_def
pillar: P02
nucleus_id: N07
role: orchestrator
sin_lens: "Orchestrating Sloth"
cli_binding: claude
model_tier: opus
model_specific: claude-opus-4-6
context_tokens: 1000000
boot_script: boot/cex.ps1
agent_card_path: N07_admin/agent_card_n07.md
pillars_owned:
  - P12
crew_templates_exposed:
  - grid_of_crews
  - mission_plan
domain_agents:
  - agent_dispatcher
  - agent_consolidator
fallback_cli: codex
title: "Nucleus Def N07"
version: "1.0.0"
author: n07_crewwiring
domain: "orchestration, dispatch, mission planning"
quality: 8.9
tags: [nucleus_def, n07, orchestrator, composable]
tldr: "N07 is the orchestrator: dispatches nuclei, assembles crews, consolidates waves. Claude Opus 1M context."
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
related:
  - p02_nd_n03.md
  - kc_nucleus_def
  - p02_nd_n01.md
  - p02_nd_n06.md
  - p02_nd_n05.md
  - p02_nd_n02.md
  - p02_nd_n04.md
  - p08_ac_admin_orchestrator
  - p12_wf_admin_orchestration
  - p12_sc_admin_orchestrator
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus ID | N07 |
| Role | orchestrator |
| Sin Lens | Orchestrating Sloth |
| CLI Binding | claude |
| Model Tier | opus |
| Model | claude-opus-4-6 |
| Context | 1M tokens |
| Boot Script | `boot/cex.ps1` |
| Agent Card | `N07_admin/agent_card_n07.md` |

## Pillars Owned

| Pillar | Domain | Sample Kinds |
|--------|--------|--------------|
| P12 | orchestration | workflow, dispatch_rule, schedule, crew_template (shared with N06 for team_charter) |

## Crew Templates Exposed

| Template | Role in Crew | Inputs | Outputs |
|----------|--------------|--------|---------|
| grid_of_crews | orchestrator | N charters | parallel crew execution |
| mission_plan | planner | user goal | wave schedule + handoffs |

## Domain Agents

| Agent | Purpose | Path |
|-------|---------|------|
| agent_dispatcher | Spawn + monitor nuclei | `N07_admin/P02_model/` |
| agent_consolidator | Post-wave verify + archive | `N07_admin/P02_model/` |

## Boot Contract

- Boot file: `boot/cex.ps1` (user-facing entry)
- Task source: N/A -- N07 is always interactive
- Signal: N07 WRITES signals for its children; emits completion via commits

## Composability

| Direction | Nucleus | What Flows |
|-----------|---------|-----------|
| outbound | all | handoffs + crew charters + grid schedules |
| inbound | all | completion signals + quality scores |
| outbound | user | reports, GDP prompts, final artifacts |

## N07 Unique Powers

- Dispatches grids, solos, and crews (the only nucleus that dispatches)
- Never builds directly -- always routes
- Owns the `grid of crews` composition (WAVE8 highest-leverage pattern)
- Enforces GDP before autonomous waves

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_nd_n03.md]] | sibling | 0.44 |
| [[kc_nucleus_def]] | upstream | 0.43 |
| [[p02_nd_n01.md]] | sibling | 0.40 |
| [[p02_nd_n06.md]] | sibling | 0.40 |
| [[p02_nd_n05.md]] | sibling | 0.36 |
| [[p02_nd_n02.md]] | sibling | 0.35 |
| [[p02_nd_n04.md]] | sibling | 0.35 |
| [[p08_ac_admin_orchestrator]] | downstream | 0.34 |
| [[p12_wf_admin_orchestration]] | downstream | 0.34 |
| [[p12_sc_admin_orchestrator]] | downstream | 0.31 |
