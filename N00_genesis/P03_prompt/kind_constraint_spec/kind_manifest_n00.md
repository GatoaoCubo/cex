---
id: n00_constraint_spec_manifest
kind: knowledge_card
8f: F3_inject
pillar: P03
nucleus: n00
title: "Constraint Spec -- Canonical Manifest"
version: 1.0
quality: 8.8
tags: [manifest, constraint_spec, p03, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_constraint_spec
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_usage_report
  - bld_schema_sandbox_spec
  - bld_schema_kind
  - bld_schema_prompt_technique
  - bld_schema_multimodal_prompt
  - bld_schema_nps_survey
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A constraint_spec defines the constrained generation rules that bound what an LLM may produce: output format, token budget, forbidden patterns, required fields, and compliance guardrails. It is consumed at F1 CONSTRAIN in the 8F pipeline to ensure all downstream generation adheres to hard limits before a single token is produced. The output is a machine-readable constraint envelope applied to every builder run.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `constraint_spec` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| max_tokens | integer | yes | Hard token ceiling for this generation scope |
| required_fields | list | yes | Fields that must appear in every output |
| forbidden_patterns | list | no | Regex or literal strings that must not appear |
| output_format | string | yes | Expected format: markdown, json, yaml, html |

## When to use
- When a builder must produce output within strict token, format, or compliance boundaries
- When generating content for regulated domains (legal, medical, finance) that require hard guardrails
- When the 8F F1 CONSTRAIN step needs an explicit, versioned constraint envelope

## Builder
`archetypes/builders/constraint_spec-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind constraint_spec --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cs_landing_page_gen
kind: constraint_spec
pillar: P03
nucleus: n03
title: "Landing Page Generation Constraints"
version: 1.0
quality: null
---
max_tokens: 4096
output_format: html
required_fields: [headline, cta, social_proof]
forbidden_patterns: ["TODO", "placeholder", "lorem ipsum"]
```

## Related kinds
- `context_window_config` (P03) -- token budget allocation that feeds constraint_spec
- `guardrail` (P11) -- runtime safety layer that enforces constraint_spec rules
- `input_schema` (P06) -- schema-level constraints on incoming data
- `prompt_template` (P03) -- template that references constraint_spec for bounded generation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_constraint_spec]] | downstream | 0.43 |
| [[bld_schema_reranker_config]] | downstream | 0.43 |
| [[bld_schema_integration_guide]] | downstream | 0.41 |
| [[bld_schema_benchmark_suite]] | downstream | 0.40 |
| [[bld_schema_usage_report]] | downstream | 0.39 |
| [[bld_schema_sandbox_spec]] | downstream | 0.39 |
| [[bld_schema_kind]] | downstream | 0.39 |
| [[bld_schema_prompt_technique]] | downstream | 0.39 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.39 |
| [[bld_schema_nps_survey]] | downstream | 0.38 |
