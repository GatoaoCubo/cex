---
id: kc_revision_loop_policy
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "KC: revision_loop_policy"
version: 1.0.0
quality: 9.0
tags: [knowledge_card, revision_loop_policy, p11, hermes, escalation, iteration]
density_score: 0.92
upstream_source: "1ilkhamov/opencode-hermes-multiagent"
related:
  - bld_collaboration_quality_gate
  - quality-gate-builder
  - p03_sp_quality_gate_builder
  - p03_ins_quality_gate
  - bugloop-builder
  - bld_memory_quality_gate
  - p08_ac_verification
  - n04_qg_knowledge
  - p03_sp_bugloop_builder
  - bld_knowledge_card_quality_gate
---

## What is revision_loop_policy?

A `revision_loop_policy` is a declarative artifact (P11, GOVERN) that specifies the maximum
number of iterative revision cycles permitted on an artifact before the pipeline escalates
to a human reviewer or a senior nucleus.

Originating from the OpenCode-Hermes multiagent spec: "Revision Loops: Up to 3 iterations
permitted before escalation. Conflict Resolution: Priority-based (security > quality > implementation)."

## Core Fields

| Field | Type | Default | Description |
|-------|------|---------|-------------|
| `max_iterations` | int | 3 | Maximum revision cycles before escalation |
| `iteration_on_quality_floor` | float | 8.5 | Score below which a new revision triggers |
| `priority_order` | array | [security, quality, implementation] | Gate conflict resolution order |
| `escalation_target` | enum | user | Where to route after exhausting iterations |
| `escalation_message_template` | string | required | Message emitted on escalation |
| `per_scenario_overrides` | map | {} | Kind- or scenario-specific iteration budgets |

## Behavioral Contract

```
FOR each revision attempt:
  evaluate all quality gates
  IF all gates pass OR score >= iteration_on_quality_floor:
    ACCEPT artifact, stop loop
  ELSE IF attempt_count < max_iterations:
    increment attempt_count
    regenerate artifact with gate failure context injected
  ELSE:
    emit escalation_message_template
    route to escalation_target
```

Priority resolution when gates conflict:
1. security gates -- always evaluated first; failure blocks regardless of other scores
2. quality gates -- evaluated second; determines iteration threshold
3. implementation gates -- evaluated last; can be deferred to post-escalation

## Boundary Analysis

| Kind | What it does | Distinction |
|------|-------------|-------------|
| `revision_loop_policy` | Governs N iterative content-quality cycles | THIS kind |
| `quality_gate` (P11) | Single pass/fail check at one pipeline stage | One gate; revision_loop_policy orchestrates N of them |
| `retry_policy` (P09) | Transient-failure retries (network, timeout, rate-limit) | Infrastructure retries, not content quality |
| `regression_check` (P11) | Compares artifact output against a known baseline | Diff-based; not iterative improvement |
| `bugloop` (P11) | Auto-detect > fix > verify cycle for code bugs | Narrower domain (code bugs vs artifact quality) |

## HERMES Origin

The `revision_loop_policy` was assimilated from the opencode-hermes-multiagent spec (1ilkhamov)
where it appears as a first-class primitive alongside `pipeline_template`. The two kinds are
designed to work together: `pipeline_template` encodes the stage sequence and references a
`revision_loop_policy` for the iteration budget at each quality gate.

## Usage Patterns

### Embedded in pipeline_template
```yaml
revision_loop:
  policy_ref: rlp_standard
  max_iterations: 3
  escalation_target: user
```

### Standalone policy for 8F F7 GOVERN
```yaml
---
id: rlp_standard
kind: revision_loop_policy
max_iterations: 3
iteration_on_quality_floor: 8.5
priority_order: [security, quality, implementation]
escalation_target: user
escalation_message_template: "Reached 3 revisions without passing: {{failing_gates}}"
---
```

### Security-critical override
```yaml
per_scenario_overrides:
  security_critical: 5
  documentation: 2
  standard: 3
```

## Builder
`archetypes/builders/revision-loop-policy-builder/`

## Related Kinds
- `quality_gate` (P11) -- the gate evaluated on each iteration
- `pipeline_template` (P12) -- embeds revision_loop_policy as `revision_loop` block
- `bugloop` (P11) -- auto-correction loop for code bugs
- `retry_policy` (P09) -- transient-failure retries (different domain)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_quality_gate]] | downstream | 0.28 |
| [[quality-gate-builder]] | downstream | 0.28 |
| [[p03_sp_quality_gate_builder]] | downstream | 0.24 |
| [[p03_ins_quality_gate]] | downstream | 0.23 |
| [[bugloop-builder]] | downstream | 0.23 |
| [[bld_memory_quality_gate]] | downstream | 0.21 |
| [[p08_ac_verification]] | downstream | 0.21 |
| [[n04_qg_knowledge]] | related | 0.21 |
| [[p03_sp_bugloop_builder]] | downstream | 0.20 |
| [[bld_knowledge_card_quality_gate]] | sibling | 0.20 |
