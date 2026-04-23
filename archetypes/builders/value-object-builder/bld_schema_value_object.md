---
id: bld_schema_value_object
kind: schema
pillar: P06
title: "Value Object Builder -- Schema"
version: 1.0.0
quality: 7.9
tags: [builder, value_object, schema]
llm_function: CONSTRAIN
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_schema_model_registry
  - bld_schema_input_schema
  - bld_schema_experiment_tracker
  - bld_schema_constraint_spec
  - bld_schema_enum_def
  - bld_schema_prompt_compiler
  - bld_schema_benchmark_suite
  - bld_schema_training_method
  - bld_schema_integration_guide
  - bld_schema_validation_schema
---
# Schema: value_object
## Frontmatter Fields
### Required
| Field | Type | Notes |
|-------|------|-------|
| id | string `p06_vo_{slug}` | namespace + slug |
| kind | literal `value_object` | type integrity |
| pillar | literal `P06` | pillar assignment |
| title | string | human label |
| version | semver | versioning |
| attributes | list[{name, type, constraint}] | at least 1 attribute |
| equality | literal `structural` | always structural for value objects |
| quality | null | never self-score |
| tags | list[string] >= 3 | searchability |
| tldr | string <= 160ch | dense summary |
### Recommended
| Field | Type | Notes |
|-------|------|-------|
| used_in | list[string] | aggregate_root or entity that uses this |
| transformations | list[string] | operations returning new instances |
| language_examples | list[string] | code snippets in target language |
| hashable | bool | whether usable as dict key / set member |
## ID Pattern
Regex: `^p06_vo_[a-z][a-z0-9_]+$`
## Body Structure
1. `## Attributes` -- field table: name, type, constraint, valid range
2. `## Equality` -- structural equality contract definition
3. `## Validation` -- what makes an instance valid (and invalid examples)
4. `## Transformations` -- methods that return new instances, never mutate
5. `## Usage` -- which aggregates or entities use this value object
## Constraints
- max_bytes: 2048
- naming: p06_vo_{slug}.md
- NO identity fields (id, uuid, pk)
- NO mutation methods
- equality MUST be structural
- quality: null always

## Schema Validation Checklist

- Verify all required fields have type annotations
- Validate enum values against domain vocabulary
- Cross-reference with related schemas for consistency
- Test schema parsing with sample data before publishing

## Schema Pattern

```yaml
# Schema validation contract
types_annotated: true
enums_valid: true
cross_refs_checked: true
sample_data_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_schema_hydrate.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | sibling | 0.38 |
| [[bld_schema_input_schema]] | sibling | 0.37 |
| [[bld_schema_experiment_tracker]] | sibling | 0.36 |
| [[bld_schema_constraint_spec]] | sibling | 0.34 |
| [[bld_schema_enum_def]] | sibling | 0.34 |
| [[bld_schema_prompt_compiler]] | sibling | 0.33 |
| [[bld_schema_benchmark_suite]] | sibling | 0.33 |
| [[bld_schema_training_method]] | sibling | 0.32 |
| [[bld_schema_integration_guide]] | sibling | 0.32 |
| [[bld_schema_validation_schema]] | sibling | 0.32 |
