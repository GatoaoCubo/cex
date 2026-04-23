---
id: n00_scoring_rubric_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Scoring Rubric -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, scoring_rubric, p07, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_scoring_rubric
  - bld_collaboration_scoring_rubric
  - bld_schema_reranker_config
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_kind
  - bld_schema_eval_metric
  - bld_schema_search_strategy
  - bld_schema_usage_report
  - p01_kc_scoring_rubric
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Scoring rubric defines a multi-dimensional evaluation criterion used for artifact quality assessment. CEX supports three rubric types: 5D (five weighted quality dimensions), 12LP (12-point checklist for landing pages and content), and custom rubrics for specific kinds. Scoring rubrics are consumed by LLM judges, human reviewers, and the automated cex_score.py tool to produce the quality scores stored in artifact frontmatter.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `scoring_rubric` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Rubric name + target kind |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| rubric_type | enum | yes | 5D / 12LP / custom |
| target_kinds | list | yes | Kinds this rubric applies to |
| dimensions | list | yes | Scoring dimensions with weight and description |
| max_score | float | yes | Maximum achievable score (typically 10.0) |
| pass_threshold | float | yes | Minimum score for publication (typically 8.0) |

## When to use
- Defining quality criteria for a new kind that lacks a rubric
- Customizing the 5D rubric with domain-specific weighting for a specialized artifact type
- Providing the evaluation framework for a new LLM judge or human review process

## Builder
`archetypes/builders/scoring_rubric-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind scoring_rubric --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence defines rubrics; all nuclei follow them
- `{{SIN_LENS}}` -- Analytical Envy: every dimension precisely weighted, no ambiguity
- `{{TARGET_AUDIENCE}}` -- LLM judges, cex_score.py, and human peer reviewers
- `{{DOMAIN_CONTEXT}}` -- artifact type, quality standards, publication requirements

## Example (minimal)
```yaml
---
id: scoring_rubric_5d_standard
kind: scoring_rubric
pillar: P07
nucleus: n01
title: "CEX 5D Standard Scoring Rubric"
version: 1.0
quality: null
---
rubric_type: 5D
max_score: 10.0
pass_threshold: 8.0
target_kinds: [knowledge_card, agent, prompt_template, workflow]
dimensions:
  - {name: D1_structural, weight: 0.30, description: "Frontmatter + required sections present"}
  - {name: D2_rubric, weight: 0.30, description: "Content quality and adherence to kind spec"}
  - {name: D3_semantic, weight: 0.40, description: "Accuracy, density, and domain correctness"}
```

## Related kinds
- `llm_judge` (P07) -- executes scoring using this rubric
- `eval_metric` (P07) -- individual metrics that compose into rubric dimensions
- `validator` (P06) -- structural validation that precedes rubric scoring

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_scoring_rubric]] | upstream | 0.45 |
| [[bld_collaboration_scoring_rubric]] | related | 0.41 |
| [[bld_schema_reranker_config]] | upstream | 0.40 |
| [[bld_schema_integration_guide]] | upstream | 0.39 |
| [[bld_schema_benchmark_suite]] | upstream | 0.38 |
| [[bld_schema_kind]] | upstream | 0.38 |
| [[bld_schema_eval_metric]] | upstream | 0.37 |
| [[bld_schema_search_strategy]] | upstream | 0.37 |
| [[bld_schema_usage_report]] | upstream | 0.37 |
| [[p01_kc_scoring_rubric]] | sibling | 0.36 |
