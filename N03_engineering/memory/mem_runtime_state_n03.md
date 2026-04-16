---
id: mem_runtime_state_n03
kind: runtime_state
pillar: P10
nucleus: N03
title: "N03 Runtime State"
version: "1.0.0"
created: "2026-04-16"
updated: "2026-04-16"
author: n03_engineering
domain: engineering operational memory
quality: null
tags: [runtime_state, p10, n03, routing, decisions, inventive_pride]
---
<!-- 8F: F1=runtime_state/P10 F2=runtime-state-builder F3=nucleus_def_n03+kc_runtime_state+P10_schema F4=runtime state for routing and active build defaults
     F5=Get-Content+rg+apply_patch+cex_compile.py F6=bytes:5385 F7=self-check:frontmatter+8f+properties+80l+ascii F8=N03_engineering/memory/mem_runtime_state_n03.md -->

# N03 Runtime State

## Properties

| Property | Value |
|----------|-------|
| Kind | `runtime_state` |
| Pillar | `P10` |
| Nucleus | `N03` |
| Lens | `Inventive Pride` |
| Persistence scope | cross-session mutable state |
| Main payload | routing choices, active defaults, counters |
| Session noise policy | exclude ephemeral chatter |
| Reset rule | prune when state stops serving builds |
| Critical fields | queue, mode, degraded_flags, preferred_defaults |
| Identity boundary | never store immutable persona here |

## Purpose

Runtime state holds what N03 is currently doing and how it is choosing.
It is mutable and practical.
Inventive Pride means the state should be explicit enough to support disciplined work, but lean enough to avoid self-imposed fog.

## Core Fields

| Field | Purpose |
|------|---------|
| `active_mission` | current mission identifier |
| `build_queue` | pending artifacts or phases |
| `preferred_defaults` | chosen retrieval and build defaults |
| `routing_decisions` | branch choices made during execution |
| `degraded_flags` | service outages or fallback modes |
| `retry_counters` | bounded operational retries |
| `last_success` | most recent stable milestone |

## What Belongs Here

- current artifact batch focus
- chosen default chunk size
- chosen retrieval mode
- temporary degraded infrastructure flags
- active priorities for the present execution wave
- unresolved blockers that affect the next step

## What Does Not Belong Here

- fixed N03 identity
- broad architectural essays
- full session transcript
- permanent lessons from completed failures
- long-lived entity facts better stored elsewhere

## Inventive Pride Lens

A lazy runtime state becomes a junk drawer.
A proud runtime state behaves like a calibrated instrument panel.
It shows only what the next decision needs.
Anything beyond that is vanity accumulation.

## Routing Use

| Situation | State response |
|----------|----------------|
| user asks for build | route into 8F with current defaults |
| handoff mandates no commit | set `commit_policy=disabled` |
| compile unavailable | mark degraded and preserve output paths |
| ambiguous kind | store resolution confidence and pending clarification |
| batch mission | keep ordered queue with completion marks |

## Degraded Mode Fields

When systems are impaired, state should record:
- `vector_search_degraded`
- `compile_errors_present`
- `missing_rule_source`
- `fallback_toolchain_active`
- `manual_validation_required`

These flags prevent silent optimism.
N03 should know when it is operating below ideal conditions.

## Queue Discipline

1. keep only pending or blocked items in the active queue
2. remove completed items after milestone capture
3. avoid more than one source of truth for current work
4. order queue by dependency, not sentiment
5. preserve the next concrete action at the top

## Counters

Useful counters include:
- retry count for compile
- artifacts completed in current wave
- validation pass count
- fallback invocations
- unresolved blocker count

Counters should explain operational state, not create ceremony.

## Failure Modes

| Failure | Damage | Fix |
|--------|--------|-----|
| identity drift | runtime state mutates persona | move identity to stable artifacts |
| unbounded queue | context pollution | drain after completion |
| missing degraded flags | false confidence | write explicit impairment markers |
| stale defaults | repeated wrong decisions | refresh from latest chosen config |
| session transcript leakage | byte waste | summarize elsewhere |

## Update Triggers

- mission changes
- default retrieval parameters change
- infrastructure degrades or recovers
- compile step fails or resumes
- a batch wave advances to a new phase

## Synchronization Rules

When runtime state updates:
- compare preferred defaults with current knowledge artifacts
- refresh summaries if the new state will matter next session
- ensure entity memory is not being used as state storage
- clear obsolete flags once recovery is verified

## Quality Standard

- actionable in under one screenful
- explicit about degraded conditions
- aligned with current mission and queue
- free of immutable identity claims
- pruned aggressively after milestones

## Recommended N03 Defaults

- commit policy should be writable as a runtime flag
- compile requirement should stay visible until complete
- retrieval mode should show `hybrid` unless degraded
- preferred backend should show `pgvector` unless fallback active
- top-level queue should map to current wave artifacts

## Final Position

N03 runtime state should be a compact control surface for routing and active defaults, not a memory landfill.
When the state is sharp, the build stays sharp.
