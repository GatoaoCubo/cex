---
id: p07_ds_training_dataset_quality_metrics
kind: eval_dataset
8f: F3_inject
pillar: P07
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "eval-dataset-builder"
name: "Training Dataset Quality Metrics Evaluation"
size: 150
splits:
  test: 1.0
schema_fields:
  - input
  - expected_output
  - metadata
quality: 9.1
tags: [eval_dataset, training-data-quality, dataset-validation, P07, quality-metrics]
tldr: "150 test cases for evaluating training dataset quality across 7 dimensions: completeness, consistency, diversity, accuracy, balance, deduplication, and noise."
description: "Eval dataset for systems that assess training data quality — covers schema contract validation, metric computation, and quality gate classification."
source: "synthetic"
framework: "braintrust"
task_type: "classification"
language: "en"
license: "MIT"
refresh_cadence: "on-demand"
density_score: 0.88
related:
  - bld_examples_eval_dataset
  - bld_knowledge_card_eval_dataset
  - p07_eval_dataset
  - eval-dataset-builder
  - bld_collaboration_eval_dataset
  - p01_kc_eval_dataset
  - p03_sp_eval_dataset_builder
  - bld_tools_eval_dataset
  - bld_instruction_eval_dataset
  - p01_kc_fine_tuning_dataset_preparation
---
## Overview
Tests quality-assessment systems that ingest training dataset samples and produce structured quality metric reports. Covers all 7 measurable quality dimensions: completeness, consistency, diversity, accuracy, class balance, deduplication, and noise level. Primary users are data pipeline validators, pre-training ingestion gates, and fine-tuning dataset auditors.

Each case presents a training dataset sample or metadata payload; the expected output is a structured quality verdict — a per-dimension score, an aggregate pass/fail, and a list of violations found. This collection is evaluation-only: no training use because the underlying validator is rule-based.

## Schema

### input
Type: dict
A training dataset batch descriptor with two required keys: `sample` (list of dicts, each a training example with `input` and `output` keys) and `metadata` (dict with `task_type`, `expected_size`, and `schema_fields`).
Example: `{"sample": [{"input": "What is 2+2?", "output": "4"}, {"input": "What is 2+2?", "output": "four"}], "metadata": {"task_type": "qa", "expected_size": 500, "schema_fields": ["input", "output"]}}`

### expected_output
Type: dict
Structured quality assessment with keys: `passed` (bool), `aggregate_score` (float 0.0–1.0), `dimension_scores` (dict mapping dimension name to float), `violations` (list of strings describing each failure).
Example: `{"passed": false, "aggregate_score": 0.61, "dimension_scores": {"completeness": 1.0, "deduplication": 0.4, "balance": 0.8, "consistency": 1.0, "diversity": 0.5, "accuracy": 0.7, "noise": 0.8}, "violations": ["deduplication: 3 duplicate pairs found", "diversity: only 2 of 7 categories covered"]}`

### metadata
Type: dict
Case-level annotations for filtering, coverage analysis, and failure attribution.
Values: `{dimension: "deduplication", severity: "hard|soft", case_group: "duplicate_exact|duplicate_semantic|balance_skew|missing_field|label_noise|schema_drift|coverage_gap", difficulty: "easy|medium|hard"}`

## Splits
| Split | Percentage | Cases | Rationale |
|-------|-----------|-------|-----------|
| test | 100% | 150 | Pure evaluation — validator is deterministic rule-based logic; no training split needed |

Total: 100% (150 cases)
Split rationale: Quality metric computation for training datasets is rule-based and threshold-driven. Training a model on these cases would introduce leakage between the validator's own calibration data and its test distribution. Eval-only is the correct contract.

Case distribution: 30 cases per dimension (completeness ×30, deduplication ×30, balance ×30, diversity ×30, noise/accuracy ×30). Within each group: 15 clean pass cases, 10 single-violation cases, 5 multi-violation cases.

## Integration
Framework: braintrust
Loading:
```python
import braintrust

project = braintrust.init(project="training-data-quality")
dataset = project.datasets.create(
    name="p07_ds_training_dataset_quality_metrics"
)

for case in dataset.fetch():
    result = validate_training_batch(
        sample=case["input"]["sample"],
        metadata=case["input"]["metadata"]
    )
    dataset.log_feedback(
        id=case["id"],
        scores={
            "passed": int(result["passed"] == case["expected"]["passed"]),
            "score_error": abs(result["aggregate_score"] - case["expected"]["aggregate_score"]),
        }
    )
```
Version migration: v1.x → v2.0 if `dimension_scores` keys change (new dimension added or renamed). Bump minor for new `case_group` values in metadata; patch for data corrections. Never reuse dataset ID across incompatible schemas — create `p07_ds_training_dataset_quality_metrics_v2` instead.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_eval_dataset]] | related | 0.40 |
| [[bld_knowledge_card_eval_dataset]] | upstream | 0.32 |
| [[p07_eval_dataset]] | sibling | 0.30 |
| [[eval-dataset-builder]] | related | 0.29 |
| [[bld_collaboration_eval_dataset]] | downstream | 0.27 |
| [[p01_kc_eval_dataset]] | related | 0.27 |
| [[p03_sp_eval_dataset_builder]] | related | 0.25 |
| [[bld_tools_eval_dataset]] | upstream | 0.24 |
| [[bld_instruction_eval_dataset]] | upstream | 0.24 |
| [[p01_kc_fine_tuning_dataset_preparation]] | upstream | 0.23 |
