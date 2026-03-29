---
id: p10_lr_enum_def_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "Enum artifacts without per-value descriptions caused consumer ambiguity in 5 of 8 integration reviews — developers chose wrong values for edge cases (e.g., 'inactive' vs 'archived' vs 'deprecated' used interchangeably). Enums with descriptions for every value had zero misuse across the same review set."
pattern: "Write descriptions for every value. Declare extensible explicitly. Mirror values list in frontmatter to body section names exactly. Keep body under 1024 bytes. Deprecated values stay in the list until major version."
evidence: "8 integration reviews: 5 had value misuse without descriptions; 0 misuse with descriptions. 3 breaking changes traced to removing deprecated values without major version bump."
confidence: 0.75
outcome: SUCCESS
domain: enum_def
tags: [enum-def, per-value-descriptions, extensibility, deprecation, value-naming, composability]
tldr: "Per-value descriptions prevent misuse. Declare extensible. Mirror values to body. Deprecated stays until major bump."
impact_score: 7.5
decay_rate: 0.05
satellite: edison
keywords: [enum, enumeration, values, descriptions, extensible, deprecated, naming, JSON Schema, Pydantic, Zod, GraphQL, TypeScript]
---

## Summary
Enumerations appear simple — a list of strings — but consumer misuse concentrates in two decisions made at spec time: whether each value has a clear description, and whether the set is declared open or closed. Both are invisible during happy-path use and expensive to diagnose when wrong values propagate through a system.
A value named `inactive` without a description will be confused with `archived`, `deprecated`, and `disabled` by different developers. An enum declared without `extensible` forces consumers to guess whether exhaustive match is safe — guessing wrong causes runtime panics in strongly-typed languages.
## Pattern
**Per-value descriptions and explicit extensibility declaration.**
Description rules:
- Every value gets exactly one sentence in frontmatter `descriptions` map
- The sentence answers: "use this value when X happens; do NOT use it when Y"
- Body `## Values` section expands each value to 1-2 sentences with context
Extensibility rules:
- `extensible: false` — set is closed; consumers may use exhaustive switch/match
- `extensible: true` — new values expected; consumers MUST handle unknown values gracefully
- Default to `false` unless the domain is explicitly open-ended
Value naming rules:
- Pick one convention per enum: SCREAMING_SNAKE or lowercase — never mix
- SCREAMING_SNAKE: use for GraphQL enums and constants referenced in code
- lowercase: use for JSON/REST APIs and TypeScript string literal unions
- Never use spaces, hyphens, or camelCase in enum values
Deprecation rules:
- Deprecated values remain in `values` list until major version bump
- Document reason and migration: "use PUBLISHED instead; removed in v2.0"
- `deprecated: []` preferred over omitting the field — explicit empty set aids tooling
Body budget (1024 bytes max): Overview (80) + Values (500) + Usage (250) + Constraints (150) = ~980.
## Anti-Pattern
- Omitting descriptions: consumers cannot distinguish similar values; misuse is silent.
- Missing `extensible` declaration: exhaustive match may panic on unknown values in production.
- Mixed case convention in one enum (DRAFT and published together): serialization parity breaks.
- Removing deprecated values without a major version bump: breaks consumers using exhaustive match.
- Single-value enum: that is a constant; use constant-builder or just inline the value.
- Values list in frontmatter not matching body `## Values` section names: spec drift; validation catches it but wastes a build cycle.
- Confusing enum_def with type_def: an enum_def is a CLOSED VALUE SET; a type_def defines abstract structure with constraints and methods. If you are defining a struct with fields, use type-def-builder.
- Encoding workflow logic in value names (STATUS_WAITING_FOR_HUMAN_REVIEW): workflow belongs in a process spec, not an enum value name.
## Context
The 1024-byte body limit for enum_def is tight. Write the values list in frontmatter first (forces scope decision before prose), then allocate body bytes from a fixed budget. The `descriptions` frontmatter map is the machine-readable form; the body `## Values` section is the human-readable expansion. Both must be present and consistent. Framework representations in `## Usage` are load-bearing for consumers who copy-paste into their codebase — at minimum provide JSON Schema + one of Pydantic/Zod/TypeScript.
