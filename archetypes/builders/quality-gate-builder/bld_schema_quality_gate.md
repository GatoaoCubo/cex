---
kind: schema
id: bld_schema_quality_gate
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for quality_gate
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: "2.0.0"
quality: 9.1
title: "Schema Quality Gate"
author: n03_builder
tags: [quality_gate, builder, examples]
tldr: "Golden and anti-examples for quality gate construction, demonstrating ideal structure and common pitfalls."
domain: "quality gate construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_golden_test
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_scoring_rubric
  - bld_schema_search_strategy
  - bld_schema_quickstart_guide
  - bld_schema_integration_guide
  - bld_schema_smoke_eval
  - bld_schema_unit_eval
  - bld_schema_guardrail
---

# Schema: quality_gate
## Frontmatter Fields
### Required (12)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p11_qg_{slug}) | YES | — | Namespace compliance |
| kind | literal "quality_gate" | YES | — | Type integrity |
| pillar | literal "P11" | YES | — | Pillar assignment |
| title | string "Gate: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| domain | string | YES | — | What this gate protects |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3, includes "quality-gate" | YES | — | Classification |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended (1)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| density_score | float 0.80-1.00 | REC | — | Content density metric |
## Gate Counts
| Metric | Type | Constraint | Rationale |
|--------|------|------------|-----------|
| hard_gates_count | integer | 8-10 required | <6 too permissive, >12 diminishing returns |
| soft_gates_count | integer | 5-20 recommended | Varies by kind complexity |
| scoring_weights_sum | percentage | MUST equal 100% | Invariant: all SOFT weights sum to 1.0 |
## Body Structure (5 required sections)
1. **Definition** — metric, threshold, operator, scope
2. **HARD Gates** — binary checks, all must pass (AND logic)
3. **SOFT Scoring** — weighted dimensions, each with explicit weight (0.5 or 1.0)
4. **Actions** — pass/fail/tier consequences (GOLDEN >= 9.5, PUBLISH >= 8.0, REVIEW >= 7.0, REJECT < 7.0)
5. **Bypass** — conditions, approver, audit trail, expiry; NEVER bypass H01 or H05
## Constraints
- max_bytes: 4096 (body only)
- naming: p11_qg_{gate_slug}.md
- id == filename stem
- threshold MUST be numeric
- scoring weights MUST sum to 100%
- quality: null always
- HARD gates: universal H01-H06 always present, kind-specific gates extend beyond
- SOFT gates: weight >= 0.5 (never use weight < 0.5)
- Bypass: MUST include condition + approver + audit_log + expiry fields
## Scoring Formula
```
hard_pass = ALL hard gates pass (AND)
soft_score = sum(gate * weight) / sum(weights)
final = hard_pass ? soft_score : 0
```
## ID Pattern
Regex: `^p11_qg_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_golden_test]] | sibling | 0.55 |
| [[bld_schema_reranker_config]] | sibling | 0.55 |
| [[bld_schema_usage_report]] | sibling | 0.54 |
| [[bld_schema_scoring_rubric]] | sibling | 0.54 |
| [[bld_schema_search_strategy]] | sibling | 0.53 |
| [[bld_schema_quickstart_guide]] | sibling | 0.53 |
| [[bld_schema_integration_guide]] | sibling | 0.53 |
| [[bld_schema_smoke_eval]] | sibling | 0.53 |
| [[bld_schema_unit_eval]] | sibling | 0.52 |
| [[bld_schema_guardrail]] | sibling | 0.52 |
