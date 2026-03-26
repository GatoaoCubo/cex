---
id: type-def-builder-architecture
kind: architecture
pillar: P08
llm_function: CONSTRAIN
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: EDISON
tags: [architecture, type-def, P08, boundary]
---

## Boundary Description

`type_def` declares reusable, abstract type vocabulary in the CEX spec layer. It is a named type declaration — not a contract, not a rule, not an executable artifact. It provides the shared type language that other artifacts reference via `$ref` or `type_ref`.

## NAO EH Table (All P06 Siblings)

| Kind | Why NOT type_def |
|---|---|
| `input_schema` | Concrete entry contract for a specific operation; references type_defs but is not one |
| `validator` | Executable pass/fail rule applied at runtime; governs data, does not declare types |
| `interface` | Bilateral integration contract between two agents; defines handshake, not vocabulary |
| `validation_schema` | Post-generation output contract; governs artifact quality, not type declarations |
| `artifact_blueprint` | Structural spec for artifact generation; describes what to build, not what types exist |
| `grammar` | Formal generative constraint (BNF, EBNF, regex, FSM); governs syntax, not type system |

## Decision Question

> "Am I declaring what this type IS (its shape, constraints, and vocabulary), or am I declaring how something USES it?"

- **Declaring what it IS** → `type_def`
- **Declaring how a specific operation receives it** → `input_schema`
- **Declaring pass/fail rules** → `validator`
- **Declaring agent-to-agent contract** → `interface`

## Position Diagram

```
CEX Spec Layer (P06)
├── type_def          ← YOU ARE HERE (vocabulary layer)
│     └── referenced by →
├── input_schema      (concrete entry contracts)
├── validator         (executable rules)
├── interface         (bilateral contracts)
├── validation_schema (output contracts)
├── artifact_blueprint (generation specs)
└── grammar           (formal constraints)
```

## Dependency Graph

```
KNOWLEDGE.md (P01)       --> type-def-builder (informs domain vocabulary)
SCHEMA.md (P06)          --> type-def-builder (source of truth for fields)
type_def artifact        --> input_schema builder (referenced as field types)
type_def artifact        --> validator builder (type assertions reference type_defs)
type_def artifact        --> grammar builder (terminal symbols may ref type_defs)
type-def-builder         --> independent of interface, validation_schema, artifact_blueprint
```

Arrow key:
- `A --> B` means A is consumed by / produces input for B
- `independent of` means no data flow in either direction

## Fractal Position

```
CEX
└── archetypes
    └── builders
        └── type-def-builder        ← this builder
            └── produces: p06_td_*.yaml
                └── consumed by: input_schema_builder, validator_builder, grammar_builder
```

type_def sits at the **vocabulary foundation** of the spec layer. It has no upstream artifact dependencies (only domain knowledge) but is downstream-referenced by most other P06 kinds.
