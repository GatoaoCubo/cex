---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for input_schema production
sources: [JSON Schema, OpenAPI requestBody, CEX contract layer]
---

# Domain Knowledge: input_schema

## Foundational Concept
Input schemas are unilateral entry contracts: the receiving system declares what
data it requires, with types, constraints, and defaults. Rooted in JSON Schema
(draft-07+), OpenAPI requestBody, and function signature design. In CEX,
input_schemas sit in the spec layer of P06 — they define data requirements,
not bilateral agreements or abstract types.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| JSON Schema (draft-07+) | Object properties, required, types, defaults | fields structure with types and required |
| OpenAPI requestBody | API input contract with validation | Unilateral input contract pattern |
| TypeScript function params | Typed parameter definitions | Field-level type constraints |
| GraphQL Input Types | Typed input objects for mutations | Structured input with defaults |
| Pydantic BaseModel | Python data validation with defaults | fields + coercion + defaults pattern |

## Key Patterns
- Input schemas are UNILATERAL: the receiver defines what it needs
- Input schemas define FIELDS: named properties with types and constraints
- Fields are REQUIRED or OPTIONAL: optional fields MUST have defaults
- Input schemas support COERCION: "123" -> 123 when type is integer
- Error messages are FIELD-LEVEL: each required field has its own error text
- Input schemas include EXAMPLES: at least one valid payload
- Input schemas are VERSIONED: semver for evolution
- Boundary is CLEAR: input_schema defines shape, validator checks compliance

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| coercion | CEX agents receive mixed-type data from LLMs | Pydantic validators |
| error_messages | Per-field error text for LLM-friendly feedback | JSON Schema errorMessage |
| scope | What operation/agent this input serves | OpenAPI operationId |
| examples | Valid payloads for testing and documentation | OpenAPI examples |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT input_schema |
|------|------------|--------------------------|
| interface (P06) | Bilateral integration contract | Interfaces are bilateral; input_schemas are unilateral |
| type_def (P06) | Abstract type definition | type_defs define reusable types; input_schemas define concrete entry points |
| validator (P06) | Pass/fail validation rule | Validators check rules; input_schemas define expected shape |
| validation_schema (P06) | Post-generation system contract | Applied silently; input_schemas are explicit contracts |
| output_schema (P05/P06) | Output format/validation | Defines what comes OUT; input_schema defines what goes IN |

## References
- JSON Schema: https://json-schema.org/
- OpenAPI requestBody: https://spec.openapis.org/oas/latest.html
- Pydantic: https://docs.pydantic.dev/
