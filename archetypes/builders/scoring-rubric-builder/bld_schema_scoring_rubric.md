---
kind: schema
id: bld_schema_scoring_rubric
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for scoring_rubric
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Scoring Rubric"
version: "1.0.0"
author: n03_builder
tags: [scoring_rubric, builder, examples]
tldr: "Golden and anti-examples for scoring rubric construction, demonstrating ideal structure and common pitfalls."
domain: "scoring rubric construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_golden_test
  - bld_schema_reranker_config
  - bld_schema_unit_eval
  - bld_schema_usage_report
  - bld_schema_smoke_eval
  - bld_schema_quickstart_guide
  - bld_schema_guardrail
  - bld_schema_retriever_config
  - bld_schema_search_strategy
  - bld_schema_action_prompt
---

# Schema: scoring_rubric
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_sr_{framework_slug}) | YES | — | Namespace compliance |
| kind | literal "scoring_rubric" | YES | — | Type integrity |
| pillar | literal "P07" | YES | — | Pillar assignment |
| title | string "Rubric: {name}" | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| framework | string | YES | — | Framework name (5D, 12LP, costm) |
| target_kinds | list[string] | YES | — | Artifact kinds this rubric evaluates |
| dimensions_count | integer >= 3 | YES | — | Number of evaluation dimensions |
| total_weight | literal 100 | YES | 100 | Weights must sum to 100% |
| threshold_golden | float | YES | 9.5 | GOLDEN tier floor |
| threshold_publish | float | YES | 8.0 | PUBLISH tier floor |
| threshold_review | float | YES | 7.0 | REVIEW tier floor |
| automation_status | enum (manual, semi-automated, automated) | YES | — | How dimensions are checked |
| domain | string | YES | — | Domain this rubric covers |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| calibration_set | list[string] | REC | — | golden_test refs for anchoring |
| inter_rater_agreement | float 0.0-1.0 | REC | — | Reliability measure |
| appeals_process | string | REC | — | How to contest a score |
| density_score | float 0.80-1.00 | REC | — | Content density |
| linked_artifacts | object {primary, related} | REC | — | Cross-references |
## ID Pattern
Regex: `^p07_sr_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Framework Overview` — what it measures, why, and for which artifact kinds
2. `## Dimensions` — table: name, weight(%), scale, criteria, examples
3. `## Thresholds` — 4-tier table: GOLDEN/PUBLISH/REVIEW/REJECT with score ranges and actions
4. `## Calibration` — examples at each tier with rationale (link golden_tests)
5. `## Automation` — status per dimension (manual/semi/automated) with tool refs
## Constraints
- max_bytes: 5120 (body only)
- naming: p07_sr_{framework_slug}.md
- id == filename stem
- dimension weights MUST sum to exactly 100%
- dimensions_count MUST be >= 3
- all 4 tier thresholds MUST be present
- criteria MUST be concrete (no subjective language)
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_golden_test]] | sibling | 0.70 |
| [[bld_schema_reranker_config]] | sibling | 0.65 |
| [[bld_schema_unit_eval]] | sibling | 0.65 |
| [[bld_schema_usage_report]] | sibling | 0.65 |
| [[bld_schema_smoke_eval]] | sibling | 0.65 |
| [[bld_schema_quickstart_guide]] | sibling | 0.64 |
| [[bld_schema_guardrail]] | sibling | 0.64 |
| [[bld_schema_retriever_config]] | sibling | 0.64 |
| [[bld_schema_search_strategy]] | sibling | 0.64 |
| [[bld_schema_action_prompt]] | sibling | 0.64 |
