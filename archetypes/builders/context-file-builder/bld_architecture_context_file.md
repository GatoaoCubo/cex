---
kind: architecture
id: bld_architecture_context_file
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of context_file -- inventory, dependencies, and architectural position
quality: 8.8
title: "Architecture: context_file in CEX"
version: "1.0.0"
author: n03_builder
tags: [context_file, builder, architecture, P08, hermes_origin]
tldr: "Component inventory and dependency graph for context_file: scope stack, injection pipeline, inheritance chain."
domain: "workspace instruction auto-injection"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.91
related:
  - bld_architecture_system_prompt
  - bld_architecture_legal_vertical
  - bld_architecture_healthcare_vertical
  - bld_architecture_fintech_vertical
  - p01_kc_session_state
  - p08_pat_nucleus_fractal
  - bld_architecture_press_release
  - p01_kc_session_backend
  - bld_collaboration_memory_scope
  - p03_sp_session_state_builder
---

# Architecture: context_file in the CEX

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | 13 required metadata fields (id, scope, injection_point, etc.) | context-file-builder | active |
| scope_classifier | Determines coverage domain: workspace/nucleus/session/global | author | active |
| injection_point | When the file enters context: session_start/every_turn/f3_inject | harness / F3 | active |
| inheritance_chain | List of parent context_file IDs this artifact inherits from | author | active |
| priority_ordering | Integer 0-N: determines which rules win on conflict in same scope | author | active |
| applies_to_nuclei | Which nuclei receive this injection: [all] or explicit IDs | author | active |
| instruction_body | Static behavioral rules, standing constraints, ambient conventions | author | active |
| byte_budget | max_bytes enforced by harness before injection; oversize silently truncated | harness | active |

## Dependency Graph
```
knowledge_card  --facts-->  context_file  --injected_by-->  agent_session
system_prompt   --identity--> (BEFORE context_file in load order)
context_file    --loaded_at--> F3_INJECT
context_file    --inherits-->  parent_context_file
memory_scope    --lifespan-->  session context_file (expires with session)
```

| From | To | Type | Data |
|------|----|------|------|
| system_prompt (P03) | agent | loads first | identity; context_file loads after in F3 |
| context_file | agent_session | injected into | standing instructions per scope |
| parent_context_file | context_file | inheritance | child extends parent; overrides on conflict |
| memory_scope (P10) | context_file (session) | lifespan control | session scope expires when memory_scope closes |
| harness / 8F F3 | context_file | triggers injection | based on injection_point and applies_to_nuclei |
| knowledge_card (P01) | context_file | sibling injection | facts and instructions co-injected at F3 |

## Scope Stack (load order)
```
global_context.md       (priority: 0)  -- loads first, most authoritative
  |
  workspace_context.md  (priority: 1)  -- overrides global where specified
    |
    nucleus_context.md  (priority: 2)  -- overrides workspace for that nucleus
      |
      session_context.md (priority: 3) -- overrides nucleus; expires on session close
```
Rule: lower priority number = loads earlier; higher number wins on rule conflict within same scope.

## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity (F2 BECOME) | system_prompt | Who the agent is -- BEFORE context_file |
| Instruction (F3 INJECT) | context_file, knowledge_card | Standing rules + domain facts |
| Task (F3/F4) | action_prompt, instruction | What to do in this turn |
| Execution (F5-F6) | tools, builders | How to produce |
| Governance (F7) | quality_gate | Did the output comply with context_file rules? |

## Boundary Table
| context_file IS | context_file IS NOT |
|-----------------|---------------------|
| Static instruction file auto-injected by harness | `system_prompt` -- agent identity, loaded at BECOME, not INJECT |
| Project-scoped; applies to many turns / sessions | `knowledge_card` -- facts and domain knowledge; not instructions |
| Scope-aware: workspace/nucleus/session/global | `prompt_template` -- requires variable instantiation |
| Inheritance chain with priority resolution | `instruction` -- task-scoped procedural recipe |
| HERMES CLAUDE.md / AGENTS.md pattern | `action_prompt` -- single user-driven task execution |

## Integration Points
| System | How context_file participates |
|--------|-------------------------------|
| 8F pipeline | Loaded at F3 INJECT; governs F6 PRODUCE compliance |
| Agent boot | Workspace and global scope files loaded at session_start |
| Nucleus dispatch | Nucleus scope file injected when that nucleus is activated |
| Memory expiry | Session scope auto-expires when session closes |
| Quality gate | F7 GOVERN checks: did output respect the context_file's rules? |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_system_prompt]] | sibling | 0.32 |
| [[bld_architecture_legal_vertical]] | sibling | 0.25 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.25 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.25 |
| [[p01_kc_session_state]] | downstream | 0.24 |
| [[p08_pat_nucleus_fractal]] | related | 0.23 |
| [[bld_architecture_press_release]] | sibling | 0.22 |
| [[p01_kc_session_backend]] | downstream | 0.22 |
| [[bld_collaboration_memory_scope]] | downstream | 0.22 |
| [[p03_sp_session_state_builder]] | upstream | 0.22 |
