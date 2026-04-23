---
quality: 7.7
id: bld_architecture_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Architecture"
version: 1.0.0
quality: 7.3
tags: [builder, value_object, architecture]
llm_function: CONSTRAIN
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_architecture_enum_def
  - bld_schema_input_schema
  - p03_ins_type_def
  - bld_schema_optimizer
  - bld_output_template_function_def
  - p01_kc_type_def
  - p11_qg_enum_def
  - p11_qg_entity_memory
  - bld_schema_boot_config
  - bld_instruction_enum_def
---
# Architecture: value_object
## Pattern Origin
Evans DDD (2003): Value Object = object that describes some characteristic of a thing.
No identity. Two instances with same attribute values are interchangeable.
## Properties (from Evans)
1. No conceptual identity (not tracked as "this specific thing")
2. Immutable (never changed after creation)
3. Structural equality (equal if all attributes equal)
4. Self-contained (carries its own validation at construction time)
5. Side-effect-free (transformation methods return new instances)
## Structural Topology
```
ValueObject {
  attribute_1: Type (constraint)
  attribute_2: Type (constraint)
  equals(other) -> bool  -- structural equality
  hashCode() -> int      -- if hashable
  withX(x) -> ValueObject  -- transformation (new instance)
}
```
## Relationship to Other Kinds
| Kind | Relationship |
|------|-------------|
| aggregate_root | uses value_objects as typed attributes |
| type_def | generic type alias, no domain semantics, no DDD contract |
| enum_def | fixed set of named constants, subset of value object concept |
| input_schema | validates raw input BEFORE constructing value objects |
## Common Value Object Examples
- Money(amount: Decimal, currency: ISO4217)
- Email(address: string, matches: RFC5322)
- Address(street, city, country, zip)
- DateRange(start: Date, end: Date, invariant: start <= end)
- Coordinates(lat: float, lng: float)
## Anti-Patterns
- Mutable value object: breaks referential transparency
- Value object with identity field: use entity instead
- Large value object (>5 attributes): consider decomposing

## Architecture Checklist

- Verify component inventory is complete (no orphans)
- Validate dependency graph has no cycles
- Cross-reference with boundary table for scope correctness
- Test layer map against actual codebase structure

## Architecture Pattern

```yaml
# Architecture validation
components: inventoried
dependencies: acyclic
boundaries: defined
layers: mapped
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_doctor.py --scope architecture
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_enum_def]] | downstream | 0.22 |
| [[bld_schema_input_schema]] | related | 0.21 |
| [[p03_ins_type_def]] | upstream | 0.21 |
| [[bld_schema_optimizer]] | related | 0.21 |
| [[bld_output_template_function_def]] | upstream | 0.21 |
| [[p01_kc_type_def]] | sibling | 0.20 |
| [[p11_qg_enum_def]] | downstream | 0.19 |
| [[p11_qg_entity_memory]] | downstream | 0.18 |
| [[bld_schema_boot_config]] | related | 0.17 |
| [[bld_instruction_enum_def]] | upstream | 0.17 |
