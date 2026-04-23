---
kind: schema
id: bld_schema_few_shot_example
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for few_shot_example
pattern: TEMPLATE derives from this. CONFIG restricts this.
version: "2.0.0"
quality: 9.1
title: "Schema Few Shot Example"
author: n03_builder
tags: [few_shot_example, builder, examples]
tldr: "Golden and anti-examples for few shot example construction, demonstrating ideal structure and common pitfalls."
domain: "few shot example construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_golden_test
  - bld_schema_unit_eval
  - bld_schema_input_schema
  - bld_schema_smoke_eval
  - bld_schema_retriever_config
  - bld_schema_action_prompt
  - bld_schema_output_validator
  - bld_schema_reranker_config
  - bld_schema_handoff_protocol
  - bld_schema_constraint_spec
---

# Schema: few_shot_example
SOURCE OF TRUTH. OUTPUT_TEMPLATE derives from here. CONFIG restricts from here.
## Required Fields (12)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string | YES | — | Pattern: `^p01_fse_[a-z][a-z0-9_]+$`, must equal filename stem |
| kind | literal "few_shot_example" | YES | — | Type integrity |
| pillar | literal "P01" | YES | — | Pillar assignment |
| title | string | YES | — | Human-readable label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| input | string | YES | — | Non-empty task/prompt being demonstrated |
| output | string | YES | — | Non-empty ideal response showing format |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3, includes "few-shot" | YES | — | Classification |
| tldr | string <= 160ch | YES | — | Dense summary |
## Recommended Fields (7)
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| author | string | REC | — | Who produced this example |
| domain | string | REC | — | Artifact kind being exemplified |
| difficulty | enum: easy, medium, hard | REC | — | Complexity tier |
| edge_case | boolean | REC | false | True if tests boundary condition |
| format | string | REC | — | What format this exemplifies |
| explanation | string | REC | — | Why this pair teaches the format |
| keywords | list[string], len >= 3 | REC | — | Search terms |
## Example Counts
| Metric | Type | Constraint | Rationale |
|--------|------|------------|-----------|
| golden_count | integer | >= 1 required | Minimum 1 golden example per builder |
| anti_count | integer | >= 1 required | Minimum 1 anti-example per builder |
| max_golden | integer | <= 3 | Context budget: never exceed 3 golden |
| max_anti | integer | <= 3 | Context budget: never exceed 3 anti |
## Body Structure (3 required sections)
1. **Golden Example** — 3 layers:
   - Frontmatter: every schema field with realistic value
   - Dense Body: concrete domain content, no filler
   - WHY GOLDEN: maps each quality gate to example (`- quality: null (H05 pass)`)
2. **Anti-Example** — 3 layers:
   - Wrong Frontmatter: deliberately violates schema (wrong prefix, missing fields, self-scored quality)
   - Generic Body: filler language, no domain content
   - FAILURES: numbered list of violated gates (`1. id: no p03_sp_ prefix -> H02 FAIL`)
3. **Bridge Table** — gate coverage matrix:
   - Every schema field appears in golden example
   - Every HARD gate referenced in golden (pass) or anti (fail)
   - >= 80% of SOFT gates referenced across both examples
## Gate References
Anti-examples MUST reference gate codes for each failure:
```
1. id: missing p01_fse_ prefix -> H02 FAIL
2. quality: 8.5 (self-scored) -> H05 FAIL
3. tags: only 1 tag -> H06 FAIL (len >= 3)
```
## Constraints
- max_bytes: 5120 (body only) — builder EXAMPLES.md avg 3985B, max 6918B; old 1024 limit was insufficient
- naming: p01_fse_{topic}.md + p01_fse_{topic}.yaml
- id MUST equal filename stem
- input AND output MUST both be non-empty strings
- NO scoring rubric (that is golden_test P07)
- quality MUST be null
- Golden input: specific, names concrete artifact
- Anti input: vague, generic (demonstrates what NOT to do)
- Density test: if replacing a sentence with "blah blah" and example seems complete, it is filler — remove it
## Boundary Rule
few_shot_example SHOWS format. golden_test (P07) EVALUATES quality with scoring rubric.
If your artifact has a rubric or scores, it is NOT a few_shot_example.
## ID Pattern
Regex: `^p01_fse_[a-z][a-z0-9_]+$`
Examples: `p01_fse_kc_frontmatter`, `p01_fse_validator_conditions`, `p01_fse_rag_source_yaml`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_golden_test]] | sibling | 0.56 |
| [[bld_schema_unit_eval]] | sibling | 0.52 |
| [[bld_schema_input_schema]] | sibling | 0.52 |
| [[bld_schema_smoke_eval]] | sibling | 0.51 |
| [[bld_schema_retriever_config]] | sibling | 0.51 |
| [[bld_schema_action_prompt]] | sibling | 0.51 |
| [[bld_schema_output_validator]] | sibling | 0.50 |
| [[bld_schema_reranker_config]] | sibling | 0.50 |
| [[bld_schema_handoff_protocol]] | sibling | 0.50 |
| [[bld_schema_constraint_spec]] | sibling | 0.49 |
