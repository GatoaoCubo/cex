---
id: sch_enum_def_n05
kind: enum_def
pillar: P06
nucleus: n05
title: Release Gate Enum
version: 1.0
quality: 9.0
tags: [schema, enum, operations, release, gating]
density_score: 1.0
related:
  - bld_schema_safety_policy
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - p10_ck_railway_deploy_checkpoint
  - bld_schema_sandbox_config
  - bld_schema_quickstart_guide
  - bld_schema_enum_def
  - bld_schema_smoke_eval
  - bld_schema_action_paradigm
---
<!-- 8F: F1 constrain=P06/enum_def F2 become=enum-def-builder F3 inject=nucleus_def_n05+n05-operations+kc_enum_def+P06_schema+N05 schema examples
     F4 reason=closed set for ops gating states with deny-first semantics F5 call=apply_patch F6 produce=6577 bytes
     F7 govern=self-check headings+tables+gating_wrath+ascii+80_lines F8 collaborate=N05_operations/P06_schema/sch_enum_def_n05.md -->

# Release Gate Enum

## Purpose

| Field | Value |
|---|---|
| Intent | Define the finite release gate states reused by N05 review, CI, deploy, and rollback flows. |
| Scope | Build pipelines, smoke checks, security scans, deploy approvals, post-deploy verification. |
| Gating Wrath Lens | Every value must force a clear operational branch. No vague "maybe" states. |
| Default Posture | Fail closed. If evidence is missing, the state is not promotable. |
| Reuse Rule | Referenced by schemas, validators, runtime rules, and incident reports. |

## Schema

| Property | Type | Required | Rule | Rationale |
|---|---|---|---|---|
| name | string | yes | `release_gate_state` | Stable reusable enum name. |
| value_type | string | yes | `string` | Predictable interop across YAML, JSON, and markdown references. |
| closed_set | boolean | yes | `true` | Prevents ad hoc status inflation during incidents. |
| default_value | string | yes | `blocked` | Unknown evidence must not pass a gate. |
| ordering | list[string] | yes | strict progression | Makes escalation and dashboard sorting deterministic. |
| descriptions | map[string,string] | yes | one sentence per value | Operators need exact meaning under stress. |
| allowed_in_manual_override | list[string] | yes | bounded subset | Human override can only relax within audited limits. |

## Values

| Value | Meaning | Allowed Transition In | Allowed Transition Out | Operational Action |
|---|---|---|---|---|
| blocked | Hard stop due to missing evidence, failed control, or unresolved risk. | initial, failed | review_pending | Hold deploy, open incident, require owner. |
| review_pending | Evidence exists but human or automated review is still incomplete. | blocked, initial | approved, blocked | Wait for gate owner sign-off. |
| approved | Required checks passed and deployment may proceed within the current window. | review_pending | deployed, blocked | Permit next stage only while evidence remains fresh. |
| deployed | Artifact was released and is now under active observation. | approved | observed, rolled_back | Start smoke, telemetry, and rollback timers. |
| observed | Post-deploy checks passed during the defined soak period. | deployed | retired, blocked | Mark stable release candidate. |
| rolled_back | Release was reversed because blast radius exceeded tolerance. | deployed, blocked | review_pending | Freeze promotion and require corrective review. |
| retired | State is closed and immutable for the release cycle. | observed | none | Preserve for audit only. |

## Transition Controls

| From | To | Gate Condition | Evidence Required | Reject Reason |
|---|---|---|---|---|
| blocked | review_pending | incident owner assigned | failing control documented | No owner, no movement. |
| review_pending | approved | all mandatory checks green | CI, security, smoke, change record | Partial green is still red. |
| approved | deployed | release window open | deployment ticket + artifact digest | Out-of-window deploys widen blast radius. |
| deployed | observed | soak timer complete | telemetry, logs, health endpoints | Silent services are not healthy services. |
| deployed | rolled_back | rollback trigger fired | alert, regression, or policy breach | Delay increases damage. |
| observed | retired | release review archived | immutable audit package | Missing archive blocks closure. |

## Rationale

| Design Choice | Why It Exists | Gating Wrath Effect |
|---|---|---|
| `blocked` as default | New work starts stopped until proof appears. | Removes wishful promotion. |
| `review_pending` separate from `approved` | Human review latency is real and must be explicit. | Prevents hidden bypasses. |
| `deployed` separate from `observed` | Shipping is not validation. | Forces soak discipline. |
| `rolled_back` as first-class value | Rollback must be visible, not inferred from logs. | Makes failure auditable and actionable. |
| No `warning` state | Ambiguous values create policy drift. | Every branch becomes enforceable. |
| Immutable `retired` state | Closed releases should not be rewritten retroactively. | Protects audit integrity. |

## Example

| Scenario | Input Evidence | Resolved Value | Why |
|---|---|---|---|
| Security scan failed on migration branch | CI pass, SAST fail | blocked | A critical control failed. |
| CI green, QA reviewing smoke logs | checks present, approval absent | review_pending | Evidence exists but gate is not closed. |
| All checks green, change window open | CI green, approval signed | approved | Promotion can proceed. |
| Release pushed to production 15 minutes ago | deploy done, soak active | deployed | Observation period has not finished. |
| No alerts after soak window | telemetry stable, checks green | observed | Release proved stable under monitoring. |
| Elevated error rate after deploy | health degraded, rollback executed | rolled_back | Blast radius required reversal. |

```yaml
name: release_gate_state
value_type: string
closed_set: true
default_value: blocked
ordering:
  - blocked
  - review_pending
  - approved
  - deployed
  - observed
  - rolled_back
  - retired
descriptions:
  blocked: Hard stop until evidence and owner exist.
  review_pending: Review underway but not complete.
  approved: Mandatory controls passed and window is open.
  deployed: Release is live and under observation.
  observed: Soak completed without critical regression.
  rolled_back: Release reversed to contain risk.
  retired: Release record closed for audit.
allowed_in_manual_override:
  - review_pending
  - approved
```

## Properties

| Property | Value |
|---|---|
| Kind | `enum_def` |
| Pillar | `P06` |
| Nucleus | `n05` |
| Primary Consumers | `input_schema`, `validator`, `runtime_rule`, `quality_gate` |
| Failure Mode | Treat unknown value as `blocked` and page owner. |
| Review Cadence | At every release process change. |
| Compatibility | YAML, JSON, markdown references. |
| Sin Lens | Gating Wrath: no soft states, no silent passes, no unaudited promotion. |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_safety_policy]] | related | 0.30 |
| [[bld_schema_usage_report]] | related | 0.29 |
| [[bld_schema_dataset_card]] | related | 0.29 |
| [[bld_schema_reranker_config]] | related | 0.29 |
| [[p10_ck_railway_deploy_checkpoint]] | downstream | 0.29 |
| [[bld_schema_sandbox_config]] | related | 0.29 |
| [[bld_schema_quickstart_guide]] | related | 0.29 |
| [[bld_schema_enum_def]] | related | 0.29 |
| [[bld_schema_smoke_eval]] | related | 0.29 |
| [[bld_schema_action_paradigm]] | related | 0.28 |
