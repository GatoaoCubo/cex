---
id: sch_type_def_n05
kind: type_def
pillar: P06
nucleus: n05
title: Release Decision Type
version: 1.0
quality: null
tags: [schema, type, operations, release, audit]
---
<!-- 8F: F1 constrain=P06/type_def F2 become=type-def-builder F3 inject=nucleus_def_n05+n05-operations+kc_type_def+P06_schema+N05 schema examples
     F4 reason=typed release decision record with explicit evidence and rollback gates F5 call=apply_patch F6 produce=5661 bytes
     F7 govern=self-check headings+tables+gating_wrath+ascii+80_lines F8 collaborate=N05_operations/P06_schema/sch_type_def_n05.md -->

# Release Decision Type

## Purpose

| Field | Value |
|---|---|
| Intent | Define the reusable typed object that records a release decision and the evidence behind it. |
| Scope | CI verdicts, deploy approvals, rollback decisions, incident follow-up, audit export. |
| Gating Wrath Lens | Every decision must expose owner, proof, expiry, and rollback path. |
| Default Posture | Reject incomplete objects; partial decision records are operational debt. |
| Reuse Rule | Upstream schemas reference this type instead of cloning ad hoc release objects. |

## Schema

| Property | Type | Required | Constraint | Rationale |
|---|---|---|---|---|
| type_name | string | yes | `release_decision_record` | Stable canonical name. |
| base_type | string | yes | `object` | Decision data is composite and auditable. |
| nullable | boolean | yes | `false` | Missing decision object is not acceptable. |
| extends | string | no | null | Keep this type explicit and self-contained. |
| versioning | string | yes | semver reference | Safe evolution across pipelines. |
| serialization | list[string] | yes | `yaml`, `json` | Common runtime and export formats. |
| required_fields | list[string] | yes | non-empty | Prevents silent omission. |

## Field Model

| Field | Type | Required | Constraint | Operational Meaning |
|---|---|---|---|---|
| decision_id | string | yes | immutable, unique | Traceable release decision identifier. |
| release_ref | string | yes | commit or artifact digest | Binds record to a concrete candidate. |
| gate_state | enum `release_gate_state` | yes | closed set only | Forces valid lifecycle state. |
| risk_level | string | yes | low, medium, high, critical | Drives urgency and reviewer tier. |
| decision_owner | string | yes | non-empty | Named accountable operator. |
| evidence_refs | list[string] | yes | min 3 for prod | CI, scan, smoke, or change records. |
| expires_at | string | yes | ISO8601 timestamp | Approval cannot live forever. |
| rollback_plan_ref | string | yes | non-empty | Every promotion needs a reverse path. |
| exception_ticket | string | no | required when risk_level=critical | Overrides must be visible. |
| notes | string | no | max 500 chars | Short operator context only. |

## Composition Rules

| Rule | Expression | Enforcement |
|---|---|---|
| Prod evidence floor | `environment=prod -> len(evidence_refs) >= 3` | Block approval on weak proof. |
| Critical risk exception | `risk_level=critical -> exception_ticket != null` | No implicit acceptance of critical risk. |
| Approval freshness | `expires_at > decision_time and <= 24h window` | Prevent stale approvals from drifting into deploys. |
| Rollback always present | `rollback_plan_ref != null` | No forward-only deployments. |
| Immutable identity | `decision_id` and `release_ref` never mutate | Audit trail remains stable. |

## Rationale

| Design Choice | Why It Exists | Gating Wrath Effect |
|---|---|---|
| Explicit `gate_state` reference | Avoids free-form status strings. | Eliminates interpretive drift. |
| Mandatory `decision_owner` | Someone must carry the page. | Prevents anonymous approvals. |
| `expires_at` required | Approval without freshness becomes a latent hazard. | Forces re-validation. |
| `rollback_plan_ref` mandatory | Recovery planning is part of approval, not aftermath. | Cuts rollback latency. |
| Constrained `notes` | Long prose hides the signal. | Keeps operator review fast. |
| No nullable record | Empty objects create fake compliance. | Fail fast on missing structure. |

## Example

| Example Slice | Value |
|---|---|
| Candidate | `api@sha256:4f1c9d` |
| State | `approved` |
| Risk | `medium` |
| Owner | `release_manager_n05` |
| Expiry | `2026-04-16T18:00:00Z` |
| Rollback | `runbook://ops/rollback/api-blue-green` |

```yaml
type_name: release_decision_record
base_type: object
nullable: false
extends: null
versioning: 1.0.0
serialization:
  - yaml
  - json
required_fields:
  - decision_id
  - release_ref
  - gate_state
  - risk_level
  - decision_owner
  - evidence_refs
  - expires_at
  - rollback_plan_ref
fields:
  decision_id:
    type: string
    required: true
  release_ref:
    type: string
    required: true
  gate_state:
    type: enum_ref
    ref: release_gate_state
    required: true
  risk_level:
    type: string
    enum: [low, medium, high, critical]
    required: true
  decision_owner:
    type: string
    required: true
  evidence_refs:
    type: list[string]
    required: true
  expires_at:
    type: string
    format: iso8601
    required: true
  rollback_plan_ref:
    type: string
    required: true
```

## Properties

| Property | Value |
|---|---|
| Kind | `type_def` |
| Pillar | `P06` |
| Nucleus | `n05` |
| Base Type | `object` |
| Primary Consumers | `input_schema`, `interface`, `validation_schema`, `incident report` |
| Failure Mode | Reject record if any mandatory field is absent or stale. |
| Mutation Policy | Append-only for notes, immutable for identity and evidence links. |
| Sin Lens | Gating Wrath: typed proof before promotion, typed rollback before exposure. |
