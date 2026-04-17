---
id: p10_lr_enum_def_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
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
agent_group: edison
keywords: [enum, enumeration, values, descriptions, extensible, deprecated, naming, JSON Schema, Pydantic, Zod, GraphQL, TypeScript]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.1
title: "Memory Enum Def"
density_score: 0.90
llm_function: INJECT
---
## Summary
Enumerations appear simple but consumer misuse concentrates in two spec-time decisions: whether each value has a clear description, and whether the set is declared open or closed. A value named `inactive` without a description will be confused with `archived`, `deprecated`, and `disabled`. An enum without `extensible` forces consumers to guess whether exhaustive match is safe — guessing wrong causes runtime panics in strongly-typed languages.
## Pattern
**Per-value descriptions and explicit extensibility declaration.**

Description rules:
1. Every value gets exactly one sentence in frontmatter `descriptions` map
2. The sentence answers: "use this value when X; do NOT use it when Y"
3. Body `## Values` section expands each value to 1-2 sentences with context

Extensibility rules:
1. `extensible: false` — closed set; consumers may use exhaustive switch/match
2. `extensible: true` — new values expected; consumers MUST handle unknown values
3. Default to `false` unless the domain is explicitly open-ended

Value naming rules:
1. Pick one convention: SCREAMING_SNAKE or lowercase — never mix within one enum
2. SCREAMING_SNAKE: GraphQL enums and code constants
3. lowercase: JSON/REST APIs and TypeScript string literal unions

Deprecation rules:
1. Deprecated values remain in `values` list until major version bump
2. Document reason and migration: "use PUBLISHED instead; removed in v2.0"
3. `deprecated: []` preferred over omitting the field — explicit empty set aids tooling
## Anti-Pattern
1. Omitting descriptions: consumers cannot distinguish similar values; misuse is silent.
2. Missing `extensible` declaration: exhaustive match may panic on unknown values.
3. Mixed case convention (DRAFT and published together): serialization parity breaks.
4. Removing deprecated values without a major version bump: breaks exhaustive match consumers.
5. Single-value enum: that is a constant; use constant-builder or inline the value.

## Metadata

```yaml
id: p10_lr_enum_def_builder
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply p10-lr-enum-def-builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | enum_def |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
