---
kind: schema
id: bld_schema_smoke_eval
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for smoke_eval
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Smoke Eval"
version: "1.0.0"
author: n03_builder
tags: [smoke_eval, builder, examples]
tldr: "Golden and anti-examples for smoke eval construction, demonstrating ideal structure and common pitfalls."
domain: "smoke eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_unit_eval
  - bld_schema_output_validator
  - bld_schema_golden_test
  - bld_schema_retriever_config
  - bld_schema_action_prompt
  - bld_schema_e2e_eval
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_quickstart_guide
  - bld_schema_usage_report
---

# Schema: smoke_eval
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_se_{scope_slug}) | YES | — | Namespace compliance |
| kind | literal "smoke_eval" | YES | — | Type integrity |
| pillar | literal "P07" | YES | — | Pillar assignment |
| title | string | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| scope | string | YES | — | What is being smoke tested |
| critical_path | list[string] | YES | — | Minimum checks in order |
| timeout | integer <= 30 | YES | 30 | Max seconds (MUST be <= 30) |
| assertions | list[object] | YES | — | Fast binary checks |
| fast_fail | boolean | YES | true | Abort on first failure |
| domain | string | YES | — | Domain scope |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| prerequisites | list[string] | REC | — | What must exist before test |
| environment | string | REC | — | Target environment |
| health_check | string | REC | — | Health endpoint or check |
| frequency | string | REC | — | How often to run |
| alerting | string | REC | — | Who to notify on failure |
| density_score | float 0.80-1.00 | REC | — | Content density |
## ID Pattern
Regex: `^p07_se_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Assertion Object Schema
```yaml
- check: "API responds to /health"
  expected: "200 OK"
  timeout_ms: 5000
```
## Body Structure (required sections)
1. `## Critical Path` — ordered minimum checks
2. `## Assertions` — fast binary pass/fail checks
3. `## Prerequisites` — what must exist before running
4. `## On Failure` — what to do when smoke fails
## Constraints
- max_bytes: 3072 (body only — smaller than unit_eval)
- naming: p07_se_{scope_slug}.md
- id == filename stem
- quality: null always
- timeout MUST be <= 30 seconds
- fast_fail MUST be true

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_unit_eval]] | sibling | 0.73 |
| [[bld_schema_output_validator]] | sibling | 0.69 |
| [[bld_schema_golden_test]] | sibling | 0.69 |
| [[bld_schema_retriever_config]] | sibling | 0.68 |
| [[bld_schema_action_prompt]] | sibling | 0.67 |
| [[bld_schema_e2e_eval]] | sibling | 0.67 |
| [[bld_schema_handoff_protocol]] | sibling | 0.67 |
| [[bld_schema_memory_scope]] | sibling | 0.67 |
| [[bld_schema_quickstart_guide]] | sibling | 0.67 |
| [[bld_schema_usage_report]] | sibling | 0.67 |
