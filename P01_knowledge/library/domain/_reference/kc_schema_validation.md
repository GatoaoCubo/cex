---
id: p01_kc_schema_validation
kind: knowledge_card
type: domain
pillar: P01
title: Schema Validation -- Types, Enums, Interfaces, Validators
version: 1.0.0
created: '2026-03-29'
author: orchestrator
domain: schema
origin: manual
quality: 9.0
tags:
- schema
- validation
- pydantic
- json-schema
- zod
tldr: Type defs, enums, interfaces, validators using Pydantic/Zod/JSON Schema for LLM contracts
when_to_use: Defining I/O contracts, type systems, or validation rules
feeds_kinds:
- type_def
- enum_def
- interface
- validation_schema
- validator
density_score: 0.85
updated: "2026-04-07"
---

## Quick Reference
| Framework | Validator | CEX Kind |
|-----------|-----------|----------|
| Pydantic BaseModel | Python | type_def, validator |
| JSON Schema | Universal | validation_schema |
| Zod z.object | TypeScript | type_def, interface |
| GraphQL enum | API | enum_def |
| Instructor | Python | validator |

## Key Concepts
- **Type Def**: complex type with fields and constraints (Pydantic model)
- **Enum Def**: finite set of allowed values (provider list, status codes)
- **Interface**: contract between systems (input/output agreement)
- **Validator**: runtime constraint check (range, format, semantic)
- **Validation Schema**: declarative rules (JSON Schema)

## Patterns
| Trigger | Action |
|---------|--------|
| LLM input needs contract | Define input_schema |
| Fixed set of options | Create enum_def |
| Two systems exchange data | Define interface |
| Output needs runtime check | Apply validator |

## Anti-Patterns
- Validating with prompts instead of schemas
- Enum with 50+ values (use lookup table)
- Interface without version

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_schema_validation`
- **Tags**: 

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_schema_validation`
- **Tags**: 

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |
