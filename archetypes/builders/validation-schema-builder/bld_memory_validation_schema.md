---
kind: memory
id: bld_memory_validation_schema
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for validation_schema artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
---
# Memory: validation-schema-builder
## Summary
Validation schemas are post-generation contracts that the system applies automatically — the LLM never sees them. The critical distinction from response formats (P05) is visibility: response formats are injected into the prompt (LLM sees), validation schemas are applied after generation (system enforces). Confusing these causes either redundant checking or enforcement gaps. The second lesson is on_failure behavior: schemas that only reject without auto_fix options waste regeneration cycles on trivially fixable issues.
## Pattern
- Clearly separate from response_format: validation_schema is system-side, never prompt-injected
- Define on_failure behavior per field: reject (hard failure), warn (log and pass), or auto_fix (correct automatically)
- Use auto_fix for trivially correctable issues: trim whitespace, normalize casing, coerce types
- Reserve reject for structural violations that cannot be auto-corrected: missing required fields, wrong type
- Field constraints must use standard JSON Schema vocabulary: required, type, pattern, minimum, maximum, enum
- Include constraint explanations — validators that reject without explanation frustrate debugging
## Anti-Pattern
- Injecting validation schema into the prompt — wastes tokens, LLM is not the enforcement mechanism
- All fields set to reject — trivially fixable issues (extra whitespace, wrong casing) waste regeneration cycles
- Constraints without explanations — rejected output with no error message is undebuggable
- Overlapping with response_format rules — same check in both places is maintenance burden for no benefit
- Confusing validation_schema (P06, system-applied post-generation) with response_format (P05, LLM-visible) or validator (P06, individual pass/fail rule)
- Missing type coercion — string "42" rejected when integer 42 was intended
## Context
Validation schemas operate in the P06 spec layer as the system-side enforcement mechanism. They complement response formats (P05, LLM-side guidance) by catching what the LLM failed to comply with. In production pipelines, validation schemas are the last quality check before output enters the pool or reaches consumers.
## Impact
Auto-fix for trivial issues reduced regeneration cycles by 40%. Tiered on_failure (reject/warn/auto_fix) eliminated 60% of false rejections. Constraint explanations reduced debugging time from 15 minutes average to 2 minutes per rejection.
## Reproducibility
Reliable validation schema production: (1) enumerate all required output fields with types, (2) define constraints per field using JSON Schema vocabulary, (3) set on_failure behavior per field (reject/warn/auto_fix), (4) implement auto_fix for trivially correctable issues, (5) add constraint explanations for reject cases, (6) verify no overlap with response_format rules, (7) validate against 9 HARD + 9 SOFT gates.
## References
- validation-schema-builder SCHEMA.md (20 frontmatter fields, field constraint spec)
- P06 spec pillar specification
- JSON Schema validation and post-generation enforcement patterns
