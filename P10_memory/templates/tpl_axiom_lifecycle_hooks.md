---
# TEMPLATE: Axiom — Lifecycle Hooks (P10 Memory)
# Valide contra P10_memory/_schema.yaml (types.axiom)
# Max 3072 bytes

id: p10_ax_{{RULE_SLUG}}
kind: axiom
pillar: P10
title: "Axiom: Memory Lifecycle Hooks"
quality: {{QUALITY_8_TO_10}}
---

# Axiom: Memory Lifecycle Hooks

## Rule
Memory capture follows a 5-hook lifecycle. Each hook has a single responsibility and communicates with the memory daemon via HTTP. Hooks are thin clients; all persistence logic lives in the daemon.

## Hook Chain

| # | Hook | Responsibility | Timeout | Fires |
|---|------|---------------|---------|-------|
| 1 | Setup | Gate all other hooks; verify daemon health | 300s | Once per session init |
| 2 | SessionStart | Inject prior context into conversation | 60s | Once after Setup succeeds |
| 3 | UserPromptSubmit | Initialize session record if first prompt | 30s | Every user message |
| 4 | PostToolUse | Capture observations from tool results | 120s | Every tool completion |
| 5 | Stop | Trigger compression + summary generation | 120s | Once at session end |

## Invariants
- **Single responsibility**: each hook does ONE thing
- **HTTP to daemon**: hooks never access DB directly
- **Fire-and-forget on error**: non-critical hooks exit 0 even on failure
- **Setup gates everything**: if Setup fails, all subsequent hooks are skipped

## Exit Code Contract

| Code | Meaning | Effect |
|------|---------|--------|
| 0 | Success / graceful skip | Continue normally |
| 1 | Non-blocking error | Log warning, continue |
| 2 | Blocking error | Halt hook chain |

## Rationale
- Why: Memory capture must be reliable, ordered, and non-intrusive to the user session
- Protects: Session continuity — a failed hook must never crash the conversation

## Examples
- Correct: PostToolUse sends observation via HTTP POST to daemon, daemon persists async, hook exits 0
- Incorrect: PostToolUse writes directly to SQLite file (bypasses daemon, causes lock contention)
