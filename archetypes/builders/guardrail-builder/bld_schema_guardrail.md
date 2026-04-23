---
kind: schema
id: bld_schema_guardrail
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for guardrail
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Guardrail"
version: "1.0.0"
author: n03_builder
tags: [guardrail, builder, examples]
tldr: "Golden and anti-examples for guardrail construction, demonstrating ideal structure and common pitfalls."
domain: "guardrail construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_golden_test
  - bld_schema_smoke_eval
  - bld_schema_output_validator
  - bld_schema_unit_eval
  - bld_schema_retriever_config
  - bld_schema_runtime_state
  - bld_schema_usage_report
  - bld_schema_action_prompt
  - bld_schema_e2e_eval
  - bld_schema_reranker_config
---

# Schema: guardrail
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p11_gr_{scope_slug}) | YES | — | Namespace compliance |
| kind | literal "guardrail" | YES | — | Type integrity |
| pillar | literal "P11" | YES | — | Pillar assignment |
| title | string "Guardrail: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| scope | string | YES | — | What this guardrail protects |
| severity | enum (critical, high, medium, low) | YES | — | Impact classification |
| enforcement | enum (block, warn, log) | YES | — | How violation is handled |
| applies_to | list[string] | YES | — | Agent kinds or pipeline stages |
| domain | string | YES | — | Domain this guardrail covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| bypass_approver | string | REC | — | Who can override |
| remediation | string | REC | — | How to fix a violation |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
| density_score | float 0.80-1.00 | REC | — | Content density |
## ID Pattern
Regex: `^p11_gr_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Definition` — what it protects and why (threat model)
2. `## Rules` — numbered, concrete, measurable restrictions
3. `## Violations` — specific examples of what breaks this guardrail
4. `## Enforcement` — how violations are detected (automated/manual) and handled
5. `## Bypass` — conditions, approver, audit trail
## Constraints
- max_bytes: 4096 (body only)
- naming: p11_gr_{scope_slug}.md
- id == filename stem
- severity MUST be valid enum
- enforcement MUST be valid enum
- rules MUST be concrete (no subjective language)
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_golden_test]] | sibling | 0.67 |
| [[bld_schema_smoke_eval]] | sibling | 0.66 |
| [[bld_schema_output_validator]] | sibling | 0.65 |
| [[bld_schema_unit_eval]] | sibling | 0.65 |
| [[bld_schema_retriever_config]] | sibling | 0.65 |
| [[bld_schema_runtime_state]] | sibling | 0.65 |
| [[bld_schema_usage_report]] | sibling | 0.65 |
| [[bld_schema_action_prompt]] | sibling | 0.64 |
| [[bld_schema_e2e_eval]] | sibling | 0.64 |
| [[bld_schema_reranker_config]] | sibling | 0.64 |
