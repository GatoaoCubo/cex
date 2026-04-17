---
id: bld_knowledge_card_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Knowledge Card"
version: 1.0.0
quality: 5.3
tags: [builder, value_object, knowledge]
llm_function: INJECT
density_score: 0.96
updated: "2026-04-17"
---
# Knowledge: value_object
## Core Concept
Value Object is the Evans DDD pattern for domain attributes that have no identity.
Equality is structural: two Money(10, USD) instances are identical and interchangeable.
Immutability is absolute: to change a value, construct a new instance.
## When to Use
- Domain attribute is defined entirely by its data (Money, Email, Address)
- Two instances with same data are interchangeable (no tracking needed)
- Attribute has domain-level validation rules
- Attribute participates in rich transformations (add, scale, convert)
## When NOT to Use
- Object needs to be tracked over time (identity): use entity instead
- Simple enum: use enum_def
- Generic type alias without domain semantics: use type_def
- Raw input validation (pre-domain): use input_schema
## Key Properties (from Evans)
1. No identity -- no id/uuid field
2. Immutable -- constructor sets all attributes, no setters
3. Structural equality -- equals() compares all attributes
4. Whole value -- carries validation at construction time (invalid state impossible)
5. Side-effect-free transformations -- withX() returns new instance
## CEX Integration
- Pillar: P06 (Schema)
- Builder: value-object-builder (13 ISOs)
- Related: aggregate_root (P06), type_def (P06), enum_def (P06)
- Produced by: N03 (Engineering)
- max_bytes: 2048
