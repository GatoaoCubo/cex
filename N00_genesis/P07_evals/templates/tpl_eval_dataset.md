---
id: p07_eval_dataset
kind: eval_dataset
8f: F3_inject
pillar: P07
version: 1.0.0
title: "Template — Eval Dataset"
tags: [template, eval, dataset, benchmark, testing]
tldr: "A curated set of input-output pairs for evaluating LLM performance. Defines test cases, expected outputs, scoring rubric, and pass/fail thresholds."
quality: 9.0
updated: "2026-04-07"
domain: "evaluation and testing"
author: n03_builder
created: "2026-04-07"
density_score: 0.97
related:
  - p07_eval_research_outputs
  - bld_examples_eval_dataset
  - bld_collaboration_eval_dataset
  - eval-dataset-builder
  - p07_ds_training_dataset_quality_metrics
  - p01_kc_eval_dataset
  - p10_lr_few_shot_example_builder
  - bld_examples_few_shot_example
  - p07_dataset_rag_qa_v1
  - bld_output_template_few_shot_example
---

# Eval Dataset: [DATASET_NAME]

## Purpose
[WHAT capability this dataset evaluates — accuracy, format compliance, domain knowledge]

## Dataset Schema
```yaml
id: "[DATASET_ID]"
size: [10 | 50 | 100 | 500]
domain: "[DOMAIN]"
difficulty: [easy | medium | hard | mixed]
created: "[YYYY-MM-DD]"
```

## Test Cases

| # | Input | Expected Output | Tags |
|---|-------|----------------|------|
| 1 | [INPUT_1] | [EXPECTED_1] | [easy, format] |
| 2 | [INPUT_2] | [EXPECTED_2] | [medium, accuracy] |
| 3 | [INPUT_3] | [EXPECTED_3] | [hard, edge_case] |

## Scoring Rubric

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| Accuracy | 0.4 | Output matches expected (exact or semantic) |
| Format | 0.3 | Correct structure, frontmatter, sections |
| Completeness | 0.2 | All required fields present |
| Conciseness | 0.1 | No unnecessary verbosity |

## Pass/Fail Thresholds
| Level | Score | Meaning |
|-------|-------|---------|
| Pass | ≥ 0.8 | Production ready |
| Marginal | 0.6-0.8 | Needs improvement |
| Fail | < 0.6 | Unacceptable |

## Dataset Maintenance
- **Update frequency**: [monthly | quarterly | on_model_change]
- **Add cases when**: New failure pattern discovered in production
- **Remove cases when**: No longer relevant (deprecated kind/feature)
- **Version**: Track dataset version separately from model version

## Quality Gate
- [ ] ≥ 10 test cases (minimum for statistical relevance)
- [ ] Mix of easy/medium/hard difficulty
- [ ] Expected outputs manually verified
- [ ] Scoring rubric has ≥ 3 dimensions

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_eval_research_outputs]] | sibling | 0.35 |
| [[bld_examples_eval_dataset]] | related | 0.33 |
| [[bld_collaboration_eval_dataset]] | downstream | 0.32 |
| [[eval-dataset-builder]] | related | 0.29 |
| [[p07_ds_training_dataset_quality_metrics]] | sibling | 0.28 |
| [[p01_kc_eval_dataset]] | related | 0.26 |
| [[p10_lr_few_shot_example_builder]] | downstream | 0.25 |
| [[bld_examples_few_shot_example]] | related | 0.24 |
| [[p07_dataset_rag_qa_v1]] | sibling | 0.23 |
| [[bld_output_template_few_shot_example]] | upstream | 0.23 |
