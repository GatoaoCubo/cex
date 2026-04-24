---
id: p11_gr_stella_dispatch
kind: guardrail
8f: F7_govern
pillar: P11
title: "Guardrail: orchestrator Dispatch Boundaries"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.0
tags: [guardrail, stella, dispatch, safety, orchestration]
tldr: "orchestrator is orchestrator-only: never executes tasks directly, never uses tsp_manager.py, never spawns >3 agent_groups, never writes handoffs to .claude/temp/"
max_bytes: 512
density_score: 0.90
source: organization-core/.claude/rules/orchestrator_RULES.md (NUNCA section)
linked_artifacts:
  workflow: p12_wf_stella_dispatch
  law: p08_law_shokunin
related:
  - p12_wf_stella_dispatch
  - p09_rr_agent_group_spawn
  - p03_sp_admin_orchestrator
  - p08_cmap_organization_core
  - p02_agent_admin_orchestrator
  - bld_examples_diagram
  - p03_pt_agent_group_orchestrator
  - bld_knowledge_card_agent_card
  - p08_ac_orchestrator
  - p01_kc_orchestration_best_practices
---

# Guardrail: orchestrator Dispatch Boundaries

## Hard Prohibitions

```yaml
stella_never:
  - execute_directly: "orchestrator routes tasks — never executes code, research, or builds"
  - tsp_manager: "tsp_manager.py is deprecated — invisible window, cannot kill claude.exe"
  - temp_handoffs: ".claude/temp/ is gitignored — commits will fail silently"
  - exceed_3_agent_groups: "4+ concurrent agent_groups = BSOD risk"
  - tasks_over_30min_in_3_sats: "RAM limit — use sequential waves instead"
```

## Decision Gate

```
User request received:
  → Is this a task orchestrator should execute directly? NO → ALWAYS dispatch
  → Is this research? → research_agent
  → Is this building/coding? → builder_agent
  → Is this knowledge/docs? → knowledge_agent
  → Is this deploy/test? → operations_agent
  → Is this marketing? → marketing_agent
  → Is this monetization? → commercial_agent
```

## Spawn Validation

```yaml
before_spawn:
  - count_active_agent_groups: "Must be < 3 before spawning"
  - check_handoff_location: ".claude/handoffs/ (NOT .claude/temp/)"
  - verify_inline_prompt_length: "< 200 chars"
  - confirm_with_user: "Show agent_group table + Confirma? (sim/ajustar)"
```

## Violation Consequences

| Violation | Consequence |
|-----------|-------------|
| orchestrator executes directly | Bypasses agent_group expertise, lower quality |
| tsp_manager.py | Invisible process, agent_group hangs |
| Handoff in temp/ | Silent commit failure, lost work |
| 4+ agent_groups | BSOD (hardware confirmed limit) |
| No user confirmation | User loses control of dispatch scope |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_stella_dispatch]] | downstream | 0.31 |
| [[p09_rr_agent_group_spawn]] | upstream | 0.28 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.27 |
| [[p08_cmap_organization_core]] | upstream | 0.27 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.27 |
| [[bld_examples_diagram]] | related | 0.26 |
| [[p03_pt_agent_group_orchestrator]] | upstream | 0.26 |
| [[bld_knowledge_card_agent_card]] | upstream | 0.24 |
| [[p08_ac_orchestrator]] | upstream | 0.23 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.22 |
