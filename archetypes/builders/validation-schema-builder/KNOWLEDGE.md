---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for validation_schema production
sources: [JSON Schema, OpenAPI, Pydantic, Zod, CEX _schema.yaml]
---

# Domain Knowledge: validation_schema

## Foundational Concepts
Validation schemas originate from data contracts (JSON Schema draft-07/2020-12).
In LLM systems: post-generation structural validation ensures output conformity without constraining the LLM's generation process.
In CEX: formal contracts applied by the system after generation to enforce field presence, types, and constraints.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| JSON Schema | Field types, required, patterns, enums | Field-level constraint model |
| OpenAPI 3.1 | Response schema validation | Post-generation output validation |
| Pydantic v2 | Python runtime type validation with coercion | Coercion and auto_fix pattern |
| Zod | TypeScript runtime validation with parse/safeParse | reject vs warn pattern |
| Guardrails AI | LLM output validation framework | Post-generation validation pipeline |

## Key Principles
- validation_schema is INVISIBLE to the LLM (never injected in prompt)
- Fields must use JSON-compatible types (string, integer, number, boolean, array, object)
- Required fields MUST be present; optional fields MAY be absent
- Constraints are STRUCTURAL (type, format, range) not SEMANTIC (meaning, quality)
- on_failure defines system behavior: reject (block), warn (log), auto_fix (coerce)
- Strict mode rejects unknown fields; lenient mode ignores them
- Coercion converts compatible types before validation (string "42" -> integer 42)

## The P05/P06 Boundary (critical distinction)
| Aspect | response_format (P05) | validation_schema (P06) |
|--------|----------------------|------------------------|
| Who sees it? | LLM (injected in prompt) | System only (post-generation) |
| When applied? | During generation | After generation |
| Purpose | Guide LLM output structure | Enforce structural correctness |
| Failure mode | LLM tries to comply | System rejects/warns/fixes |

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| on_failure | Explicit failure behavior (reject/warn/auto_fix) | Zod: parse vs safeParse |
| strict | Controls unknown field handling | JSON Schema: additionalProperties |
| coercion | Auto-type-coerce before validation | Pydantic: coerce mode |

## Boundary vs Nearby Types
| Type | What it does | NOT this |
|------|-------------|----------|
| response_format (P05) | Tells LLM HOW to format output | LLM sees it during generation |
| validator (P06) | Checks ONE rule pass/fail | Single rule, not structural contract |
| input_schema (P06) | Validates INPUT to a process | Validates entry, not exit |
| grammar (P06) | Constrains DECODER tokens | Applied during generation, not after |

## References
- JSON Schema: https://json-schema.org/specification
- Pydantic v2: https://docs.pydantic.dev/latest/
- Guardrails AI: https://www.guardrailsai.com/
- OpenAPI 3.1: https://spec.openapis.org/oas/v3.1.0
