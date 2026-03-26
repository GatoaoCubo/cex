---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for quality_gate
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: quality_gate

## Frontmatter Fields
| Field | Type | Required | Default |
|-------|------|----------|---------|
| id | string (p11_qg_{slug}) | YES | — |
| kind | literal "quality_gate" | YES | — |
| lp | literal "P11" | YES | — |
| title | string "Gate: {name}" | YES | — |
| version | semver string | YES | "1.0.0" |
| created | date YYYY-MM-DD | YES | — |
| updated | date YYYY-MM-DD | YES | — |
| author | string | YES | — |
| domain | string (what this gate protects) | YES | — |
| quality | null | YES | null |
| tags | list[string], len >= 3, includes "quality-gate" | YES | — |
| tldr | string < 160ch | YES | — |
| density_score | float 0.80-1.00 | REC | — |

## Body Structure (required sections)
1. Definition — metric, threshold, operator, scope
2. Checklist — HARD gates, all must pass
3. Scoring — SOFT gates, weighted dimensions summing to 100%
4. Actions — pass/fail consequences
5. Bypass — conditions, approver, audit trail

## Constraints
- max_bytes: 4096 (body only)
- naming: p11_qg_{gate_slug}.md
- id == filename stem
- threshold MUST be numeric
- scoring weights MUST sum to 100%
- quality: null always
