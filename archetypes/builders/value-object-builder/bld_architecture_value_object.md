---
id: bld_architecture_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Architecture"
version: 1.0.0
quality: null
tags: [builder, value_object, architecture]
llm_function: CONSTRAIN
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
