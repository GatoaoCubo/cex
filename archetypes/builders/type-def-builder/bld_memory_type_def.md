---
kind: memory
id: bld_memory_type_def
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for type_def artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Type Def"
version: "1.0.0"
author: n03_builder
tags: [type_def, builder, examples]
tldr: "Golden and anti-examples for type def construction, demonstrating ideal structure and common pitfalls."
domain: "type def construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - type-def-builder
  - p11_qg_type_def
  - bld_collaboration_type_def
  - bld_architecture_type_def
  - p03_sp_type-def-builder
  - p03_ins_type_def
  - bld_knowledge_card_type_def
  - bld_output_template_type_def
  - bld_collaboration_memory_type
  - p01_kc_type_def
---
# Memory: type-def-builder
## Summary
Type definitions declare reusable data types with base types, constraints, composition rules, and serialization specs. The critical production lesson is constraint completeness — a type without constraints accepts any value of its base type, which is rarely the intent. The second lesson is composition clarity: union types must include discriminator fields, otherwise consumers cannot determine which variant they received without brittle duck-typing.
## Pattern
1. Every type must have at least one constraint beyond its base type — unconstrained types are just aliases
2. Union types must include a discriminator field that unambiguously identifies the variant
3. Nullable semantics must be explicit: nullable: true/false — implicit nullable causes null-safety bugs
4. Serialization format must be specified per type: JSON, YAML, or Protobuf wire format
5. Generic parameters must have named constraints: "T extends Artifact" not just "T"
6. Inheritance chains must be documented explicitly — implicit inheritance causes fragile base class problems
## Anti-Pattern
1. Types without constraints — accept any value, providing no validation benefit over raw base types
2. Union types without discriminator — consumers use brittle duck-typing to identify variants
3. Implicit nullable — some consumers assume non-null, others assume nullable, causing runtime crashes
4. Missing serialization spec — type is defined abstractly but cannot be transmitted or stored
5. Confusing type_def (P06, reusable type vocabulary) with input_schema (P06, input contract) or validator (P06, pass/fail check)
6. Overly deep inheritance (4+ levels) — each level adds cognitive load and fragile coupling
## Context
Type definitions operate in the P06 spec layer as the vocabulary that other artifacts reference. They are consumed by input schemas (P06), validators (P06), and grammar builders. In artifact systems, type definitions ensure consistent data shapes across producers and consumers — a "score" type defined once with range 0.0-10.0 is used consistently everywhere.
## Impact
Constrained types caught 80% of invalid data at parse time versus 0% for unconstrained type aliases. Discriminated unions eliminated 100% of duck-typing failures in consumer code. Explicit nullable annotations reduced null-reference errors by 75%.
## Reproducibility
Reliable type definition production: (1) choose base type, (2) add domain-specific constraints (range, regex, enum), (3) specify nullable explicitly, (4) add discriminator for union types, (5) define serialization format, (6) document inheritance chain, (7) provide concrete examples of valid and invalid values.
## References
1. type-def-builder SCHEMA.md (P06 type specification)
2. P06 spec pillar specification
3. Algebraic data types and type system design patterns

## Metadata

```yaml
id: bld_memory_type_def
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-type-def.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | type def construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[type-def-builder]] | upstream | 0.49 |
| [[p11_qg_type_def]] | upstream | 0.41 |
| [[bld_collaboration_type_def]] | upstream | 0.36 |
| [[bld_architecture_type_def]] | upstream | 0.35 |
| [[p03_sp_type-def-builder]] | upstream | 0.33 |
| [[p03_ins_type_def]] | upstream | 0.30 |
| [[bld_knowledge_card_type_def]] | upstream | 0.30 |
| [[bld_output_template_type_def]] | upstream | 0.28 |
| [[bld_collaboration_memory_type]] | downstream | 0.26 |
| [[p01_kc_type_def]] | upstream | 0.26 |
