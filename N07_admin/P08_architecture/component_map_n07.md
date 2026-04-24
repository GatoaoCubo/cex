---
id: component_map_n07
kind: component_map
8f: F4_reason
pillar: P08
nucleus: n07
title: "N07 Admin -- Component Map"
version: 1.0.0
created: 2026-04-18
author: n07_admin
domain: orchestration-admin-architecture
quality: 8.7
tags: [component_map, n07, admin, orchestration, dispatch, architecture]
tldr: "Internal component map of N07 Admin nucleus: dispatch engine, grid orchestration, signal bus, handoff protocol, consolidation pipeline, and inter-nucleus coordination flows."
density_score: null
related:
  - p01_kc_orchestration_best_practices
  - p03_sp_orchestration_nucleus
  - p08_ac_orchestrator
  - p12_wf_orchestration_pipeline
  - p12_wf_admin_orchestration
  - agent_card_n07
  - p02_agent_admin_orchestrator
  - dispatch
  - p08_ac_admin_orchestrator
  - p01_kc_orchestration
---

# N07 Admin -- Component Map

## System Overview

N07 is the orchestrator nucleus. It NEVER builds artifacts directly.
Its function is decomposing goals, dispatching nuclei, monitoring completion,
and consolidating results. Every user request is transmuted to a
{kind, pillar, nucleus, verb} tuple before any action occurs.

**Sin Lens**: Orchestrating Sloth -- laziness as leverage. Never builds when
a specialized nucleus can do it better. Delegates perfectly; monitors efficiently.

---

## Artifact Inventory

| Pillar | Count | Primary Kinds |
|--------|------:|---------------|
| P01 Knowledge | 8 | knowledge_card, context_doc |
| P02 Model | 5 | agent, boot_config, personality, nucleus_def |
| P03 Prompt | 3 | system_prompt, context_file |
| P04 Tools | 2 | skill, toolkit |
| P05 Output | 3 | analyst_briefing, report |
| P06 Schema | 5 | input_schema, validation_schema, interface |
| P07 Evals | 2 | audit_self_review, quality_gate |
| P08 Architecture | 3 | component_map, agent_card, nucleus_def |
| P09 Config | 6 | env_config, rate_limit_config, boot_config |
| P10 Memory | 13 | entity_memory, session_state, user_model, memory_summary |
| P11 Feedback | 4 | curation_nudge, revision_loop_policy |
| P12 Orchestration | 27 | workflow, dispatch_rule, handoff, schedule, pipeline_template |

**Total: 83 artifacts**

---

## Internal Components

### C1 -- Dispatch Engine
```
User intent
  |
  v
[C1.1] Intent transmutation   -- cex_intent_resolver.py -> {kind, pillar, nucleus, verb}
  |
  v
[C1.2] GDP gate               -- subjective? GDP -> manifest; technical? autonomous
  |
  v
[C1.3] Handoff writer         -- .cex/runtime/handoffs/{MISSION}_{nucleus}.md
  |
  v
[C1.4] dispatch.sh            -- bash _spawn/dispatch.sh solo|grid|swarm
  |
  v
[C1.5] PID tracker            -- .cex/runtime/pids/spawn_pids.txt (session-tagged)
```

### C2 -- Grid Orchestration
```
bash _spawn/dispatch.sh grid MISSION
  |
  v
spawn_grid.ps1                -- Start-Process per nucleus, tree-kill-safe
  |
  v
Up to 6 parallel nuclei
  |-- N01 intelligence (Sonnet)
  |-- N02 marketing   (Sonnet)
  |-- N03 engineering (Opus)
  |-- N04 knowledge   (Sonnet)
  |-- N05 operations  (Sonnet)
  |-- N06 commercial  (Sonnet)
  |
  v
N07 monitors via:
  git log --since "5 min ago"
  bash _spawn/dispatch.sh status
```

### C3 -- Signal Bus
```
nucleus completes
  |
  v
signal_writer.py -> .cex/runtime/signals/signal_{nucleus}_{ts}.json
  |
  v
N07 detects via git log / dispatch.sh status
  |
  v
Consolidation: cex_doctor.py + cex_compile.py + git commit
```

### C4 -- Autonomous Lifecycle (n07-autonomous-lifecycle.md)
```
DISPATCH wave
  -> WORK + MONITOR (interleaved, non-blocking)
    -> CHECK git log every ~2min
    -> If nucleus committed: note, continue
    -> If ALL wave nuclei committed: CONSOLIDATE + DISPATCH next wave
  -> CONSOLIDATE
    -> verify deliverables
    -> stop completed processes (taskkill /F /PID /T)
    -> cex_doctor.py
    -> git add + commit
  -> NEXT WAVE
```

### C5 -- Decision Manifest (GDP)
```
User decision points
  |
  v
skill_guided_decisions.md    -- 2-3 DPs at a time
  |
  v
.cex/runtime/decisions/decision_manifest.yaml (status: locked)
  |
  v
Included in ALL handoffs -> nuclei read, never re-ask
```

---

## Data Flows

| Source | -> | N07 | -> | Destination |
|--------|----|----|-----|-------------|
| User intent | -> | transmutation | -> | {kind, pillar, nucleus, verb} |
| GDP decisions | -> | decision manifest | -> | All nuclei via handoff |
| Nucleus signals | -> | completion detection | -> | consolidation |
| N07 consolidation | -> | git commit | -> | repository state |
| Flywheel audit | -> | 109 checks | -> | system health report |

---

## Key Tools

| Tool | Function |
|------|----------|
| `cex_intent_resolver.py` | Intent -> {kind, pillar, nucleus, verb} (0 tokens) |
| `_spawn/dispatch.sh` | Solo / grid / swarm / stop dispatch |
| `_spawn/spawn_grid.ps1` | PowerShell grid launcher (session-aware v4.0) |
| `signal_writer.py` | F8 completion signals |
| `cex_mission_runner.py` | Autonomous multi-wave orchestration |
| `cex_signal_watch.py` | Blocking signal poll (headless mode only) |
| `cex_gdp.py` | GDP manifest I/O + NeedsUserDecision gate |
| `cex_flywheel_audit.py` | 109-check system audit |
| `cex_kind_deps.py` | 289/293 kind dependency graph |
| `cex_kind_tool_map.py` | Tool-to-kind registry builder |

---

## Coverage Status (FULL_COVERAGE W1-W5)

| Coverage Tier | Before | After W1-W5 |
|---------------|--------|-------------|
| T1 depends_on | 62/293 (21%) | 289/293 (99%) |
| T2 component_map | 3/7 nuclei | 7/7 nuclei (this file) |
| T3 quality null | 81 artifacts | 0 (all scored) |
| T4 SDK domains | 11/14 pillars | in progress |
| T5 tool-to-kind | 47/293 | in progress |
| T6 flywheel | 109/109 (100%) | 109/109 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_orchestration_best_practices]] | upstream | 0.58 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.54 |
| [[p08_ac_orchestrator]] | related | 0.50 |
| [[p12_wf_orchestration_pipeline]] | downstream | 0.46 |
| [[p12_wf_admin_orchestration]] | downstream | 0.46 |
| [[agent_card_n07]] | downstream | 0.45 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.45 |
| [[dispatch]] | related | 0.45 |
| [[p08_ac_admin_orchestrator]] | related | 0.44 |
| [[p01_kc_orchestration]] | upstream | 0.44 |
