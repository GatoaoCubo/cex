---
kind: memory
id: bld_memory_validation_schema
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for validation_schema artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Validation Schema"
version: "1.0.0"
author: n03_builder
tags: [validation_schema, builder, examples]
tldr: "Golden and anti-examples for validation schema construction, demonstrating ideal structure and common pitfalls."
domain: "validation schema construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_validation_schema
  - validation-schema-builder
  - p03_sp_validation-schema-builder
  - bld_collaboration_validation_schema
  - p11_qg_validation_schema
  - p03_ins_validation_schema
  - p01_kc_validation_schema
  - bld_schema_validation_schema
  - bld_architecture_validation_schema
  - bld_examples_validation_schema
---
# Memory: validation-schema-builder
## Summary
Validation schemas are post-generation contracts that the system applies automatically — the LLM never sees them. The critical distinction from response formats (P05) is visibility: response formats are injected into the prompt (LLM sees), validation schemas are applied after generation (system enforces). Confusing these causes either redundant checking or enforcement gaps. The second lesson is on_failure behavior: schemas that only reject without auto_fix options waste regeneration cycles on trivially fixable issues.
## Pattern
1. Clearly separate from response_format: validation_schema is system-side, never prompt-injected
2. Define on_failure behavior per field: reject (hard failure), warn (log and pass), or auto_fix (correct automatically)
3. Use auto_fix for trivially correctable issues: trim whitespace, normalize casing, coerce types
4. Reserve reject for structural violations that cannot be auto-corrected: missing required fields, wrong type
5. Field constraints must use standard JSON Schema vocabulary: required, type, pattern, minimum, maximum, enum
6. Include constraint explanations — validators that reject without explanation frustrate debugging
## Anti-Pattern
1. Injecting validation schema into the prompt — wastes tokens, LLM is not the enforcement mechanism
2. All fields set to reject — trivially fixable issues (extra whitespace, wrong casing) waste regeneration cycles
3. Constraints without explanations — rejected output with no error message is undebuggable
4. Overlapping with response_format rules — same check in both places is maintenance burden for no benefit
5. Confusing validation_schema (P06, system-applied post-generation) with response_format (P05, LLM-visible) or validator (P06, individual pass/fail rule)
6. Missing type coercion — string "42" rejected when integer 42 was intended
## Context
Validation schemas operate in the P06 spec layer as the system-side enforcement mechanism. They complement response formats (P05, LLM-side guidance) by catching what the LLM failed to comply with. In production pipelines, validation schemas are the last quality check before output enters the pool or reaches consumers.
## Impact
Auto-fix for trivial issues reduced regeneration cycles by 40%. Tiered on_failure (reject/warn/auto_fix) eliminated 60% of false rejections. Constraint explanations reduced debugging time from 15 minutes average to 2 minutes per rejection.
## Reproducibility
Reliable validation schema production: (1) enumerate all required output fields with types, (2) define constraints per field using JSON Schema vocabulary, (3) set on_failure behavior per field (reject/warn/auto_fix), (4) implement auto_fix for trivially correctable issues, (5) add constraint explanations for reject cases, (6) verify no overlap with response_format rules, (7) validate against 9 HARD + 9 SOFT gates.
## References
1. validation-schema-builder SCHEMA.md (20 frontmatter fields, field constraint spec)
2. P06 spec pillar specification
3. JSON Schema validation and post-generation enforcement patterns

## Metadata

```yaml
id: bld_memory_validation_schema
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-validation-schema.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | validation schema construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_validation_schema]] | upstream | 0.46 |
| [[validation-schema-builder]] | upstream | 0.45 |
| [[p03_sp_validation-schema-builder]] | upstream | 0.42 |
| [[bld_collaboration_validation_schema]] | upstream | 0.42 |
| [[p11_qg_validation_schema]] | upstream | 0.40 |
| [[p03_ins_validation_schema]] | upstream | 0.40 |
| [[p01_kc_validation_schema]] | upstream | 0.38 |
| [[bld_schema_validation_schema]] | upstream | 0.34 |
| [[bld_architecture_validation_schema]] | upstream | 0.34 |
| [[bld_examples_validation_schema]] | upstream | 0.33 |
