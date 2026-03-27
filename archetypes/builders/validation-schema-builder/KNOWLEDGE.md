---
pillar: P01
llm_function: INJECT
purpose: Distilled patterns for building validation schemas that LLMs and systems actually follow
sources: [JSON Schema draft-07, OpenAPI 3.1, Pydantic v2, Zod, real production schemas]
---

# Domain Knowledge: validation_schema

## Core Concept

Validation schema = structural contract applied AFTER generation to enforce fields, types, constraints. Invisible to LLM during generation (system-only, post-generation). Distinct from response_format which guides LLM DURING generation.

## Fields Table Pattern

```
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
```

- All 5 columns mandatory per row. Default = `--` for required fields
- Split into Required (HARD gate) and Recommended (SOFT gate) tables
- Use JSON types only: `string`, `integer`, `number`, `boolean`, `array`, `object`

## Constraint Patterns

| Constraint | Syntax | Use Case |
|------------|--------|----------|
| Regex | `pattern: "^p06_vs_[a-z][a-z0-9_]+$"` | IDs, naming |
| Enum | `enum: [reject, warn, auto_fix]` | Closed sets |
| Range | `min: 1, max: 100` | Numeric bounds |
| Length | `min_length: 3, max_length: 160` | String limits |
| Size | `max_bytes: 3072` | Payload limits |
| List min | `len >= 3` | Diversity gates |
| Literal | `literal: "quality_gate"` | Kind/pillar |

Compose constraints on single fields: type -> format -> content. Order prevents confusing errors.

## Schema Inheritance

```yaml
inherits: "../../P01_knowledge/_schema.yaml"
fields_add: {}           # extend parent
constraints_override: {} # narrow, never loosen
```

## Derivation Hierarchy

```
SCHEMA (P06) -> TEMPLATE (P03) -> CONFIG (P04)
```

Schema is upstream. Template/config must not define fields schema doesn't know.

## Failure Handling

| Mode | Behavior | When |
|------|----------|------|
| `reject` | Block artifact | Critical fields (id, kind) |
| `warn` | Log, allow through | Recommended fields, style |
| `auto_fix` | Coerce value | Safe conversions only |

Safe: string "42" -> int 42. Unsafe: truncating content (data loss).

## ID Pattern

Enforce via regex: `^p06_vs_[a-z][a-z0-9_]+$`. Invariant: `id == filename stem`.

## Body Structure

Number sections explicitly. Each becomes a HARD gate check:
1. `## Overview` 2. `## Fields` 3. `## Failure Handling` 4. `## Integration`

## Format Choice

- YAML: humans are primary readers
- JSON Schema draft-07: automated validation tooling
- Both express same contract; format is presentation

## Anti-Patterns

| Anti-Pattern | Fix |
|-------------|-----|
| >25 fields | Split: required (<=15) + recommended |
| Ambiguous types ("data") | JSON primitives only |
| Impossible constraints | Validate consistency (min < max) |
| No failure mode | Always declare on_failure |
| Schema in prompt | Schema = post-generation only |
| Loose ID patterns | Enforce pillar+kind prefix |
| No versioning | Always version with semver |
