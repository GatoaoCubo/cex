---
kind: schema
id: bld_schema_llm_judge
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for llm_judge
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.1
title: "Schema Llm Judge"
version: "1.0.0"
author: n03_builder
tags: [llm_judge, builder, examples]
tldr: "Golden and anti-examples for llm judge construction, demonstrating ideal structure and common pitfalls."
domain: "llm judge construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_retriever_config
  - bld_schema_golden_test
  - bld_schema_reward_signal
  - bld_schema_constraint_spec
  - bld_schema_output_validator
  - bld_schema_handoff_protocol
  - bld_schema_memory_scope
  - bld_schema_unit_eval
  - bld_schema_smoke_eval
  - bld_schema_scoring_rubric
---

# Schema: llm_judge
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p07_judge_{slug}) | YES | - | Namespace compliance |
| kind | literal "llm_judge" | YES | - | Type integrity |
| pillar | literal "P07" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Human-readable judge name |
| judge_model | string | YES | - | LLM used as evaluator (e.g. "gpt-4o", "claude-3-5-sonnet") |
| criteria | list[string], len >= 1 | YES | - | Named evaluation dimensions |
| scale | map{type, min, max, anchors} | YES | - | Scoring scale definition |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "llm_judge" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What the judge evaluates |
| few_shot | list[map{input, output, score, rationale}] | REC | - | Calibration examples |
| framework | enum: braintrust, deepeval, ragas, promptfoo, openai_evals, costm | REC | - | Eval framework integration |
| temperature | float 0.0-1.0 | REC | 0.0 | Judge inference temperature |
| chain_of_thought | boolean | REC | true | Require rationale before score |
| aggregation | enum: mean, min, max, weighted_sum | REC | mean | Multi-criteria aggregation |
| pass_threshold | float | REC | - | Minimum score to pass |
## ID Pattern
Regex: `^p07_judge_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` — what the judge evaluates, use case, who/what is being judged
2. `## Criteria` — each criterion: name, definition, what high/low scores mean
3. `## Scale` — scale type, anchor labels, how to assign scores
4. `## Few-Shot Examples` — 2+ calibrated examples with input, score, rationale
## Constraints
- max_bytes: 2048 (body only — judge spec with calibration examples)
- naming: p07_judge_{slug}.md (single file)
- machine_format: yaml (compiled artifact)
- id == filename stem
- criteria list MUST match criterion names defined in ## Criteria section
- quality: null always
- NO implementation code in body — spec only
- few_shot examples MUST use the declared scale range

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_retriever_config]] | sibling | 0.62 |
| [[bld_schema_golden_test]] | sibling | 0.61 |
| [[bld_schema_reward_signal]] | sibling | 0.61 |
| [[bld_schema_constraint_spec]] | sibling | 0.61 |
| [[bld_schema_output_validator]] | sibling | 0.61 |
| [[bld_schema_handoff_protocol]] | sibling | 0.60 |
| [[bld_schema_memory_scope]] | sibling | 0.60 |
| [[bld_schema_unit_eval]] | sibling | 0.60 |
| [[bld_schema_smoke_eval]] | sibling | 0.60 |
| [[bld_schema_scoring_rubric]] | sibling | 0.60 |
