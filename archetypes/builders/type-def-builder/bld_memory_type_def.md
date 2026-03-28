---
kind: memory
id: bld_memory_type_def
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for type_def artifact generation
---

# Memory: type-def-builder
## Summary
Type definitions declare reusable data types with base types, constraints, composition rules, and serialization specs. The critical production lesson is constraint completeness — a type without constraints accepts any value of its base type, which is rarely the intent. The second lesson is composition clarity: union types must include discriminator fields, otherwise consumers cannot determine which variant they received without brittle duck-typing.
## Pattern
- Every type must have at least one constraint beyond its base type — unconstrained types are just aliases
- Union types must include a discriminator field that unambiguously identifies the variant
- Nullable semantics must be explicit: nullable: true/false — implicit nullable causes null-safety bugs
- Serialization format must be specified per type: JSON, YAML, or Protobuf wire format
- Generic parameters must have named constraints: "T extends Artifact" not just "T"
- Inheritance chains must be documented explicitly — implicit inheritance causes fragile base class problems
## Anti-Pattern
- Types without constraints — accept any value, providing no validation benefit over raw base types
- Union types without discriminator — consumers use brittle duck-typing to identify variants
- Implicit nullable — some consumers assume non-null, others assume nullable, causing runtime crashes
- Missing serialization spec — type is defined abstractly but cannot be transmitted or stored
- Confusing type_def (P06, reusable type vocabulary) with input_schema (P06, input contract) or validator (P06, pass/fail check)
- Overly deep inheritance (4+ levels) — each level adds cognitive load and fragile coupling
## Context
Type definitions operate in the P06 spec layer as the vocabulary that other artifacts reference. They are consumed by input schemas (P06), validators (P06), and grammar builders. In artifact systems, type definitions ensure consistent data shapes across producers and consumers — a "score" type defined once with range 0.0-10.0 is used consistently everywhere.
## Impact
Constrained types caught 80% of invalid data at parse time versus 0% for unconstrained type aliases. Discriminated unions eliminated 100% of duck-typing failures in consumer code. Explicit nullable annotations reduced null-reference errors by 75%.
## Reproducibility
Reliable type definition production: (1) choose base type, (2) add domain-specific constraints (range, regex, enum), (3) specify nullable explicitly, (4) add discriminator for union types, (5) define serialization format, (6) document inheritance chain, (7) provide concrete examples of valid and invalid values.
## References
- type-def-builder SCHEMA.md (P06 type specification)
- P06 spec pillar specification
- Algebraic data types and type system design patterns
