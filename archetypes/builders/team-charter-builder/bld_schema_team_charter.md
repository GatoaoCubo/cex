---
kind: schema
id: bld_schema_team_charter
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for team_charter
quality: 9.2
title: "Schema Team Charter"
version: "1.0.0"
author: n06_wave8
tags: [team_charter, builder, schema, governance]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for team_charter"
domain: "team_charter construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field               | Type     | Required | Default | Notes |
|---------------------|----------|----------|---------|-------|
| id                  | string   | yes      |         | Pattern: p12_tc_{{mission}}_v{{n}} |
| kind                | string   | yes      |         | Must be "team_charter" |
| pillar              | string   | yes      |         | Must be "P12" |
| title               | string   | yes      |         | Human-readable mission name |
| version             | string   | yes      |         | Semver |
| created             | date     | yes      |         | ISO 8601 date |
| updated             | date     | yes      |         | ISO 8601 date |
| author              | string   | yes      |         | Nucleus or user ID |
| quality             | null     | yes      | null    | Never self-score; peer review assigns |
| tags                | array    | yes      |         | Include "team_charter", mission name |
| charter_id          | string   | yes      |         | Unique ID for this charter instance |
| crew_template_ref   | string   | yes      |         | Path to the crew_template this charter instantiates |
| mission_statement   | string   | yes      |         | One sentence: action + object + deadline + outcome |
| deadline            | datetime | yes      |         | ISO 8601 datetime (hard cutoff) |

### Recommended
| Field               | Type    | Notes |
|---------------------|---------|-------|
| tldr                | string  | One-line summary for index |
| domain              | string  | Mission domain (e.g., "brand_launch", "rag_pipeline") |

## Body Structure
1. **Mission Statement** -- One-sentence contract (action, object, deadline, outcome).
2. **Deliverables** -- Numbered list: artifact kind, pillar path, owner nucleus.
3. **Success Metrics** -- OKR table: Objective + Key Results with numeric thresholds.
4. **Budget** -- Three-field table: tokens (int), time_hours (float), cost_usd (float).
5. **Stakeholders** -- RACI table: role, nucleus/user, responsibility level.
6. **Quality Gate** -- 8F floor and target, plus per-deliverable thresholds.
7. **Escalation Protocol** -- IF-THEN rules triggered by score, timeout, or failure.
8. **Termination Criteria** -- Three conditions: success, failure, timeout with hard values.

## ID Pattern
^p12_tc_[a-z][a-z0-9_]+_v[0-9]+\\.md$

## Constraints
- `crew_template_ref` must resolve to an existing file in `archetypes/` or `P12_*/`.
- `deadline` must be a future datetime at time of charter creation.
- `success_metrics` must include at least one numeric Key Result (e.g., "score >= 9.0").
- `budget.tokens` must be a positive integer; `budget.cost_usd` must be >= 0.
- `escalation_protocol` must reference at least one nucleus or user role as escalation target.
- `termination_criteria.timeout` must align with or be less than `deadline`.
