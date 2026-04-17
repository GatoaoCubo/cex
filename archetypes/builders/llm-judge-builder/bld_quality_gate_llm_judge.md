---
id: p11_qg_llm_judge
kind: quality_gate
pillar: P11
title: "Gate: llm_judge"
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
domain: "LLM-as-Judge configuration — automated quality evaluators with declared model, criteria, scale, and calibration examples"
quality: 9.0
tags: [quality-gate, llm-judge, P07, evals, criteria, scale, few-shot]
tldr: "Pass/fail gate for llm_judge artifacts: judge_model presence, criteria completeness, scale anchors, few-shot calibration, and boundary compliance."
density_score: 0.90
llm_function: GOVERN
---
# Gate: llm_judge
## Definition
| Field | Value |
|---|---|
| metric | llm_judge artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: llm_judge` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p07_judge_[a-z][a-z0-9_]+$` | ID contains uppercase, spaces, hyphens, or wrong prefix |
| H03 | ID equals filename stem | `id: p07_judge_foo` but file is `p07_judge_bar.md` |
| H04 | Kind equals literal `llm_judge` | `kind: scorer` or `kind: rubric` or any other value |
| H05 | Quality field is null | `quality: 7.5` or any non-null value |
| H06 | All required fields present | Missing `judge_model`, `criteria`, or `scale` |
| H07 | judge_model is a concrete model identifier | `judge_model: "a good model"` or empty string |
| H08 | criteria list has at least one item | `criteria: []` or criteria field absent |
| H09 | scale has min, max, and at least 2 anchors | Scale defined without anchor labels |
| H10 | Artifact is a judge config, not a pipeline blocker | Artifact conditionally halts execution flow (that is quality_gate P11) |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Criteria independence | 1.0 | Each criterion measures exactly one quality aspect; no overlap between criteria |
| Scale anchor quality | 1.0 | Anchors define concrete observable behaviors, not vague labels like "good" or "bad" |
| Few-shot coverage | 1.0 | At least 2 examples present; covers both high and low score ends of scale |
| Few-shot rationale quality | 1.0 | Each example has chain-of-thought rationale explaining score assignment |
| Judge model apownteness | 0.5 | Model is from different family than likely evaluated model (reduces self-enhancement bias) |
| Framework mapping | 0.5 | Framework field set and integration pattern documented |
| Chain-of-thought declaration | 0.5 | chain_of_thought field explicitly set; rationale provided if false |
| Temperature setting | 0.5 | temperature <= 0.2 for reproducibility; reason documented if higher |
| Aggregation method | 0.5 | aggregation declared for multi-criteria judges |
| Boundary clarity | 1.0 | Explicitly not a scoring_rubric (no model), not a quality_gate (no block), not a benchmark |
| Domain specificity | 1.0 | Criteria and few-shot examples specific to the declared evaluation domain |
| pass_threshold declaration | 0.5 | pass_threshold set when judge feeds a binary decision downstream |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Experimental judge under active calibration — few-shot examples not yet finalized |
| approver | Author self-certification with calibration plan and deadline |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 7d — experimental judges must reach >= 7.0 or be removed |
| never_bypass | H01 (unparseable YAML breaks all tooling), H05 (self-scored gates corrupt quality metrics), H07 (missing judge_model means the artifact is a scoring_rubric, not a judge) |
