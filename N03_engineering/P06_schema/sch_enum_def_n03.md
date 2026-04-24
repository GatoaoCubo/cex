---
id: sch_enum_def_n03
kind: enum_def
8f: F1_constrain
pillar: P06
nucleus: n03
title: Engineering Control Enum
version: 1.0
quality: 9.0
tags: [schema, enum, engineering, governance, n03]
density_score: 0.97
related:
  - bld_schema_enum_def
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_sandbox_config
  - bld_schema_reranker_config
  - bld_schema_safety_policy
  - bld_schema_agent_profile
---


<!-- 8F: F1 constrain=P06/enum_def F2 become=enum-def-builder F3 inject=nucleus_def_n03, n03-builder, kc_enum_def, P06_schema, sibling schemas
     F4 reason=closed-set runtime enum for engineering handoffs and governance F5 call=rg, Get-Content, apply_patch F6 produce=5883 bytes
     F7 govern=frontmatter+sections+tables+ascii+self-check F8 collaborate=save N03_engineering/P06_schema/sch_enum_def_n03.md -->

# Engineering Control Enum

## Purpose

| Field | Value |
|-------|-------|
| Mission fit | Reusable closed set for N03 engineering control states and escalation markers |
| Pride lens | Every value is sharp, non-overlapping, and worthy of reuse across artifacts |
| Primary use | Normalize status, certainty, and disposition fields in schema and config artifacts |
| Boundary | Finite literals only; no nested shape, no procedural rule, no scoring |
| Consumers | `type_def`, `validator`, `permission`, `rate_limit_config`, review workflows |
| Failure prevented | Drift caused by ad hoc wording like "ok", "done", "almost", or "maybe" |

## Schema

| Property | Type | Required | Value or Rule | Inventive Pride decision |
|----------|------|----------|---------------|--------------------------|
| enum_name | string | yes | `engineering_control_state` | One durable name instead of per-file synonyms |
| base_type | string | yes | `string` | Portable across YAML, JSON Schema, and Python |
| cardinality | integer | yes | `8` | Tight enough to stay memorable; broad enough to cover lifecycle |
| default | string | yes | `planned` | Forces deliberate promotion from intent to execution |
| case_style | string | yes | `snake_case` | Signature-grade consistency across nuclei |
| mutability | string | yes | `append_by_revision_only` | Values are governed, not casually edited |
| compat_policy | string | yes | `backward_additive` | New literals may be added, existing literals are stable |
| reference_mode | string | yes | `by_id` | Downstream artifacts should reference the enum, not copy it |

## Values

| Literal | Meaning | Use when | Avoid because |
|---------|---------|----------|---------------|
| `planned` | Identified but not yet acted on | Scope exists and resources are not yet engaged | It is not evidence of execution |
| `designing` | Structure is being specified | F1-F4 are active and choices are still being shaped | It is not a draft-ready result |
| `implementing` | Artifact is actively being built | F6 production is underway | It says nothing about correctness |
| `validating` | Binary or structural checks are running | F7 or pre-commit validators are engaged | It is not a final acceptance state |
| `approved` | Ready for trusted reuse | The artifact passed review and can be referenced broadly | It is stronger than "looks good" |
| `blocked` | Progress stopped by a named dependency | Another artifact, path, secret, or rule prevents movement | It must not hide uncertainty |
| `deprecated` | Kept for compatibility but no longer preferred | Consumers still exist but migration is underway | It is not deletion |
| `retired` | Removed from active use | Consumers are migrated and the state remains only for history | It is not recoverable without revision |

## Rationale

| Design choice | Why it exists | Pride expression |
|---------------|---------------|------------------|
| Eight literals only | A builder should recall the whole set without lookup fatigue | Precision over bloat |
| Verb-oriented progression | States map cleanly onto the 8F pipeline and review flow | Elegant fit beats generic status words |
| `deprecated` plus `retired` | Migration and end-state are different governance acts | Fine distinctions protect quality |
| `blocked` instead of `failed` | Operational blockage is different from poor artifact quality | Diagnose before judging |
| Stable `snake_case` | Reused in code, YAML, docs, and validators without translation | No sloppy format drift |
| Backward additive policy | Consumers can grow safely without rewriting old histories | Build for scale, not for today only |

## Example

```yaml
enum_name: engineering_control_state
base_type: string
default: planned
values:
  - literal: planned
    label: Planned
    description: Scoped but not yet started
  - literal: designing
    label: Designing
    description: Structure is under active design
  - literal: implementing
    label: Implementing
    description: Artifact is being produced
  - literal: validating
    label: Validating
    description: Checks are running
  - literal: approved
    label: Approved
    description: Cleared for reuse
  - literal: blocked
    label: Blocked
    description: Waiting on explicit dependency
  - literal: deprecated
    label: Deprecated
    description: Compatible but no longer preferred
  - literal: retired
    label: Retired
    description: Historical only
```

## Reference Use

| Artifact kind | Field example | Benefit |
|---------------|---------------|---------|
| `type_def` | `lifecycle_state` | Shared semantics across engineering types |
| `validator` | `allowed_state` | Deterministic pass/fail checks |
| `path_config` | `state_gate` | Release paths can be tied to explicit states |
| `permission` | `execution_state` | Dangerous writes can be denied unless approved |
| `secret_config` | `rotation_state` | Secret lifecycle remains auditable |
| `rate_limit_config` | `policy_state` | Budget policies can be promoted deliberately |

## Properties

| Property | Value |
|----------|-------|
| Nucleus | `n03` |
| Pillar | `P06` |
| Kind | `enum_def` |
| Enum name | `engineering_control_state` |
| Default | `planned` |
| Values | `8` |
| Compatibility | `backward_additive` |
| Lens | `Inventive Pride` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_enum_def]] | related | 0.38 |
| [[bld_schema_usage_report]] | related | 0.37 |
| [[bld_schema_dataset_card]] | related | 0.37 |
| [[bld_schema_benchmark_suite]] | related | 0.36 |
| [[bld_schema_quickstart_guide]] | related | 0.35 |
| [[bld_schema_pitch_deck]] | related | 0.35 |
| [[bld_schema_sandbox_config]] | related | 0.35 |
| [[bld_schema_reranker_config]] | related | 0.35 |
| [[bld_schema_safety_policy]] | related | 0.35 |
| [[bld_schema_agent_profile]] | related | 0.34 |
