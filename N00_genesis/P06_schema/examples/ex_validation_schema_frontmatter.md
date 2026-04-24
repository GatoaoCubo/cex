---
id: p06_vs_frontmatter
kind: validation_schema
8f: F1_constrain
pillar: P06
title: "Validation Schema: YAML Frontmatter"
version: "1.0.0"
created: "2026-03-28"
updated: "2026-03-28"
author: "builder_agent"
target_kind: "all"
format: "yaml"
fields_count: 8
on_failure: "reject"
strict: true
domain: "frontmatter_validation"
quality: 9.0
tags: [validation-schema, frontmatter, yaml, all-kinds]
tldr: "Validates YAML frontmatter common fields: id, kind, pillar, version, quality, tags, tldr. Rejects on parse error or missing required."
coercion: false
error_template: "{{field}} failed: {{reason}}"
density_score: 0.91
linked_artifacts:
  primary: "validation-schema-builder"
  related: [quality-gate-builder, validator-builder]
related:
  - bld_examples_validation_schema
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_nps_survey
  - bld_schema_sandbox_spec
  - bld_schema_quickstart_guide
  - bld_schema_eval_metric
  - bld_schema_usage_report
  - bld_schema_pitch_deck
---
## Schema Overview
Validates the common YAML frontmatter fields present in every organization artifact. Ensures structural integrity before kind-specific validation runs. Applied as first validation pass in the publish pipeline.
## Fields
| Field | Type | Required | Constraints | Error message |
|-------|------|----------|-------------|---------------|
| id | string | yes | matches `^p\d{2}_[a-z][a-z0-9_]+$` | id failed: must match pillar prefix pattern |
| kind | string | yes | must exist in pillar's _schema.yaml kinds list | kind failed: unrecognized kind for pillar |
| pillar | string | yes | matches `^P\d{2}$` | pillar failed: must be P01-P12 format |
| version | string | yes | semver format `^\d+\.\d+\.\d+$` | version failed: must be valid semver |
| quality | null | yes | must be literal null (not 0, not "", not "null") | quality failed: must be null for new artifacts |
| tags | list | yes | non-empty, each tag is lowercase kebab or snake | tags failed: must be non-empty list of lowercase strings |
| tldr | string | yes | 10-160 characters, no line breaks | tldr failed: must be 10-160 chars single line |
| author | string | yes | non-empty string | author failed: must be non-empty |
## Failure Handling
- **on_failure**: reject — frontmatter errors are structural and cannot be auto-fixed safely
- **strict**: true — no unknown fields allowed in common frontmatter block
- **coercion**: false — types must match exactly (no string-to-number, no "null" to null)
- **error_template**: "{{field}} failed: {{reason}}"
- **remediation**: fix the specific field per error message, re-run validation
## Integration
- **Pipeline position**: first pass, before kind-specific schema validation
- **Applied by**: cex_doctor.py and publish pipeline validator
- **Input**: raw YAML frontmatter block (between `---` markers)
- **Output**: validated frontmatter dict or list of field-level errors

## Cross-References

- **Pillar**: P06 (Schema)
- **Kind**: `validation schema`
- **Artifact ID**: `p06_vs_frontmatter`
- **Tags**: [validation-schema, frontmatter, yaml, all-kinds]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P06 | Schema domain |
| Kind `validation schema` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_validation_schema]] | downstream | 0.48 |
| [[bld_schema_integration_guide]] | related | 0.46 |
| [[bld_schema_reranker_config]] | related | 0.45 |
| [[bld_schema_benchmark_suite]] | related | 0.43 |
| [[bld_schema_nps_survey]] | related | 0.41 |
| [[bld_schema_sandbox_spec]] | related | 0.41 |
| [[bld_schema_quickstart_guide]] | related | 0.41 |
| [[bld_schema_eval_metric]] | related | 0.41 |
| [[bld_schema_usage_report]] | related | 0.41 |
| [[bld_schema_pitch_deck]] | related | 0.41 |
