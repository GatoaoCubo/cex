---
id: p11_gr_stella_dispatch
kind: guardrail
pillar: P11
title: "Guardrail: STELLA Dispatch Boundaries"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: PYTHA
quality: 9.0
tags: [guardrail, stella, dispatch, safety, orchestration]
tldr: "STELLA is orchestrator-only: never executes tasks directly, never uses tsp_manager.py, never spawns >3 satellites, never writes handoffs to .claude/temp/"
max_bytes: 512
density_score: 0.90
source: codexa-core/.claude/rules/STELLA_RULES.md (NUNCA section)
linked_artifacts:
  workflow: p12_wf_stella_dispatch
  law: p08_law_shokunin
---

# Guardrail: STELLA Dispatch Boundaries

## Hard Prohibitions

```yaml
stella_never:
  - execute_directly: "STELLA routes tasks — never executes code, research, or builds"
  - tsp_manager: "tsp_manager.py is deprecated — invisible window, cannot kill claude.exe"
  - temp_handoffs: ".claude/temp/ is gitignored — commits will fail silently"
  - exceed_3_satellites: "4+ concurrent satellites = BSOD risk"
  - tasks_over_30min_in_3_sats: "RAM limit — use sequential waves instead"
```

## Decision Gate

```
User request received:
  → Is this a task STELLA should execute directly? NO → ALWAYS dispatch
  → Is this research? → SHAKA
  → Is this building/coding? → EDISON
  → Is this knowledge/docs? → PYTHA
  → Is this deploy/test? → ATLAS
  → Is this marketing? → LILY
  → Is this monetization? → YORK
```

## Spawn Validation

```yaml
before_spawn:
  - count_active_satellites: "Must be < 3 before spawning"
  - check_handoff_location: ".claude/handoffs/ (NOT .claude/temp/)"
  - verify_inline_prompt_length: "< 200 chars"
  - confirm_with_user: "Show satellite table + Confirma? (sim/ajustar)"
```

## Violation Consequences

| Violation | Consequence |
|-----------|-------------|
| STELLA executes directly | Bypasses satellite expertise, lower quality |
| tsp_manager.py | Invisible process, satellite hangs |
| Handoff in temp/ | Silent commit failure, lost work |
| 4+ satellites | BSOD (hardware confirmed limit) |
| No user confirmation | User loses control of dispatch scope |
