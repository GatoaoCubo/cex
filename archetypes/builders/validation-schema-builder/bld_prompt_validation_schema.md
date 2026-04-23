---
id: p03_ins_validation_schema
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Validation Schema Builder Instructions
target: "validation-schema-builder agent"
phases_count: 4
prerequisites:
  - "Target artifact kind is identified (e.g. system_prompt, workflow, validator)"
  - "At least one field requiring post-generation validation is known"
  - "On-failure strategy is determined: reject, warn, or auto_fix"
  - "The schema is system-applied (not injected into the LLM prompt)"
validation_method: checklist
domain: validation_schema
quality: 9.0
tags: [instruction, validation-schema, post-generation, contract, P06]
idempotent: true
atomic: true
rollback: "Delete generated validation_schema YAML file"
dependencies: []
logging: true
tldr: "Build a validation_schema YAML that the system applies after generation to enforce field types, constraints, and on-failure behavior -- the LLM never sees it."
density_score: 0.92
llm_function: REASON
related:
  - bld_instruction_input_schema
  - bld_schema_validation_schema
  - bld_knowledge_card_validation_schema
  - p11_qg_validation_schema
  - bld_collaboration_validation_schema
  - bld_examples_validation_schema
  - p03_sp_validation-schema-builder
  - p03_ins_validator
  - p06_vs_frontmatter
  - p10_lr_input_schema_builder
---
## Context
The validation-schema-builder produces a `validation_schema` artifact -- a structured YAML that defines the formal contract the system enforces on generated output after an LLM call complete. This contract runs automatically; the LLM does not see it.
**Critical distinction**: a `validation_schema` is a system-side post-generation contract. It is NOT a prompt instruction for the LLM (`response_format` -- injected into the prompt), NOT an individual pass/fail rule (`validator` -- single rule, not a schema), and NOT an input contract (`input_schema` -- governs inputs before generation). Confusing these produces contracts applied at the wrong layer.
**Input contract**:
- `target_kind`: string -- the artifact kind this schema validates (e.g. `system_prompt`, `workflow`)
- `fields`: list of field definition objects (see Phase 2)
- `on_failure`: enum -- `reject` | `warn` | `auto_fix`
- `format`: enum -- `yaml` | `json` | `markdown`
- `applied_at`: string -- pipeline stage where validation runs (e.g. `post_generation`, `pre_commit`)
- `strict_mode`: boolean -- whether unknown fields cause failure
**Output contract**: a single `validation_schema` YAML with all required fields, stored at `records/validation_schemas/{target_kind}_schema.yaml`.
**Variables**:
- `{{target_kind}}` -- artifact kind being validated
- `{{field_N_name}}` -- Nth field name
- `{{field_N_type}}` -- Nth field type
- `{{on_failure}}` -- failure behavior enum value
- `{{applied_at}}` -- pipeline stage
## Phases
### Phase 1: Identify Target Contract Scope
**Action**: Determine which fields of the target artifact require system-side enforcement.
```
FOR the given target_kind:
    1. List all fields that appear in the target artifact's SCHEMA.md
    2. Classify each field:
       - REQUIRED: must be present and non-null
       - TYPED: must match a specific type
       - CONSTRAINED: must satisfy a value constraint (regex, enum, range)
       - OPTIONAL: validated if present, ignored if absent
    3. Determine on_failure behavior:
       reject   -> generation is discarded, error returned to caller
       warn     -> generation proceeds with warning logged
       auto_fix -> system attempts correction (only for formatting/casing issues)
    4. Determine strict_mode:
       true  -> unknown fields fail validation
       false -> unknown fields are ignored (default for extensible schemas)
```
Verifiable exit: all fields classified; on_failure is set; strict_mode is set.
### Phase 2: Define Field Validation Rules
**Action**: Convert each field classification into a structured field definition object.
Field definition object schema:
```
{
  name: string -- field name as it appears in the artifact
  type: enum [string, integer, number, boolean, object, array, null, any]
  required: boolean
  constraints: {
    pattern: regex string (for string fields)
    enum: list of allowed values
    min: numeric minimum
    max: numeric maximum
    min_length: integer (for strings/arrays)
    max_length: integer (for strings/arrays)
  }
  on_failure_override: enum or null -- overrides top-level on_failure for this field
  error_message: string -- human-readable message when this field fails
}
```
Rules:
- `required: true` fields must appear in the output; absence is a hard failure
- Type `any` disables type checking for that field (use sparingly)
- `on_failure_override` allows critical fields to `reject` even if top-level is `warn`
```
ASSERT len(fields) >= 1
FOR each field:
    ASSERT field.name is non-empty
    ASSERT field.type is a valid enum value
    ASSERT field.error_message is non-empty
```
Verifiable exit: fields list is non-empty; each field has name, type, required, and error_message.
### Phase 3: Specify Integration Point
**Action**: Define where in the pipeline this schema is applied and how failures surface.
```
applied_at options:
  post_generation  -> runs immediately after LLM returns output
  pre_commit       -> runs before artifact is written to storage
  on_read          -> runs when artifact is loaded by a consumer
failure_surface = {
  reject:   return error to caller with field_name + error_message
  warn:     log warning with field_name + error_message, continue
  auto_fix: attempt fix, log fix applied, continue; fail if fix fails
}
auto_fix is only valid for:
  - string casing normalization (e.g. uppercase -> lowercase)
  - whitespace trimming
  - enum value coercion (e.g. "True" -> true)
  NOT valid for: missing required fields, invalid logic, structural errors
```
Verifiable exit: applied_at is set; auto_fix scope is bounded to safe transformations only.
### Phase 4: Validate Against Quality Gates
**Action**: Run 9 HARD gates before emitting; log 9 SOFT gates as warnings.
```
HARD gates (all must pass):
  H1: target_kind is non-empty
  H2: fields list has >= 1 entry
  H3: each field has name, type, required, and error_message
  H4: on_failure is one of reject, warn, auto_fix
  H5: format is one of yaml, json, markdown
  H6: applied_at is one of post_generation, pre_commit, on_read
  H7: auto_fix is not used for structural violations
  H8: quality field is null


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_input_schema]] | sibling | 0.42 |
| [[bld_schema_validation_schema]] | downstream | 0.42 |
| [[bld_knowledge_card_validation_schema]] | upstream | 0.42 |
| [[p11_qg_validation_schema]] | downstream | 0.39 |
| [[bld_collaboration_validation_schema]] | downstream | 0.39 |
| [[bld_examples_validation_schema]] | downstream | 0.37 |
| [[p03_sp_validation-schema-builder]] | related | 0.37 |
| [[p03_ins_validator]] | sibling | 0.34 |
| [[p06_vs_frontmatter]] | downstream | 0.33 |
| [[p10_lr_input_schema_builder]] | downstream | 0.32 |
