---
pillar: P01
llm_function: INJECT
purpose: Distilled patterns for building validation schemas that LLMs and systems actually follow
sources: [JSON Schema draft-07, OpenAPI 3.1, Pydantic v2, Zod, real production schemas]
---

# Domain Knowledge: validation_schema

## What Validation Schemas Do

A validation schema is a structural contract applied AFTER generation to enforce field presence, types, and constraints. It is invisible to the LLM during generation — only the system sees it.

This is the critical distinction: response_format tells the LLM HOW to format output (visible during generation). validation_schema checks WHETHER output conforms (invisible, post-generation). Confusing these two produces artifacts that neither guide nor validate.

## Fields Table Pattern

The proven structure for defining fields:

```
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
```

Every field row must specify all 5 columns. "Notes" carries constraints, relationships, and edge cases that don't fit elsewhere. Omitting Default for required fields uses `—` (em-dash), not blank.

### Field Type Taxonomy

Use JSON-compatible types exclusively: `string`, `integer`, `number`, `boolean`, `array`, `object`. Never invent types (`date` is `string` with a format constraint, not a separate type). Compound types use nesting:

```yaml
fields:
  - name: "campaign_context"
    type: "object"
    required: true
    constraints:
      properties:
        monthly_budget: {type: number, required: true}
        campaign_type: {type: string, enum: [launch, optimization, scaling]}
```

### Required vs Recommended Separation

Split fields into two tables: Required (must be present or artifact is rejected) and Recommended (improves quality but absence is not fatal). This maps directly to HARD vs SOFT gate behavior downstream.

## Constraint Patterns That Work

| Constraint | Syntax | When to Use |
|------------|--------|-------------|
| Regex pattern | `pattern: "^p06_vs_[a-z][a-z0-9_]+$"` | ID formats, naming conventions |
| Enum | `enum: [reject, warn, auto_fix]` | Closed set of valid values |
| Range | `min: 1, max: 100` | Numeric bounds |
| Length | `min_length: 3, max_length: 160` | String size limits |
| Size bounds | `max_bytes: 3072` | Body/payload limits |
| List minimum | `len >= 3` | Tags, keywords requiring diversity |
| Literal | `literal: "quality_gate"` | Kind field, pillar assignment |

### Constraint Composition

Real schemas combine constraints on single fields: `type: string` + `pattern: regex` + `max_length: 160`. Order of evaluation matters — check type first, then format, then content constraints. This prevents confusing error messages ("invalid pattern" on a null value).

## Schema Inheritance

Schemas can inherit from parent schemas and override selectively:

```yaml
inherits: "../../P01_knowledge/_schema.yaml"
nucleus: N01
role: primary
fields_add: {}           # extend parent fields
constraints_override: {} # narrow parent constraints
```

This enables domain-specific schemas (e.g., per-nucleus) while maintaining a single source of truth. The parent defines the universal contract; children add or tighten, never loosen.

## The Derivation Hierarchy

```
SCHEMA (P06) — source of truth, defines fields and constraints
  └── TEMPLATE (P03) — derives structure, adds placeholders
       └── CONFIG (P04) — restricts schema for specific contexts
```

Schema is upstream of everything. If schema changes, template and config must update. Never let template define fields that schema doesn't know about.

## Schema Formats: YAML vs JSON Schema

Two proven formats serve different purposes:

**YAML declarative** (simpler, human-readable):
```yaml
inputs:
  required:
    product_name:
      type: string
      description: Product or service to advertise
    budget:
      type: number
  optional:
    platforms:
      type: list
      items: string
      default: [meta, google]
```

**JSON Schema draft-07** (machine-validatable, tooling-rich):
```json
{
  "type": "object",
  "properties": {
    "product_info": {
      "type": "object",
      "properties": {
        "asin": {"type": "string"},
        "price": {"type": "number"}
      },
      "required": ["asin"]
    }
  },
  "required": ["product_info"]
}
```

Choose YAML when humans are the primary readers. Choose JSON Schema when automated validation tooling must consume it. Both must express the same contract — format is presentation, not substance.

## Failure Handling Modes

Every schema must declare what happens when validation fails:

| Mode | Behavior | When to Use |
|------|----------|-------------|
| `reject` | Block the artifact, return error | Critical fields (id, kind, required data) |
| `warn` | Log warning, allow through | Recommended fields, style checks |
| `auto_fix` | Coerce value to valid form | Type mismatches with safe conversion |

`auto_fix` is powerful but dangerous. Safe coercions: string "42" to integer 42, single string to array ["value"]. Unsafe: truncating content to fit max_length (data loss).

## ID Pattern Enforcement

Every schema should enforce an ID pattern via regex. The pattern encodes the artifact's pillar and kind:

```
^p06_vs_[a-z][a-z0-9_]+$   # validation_schema
^p03_sp_[a-z][a-z0-9_]+$   # system_prompt
^p02_agent_[a-z][a-z0-9_]+$ # agent
```

Additionally enforce: `id == filename stem`. This invariant enables search systems to locate artifacts by ID without a separate index.

## Body Structure Sections

Schema defines which markdown sections the body MUST contain. Pattern:

```
## Body Structure (required sections)
1. `## Overview` — what and why
2. `## Fields` — table with constraints
3. `## Failure Handling` — on_failure behavior
4. `## Integration` — where this fits in the pipeline
```

Number sections explicitly. Each section name becomes a HARD gate check ("body has ## Fields section"). Ambiguous section names ("## Details") create gate-checking headaches.

## Anti-Patterns

| Anti-Pattern | Problem | Fix |
|-------------|---------|-----|
| Too many fields (>25) | LLM ignores excess, validators slow down | Split into required (<=15) + recommended |
| Ambiguous types ("data") | No automated validation possible | Use JSON primitives only |
| Impossible constraints | `min: 10, max: 5` or `required + default: null` | Validate constraint consistency |
| No failure mode | System doesn't know what to do on violation | Always declare on_failure |
| Schema in prompt | Confuses guidance with validation | Schema = post-generation only |
| Loose ID patterns | Collisions, search failures | Enforce pillar+kind prefix |
| Mutable schema without versioning | Breaking changes silently | Always version with semver |

## References

- JSON Schema: https://json-schema.org/specification
- Pydantic v2: https://docs.pydantic.dev/latest/
- OpenAPI 3.1: https://spec.openapis.org/oas/v3.1.0
- Zod: https://zod.dev/
- Guardrails AI: https://www.guardrailsai.com/
