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
Enumerations appear simple but consumer misuse concentrates in two spec-time decisions: whether each value has a clear description, and whether the set is declared open or closed. A value named `inactive` without a description will be confused with `archived`, `deprecated`, and `disabled`. An enum without `extensible` forces consumers to guess whether exhaustive match is safe — guessing wrong causes runtime panics in strongly-typed languages.
## Pattern
**Per-value descriptions and explicit extensibility declaration.**

Description rules:
- Every value gets exactly one sentence in frontmatter `descriptions` map
- The sentence answers: "use this value when X; do NOT use it when Y"
- Body `## Values` section expands each value to 1-2 sentences with context

Extensibility rules:
- `extensible: false` — closed set; consumers may use exhaustive switch/match
- `extensible: true` — new values expected; consumers MUST handle unknown values
- Default to `false` unless the domain is explicitly open-ended

Value naming rules:
- Pick one convention: SCREAMING_SNAKE or lowercase — never mix within one enum
- SCREAMING_SNAKE: GraphQL enums and code constants
- lowercase: JSON/REST APIs and TypeScript string literal unions

Deprecation rules:
- Deprecated values remain in `values` list until major version bump
- Document reason and migration: "use PUBLISHED instead; removed in v2.0"
- `deprecated: []` preferred over omitting the field — explicit empty set aids tooling
## Anti-Pattern
- Omitting descriptions: consumers cannot distinguish similar values; misuse is silent.
- Missing `extensible` declaration: exhaustive match may panic on unknown values.
- Mixed case convention (DRAFT and published together): serialization parity breaks.
- Removing deprecated values without a major version bump: breaks exhaustive match consumers.
- Single-value enum: that is a constant; use constant-builder or inline the value.
