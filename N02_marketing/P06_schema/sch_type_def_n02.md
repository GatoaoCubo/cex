---
id: sch_type_def_n02
kind: type_def
8f: F1_constrain
pillar: P06
nucleus: n02
title: Campaign Desire Type
version: 1.0
quality: 9.0
tags: [type, schema, campaign, copy, marketing]
density_score: 1.0
related:
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_quickstart_guide
  - bld_schema_playground_config
  - bld_schema_safety_policy
  - bld_schema_optimizer
---


<!-- 8F: F1 constrain=P06/type_def F2 become=type_def-builder F3 inject=nucleus_def_n02+n02_rules+kc_type_def+P06_schema
     F4 reason=reusable_shape_for_desire_driven_copy_objects F5 call=shell_command,apply_patch F6 produce=5745 bytes
     F7 govern=frontmatter_sections_ascii_density_linecount F8 collaborate=N02_marketing/P06_schema/sch_type_def_n02.md -->

# Purpose

| Item | Definition |
|------|------------|
| Mission fit | Shared object model for N02 campaign copy planning |
| Creative Lust lens | Every field must increase desire, clarify friction, or sharpen the ask |
| Primary use | Reusable shape for briefs, prompt inputs, review packets, and deployment payloads |
| Scope | One campaign message unit from hook through proof and CTA |
| Why reusable shape matters | Seduction scales only when the structure repeats without losing emotional force |

## Schema

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| asset_id | string | yes | Stable identifier for the copy unit |
| audience_segment | string | yes | Named audience slice with shared desire pattern |
| messaging_stage | enum_ref: sch_enum_def_n02.messaging_stage | yes | Funnel stage of the copy |
| emotional_trigger | enum_ref: sch_enum_def_n02.emotional_trigger | yes | Core desire driver |
| promise | string | yes | Outcome the reader wants |
| friction | string | yes | Objection or emotional resistance |
| proof_style | enum_ref: sch_enum_def_n02.proof_style | yes | Proof format used to intensify trust |
| proof_payload | string | yes | Exact fact, quote, or contrast asset |
| cta_force | enum_ref: sch_enum_def_n02.cta_force | yes | CTA intensity level |
| cta_line | string | yes | Final action line shown to user |
| channel | string | yes | Email, ad, landing_page, social, or nurture |
| compliance_note | string | no | Legal or brand caveat for publication |
| review_outcome | enum_ref: sch_enum_def_n02.review_outcome | yes | Status after validation |

## Field Semantics

| Field | Constraint | Lust Lens Guidance |
|-------|------------|--------------------|
| asset_id | snake_case, <= 48 chars | Clear IDs protect reuse and testing discipline |
| audience_segment | concrete noun phrase | Desire is stronger when the target feels seen |
| promise | one sentence, <= 120 chars | Promise should seduce with result, not jargon |
| friction | one sentence, <= 120 chars | Name the hesitation that blocks motion |
| proof_payload | fact-rich, source-ready | Seduction without evidence becomes cheap hype |
| cta_line | imperative, <= 70 chars | Ask with confidence matched to funnel heat |
| channel | controlled label | Channel shapes tone, width, and urgency |
| compliance_note | optional | Used when desire must be tempered by policy |

## Object Contract

| Rule | Value |
|------|-------|
| Root type | object |
| Additional fields | blocked |
| Required field count | 12 |
| Optional field count | 1 |
| Nested objects | none |
| Enum dependencies | 5 references to sch_enum_def_n02 |
| Serialization target | yaml or json |
| Reuse target | 3 or more N02 artifacts |

## Validation Map

| Check | Method | Fail Condition |
|-------|--------|----------------|
| required_fields_present | structural | any required field missing |
| enum_values_valid | enum lookup | value not in shared set |
| promise_specificity | semantic review | promise is generic or empty-calorie |
| proof_alignment | semantic review | proof does not support promise |
| cta_heat_match | rule check | hard_close used in attract stage |
| review_status_present | structural | review outcome omitted |

## Rationale

| Decision | Reason |
|----------|--------|
| Flat object design | Easier to reuse in prompts, forms, and validators |
| Promise plus friction pairing | Desire strengthens when aspiration and resistance are both visible |
| Separate proof_style and proof_payload | Keeps form reusable while allowing rich evidence |
| Single CTA field | Forces the asset toward one decisive move |
| Optional compliance_note | Preserves agility without hiding legal friction |

## Example

```yaml
campaign_desire_unit:
  asset_id: launch_demo_wave_a
  audience_segment: founder_led_saas
  messaging_stage: intensify
  emotional_trigger: relief
  promise: Replace launch chaos with a repeatable campaign engine.
  friction: The buyer fears another noisy launch that burns attention.
  proof_style: contrast_demo
  proof_payload: Before CEX, launches stalled in ad hoc docs; after adoption, every wave shipped with tracked handoffs.
  cta_force: guided_step
  cta_line: See the launch system in action.
  channel: landing_page
  compliance_note: Claims must match published case material.
  review_outcome: pass
```

| Example Signal | Value | Interpretation |
|----------------|-------|----------------|
| Desire vector | relief | The copy sells calm control, not raw prestige |
| Proof choice | contrast_demo | The gap is made vivid and memorable |
| CTA heat | guided_step | Warm invitation without premature hard close |
| Review status | pass | Structurally valid and lens-consistent |

## Properties

| Property | Value |
|----------|-------|
| Kind | type_def |
| Pillar | P06 |
| Nucleus | n02 |
| Root shape | flat reusable object |
| Consumer set | prompts, configs, validators, review docs |
| Emotional design | desire plus friction plus proof |
| Governance design | enum-backed and no extra fields |
| Change tolerance | medium |
| Primary risk prevented | inconsistent campaign packet shape |
| Save path | N02_marketing/P06_schema/sch_type_def_n02.md |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | related | 0.45 |
| [[bld_schema_benchmark_suite]] | related | 0.44 |
| [[bld_schema_reranker_config]] | related | 0.44 |
| [[bld_schema_sandbox_config]] | related | 0.44 |
| [[bld_schema_dataset_card]] | related | 0.43 |
| [[bld_schema_pitch_deck]] | related | 0.43 |
| [[bld_schema_quickstart_guide]] | related | 0.43 |
| [[bld_schema_playground_config]] | related | 0.42 |
| [[bld_schema_safety_policy]] | related | 0.41 |
| [[bld_schema_optimizer]] | related | 0.41 |
