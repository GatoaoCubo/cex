---
kind: schema
id: bld_schema_input_schema
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for input_schema
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: input_schema

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_is_{scope}) | YES | - | Namespace compliance |
| kind | literal "input_schema" | YES | - | Type integrity |
| pillar | literal "P06" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| scope | string | YES | - | What operation/agent this input serves |
| fields | list[object] | YES | - | Field definitions (min 1) |
| coercion | list[object] | REC | null | Type conversion rules |
| examples | list[object] | REC | - | Valid payload examples |
| domain | string | YES | - | Schema domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "input-schema" |
| tldr | string <= 160ch | YES | - | Dense summary |
| keywords | list[string] | REC | - | Brain search terms |
| density_score | float 0.80-1.00 | REC | - | Content density |

## Fields Object

```yaml
fields:
  - name: "topic"
    type: "string"
    required: true
    default: null
    description: "Research topic"
    error_message: "topic is required"
```

Each field MUST have: name, type, required. Optional: default, description, error_message.
Type: string, integer, float, boolean, list, object.

## Coercion Object

```yaml
coercion:
  - from: "string"
    to: "integer"
    rule: "Parse numeric string to int, fail if non-numeric"
```

## ID Pattern
Regex: `^p06_is_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Contract Definition` — what operation this input serves
2. `## Fields` — table with name/type/required/default/description
3. `## Coercion Rules` — type conversion rules (if any)
4. `## Examples` — at least one valid payload

## Constraints
- max_bytes: 3072 (body only)
- naming: p06_is_{scope}.yaml
- machine_format: json (compiled form)
- id == filename stem
- fields MUST have at least 1 entry
- each field MUST have name and type
- optional fields SHOULD have default values
- quality: null always
- input_schema is unilateral — defines what ONE receiver needs
