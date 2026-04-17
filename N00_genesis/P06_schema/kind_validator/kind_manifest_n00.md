---
id: n00_validator_manifest
kind: knowledge_card
pillar: P06
nucleus: n00
title: "Validator -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, validator, p06, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P06 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Validator defines a reusable validation rule that can be referenced by multiple validation schemas or quality gates. Each validator encapsulates a single testable assertion (e.g., "frontmatter has required fields", "quality is null or in range 0-10") with pass/fail semantics, severity level, and an error message template. Validators compose into validation schemas and output validators via reference.

## Pillar
P06 -- Schema

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `validator` |
| pillar | string | yes | Always `P06` |
| title | string | yes | Validator name (describes what it checks) |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| check_type | enum | yes | structural / semantic / business_rule / security |
| assertion | string | yes | Human-readable description of the check |
| severity | enum | yes | error / warning / info |
| error_message | string | yes | Template message on failure (may use {field}, {value}) |
| applies_to | list | yes | List of kinds this validator applies to |

## When to use
- Defining a reusable quality gate assertion for pre-commit or pipeline use
- Building a shared validator library that multiple schemas reference
- Implementing a specific H01-H07 gate from the 8F governance framework

## Builder
`archetypes/builders/validator-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind validator --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N05 operations implements and registers validators
- `{{SIN_LENS}}` -- Gating Wrath: one rule, one check, no ambiguity
- `{{TARGET_AUDIENCE}}` -- validation_schema and output_validator instances composing this rule
- `{{DOMAIN_CONTEXT}}` -- artifact type, quality standard, enforcement severity

## Example (minimal)
```yaml
---
id: validator_has_frontmatter
kind: validator
pillar: P06
nucleus: n05
title: "Has Required Frontmatter Fields"
version: 1.0
quality: null
---
check_type: structural
assertion: "Artifact has id, kind, pillar, nucleus, title, version, quality fields"
severity: error
error_message: "Missing required frontmatter field: {field}"
applies_to: [knowledge_card, agent, prompt_template, workflow]
```

## Related kinds
- `validation_schema` (P06) -- composes multiple validators into a full schema
- `output_validator` (P05) -- runtime component that executes these validators
- `scoring_rubric` (P07) -- quality scoring that complements structural validation
