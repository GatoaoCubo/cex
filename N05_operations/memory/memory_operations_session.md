---
id: p10_memory_operations_session
kind: runtime_state
pillar: P10
title: Operations Session Memory
version: 1.0.0
created: 2026-04-07
updated: 2026-04-07
author: n05_operations
domain: operations-memory
quality: 8.9
tags: [runtime_state, memory, operations, N05, session, context]
tldr: "Persistent session memory for N05 operations tracking corrections, preferences, conventions, and accumulated context across sessions."
density_score: 0.95
---

# Operations Session Memory

## Purpose

This memory artifact persists operational knowledge across N05 sessions.
It tracks corrections (mistakes not to repeat), preferences (user-chosen
approaches), conventions (established patterns), and accumulated context
(facts learned during operations).

## Memory Types

### Corrections (mistakes to avoid)

| date | correction | source | confidence |
|------|-----------|--------|------------|
| 2026-04-07 | YAML frontmatter with unquoted colons in tldr fails pre-commit validation | pre-commit hook | 1.0 |
| 2026-04-07 | Files from other nuclei get staged when using `git add -A` — use `git add N05_operations/` for surgical commits | git staging | 1.0 |

### Preferences (user-decided approaches)

| date | preference | decision_ref |
|------|-----------|--------------|
| 2026-04-07 | Sanitize scope is all_tools (not selective) | decision_manifest.yaml |
| 2026-04-07 | Encoding enforcement is utf8_strict | decision_manifest.yaml |
| 2026-04-07 | Hooks target is pre_commit | decision_manifest.yaml |
| 2026-04-07 | Auto-publish mode (speed over manual approval) | decision_manifest.yaml |

### Conventions (established patterns)

| convention | example | scope |
|------------|---------|-------|
| Agent frontmatter includes `llm_function: BECOME` | agent_operations.md | all agents |
| System prompts include sin lens block at top | system_prompt_operations.md | all prompts |
| Quality gates have hard gates (blocking) + soft gates (weighted) | quality_gate_operations.md | all gates |
| Output artifacts use `output_` prefix | output_health_endpoint.md | all outputs |
| Schemas define YAML validation rules | env_contract_schema.md | all schemas |
| Commit messages follow `[N05] description` format | git history | all commits |

### Context (accumulated facts)

| date | fact | confidence | decay_days |
|------|------|------------|------------|
| 2026-04-07 | N05 agent card identifies 8 gaps to close | 1.0 | 365 |
| 2026-04-07 | N05 owns 28 kinds across 8 pillars | 1.0 | 365 |
| 2026-04-07 | Pre-commit hook runs cex_hooks.py on staged .md files | 1.0 | 365 |
| 2026-04-07 | Railway topology has 4 services: api, frontend, dashboard, gateway | 1.0 | 365 |
| 2026-04-07 | 63 environment variables required for full deploy | 1.0 | 365 |

## Session State

| field | value |
|-------|-------|
| last_active | 2026-04-07T19:56:00-03:00 |
| task_source | n05_task.md handoff from N07 |
| artifacts_created | 16 (this session) |
| commits_made | 4 (this session) |
| gates_passed | 14/14 pre-commit checks |
| gates_failed | 1 (tldr colon — fixed) |

## Boundary

Estado mental variavel acumulado em runtime. NAO eh mental_model P02 (identidade fixa do agente, imutavel) nem session_state (efemero, snapshot).


## 8F Pipeline Function

Primary function: **INJECT**
