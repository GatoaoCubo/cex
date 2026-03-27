---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for validation_schema
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: validation_schema

## Frontmatter Fields

### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p06_vs_{scope}) | YES | — | Namespace compliance |
| kind | literal "validation_schema" | YES | — | Type integrity |
| pillar | literal "P06" | YES | — | Pillar assignment |
| title | string "Validation Schema: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| target_kind | string | YES | — | Artifact kind this schema validates |
| format | enum: json, yaml | YES | — | Expected output format |
| fields_count | integer >= 1 | YES | — | Number of validated fields |
| on_failure | enum: reject, warn, auto_fix | YES | — | System behavior when validation fails |
| strict | boolean | YES | false | If true, reject unknown fields |
| domain | string | YES | — | Domain this schema covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Must include "validation-schema" |
| tldr | string <= 160ch | YES | — | Dense summary |

### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| coercion | boolean | REC | false | Auto-coerce types before validation |
| error_template | string | REC | — | Template for error messages |
| density_score | float 0.80-1.00 | REC | — | Content density |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |

## Fields Object
```yaml
fields:
  - name: "{{field_name}}"
    type: "{{string|integer|number|boolean|array|object}}"
    required: {{true|false}}
    constraints:
      min_length: {{integer}}
      max_length: {{integer}}
      pattern: "{{regex}}"
      enum: [{{value_1}}, {{value_2}}]
      min: {{number}}
      max: {{number}}
```

## ID Pattern
Regex: `^p06_vs_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Schema Overview` — what this schema validates and why
2. `## Fields` — table: name, type, required, constraints
3. `## Failure Handling` — on_failure behavior, error messages, remediation
4. `## Integration` — how the system applies this schema (pipeline position)

## Constraints
- max_bytes: 3072 (body only)
- naming: p06_vs_{scope}.yaml
- machine_format: json
- id == filename stem
- fields_count >= 1
- on_failure MUST be one of: reject, warn, auto_fix
- format MUST be one of: json, yaml
- LLM NEVER sees this schema — system-side only
- quality: null always
