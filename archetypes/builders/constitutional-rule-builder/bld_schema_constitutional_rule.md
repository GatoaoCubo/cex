---
quality: 8.0
quality: 7.6
id: bld_schema_constitutional_rule
kind: schema
pillar: P11
title: "Constitutional Rule Builder -- Schema"
version: 1.0.0
tags: [builder, constitutional_rule, schema]
llm_function: CONSTRAIN
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_schema_guardrail
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - bld_schema_invariant
  - bld_schema_prompt_compiler
  - bld_schema_output_validator
  - bld_schema_enum_def
  - bld_schema_input_schema
  - bld_schema_retriever_config
  - bld_schema_benchmark_suite
---
# Schema: constitutional_rule
## Frontmatter Fields
### Required
| Field | Type | Notes |
|-------|------|-------|
| id | string `p11_cr_{slug}` | namespace + slug |
| kind | literal `constitutional_rule` | type integrity |
| pillar | literal `P11` | pillar assignment |
| title | string | human label |
| version | semver | versioning |
| constitutional_basis | enum(harm_prevention, honesty, autonomy_preservation, legality) | which value this protects |
| principle | string | one concrete prohibition statement |
| bypass_policy | literal `none` | MUST be none -- no exceptions |
| core | literal `true` | marks as non-overridable core rule |
| quality | null | never self-score |
| tags | list[string] >= 3 | searchability |
| tldr | string <= 160ch | dense summary |
### Recommended
| Field | Type | Notes |
|-------|------|-------|
| applies_to | list[string] | which agent kinds this rule applies to |
| detection_method | string | how violations are identified |
| cai_reference | string | which CAI principle this maps to |
| severity | literal `critical` | always critical for constitutional rules |
## ID Pattern
Regex: `^p11_cr_[a-z][a-z0-9_]+$`
## Body Structure
1. `## Principle` -- one clear, concrete prohibition
2. `## Constitutional Basis` -- which value this protects and why it is absolute
3. `## Rationale` -- why this has zero exceptions
4. `## Violations` -- concrete examples of what breaking this looks like
5. `## Detection` -- how a reviewer identifies a violation
6. `## Boundary` -- why this is not a guardrail (no bypass) and not a safety_policy (has enforcement)
## Constraints
- max_bytes: 2048
- naming: p11_cr_{slug}.md
- bypass_policy MUST be "none" -- any bypass downgrades to guardrail
- core MUST be true
- severity MUST be critical (constitutional rules are always critical)
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
| [[bld_schema_guardrail]] | sibling | 0.41 |
| [[bld_schema_model_registry]] | sibling | 0.36 |
| [[bld_schema_experiment_tracker]] | sibling | 0.34 |
| [[bld_schema_invariant]] | sibling | 0.34 |
| [[bld_schema_prompt_compiler]] | sibling | 0.34 |
| [[bld_schema_output_validator]] | sibling | 0.33 |
| [[bld_schema_enum_def]] | sibling | 0.32 |
| [[bld_schema_input_schema]] | sibling | 0.32 |
| [[bld_schema_retriever_config]] | sibling | 0.32 |
| [[bld_schema_benchmark_suite]] | sibling | 0.31 |
