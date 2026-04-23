---
id: p12_dag_admin_orchestration
title: "Dag Admin"
kind: dag
pillar: P12
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
pipeline: admin_orchestration
nodes:
  - id: receive_intent
    label: "Receive human intent or mission plan"
    agent_group: orchestrator
  - id: classify_domain
    label: "Classify intent by domain keywords"
    agent_group: orchestrator
  - id: write_handoff
    label: "Write structured handoff to .cex/runtime/handoffs/"
    agent_group: orchestrator
  - id: dispatch_builder
    label: "Dispatch builder via bash _spawn/dispatch.sh"
    agent_group: orchestrator
  - id: monitor_signals
    label: "Monitor .cex/runtime/signals/ for completion or error"
    agent_group: orchestrator
  - id: validate_quality
    label: "Validate builder output quality >= 8.0"
    agent_group: orchestrator
  - id: accept_or_reject
    label: "Accept deliverable or return with feedback"
    agent_group: orchestrator
edges:
  - from: receive_intent
    to: classify_domain
  - from: classify_domain
    to: write_handoff
  - from: write_handoff
    to: dispatch_builder
  - from: dispatch_builder
    to: monitor_signals
  - from: monitor_signals
    to: validate_quality
  - from: validate_quality
    to: accept_or_reject
domain: orchestration
quality: 9.1
tags: [dag, orchestration, N07, dispatch, pipeline]
tldr: "7-node DAG for N07 orchestration — receive, classify, handoff, dispatch, monitor, validate, accept."
execution_order:
  - [receive_intent]
  - [classify_domain]
  - [write_handoff]
  - [dispatch_builder]
  - [monitor_signals]
  - [validate_quality]
  - [accept_or_reject]
critical_path: [receive_intent, classify_domain, write_handoff, dispatch_builder, monitor_signals, validate_quality, accept_or_reject]
node_count: 7
edge_count: 6
max_parallelism: 1
density_score: 0.89
related:
  - p12_wf_admin_orchestration
  - p12_wf_orchestration_pipeline
  - p02_agent_admin_orchestrator
  - p03_sp_admin_orchestrator
  - p01_kc_orchestration
  - p12_wf_create_orchestration_agent
  - p08_ac_admin_orchestrator
  - p12_dr_orchestration
  - workflow-builder
  - p08_pat_crew_dispatch
---

# DAG: N07 Orchestration Pipeline

## Nodes

| ID | Label | Agent | Type |
|----|-------|-------|------|
| receive_intent | Receive human intent or mission plan | orchestrator | input |
| classify_domain | Classify intent by domain keywords | orchestrator | decision |
| write_handoff | Write structured handoff file | orchestrator | action |
| dispatch_builder | Dispatch builder via spawn | orchestrator | action |
| monitor_signals | Monitor signals for completion/error | orchestrator | wait |
| validate_quality | Validate output quality >= 8.0 | orchestrator | gate |
| accept_or_reject | Accept deliverable or return with feedback | orchestrator | output |

## Edges

```text
receive_intent --> classify_domain --> write_handoff --> dispatch_builder
    --> monitor_signals --> validate_quality --> accept_or_reject
```

## Topological Order

1. `receive_intent` — parse human intent or read mission plan
2. `classify_domain` — match keywords to routing rules, select target nucleus
3. `write_handoff` — produce handoff.md with task, context, scope, commit, signal
4. `dispatch_builder` — execute `bash _spawn/dispatch.sh solo {nucleus} "task"`
5. `monitor_signals` — poll `.cex/runtime/signals/` for completion or error signal
6. `validate_quality` — check builder output quality score against 8.0 threshold
7. `accept_or_reject` — if quality >= 8.0: accept. Else: write feedback, re-dispatch

## Parallel Groups

Wave 0: [receive_intent]
Wave 1: [classify_domain]
Wave 2: [write_handoff]
Wave 3: [dispatch_builder]
Wave 4: [monitor_signals]
Wave 5: [validate_quality]
Wave 6: [accept_or_reject]

This DAG is strictly sequential — N07 orchestration is a pipeline, not a parallel graph.
Parallelism occurs at the builder level (grid dispatch), not at the orchestrator level.

## Critical Path

All 7 nodes are on the critical path (sequential pipeline):
`receive_intent` --> `classify_domain` --> `write_handoff` --> `dispatch_builder` --> `monitor_signals` --> `validate_quality` --> `accept_or_reject`

## Retry Loop

On quality rejection at `accept_or_reject`:
- Edge back to `write_handoff` with feedback context
- Max 2 retries before escalating to human
- Each retry preserves prior feedback for context

## References

- Dispatch rules: N07_admin/P12_orchestration/dispatch_rule_admin.md
- Workflow: N07_admin/P12_orchestration/workflow_admin.md

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p12_wf_admin_orchestration]] | related | 0.50 |
| [[p12_wf_orchestration_pipeline]] | related | 0.35 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.35 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.33 |
| [[p01_kc_orchestration]] | upstream | 0.33 |
| [[p12_wf_create_orchestration_agent]] | related | 0.33 |
| [[p08_ac_admin_orchestrator]] | upstream | 0.32 |
| [[p12_dr_orchestration]] | related | 0.31 |
| [[workflow-builder]] | related | 0.29 |
| [[p08_pat_crew_dispatch]] | upstream | 0.29 |
