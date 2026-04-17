---
id: n00_runtime_state_manifest
kind: knowledge_card
pillar: P10
nucleus: n00
title: "Runtime State -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, runtime_state, p10, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P10 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A runtime_state captures the variable mental state of a nucleus during a session -- the routing decisions, in-progress tasks, active signals, and temporary context that changes within a single execution window. Unlike persistent memory, runtime_state is ephemeral by design but must be snapshotted for crash recovery and handoff continuity.

## Pillar
P10 -- memory

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `runtime_state` |
| pillar | string | yes | Always `P10` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus | string | yes | Nucleus that owns this state |
| session_id | string | yes | Session identifier |
| current_task | string | yes | Description of active task |
| routing_decisions | object | no | Active routing choices made this session |
| pending_signals | array | no | Signals waiting to be sent or processed |
| wave | integer | no | Current wave number in multi-wave mission |
| snapshot_at | datetime | yes | When this state was last snapshotted |

## When to use
- When a nucleus needs to persist mid-session state before a handoff
- When recovering from a crash or interrupted session
- When N07 needs to inspect a nucleus's current operational state

## Builder
`archetypes/builders/runtime_state-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind runtime_state --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rs_n03_wave2_session
kind: runtime_state
pillar: P10
nucleus: n03
title: "Example Runtime State"
version: 1.0
quality: null
---
# N03 Runtime State -- Wave 2
current_task: "building agent_card for N05"
wave: 2
pending_signals: [signal_complete_n03]
snapshot_at: "2026-04-17T14:30:00Z"
```

## Related kinds
- `session_state` (P10) -- session-level snapshot that runtime_state feeds into
- `handoff` (P12) -- runtime_state is embedded in handoffs for context transfer
- `signal` (P12) -- pending signals tracked in runtime_state
