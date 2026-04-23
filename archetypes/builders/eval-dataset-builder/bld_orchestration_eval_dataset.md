---
kind: collaboration
id: bld_collaboration_eval_dataset
pillar: P12
llm_function: COLLABORATE
purpose: How eval-dataset-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Eval Dataset"
version: "1.0.0"
author: n03_builder
tags: [eval_dataset, builder, examples]
tldr: "Golden and anti-examples for eval dataset construction, demonstrating ideal structure and common pitfalls."
domain: "eval dataset construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - eval-dataset-builder
  - bld_collaboration_golden_test
  - bld_collaboration_regression_check
  - p01_kc_eval_dataset
  - p03_sp_eval_dataset_builder
  - bld_collaboration_unit_eval
  - bld_collaboration_builder
  - bld_collaboration_scoring_rubric
  - bld_collaboration_quality_gate
  - bld_examples_eval_dataset
---

# Collaboration: eval-dataset-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what test cases are in this collection, what is the schema, and how are splits defined?"
I do not evaluate models. I do not define evaluation criteria. I do not produce single reference cases.
I specify curated collections of test cases so evaluation pipelines can run systematic, reproducible LLM assessments.

## Crew Compositions
### Crew: "Evaluation Infrastructure"
```
  1. eval-dataset-builder  -> "test case collection with schema and splits"
  2. scoring-rubric-builder -> "evaluation criteria applied to dataset cases"
  3. benchmark-builder      -> "aggregate performance measurement consuming dataset"
```

### Crew: "LLM Quality Assurance"
```
  1. eval-dataset-builder  -> "eval_dataset artifact (collection of cases)"
  2. golden-test-builder   -> "golden_test artifacts (individual 9.5+ reference cases)"
  3. quality-gate-builder  -> "quality thresholds for accepting/rejecting model outputs"
```

### Crew: "Eval Pipeline Build"
```
  1. eval-dataset-builder  -> "dataset spec with framework integration"
  2. agent-builder         -> "eval runner agent that iterates cases"
  3. formatter-builder     -> "result output formatter (JSON/table/CSV)"
```

## Handoff Protocol
### I Receive
- seeds: task type, LLM behavior under evaluation, schema field names, approximate size
- optional: target framework, split strategy, source type, existing cases to formalize
- context: which model or system is being evaluated (affects schema design)

### I Produce
- eval_dataset artifact (.md + .yaml frontmatter)
- committed to: `cex/P07_evals/examples/p07_ds_{name}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures

## Builders I Depend On
None — independent builder (layer 0). Eval datasets can be defined standalone without other artifacts.

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| benchmark-builder | Benchmarks consume eval_dataset as their test case source |
| scoring-rubric-builder | Rubrics are applied to cases from an eval_dataset |
| agent-builder | Eval runner agents load eval_dataset to iterate cases |
| golden-test-builder | Golden tests may be promoted from eval_dataset cases that score 9.5+ |

## Boundary Handoffs
| If the request is for... | Redirect to |
|--------------------------|-------------|
| A single exemplary case scoring 9.5+ | golden-test-builder |
| Measuring model performance across datasets | benchmark-builder |
| Defining evaluation criteria with weights | scoring-rubric-builder |
| A quick 1-5 case sanity check | smoke-eval-builder |
| A single isolated function test | unit-eval-builder |
Always state the boundary reason explicitly when redirecting.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[eval-dataset-builder]] | upstream | 0.53 |
| [[bld_collaboration_golden_test]] | sibling | 0.47 |
| [[bld_collaboration_regression_check]] | sibling | 0.42 |
| [[p01_kc_eval_dataset]] | upstream | 0.41 |
| [[p03_sp_eval_dataset_builder]] | upstream | 0.41 |
| [[bld_collaboration_unit_eval]] | sibling | 0.40 |
| [[bld_collaboration_builder]] | sibling | 0.40 |
| [[bld_collaboration_scoring_rubric]] | sibling | 0.40 |
| [[bld_collaboration_quality_gate]] | sibling | 0.39 |
| [[bld_examples_eval_dataset]] | upstream | 0.39 |
