---
kind: knowledge_card
id: bld_knowledge_card_enum_def
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for enum_def production — enumeration specification
sources: JSON Schema draft-07, Pydantic v2, Zod v3, GraphQL spec June 2018, TypeScript 5.x
quality: 9.1
title: "Knowledge Card Enum Def"
version: "1.0.0"
author: n03_builder
tags: [enum_def, builder, examples]
tldr: "Golden and anti-examples for enum def construction, demonstrating ideal structure and common pitfalls."
domain: "enum def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_config_enum_def
  - p10_lr_enum_def_builder
  - bld_examples_enum_def
  - bld_instruction_enum_def
  - p11_qg_enum_def
  - p03_sp_enum_def_builder
  - enum-def-builder
  - bld_schema_enum_def
  - bld_collaboration_enum_def
  - bld_architecture_enum_def
---

# Domain Knowledge: enum_def
## Executive Summary
Enumerations are finite named value sets that constrain a field to a known list of options. They are the simplest form of schema constraint — no methods, no structural nesting, no computed properties. An enum_def is reusable: defined once, referenced by many schemas, types, and validators. They must declare extensibility (open vs closed) and handle deprecation explicitly, because consumers (especially exhaustive match in TypeScript/Rust/Swift) rely on the set being stable.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P06 (Schema) |
| llm_function | CONSTRAIN (restricts field values) |
| Min values | 2 (1 value = constant) |
| Value naming | SCREAMING_SNAKE or lowercase — consistent within enum |
| Default | optional; must be member of values |
| Extensible | false = closed/exhaustive; true = open/future values expected |
| Deprecated | subset of values; removal only on major version |
## Framework Patterns
- **JSON Schema**: `{"type": "string", "enum": ["draft", "published", "archived"]}` — values are literals; `const` is single-value form (not enum_def).
- **Pydantic**: `class PublicationStatus(str, Enum): DRAFT = "draft"` — inherit `(str, Enum)` for JSON-serializable enums; `StrEnum` (Python 3.11+) as alternative.
- **Zod**: `z.enum(["draft", "published", "archived"])` — takes readonly string tuple; `.exclude()`/`.extract()` allow sub-enums; `z.nativeEnum()` bridges TS enums.
- **GraphQL**: `enum PublicationStatus { DRAFT PUBLISHED ARCHIVED }` — values ALWAYS SCREAMING_SNAKE_CASE (spec requirement); client receives string form.
- **TypeScript**: `type PublicationStatus = "draft" | "published" | "archived"` — string literal unions preferred; `const enum` for internal use; avoid numeric enums.
## Patterns
| Pattern | When to use | Example |
|---------|-------------|---------|
| Closed enum | Domain has fixed finite states | HTTP methods: GET, POST, PUT, DELETE |
| Open enum | Domain evolves; new values expected | Plugin categories, user-defined tags |
| Lifecycle enum | Ordered state machine states | draft -> review -> published -> archived |
| Category enum | Unordered classification set | artifact kind, pillar code, log level |
| Flag-like enum | Values combined additively | permissions: READ, WRITE, ADMIN |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Single-value enum | Use constant-builder; enum implies choice |
| Values without descriptions | Consumer cannot distinguish similar values (ACTIVE vs ENABLED) |
| Mixed case convention | DRAFT and published in same enum breaks serialization parity |
| Missing extensible declaration | Consumers cannot safely use exhaustive match |
| Removing deprecated values without major bump | Breaks consumers with exhaustive match |
| Embedding business logic in enum names | STATUS_WAITING_FOR_APPROVAL is a workflow state, not a value |
| Using enums for open-ended categories | If values grow unboundedly, use taxonomy or tag system |
## Application
1. Identify: what field is being constrained? What are all meaningful distinct values?
2. Name: pick a case convention and apply it uniformly across all values
3. Describe: write one sentence per value explaining meaning and when to use it
4. Declare: extensible true/false, default if applicable, deprecated if any
5. Represent: produce JSON Schema + at least one of Pydantic/Zod/TypeScript
6. Validate: >= 2 values, all deprecated in values, default in values, body <= 1024 bytes
## References
- JSON Schema draft-07: `enum` and `const` keywords
- Pydantic v2: enum field validation
- Zod v3: z.enum(), z.nativeEnum()
- GraphQL June 2018 spec: enum type definition
- TypeScript handbook: string literal types, const enums

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_config_enum_def]] | downstream | 0.51 |
| [[p10_lr_enum_def_builder]] | downstream | 0.50 |
| [[bld_examples_enum_def]] | downstream | 0.49 |
| [[bld_instruction_enum_def]] | downstream | 0.47 |
| [[p11_qg_enum_def]] | downstream | 0.46 |
| [[p03_sp_enum_def_builder]] | downstream | 0.46 |
| [[enum-def-builder]] | downstream | 0.44 |
| [[bld_schema_enum_def]] | downstream | 0.43 |
| [[bld_collaboration_enum_def]] | downstream | 0.42 |
| [[bld_architecture_enum_def]] | downstream | 0.37 |
