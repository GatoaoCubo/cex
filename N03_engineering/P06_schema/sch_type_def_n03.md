---
id: sch_type_def_n03
kind: type_def
pillar: P06
nucleus: n03
title: Engineering Artifact Type
version: 1.0
quality: null
tags: [schema, type, engineering, contract, n03]
---


<!-- 8F: F1 constrain=P06/type_def F2 become=type-def-builder F3 inject=nucleus_def_n03, agent_engineering, kc_type_def, P06_schema, sibling schemas
     F4 reason=reusable engineering artifact contract with strict lifecycle and evidence fields F5 call=rg, Get-Content, apply_patch F6 produce=6569 bytes
     F7 govern=frontmatter+sections+tables+ascii+self-check F8 collaborate=save N03_engineering/P06_schema/sch_type_def_n03.md -->

# Engineering Artifact Type

## Purpose

| Field | Value |
|-------|-------|
| Mission fit | Canonical reusable type for N03 artifacts that require lifecycle, ownership, and evidence |
| Pride lens | The type is strict enough to prevent vague construction, but portable enough to be reused broadly |
| Primary use | Shared shape for build records, review summaries, config snapshots, and schema-derived outputs |
| Boundary | Reusable shape only; not an invocation contract and not a validator rule |
| Consumers | `input_schema`, `validator`, quality reports, orchestrated build traces |
| Failure prevented | Repeated inline object definitions with mismatched field names |

## Schema

| Property | Type | Required | Value or Rule | Inventive Pride decision |
|----------|------|----------|---------------|--------------------------|
| type_name | string | yes | `engineering_artifact_record` | A single strong noun for a shared contract |
| category | string | yes | `composite_object` | Structured data deserves explicit composition |
| extends | string | no | `none` | Keep Wave 1 foundational and dependency-light |
| nullable | boolean | yes | `false` | Missing core records are a governance smell |
| serialization | list[string] | yes | `yaml,json,markdown_table` | One type, multiple render surfaces |
| versioning | string | yes | `semantic_minor_additive` | Tight control with room for compatible growth |
| reuse_threshold | string | yes | `two_or_more_consumers` | Extract only when reuse is real |
| owner | string | yes | `n03_engineering` | Ownership must be legible |

## Fields

| Field | Type | Required | Description | Constraint |
|-------|------|----------|-------------|------------|
| `artifact_id` | string | yes | Stable artifact identifier | Matches `^[a-z0-9_]+$` |
| `artifact_kind` | string | yes | Declared CEX kind | Must map to a registered kind |
| `artifact_pillar` | string | yes | Owning pillar | Must match `^P[0-9]{2}$` |
| `title` | string | yes | Human-readable title | `4-80` chars |
| `owner_nucleus` | string | yes | Nucleus responsible for authorship | Default `n03` |
| `control_state` | enum ref | yes | Lifecycle state | References `engineering_control_state` |
| `inputs_used` | list[string] | yes | Key references injected in F3 | Minimum `1` |
| `design_rationale` | string | yes | Why this shape exists | Minimum `24` chars |
| `evidence_paths` | list[string] | yes | Supporting local paths | Each path must be relative repo path |
| `last_validated_at` | string | no | Latest validation timestamp | ISO-8601 when present |
| `compatibility_note` | string | no | Migration guidance for downstream consumers | Optional but plain ASCII |
| `review_required` | boolean | yes | Whether human review is mandatory | Default `true` |

## Type Rules

| Rule | Statement | Why it matters |
|------|-----------|----------------|
| R1 | `artifact_id`, `artifact_kind`, and `artifact_pillar` are mandatory together | Identity without classification is weak engineering |
| R2 | `control_state` cannot be `approved` if `last_validated_at` is absent | Approval must leave an evidence trail |
| R3 | `inputs_used` must contain at least one reference path or builder source | Pride means designs are grounded |
| R4 | `evidence_paths` may be empty only when `control_state=planned` | Execution states require receipts |
| R5 | `review_required=true` unless explicitly waived by a downstream policy | Human signature remains visible |
| R6 | Optional fields never carry secrets or runtime values | Type contracts must stay clean and reusable |

## Rationale

| Design choice | Why it exists | Pride expression |
|---------------|---------------|------------------|
| Explicit artifact identity trio | IDs, kind, and pillar are the minimum reliable coordinates | No anonymous outputs |
| Embedded rationale field | Reuse improves when intent is carried with the data | Craft includes explanation |
| Evidence list | N03 outputs should be inspectable, not mystical | Show the work |
| Validation timestamp gate | Governance is attached to state, not detached paperwork | Approval earns its name |
| Mandatory review flag | Foundation types should bias toward scrutiny | Signature-worthy by default |
| Multi-format serialization | One durable type should survive across compiled and human views | Build once, project cleanly |

## Example

```yaml
type_name: engineering_artifact_record
category: composite_object
nullable: false
serialization:
  - yaml
  - json
  - markdown_table
fields:
  artifact_id: sch_type_def_n03
  artifact_kind: type_def
  artifact_pillar: P06
  title: Engineering Artifact Type
  owner_nucleus: n03
  control_state: implementing
  inputs_used:
    - N03_engineering/architecture/nucleus_def_n03.md
    - P01_knowledge/library/kind/kc_type_def.md
  design_rationale: Shared contract for evidence-backed engineering artifacts
  evidence_paths:
    - N03_engineering/P06_schema/sch_type_def_n03.md
  review_required: true
```

## Integration Notes

| Consumer | How it uses this type | Constraint carried forward |
|----------|-----------------------|----------------------------|
| `input_schema` | Embeds the object as a reusable payload component | Preserves naming and validation timestamp requirements |
| `validator` | Checks field presence and state transitions | Converts semantic rules into pass/fail logic |
| `quality_gate` | Reads evidence density and review requirement | Governance stays measurable |
| `workflow` | Moves records between planning and implementation phases | State changes remain typed |
| `memory` artifacts | Persist learned build facts | Historical records stay compatible |

## Properties

| Property | Value |
|----------|-------|
| Nucleus | `n03` |
| Pillar | `P06` |
| Kind | `type_def` |
| Type name | `engineering_artifact_record` |
| Required fields | `10` |
| Optional fields | `2` |
| Serialization | `yaml,json,markdown_table` |
| Lens | `Inventive Pride` |
