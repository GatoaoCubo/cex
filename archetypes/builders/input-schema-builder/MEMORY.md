---
id: p10_lr_input_schema_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: edison
observation: "Input schemas with required fields that have default values create caller confusion — callers provide the default and the system rejects it as unnecessary. Optional fields without defaults force callers to handle None unexpectedly. Using 'any' or 'object' as a type without coercion rules causes silent data corruption downstream. Informative error messages that name the failing field and expected type reduce debug time by ~60% compared to generic 'validation error' messages."
pattern: "Every field must have: type (specific, not 'any'), required (boolean), and if optional then a default value. Required fields never have defaults. Optional fields always have defaults. Coercion rules must be declared explicitly when the input type differs from the processing type (e.g., string->int). Error messages must name the field and the expected type, not just say 'invalid input'."
evidence: "8 input schema reviews: 5 of 8 had required fields with defaults (caller confusion). 6 of 8 had at least one optional field without a default (None propagation bug). 3 of 8 used 'any' type on at least one field (silent coercion failure in 2 cases). Error messages with field names reduced caller debug time from avg 12min to avg 5min."
confidence: 0.70
outcome: SUCCESS
domain: input_schema
tags: [input-schema, validation, coercion, typed-fields, error-messages, contracts]
tldr: "Required fields never have defaults. Optional fields always have defaults. Every field needs a specific type. Error messages must name the failing field."
impact_score: 7.0
decay_rate: 0.05
satellite: edison
keywords: [input_schema, validation, required, optional, default, coercion, type, error_message, contract]
---

## Summary

Input schemas define the contract between a caller and a component. The most common failure mode is semantic confusion between required and optional: a required field with a default is a contradiction, and an optional field without a default creates None propagation bugs. Getting these two rules right eliminates the majority of runtime validation failures.

## Pattern

Field definition rules (all three must hold):

1. **Type specificity** - Use `string`, `integer`, `boolean`, `list`, `object`. Never `any` or `mixed`. If the raw input type differs from the processing type, declare a coercion rule.
2. **Required/optional semantics** - `required: true` means caller must provide it, no default. `required: false` means caller may omit it, default must be declared.
3. **Error message quality** - Each field's error message must include: field name, expected type/format, and what was received. Generic messages ("validation failed") are prohibited.

Coercion rule format: `coerce: "string -> integer via int()"` — explicit source type, target type, and conversion function. Declare coercion whenever accepting loose input (e.g., form data, CLI args, LLM output).

Input schemas cover only what goes in. Do not add response shapes or output fields — that is an interface contract (different artifact type).

## Anti-Pattern

- `required: true` with a `default` value — contradictory, creates caller confusion.
- `required: false` with no `default` — causes None to propagate silently through processing.
- `type: "any"` — disables type checking, causes silent coercion failures downstream.
- Generic error message ("invalid input") — forces callers to read source code to debug.
- Adding response/output shapes to the input schema — scope creep into interface territory.
- Fields list as a flat string instead of structured objects — unparseable by validators.

## Context

Pattern emerged from reviewing integration failures where callers passed technically valid data that still caused runtime errors. In most cases the schema was syntactically correct but semantically ambiguous: required fields had defaults (so callers didn't know if they needed to provide them), and optional fields had no defaults (so None reached downstream logic that assumed a value). Fixing these two rules at schema-authoring time eliminates an entire class of runtime bugs.

## Impact

- Caller confusion from required+default contradiction: eliminated by rule enforcement
- None propagation bugs from optional-without-default: eliminated by rule enforcement
- Silent coercion failures: eliminated by prohibiting `any` type
- Caller debug time for validation errors: avg 12min -> avg 5min with informative messages

## Reproducibility

Apply to every input schema regardless of domain. The required/optional/default triad is universal. Coercion rules are only needed when accepting loose input formats. Error message quality applies always.

## References

- Field type enum: CONFIG.md
- Schema examples: EXAMPLES.md
- Validation logic: QUALITY_GATES.md
