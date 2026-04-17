---
id: n00_output_validator_manifest
kind: knowledge_card
pillar: P05
nucleus: n00
title: "Output Validator -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, output_validator, p05, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P05 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Output validator defines post-LLM validation logic that checks generated content against structural, semantic, and business-rule constraints before it is returned to the caller or persisted. It operates at F7 GOVERN in the 8F pipeline, acting as the final quality gate. Validation failures trigger retry, correction, or escalation based on configured severity levels.

## Pillar
P05 -- Output

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `output_validator` |
| pillar | string | yes | Always `P05` |
| title | string | yes | Validator name describing what it checks |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| target_kind | string | yes | The kind of artifact being validated |
| rules | list | yes | Ordered validation rules with id, condition, severity |
| on_fail | enum | yes | retry / correct / escalate / reject |
| max_retries | int | no | Maximum retry attempts before escalation (default 2) |
| correction_prompt | string | no | Prompt injected on retry to guide correction |

## When to use
- Enforcing structural completeness (all required frontmatter fields present)
- Blocking hallucinated facts or policy violations before they reach users
- Implementing quality gates in automated pipeline runs where human review is not possible

## Builder
`archetypes/builders/output_validator-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind output_validator --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations implements; N03 engineering designs rules
- `{{SIN_LENS}}` -- Gating Wrath: zero tolerance for malformed or policy-violating output
- `{{TARGET_AUDIENCE}}` -- downstream systems or users receiving validated output
- `{{DOMAIN_CONTEXT}}` -- output type, business rules, acceptable error rate

## Example (minimal)
```yaml
---
id: output_validator_knowledge_card_completeness
kind: output_validator
pillar: P05
nucleus: n05
title: "Knowledge Card Completeness Validator"
version: 1.0
quality: null
---
target_kind: knowledge_card
on_fail: retry
max_retries: 2
rules:
  - {id: has_frontmatter, severity: error}
  - {id: quality_field_null, severity: warn}
```

## Related kinds
- `formatter` (P05) -- transforms output structure; validator checks the result
- `parser` (P05) -- extracts fields from output; validator checks extracted values
- `validation_schema` (P06) -- declarative contract that the validator enforces
