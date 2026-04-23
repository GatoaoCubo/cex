---
quality: 7.5
id: bld_knowledge_card_value_object
kind: knowledge_card
pillar: P06
title: "Value Object Builder -- Knowledge Card"
version: 1.0.0
quality: 7.3
tags: [builder, value_object, knowledge]
llm_function: INJECT
author: builder
density_score: 0.96
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_architecture_enum_def
  - input-schema-builder
  - bld_architecture_type_def
  - bld_collaboration_enum_def
  - p01_kc_type_def
  - p03_sp_enum_def_builder
  - p11_qg_enum_def
  - p01_kc_schema_validation
  - enum-def-builder
  - type-def-builder
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

## Knowledge Injection Checklist

- Verify domain facts are sourced and citable
- Validate density_score >= 0.85 (no filler content)
- Cross-reference with related KCs for consistency
- Check for outdated facts that need refresh

## Injection Pattern

```yaml
# KC injection at F3
source: verified
density: 0.85+
cross_refs: checked
freshness: current
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_retriever.py --query "{DOMAIN}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_enum_def]] | downstream | 0.21 |
| [[input-schema-builder]] | related | 0.20 |
| [[bld_architecture_type_def]] | downstream | 0.19 |
| [[bld_collaboration_enum_def]] | downstream | 0.18 |
| [[p01_kc_type_def]] | sibling | 0.18 |
| [[p03_sp_enum_def_builder]] | related | 0.17 |
| [[p11_qg_enum_def]] | downstream | 0.16 |
| [[p01_kc_schema_validation]] | sibling | 0.16 |
| [[enum-def-builder]] | related | 0.16 |
| [[type-def-builder]] | related | 0.16 |
