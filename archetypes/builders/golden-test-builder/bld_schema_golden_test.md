---
kind: schema
id: bld_schema_golden_test
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for golden_test
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Golden Test"
version: "1.0.0"
author: n03_builder
tags: [golden_test, builder, examples]
tldr: "Golden and anti-examples for golden test construction, demonstrating ideal structure and common pitfalls."
domain: "golden test construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_unit_eval
  - bld_schema_retriever_config
  - bld_schema_output_validator
  - bld_schema_smoke_eval
  - bld_schema_action_prompt
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_scoring_rubric
  - bld_schema_constraint_spec
  - bld_schema_usage_report
---

# Schema: golden_test
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_gt_{case_slug}) | YES | — | Namespace compliance |
| kind | literal "golden_test" | YES | — | Type integrity |
| pillar | literal "P07" | YES | — | Pillar assignment |
| title | string "Golden: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| target_kind | string | YES | — | Artifact kind being tested |
| input | string | YES | — | Request/prompt that triggers production |
| golden_output_ref | string | YES | — | Path to golden artifact or "inline" |
| quality_threshold | float >= 9.5 | YES | 9.5 | Golden floor |
| rationale | string | YES | — | Why golden, with gate refs |
| domain | string | YES | — | Domain this test covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| edge_case | boolean | REC | false | Edge case flag |
| reviewer | string | REC | — | Who approved as golden |
| approval_date | date YYYY-MM-DD | REC | — | Approval timestamp |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
| density_score | float 0.80-1.00 | REC | — | Content density |
## ID Pattern
Regex: `^p07_gt_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Input Scenario` — the complete request/prompt (verbatim)
2. `## Golden Output` — the full artifact (no abbreviation, no "...")
3. `## Rationale` — why golden, mapped to gate IDs (H01, S03, etc.)
4. `## Evaluation Criteria` — specific checks this golden validates
## Constraints
- max_bytes: 4096 (body only)
- naming: p07_gt_{case_slug}.md
- id == filename stem
- quality_threshold MUST be >= 9.5
- golden_output MUST be complete (no truncation)
- quality: null always
- rationale MUST reference gate IDs

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_unit_eval]] | sibling | 0.70 |
| [[bld_schema_retriever_config]] | sibling | 0.67 |
| [[bld_schema_output_validator]] | sibling | 0.67 |
| [[bld_schema_smoke_eval]] | sibling | 0.67 |
| [[bld_schema_action_prompt]] | sibling | 0.66 |
| [[bld_schema_handoff_protocol]] | sibling | 0.66 |
| [[bld_schema_memory_scope]] | sibling | 0.65 |
| [[bld_schema_scoring_rubric]] | sibling | 0.65 |
| [[bld_schema_constraint_spec]] | sibling | 0.64 |
| [[bld_schema_usage_report]] | sibling | 0.64 |
