---
kind: schema
id: bld_schema_permission
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for permission
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Permission"
version: "1.0.0"
author: n03_builder
tags: [permission, builder, examples]
tldr: "Golden and anti-examples for permission construction, demonstrating ideal structure and common pitfalls."
domain: "permission construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_golden_test
  - bld_schema_smoke_eval
  - bld_schema_guardrail
  - bld_schema_action_prompt
  - bld_schema_retriever_config
  - bld_schema_usage_report
  - bld_schema_unit_eval
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_reranker_config
---

# Schema: permission
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_perm_{scope_slug}) | YES | — | Namespace compliance |
| kind | literal "permission" | YES | — | Type integrity |
| pillar | literal "P09" | YES | — | Pillar assignment |
| title | string "Permission: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| scope | string | YES | — | What resource this permission controls |
| roles | list[string] | YES | — | Roles that can hold this permission |
| read | enum (allow, deny, conditional) | YES | — | Read access level |
| write | enum (allow, deny, conditional) | YES | — | Write access level |
| execute | enum (allow, deny, conditional) | YES | — | Execute access level |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
| domain | string | YES | — | Domain this permission covers |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| inheritance | string | REC | — | Role hierarchy description |
| escalation | string | REC | — | How to request elevated access |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
| density_score | float 0.80-1.00 | REC | — | Content density |
## ID Pattern
Regex: `^p09_perm_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Scope` — what resource or artifact is controlled
2. `## Access Matrix` — table of role x action (read/write/execute)
3. `## Allow List` — explicit allowed role-action pairs
4. `## Deny List` — explicit denied role-action pairs (overrides allow)
5. `## Audit` — what access events get logged
6. `## Escalation` — how to request elevated access
## Constraints
- max_bytes: 3072 (body only)
- naming: p09_perm_{scope_slug}.md
- id == filename stem
- read/write/execute MUST be valid enum (allow, deny, conditional)
- deny_list overrides allow_list
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_golden_test]] | sibling | 0.60 |
| [[bld_schema_smoke_eval]] | sibling | 0.60 |
| [[bld_schema_guardrail]] | sibling | 0.60 |
| [[bld_schema_action_prompt]] | sibling | 0.59 |
| [[bld_schema_retriever_config]] | sibling | 0.59 |
| [[bld_schema_usage_report]] | sibling | 0.59 |
| [[bld_schema_unit_eval]] | sibling | 0.59 |
| [[bld_schema_handoff_protocol]] | sibling | 0.58 |
| [[bld_schema_output_validator]] | sibling | 0.58 |
| [[bld_schema_reranker_config]] | sibling | 0.58 |
