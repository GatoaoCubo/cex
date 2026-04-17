---
id: bld_schema_saga
kind: schema
pillar: P06
llm_function: CONSTRAIN
purpose: "Formal schema -- SINGLE SOURCE OF TRUTH for saga"
quality: null
title: "Schema: saga"
version: "1.0.0"
author: builder
tags: [schema, saga, P12]
domain: "distributed orchestration"
created: "2026-04-17"
updated: "2026-04-17"
density_score: null
---

# Schema: saga

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p12_saga_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "saga" | YES | - | Type integrity |
| pillar | literal "P12" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Version |
| saga_name | string | YES | - | Business transaction name |
| steps_count | integer | YES | - | Must match step list |
| topology | enum: choreography, orchestration | YES | orchestration | Coordination style |
| on_failure | enum: compensate_all, compensate_partial, abort | YES | compensate_all | Saga-level failure policy |
| domain | string | YES | - | Business domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "saga" |
| tldr | string <= 160ch | YES | - | Dense summary |
| created | date YYYY-MM-DD | YES | - | Creation date |

## ID Pattern
Regex: `^p12_saga_[a-z][a-z0-9_]+$`

## Body Structure (required sections)
1. `## Goal` -- one-sentence business transaction outcome
2. `## Steps` -- table: id, participant, action, compensating_action, on_failure
3. `## Rollback Sequence` -- ordered list of compensating actions on failure
4. `## Topology` -- choreography or orchestration, with participant diagram

## Constraints
- max_bytes: 4096
- naming: p12_saga_{name_slug}.md
- EVERY step MUST have compensating_action (non-empty)
- steps_count MUST match actual step count
- quality: null always
