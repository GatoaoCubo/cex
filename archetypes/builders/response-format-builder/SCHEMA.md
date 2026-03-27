---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for response_format
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: response_format

## Frontmatter Fields

### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p05_rf_{format_slug}) | YES | — | Namespace compliance |
| kind | literal "response_format" | YES | — | Type integrity |
| pillar | literal "P05" | YES | — | Pillar assignment |
| title | string "Response Format: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| target_kind | string | YES | — | Artifact kind that uses this format |
| format_type | enum: json, yaml, markdown, csv, plaintext | YES | — | Output format |
| injection_point | enum: system_prompt, user_message | YES | — | Where format is injected |
| sections | list[string] | YES | — | Ordered output sections |
| sections_count | integer >= 1 | YES | — | Number of output sections |
| domain | string | YES | — | Domain this format covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Must include "response-format" |
| tldr | string <= 160ch | YES | — | Dense summary |

### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| example_output | string | REC | — | Concrete example of expected output |
| composable | boolean | REC | false | Can combine with other formats |
| density_score | float 0.80-1.00 | REC | — | Content density |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |

## ID Pattern
Regex: `^p05_rf_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Body Structure (required sections)
1. `## Format Overview` — what output structure this defines and for which task
2. `## Sections` — ordered list of sections with description and constraints
3. `## Example Output` — complete example showing expected shape
4. `## Injection Instructions` — how to inject this format into the prompt

## Constraints
- max_bytes: 4096 (body only)
- naming: p05_rf_{format_slug}.yaml
- machine_format: json
- id == filename stem
- sections_count >= 1
- format_type MUST be one of: json, yaml, markdown, csv, plaintext
- injection_point MUST be one of: system_prompt, user_message
- LLM SEES this format — write as clear instructions
- quality: null always
