---
kind: schema
id: bld_schema_e2e_eval
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for e2e_eval
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema E2E Eval"
version: "1.0.0"
author: n03_builder
tags: [e2e_eval, builder, examples]
tldr: "Golden and anti-examples for e2e eval construction, demonstrating ideal structure and common pitfalls."
domain: "e2e eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_unit_eval
  - bld_schema_smoke_eval
  - bld_schema_golden_test
  - bld_schema_usage_report
  - bld_schema_action_prompt
  - bld_schema_retriever_config
  - bld_schema_dataset_card
  - bld_schema_handoff_protocol
  - bld_schema_output_validator
  - bld_schema_memory_scope
---

# Schema: e2e_eval
## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_e2e_{pipeline_slug}) | YES | — | Namespace compliance |
| kind | literal "e2e_eval" | YES | — | Type integrity |
| pillar | literal "P07" | YES | — | Pillar assignment |
| title | string | YES | — | Human label |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | — | Creation date |
| updated | date YYYY-MM-DD | YES | — | Last update |
| author | string | YES | — | Producer identity |
| pipeline | string | YES | — | Pipeline being tested |
| stages | list[object] | YES | — | Ordered pipeline stages |
| input | string | YES | — | Pipeline entry data |
| expected_output | string | YES | — | Final pipeline result |
| timeout | integer (seconds) | YES | 300 | Max execution time |
| environment | string | YES | — | Target environment |
| domain | string | YES | — | Domain scope |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | — | Searchability |
| tldr | string <= 160ch | YES | — | Dense summary |
### Recommended
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| data_fixtures | list[string] | REC | — | Test data for reproducibility |
| cleanup | string | REC | — | Post-test state reset |
| parallel | boolean | REC | false | Stages can run in parallel |
| reporting | string | REC | — | How to report results |
| density_score | float 0.80-1.00 | REC | — | Content density |
## ID Pattern
Regex: `^p07_e2e_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Stage Object Schema
```yaml
- name: "stage_name"
  agent: "agent-name"
  input: "what this stage receives"
  expected_output: "what this stage produces"
  assertion: "verifiable condition on output"
```
## Body Structure (required sections)
1. `## Pipeline Overview` — visual flow of stages
2. `## Stages` — each stage with agent, input, output, assertion
3. `## Data Fixtures` — test data for reproducibility
4. `## Expected Output` — final pipeline result
5. `## Cleanup` — post-test state reset
## Constraints
- max_bytes: 4096 (body only)
- naming: p07_e2e_{pipeline_slug}.md + .yaml
- id == filename stem
- quality: null always
- stages must be non-empty list
- stages must form connected pipeline (output_n -> input_n+1)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_unit_eval]] | sibling | 0.69 |
| [[bld_schema_smoke_eval]] | sibling | 0.66 |
| [[bld_schema_golden_test]] | sibling | 0.65 |
| [[bld_schema_usage_report]] | sibling | 0.64 |
| [[bld_schema_action_prompt]] | sibling | 0.64 |
| [[bld_schema_retriever_config]] | sibling | 0.63 |
| [[bld_schema_dataset_card]] | sibling | 0.63 |
| [[bld_schema_handoff_protocol]] | sibling | 0.63 |
| [[bld_schema_output_validator]] | sibling | 0.63 |
| [[bld_schema_memory_scope]] | sibling | 0.62 |
