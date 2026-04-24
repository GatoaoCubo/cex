---
id: mem_runtime_state_n01
kind: runtime_state
8f: F8_collaborate
pillar: P10
nucleus: N01
title: "N01 Runtime State"
version: "1.0.0"
quality: 9.1
tags: [runtime_state, n01, p10, analytical_envy, routing]
density_score: 0.99
related:
  - bld_memory_runtime_state
  - runtime-state-builder
  - p01_kc_runtime_state
  - bld_knowledge_card_runtime_state
  - p11_qg_runtime_state
  - bld_collaboration_session_state
  - bld_collaboration_runtime_state
  - bld_architecture_runtime_state
  - bld_memory_session_state
  - p03_sp_session_state_builder
---
<!-- 8F: F1=runtime_state/P10 F2=kc_runtime_state+tpl_runtime_state F3=nucleus_def_n01+kc_runtime_state+ex_runtime_state_conversation+workflow_intelligence F4=session-variable state for research execution
     F5=rg+Get-Content+apply_patch F6=target dense markdown artifact F7=self-check properties+8F+ascii+80lines F8=N01_intelligence/P10_memory/mem_runtime_state_n01.md -->

# N01 Runtime State

## Purpose
N01 runtime state stores the mutable decisions of the current research execution path.
Analytical Envy means the state must capture how the nucleus is currently choosing to compare, verify, route, and stop.
Identity stays elsewhere.
Only the live analytical posture belongs here.

## Properties

| Property | Value |
|----------|-------|
| Kind | `runtime_state` |
| Pillar | `P10` |
| Nucleus | `N01` |
| Lens | `Analytical Envy` |
| Scope | cross-session mutable research state |
| Main fields | routing, counters, open probes, conflict flags |
| Update cadence | per major task transition |
| Persistence goal | resume without losing analytical intent |
| Anti-goal | storing fixed identity or long raw history |
| Main risk | bloated state that obscures current priorities |

## State Thesis
Runtime state should explain what N01 is doing right now.
That usually means:
- what question is active
- which entities and axes are in play
- what source strategy is selected
- which conflicts remain unresolved
- what the next action is

## Core State Fields

| Field | Meaning |
|-------|---------|
| active_question | current research question |
| active_entities | competitors, products, or markets under analysis |
| active_axes | pricing, features, trust, benchmarks, distribution |
| retrieval_mode | compare, verify, scan, gap_find |
| source_plan | official-first, triangulate, conflict-hunt |
| counters | retries, source_count, unresolved_count |
| open_probes | pending verification actions |
| escalation_flags | signals that the task needs caution or more evidence |

## Example Shape
```yaml
status: running
active_question: "Which competitor has the strongest public pricing transparency?"
active_entities: [OpenAI, Anthropic, Cohere]
active_axes: [pricing, transparency]
retrieval_mode: compare
source_plan: official_first_then_triangulate
counters: {sources_reviewed: 12, unresolved_conflicts: 2}
```

## Update Rules
1. Change `retrieval_mode` only when the task objective changes.
2. Increment counters for real analytical events, not every message.
3. Add open probes when evidence gaps are concrete and actionable.
4. Clear resolved conflicts immediately.
5. Archive completed probes instead of letting them pile up.

## Routing Signals

| Signal | Runtime effect |
|--------|----------------|
| strong official source found | reduce search breadth, increase verification depth |
| contradictory tier_1 sources | escalate conflict handling |
| many low-quality hits | tighten filters and source plan |
| missing region qualifier | add geography probe |
| repeated alias confusion | trigger entity normalization |

## What Should Persist
- current analytical mode
- unresolved evidence conflicts
- active comparison axes
- next verification actions
- counters that affect stopping rules

## What Should Not Persist
- stable N01 identity
- full transcripts
- exhaustive source excerpts
- final polished conclusions
- old completed task queues

## Anti-Patterns
- runtime state as narrative log
- no distinction between hypothesis and confirmed fact
- counters that never reset
- storing full citations instead of citation handles
- letting stale open probes survive after the question changed

## Resume Behavior
When N01 resumes, runtime state should support a fast read of:
- what is being compared
- what is still uncertain
- what retrieval posture is active
- what must be validated next

If it cannot answer those four questions, the state is too noisy.

## N01 Decision
N01 runtime state is the mutable skeleton of live analysis.
It preserves the current route through the evidence landscape so the nucleus can restart with pressure and discipline instead of rereading its own confusion.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_runtime_state]] | related | 0.40 |
| [[runtime-state-builder]] | related | 0.36 |
| [[p01_kc_runtime_state]] | related | 0.34 |
| [[bld_knowledge_card_runtime_state]] | upstream | 0.28 |
| [[p11_qg_runtime_state]] | downstream | 0.27 |
| [[bld_collaboration_session_state]] | related | 0.26 |
| [[bld_collaboration_runtime_state]] | related | 0.26 |
| [[bld_architecture_runtime_state]] | upstream | 0.25 |
| [[bld_memory_session_state]] | related | 0.24 |
| [[p03_sp_session_state_builder]] | upstream | 0.24 |
