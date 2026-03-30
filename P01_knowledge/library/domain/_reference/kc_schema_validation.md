---
id: p01_kc_schema_validation
kind: knowledge_card
type: domain
pillar: P01
title: Schema Validation -- Types, Enums, Interfaces, Validators
version: 1.0.0
created: '2026-03-29'
author: STELLA
domain: schema
origin: manual
quality: 8.5
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
