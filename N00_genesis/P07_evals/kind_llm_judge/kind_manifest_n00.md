---
id: n00_llm_judge_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Llm Judge -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, llm_judge, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_llm_judge
  - bld_collaboration_llm_judge
  - llm-judge-builder
  - p01_kc_llm_judge
  - judge-config-builder
  - bld_schema_judge_config
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_eval_metric
  - bld_collaboration_judge_config
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
LLM judge configures an LLM-as-Judge evaluation pipeline for automated quality assessment. It defines the judge model, judging prompt, evaluation criteria, output schema, and the integration point where judgment scores are persisted. LLM judge is the executable artifact that implements the evaluation logic specified by a judge_config, serving as the scalable alternative to human reviewers for high-volume quality gates.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `llm_judge` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Judge name + use case |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| judge_config_id | string | yes | ID of the judge_config artifact governing this judge |
| judge_model | string | yes | LLM model acting as judge |
| judging_prompt | string | yes | Full judge prompt template with {{ARTIFACT}} placeholder |
| output_schema | object | yes | Schema for judge output (score, reasoning, pass_fail) |
| invoke_at | enum | yes | F7_govern / post_build / scheduled / on_demand |

## When to use
- Implementing automated quality review for artifact batches at F7 GOVERN
- Replacing manual peer review with calibrated LLM judgment for high-volume pipelines
- Running a quality gate that triggers based on score thresholds before artifact publication

## Builder
`archetypes/builders/llm_judge-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind llm_judge --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence owns; N05 operations runs at F7
- `{{SIN_LENS}}` -- Analytical Envy: impartial, calibrated, consistent judgment
- `{{TARGET_AUDIENCE}}` -- 8F pipeline F7 GOVERN stage consuming judge scores
- `{{DOMAIN_CONTEXT}}` -- artifact type, judging criteria, score thresholds

## Example (minimal)
```yaml
---
id: llm_judge_cex_knowledge_card_quality
kind: llm_judge
pillar: P07
nucleus: n01
title: "Knowledge Card Quality LLM Judge"
version: 1.0
quality: null
---
judge_config_id: judge_config_cex_quality_gate
judge_model: claude-opus-4-6
invoke_at: F7_govern
output_schema:
  score: {type: float, range: [0, 10]}
  reasoning: {type: string}
  pass_fail: {type: bool, threshold: 8.0}
```

## Related kinds
- `judge_config` (P07) -- configuration governing this judge's behavior
- `scoring_rubric` (P07) -- criteria the judge evaluates against
- `output_validator` (P05) -- structural validation that precedes LLM judgment

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_llm_judge]] | upstream | 0.50 |
| [[bld_collaboration_llm_judge]] | downstream | 0.48 |
| [[llm-judge-builder]] | related | 0.47 |
| [[p01_kc_llm_judge]] | sibling | 0.44 |
| [[judge-config-builder]] | related | 0.43 |
| [[bld_schema_judge_config]] | upstream | 0.42 |
| [[bld_schema_reranker_config]] | upstream | 0.41 |
| [[bld_schema_benchmark_suite]] | upstream | 0.40 |
| [[bld_schema_eval_metric]] | upstream | 0.40 |
| [[bld_collaboration_judge_config]] | downstream | 0.40 |
