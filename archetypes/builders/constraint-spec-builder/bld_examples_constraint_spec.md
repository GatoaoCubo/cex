---
kind: examples
id: bld_examples_constraint_spec
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of constraint_spec artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.1
title: "Examples Constraint Spec"
version: "1.0.0"
author: n03_builder
tags: [constraint_spec, builder, examples]
tldr: "Golden and anti-examples for constraint spec construction, demonstrating ideal structure and common pitfalls."
domain: "constraint spec construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Examples: constraint-spec-builder
## Golden Example
INPUT: "Create constraint spec for JSON output with specific schema"
OUTPUT:
```yaml
id: p03_constraint_json_product
kind: constraint_spec
pillar: P03
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "Product Data JSON Constraint"
quality: null
tags: [constraint_spec, P03, constraint]
tldr: "Product Data JSON Constraint — production-ready constraint_spec configuration"
```
## Overview
JSON schema constraint ensuring LLM outputs valid product data objects.
Applied at decode time where supported; falls back to output_validator post-generation.

## Constraint Definition
Type: json_schema
```json
{
  "type": "object",
  "required": ["name", "price", "category"],
  "properties": {
    "name": {"type": "string", "maxLength": 200},
    "price": {"type": "number", "minimum": 0},
    "category": {"type": "string", "enum": ["electronics", "home", "fashion", "food"]}
  },
  "additionalProperties": false
}
```
Temperature override: 0.3 (lower for structured output reliability).
Max tokens: 500 (bounded to prevent runaway generation).

## Provider Compatibility
| Provider | Support | Method |
|----------|---------|--------|
| OpenAI | native | response_format: json_schema |
| Anthropic | partial | tool_use with schema |
| Outlines | native | JSON guide from schema |
| LMQL | partial | where clause + type hint |
Fallback: inject schema in prompt + output_validator post-check.

## Integration
- Injected into: prompt_template as generation constraint
- Validated by: p05_oval_product_schema (post-generation safety net)
- Used by: product listing pipeline, data extraction workflows
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p03_constraint_ pattern (H02 pass)
- kind: constraint_spec (H04 pass)
- All required fields present (H06 pass)
- Body has all 4 sections: Overview, Constraint Definition, Provider Compatibility, Integration (H07 pass)
- Parameters table with value and rationale (S03 pass)
- tldr under 160 chars (S01 pass)
- tags >= 3 items, includes "constraint_spec" (S02 pass)
## Anti-Example
INPUT: "Create constraint for structured output"
BAD OUTPUT:
```yaml
id: structured-output
kind: constraint
quality: 9.0
tags: [constraint]
```
FAILURES:
1. id has hyphens and no p03_constraint_ prefix -> H02 FAIL
2. kind: 'constraint' not 'constraint_spec' -> H04 FAIL
3. Missing fields: constraint_type, pattern -> H06 FAIL
4. quality: 9.0 (not null) -> H05 FAIL
5. No ## Constraint Definition section -> H07 FAIL
6. No provider compatibility table -> S04 FAIL
