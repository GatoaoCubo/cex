---
id: type-def-builder-knowledge
kind: knowledge
pillar: P01
llm_function: INJECT
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [knowledge, type-def, P01, type-theory]
---

## Foundational Concept

A type definition declares an abstract, reusable type within a type system. Unlike an instance schema (which constrains a specific input), a type_def establishes named vocabulary — base types, composition rules, constraints, and serialization specs — that other artifacts reference by name. This mirrors TypeScript `type` aliases, Python `TypedDict`, JSON Schema `$defs`, and GraphQL custom scalars.

Type theory distinguishes: **base types** (primitives: string, integer, boolean, array, object, enum), **composite types** (union `|`, intersection `&`, tuple, record), and **algebraic types** (sum types = tagged unions, product types = structs). CEX type_def supports all three.

## Industry Table

| Ecosystem | Equivalent Construct | Key Feature |
|---|---|---|
| TypeScript | `type Alias = ...` / `interface` | Structural typing, generics, union/intersection |
| JSON Schema | `$defs` + `$ref` | Draft 2020-12, composition via `allOf/anyOf/oneOf` |
| Python | `TypedDict`, `dataclass`, `NewType` | Runtime optional, mypy enforcement |
| GraphQL | Custom scalar, `type`, `union`, `input` | SDL-declared, introspectable |
| Protobuf | `message`, `enum`, `oneof` | Wire-format serialization, field numbers |
| OpenAPI | `components/schemas` | Reusable schema definitions via `$ref` |

## Key Patterns

- **Newtype pattern**: wrap primitive with semantic identity (`UserId: base string, format uuid`)
- **Discriminated union**: tagged sum type with a `kind`/`type` discriminant field
- **Branded type**: add constraints to a base type without changing its wire representation
- **Opaque type**: hide internal structure, expose only via defined operations
- **Recursive type**: type references itself (e.g., tree nodes, nested expressions)
- **Generic type**: parameterized by one or more type variables (`List<T>`, `Result<T, E>`)
- **Intersection composition**: combine multiple types, all constraints must hold simultaneously
- **Nullable wrapper**: explicit `T | null` modeling with documented nil semantics

## CEX Extensions Table

| CEX Field | Purpose | Equivalent |
|---|---|---|
| `base_type` | Root primitive or composite | JSON Schema `type` |
| `constraints` | Structured constraint set | JSON Schema `properties` on meta-schema |
| `composition` | Union/intersection/tuple rules | JSON Schema `allOf/anyOf/oneOf` |
| `inheritance` | Extends another type_def by id | JSON Schema `$ref` + `allOf` |
| `generics` | Type parameters list | TypeScript generics |
| `nullable` | Explicit null membership | TypeScript `T | null` |
| `serialization` | Wire format rules | Protobuf field options |

## Boundary Table

| Construct | kind | Why NOT type_def |
|---|---|---|
| Entry contract | input_schema | Concrete, specific, not reusable |
| Pass/fail rule | validator | Executable logic, not declaration |
| Agent handshake | interface | Bilateral, runtime-bound |
| Post-gen contract | validation_schema | Governs outputs, not types |
| Generation spec | artifact_blueprint | Describes structure to generate |
| Formal grammar | grammar | BNF/regex/FSM, not type system |

## References

- JSON Schema 2020-12: `$defs`, `$ref`, composition keywords
- TypeScript Handbook: Advanced Types, Utility Types
- "Types and Programming Languages" (Pierce) — algebraic type theory
- GraphQL SDL specification — scalar and type declarations
