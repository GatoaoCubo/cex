---
kind: architecture
id: bld_architecture_enum_def
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of enum_def — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Enum Def"
version: "1.0.0"
author: n03_builder
tags: [enum_def, builder, examples]
tldr: "Golden and anti-examples for enum def construction, demonstrating ideal structure and common pitfalls."
domain: "enum def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p11_qg_enum_def
  - p03_sp_enum_def_builder
  - enum-def-builder
  - bld_instruction_enum_def
  - p10_lr_enum_def_builder
  - bld_collaboration_enum_def
  - bld_knowledge_card_enum_def
  - p01_kc_enum_def
  - p06_enum_def
  - bld_schema_enum_def
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| value | A single named member of the enumeration | enum_def | required |
| description | Per-value prose explanation of meaning and usage | enum_def | required |
| default | The value assumed when none is provided | enum_def | optional |
| extensible | Declares whether the set is closed or open for future values | enum_def | required |
| deprecated | Values retained for backward compatibility but no longer recommended | enum_def | optional |
| representations | Framework-specific serialization forms | enum_def | recommended |
| type_def | Structural type that may reference this enum as a field constraint | P06 | consumer |
| input_schema | Validation contract that uses enum_def to constrain field values | P06 | consumer |
| validator | Pass/fail rule that checks membership against this enum | P06 | consumer |
| guardrail | Governance constraint — which enums may be extended or deprecated | P11 | external |

## Dependency Graph
```
domain_context  --produces--> value
value           --produces--> description
value           --produces--> representations
extensible      --constrains--> value
deprecated      --depends-->  value
type_def        --depends-->  value
input_schema    --depends-->  value
validator       --depends-->  value
guardrail       --depends-->  extensible
```
| From | To | Type | Data |
|------|----|------|------|
| domain_context | value | produces | named constants from domain vocabulary |
| value | description | produces | per-value semantic meaning |
| value | representations | produces | framework-specific serialization |
| extensible | value | constrains | whether new values may be added without version bump |
| deprecated | value | depends | deprecated must be subset of values |
| type_def | value | depends | type fields reference enum values as constraints |
| input_schema | value | depends | schema fields use enum membership for validation |
| validator | value | depends | validator checks input against allowed value set |
| guardrail | extensible | depends | governance policy on open vs closed enums |

## Boundary Table
| enum_def IS | enum_def IS NOT |
|-------------|----------------|
| A finite list of named string values | An abstract type with methods or computed properties (that is type_def) |
| A constraint applied to a single field | A full validation contract for a data shape (that is input_schema) |
| A reusable definition referenced by many schemas | A pass/fail rule evaluated at runtime (that is validator) |
| A closed set (or declared-open set) of options | A single fixed value with no alternatives (that is constant) |
| Versioned — deprecated values stay until major bump | A prose definition of a concept (that is glossary_entry) |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| definition | value, description | Declare the finite set and explain each member |
| contract | extensible, deprecated | State the stability guarantees and migration path |
| representation | representations | Map the set to framework-specific forms |
| governance | guardrail | Apply extensibility and deprecation policies |
| consumers | type_def, input_schema, validator | Runtime artifacts that reference this enum |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_enum_def]] | downstream | 0.49 |
| [[p03_sp_enum_def_builder]] | upstream | 0.43 |
| [[enum-def-builder]] | upstream | 0.41 |
| [[bld_instruction_enum_def]] | upstream | 0.39 |
| [[p10_lr_enum_def_builder]] | downstream | 0.38 |
| [[bld_collaboration_enum_def]] | downstream | 0.35 |
| [[bld_knowledge_card_enum_def]] | upstream | 0.34 |
| [[p01_kc_enum_def]] | upstream | 0.33 |
| [[p06_enum_def]] | upstream | 0.32 |
| [[bld_schema_enum_def]] | upstream | 0.31 |
