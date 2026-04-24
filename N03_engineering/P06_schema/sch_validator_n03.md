---
id: sch_validator_n03
kind: validator
8f: F7_govern
pillar: P06
nucleus: n03
title: Foundation Artifact Validator
version: 1.0
quality: 9.0
tags: [schema, validator, governance, pre_commit, n03]
density_score: 1.0
related:
  - bld_schema_validator
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_kind
  - p06_vs_frontmatter
  - bld_schema_output_validator
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_pitch_deck
---


<!-- 8F: F1 constrain=P06/validator F2 become=validator-builder F3 inject=nucleus_def_n03, n03-builder, kc_validator, P06_schema, quality patterns
     F4 reason=pre-commit validator for N03 foundational artifact discipline F5 call=rg, Get-Content, apply_patch F6 produce=5317 bytes
     F7 govern=frontmatter+sections+tables+ascii+self-check F8 collaborate=save N03_engineering/P06_schema/sch_validator_n03.md -->

# Foundation Artifact Validator

## Purpose

| Field | Value |
|-------|-------|
| Mission fit | Binary validation rule for Wave 1 schema and config artifacts owned by N03 |
| Pride lens | The validator blocks weak structure instead of trusting best intentions |
| Primary use | Pre-commit and quality-gate enforcement for frontmatter, density, and evidence sections |
| Boundary | Atomic pass/fail rule set; not a scored rubric and not a lifecycle policy |
| Execution stage | `pre_commit`, `manual_review_gate`, `compile_guard` |
| Failure prevented | Bare-minimum markdown that compiles but lacks rigor |

## Schema

| Property | Type | Required | Value or Rule | Inventive Pride decision |
|----------|------|----------|---------------|--------------------------|
| validator_name | string | yes | `n03_foundation_artifact_guard` | Names the duty, not the implementation |
| rule_type | string | yes | `structural_governance` | Structure must fail fast |
| severity | string | yes | `error` | Foundation drift is not a warning |
| on_fail | string | yes | `block` | Weak artifacts do not pass by persuasion |
| scope | list[string] | yes | `N03_engineering/P06_schema/*.md`, `N03_engineering/P09_config/*.md` | Narrow ownership keeps enforcement honest |
| auto_fix | boolean | yes | `false` | Pride rejects hidden mutation of authored meaning |
| audit_trail | boolean | yes | `true` | Every block should be explainable |
| retry_policy | string | yes | `author_revision_only` | The author must repair the design intentionally |

## Checks

| Check ID | Condition | Pass rule | Fail example |
|----------|-----------|-----------|--------------|
| `V01` | Frontmatter present | Starts with HTML 8F comment then YAML frontmatter | Missing delimiter or missing `quality: null` |
| `V02` | Required keys | `id, kind, pillar, nucleus, title, version, quality, tags` all exist | Any key omitted |
| `V03` | Mandatory sections | `Purpose`, `Schema` or `Values`, `Rationale`, `Example`, `Properties` exist | Prose-only artifact |
| `V04` | Table density | At least `4` markdown tables with non-empty bodies | One small table plus filler prose |
| `V05` | Line floor | At least `80` lines | Thin artifact pretending to be complete |
| `V06` | N03 lens | Body explicitly expresses `Inventive Pride` in design logic | Generic template language |
| `V07` | ASCII-safe identifiers | IDs, keys, and code-block identifiers remain ASCII-safe | Accented identifier or decorative symbols |
| `V08` | Example coherence | Example uses the same kind and naming logic as frontmatter | Mismatched example schema |

## Rationale

| Design choice | Why it exists | Pride expression |
|---------------|---------------|------------------|
| Error severity | Foundational artifacts are upstream dependencies | Zero tolerance for silent drift |
| No auto-fix | A hidden fixer can make the file pass without making it good | Human craft stays visible |
| Explicit lens check | The mission forbids generic boilerplate | Signature over filler |
| Line and table checks together | Length alone is noisy; density alone can be gamed | Multiple gates beat vanity metrics |
| Audit trail required | Every rejection must teach the next revision | Quality compounds |
| Narrow file scope | Validators should own precise terrain | Governance with boundaries |

## Example

```yaml
validator_name: n03_foundation_artifact_guard
rule_type: structural_governance
severity: error
on_fail: block
scope:
  - N03_engineering/P06_schema/*.md
  - N03_engineering/P09_config/*.md
checks:
  - id: V01
    condition: frontmatter_present
    expected: true
  - id: V03
    condition: required_sections_present
    expected:
      - Purpose
      - Rationale
      - Example
      - Properties
  - id: V05
    condition: min_line_count
    expected: 80
  - id: V06
    condition: lens_phrase_present
    expected: Inventive Pride
audit_trail: true
auto_fix: false
```

## Enforcement Notes

| Trigger | Behavior | Outcome |
|---------|----------|---------|
| Author save | Optional local lint pass | Early correction before compile |
| Pre-commit hook | Full validator execution | Blocks commit when a hard check fails |
| Peer review | Manual spot-check against validator evidence | Confirms the rule is not being gamed |
| Compile stage | Structural re-check on source markdown | Prevents invalid compiled YAML propagation |
| Mission closeout | Review of blocked reasons | Improves future builder templates |

## Properties

| Property | Value |
|----------|-------|
| Nucleus | `n03` |
| Pillar | `P06` |
| Kind | `validator` |
| Validator name | `n03_foundation_artifact_guard` |
| Checks | `8` |
| Severity | `error` |
| Auto-fix | `false` |
| Lens | `Inventive Pride` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_validator]] | related | 0.35 |
| [[bld_schema_dataset_card]] | related | 0.34 |
| [[bld_schema_quickstart_guide]] | related | 0.33 |
| [[bld_schema_reranker_config]] | related | 0.33 |
| [[bld_schema_kind]] | related | 0.33 |
| [[p06_vs_frontmatter]] | related | 0.33 |
| [[bld_schema_output_validator]] | related | 0.33 |
| [[bld_schema_usage_report]] | related | 0.32 |
| [[bld_schema_benchmark_suite]] | related | 0.32 |
| [[bld_schema_pitch_deck]] | related | 0.32 |
