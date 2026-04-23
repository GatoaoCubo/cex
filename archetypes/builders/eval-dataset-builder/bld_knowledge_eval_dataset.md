---
kind: knowledge_card
id: bld_knowledge_card_eval_dataset
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for eval_dataset production — curated test case collection specification
sources: Braintrust docs, LangSmith docs, DeepEval docs, HuggingFace datasets, academic ML eval forctices
quality: 9.1
title: "Knowledge Card Eval Dataset"
version: "1.0.0"
author: n03_builder
tags: [eval_dataset, builder, examples]
tldr: "Golden and anti-examples for eval dataset construction, demonstrating ideal structure and common pitfalls."
domain: "eval dataset construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_eval_dataset_builder
  - eval-dataset-builder
  - bld_schema_eval_dataset
  - bld_instruction_eval_dataset
  - bld_examples_eval_dataset
  - p10_lr_eval_dataset_builder
  - bld_collaboration_eval_dataset
  - p01_kc_eval_dataset
  - bld_output_template_eval_dataset
  - bld_tools_eval_dataset
---

# Domain Knowledge: eval_dataset
## Executive Summary
Eval datasets are structured collections of test cases used to measure LLM behavior systematically. Each case has an input, an expected output (ground truth), and optional metadata. Datasets declare their schema, size, and splits upfront. They are COLLECTIONS — not single cases (golden_test), not performance benchmarks (benchmark), and not evaluation rubrics (scoring_rubric).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P07 (Evals) |
| llm_function | GOVERN |
| Minimum schema | input + expected_output |
| Splits | train / test / val (must sum to 1.0) |
| Size unit | integer count of test cases |
| Version | semver — schema changes = minor bump, data changes = patch |
| Machine format | yaml |
## Framework Patterns
- **Braintrust**: `dataset.insert({"input": "...", "expected": "...", "metadata": {}})` — uses `expected` not `expected_output`; versioning via pinned experiment IDs.
- **LangSmith**: `client.create_example(inputs={...}, outputs={...})` — nested dicts; supports `source_run_id` for trace origin.
- **DeepEval**: `EvaluationDataset(goldens=[Golden(input="...", expected_output="...", context=[])])` — `context` list for RAG evals.
- **HuggingFace**: `Dataset.from_dict({"input": [...], "expected_output": [...]})` — columnar, Arrow-backed; `DatasetDict` for splits.
## Split Strategies
| Strategy | train | test | val | When to use |
|----------|-------|------|-----|-------------|
| Eval-only | 0.0 | 1.0 | 0.0 | Pure evaluation, no training use |
| Standard ML | 0.7 | 0.2 | 0.1 | Training + evaluation |
| Heavy eval | 0.0 | 0.8 | 0.2 | Evaluation focus with held-out validation |
| Balanced | 0.6 | 0.2 | 0.2 | Equal emphasis on val and test |
## Schema Field Types
| Field | Type | Required |
|-------|------|----------|
| input | string or dict | YES |
| expected_output | string or list | YES |
| metadata | dict | REC |
| context | list[string] | OPT |
| difficulty | enum | OPT |
| source_id | string | OPT |
## Versioning Strategy
- `1.0.0` initial release; `1.1.0` new schema field (backward-compatible); `2.0.0` breaking change; `1.0.1` data correction.
- Never reuse a dataset ID for a different schema. Bump minor for additive changes.
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Missing expected_output | Cannot compute automated metrics |
| Splits not summing to 1.0 | Reproducibility breaks; train/test overlap or gap |
| No schema declaration | Consumers must read source code to load data |
| Actual data rows in artifact body | Artifact bloats; data belongs in registry |
| Confusing dataset with benchmark | Benchmark measures performance; dataset is input collection |
| Single case called a "dataset" | Single exemplary case is golden_test (P07) |
| No versioning strategy | Schema drift causes silent downstream failures |
## Application
1. Define purpose: what LLM behavior does this dataset evaluate?
2. Design schema: input fields, ground truth field, metadata fields
3. Declare splits: use eval-only (test: 1.0) unless training use is confirmed
4. Specify size: integer count now + growth target
5. Choose framework: Braintrust (experiment tracking), LangSmith (trace-linked), DeepEval (metric suites), HuggingFace (large scale)
6. Set versioning: semver with schema-change rules
7. Validate: schema_fields has input + expected_output, splits sum to 1.0, quality: null
## References
- Braintrust: braintrustdata.com/docs/guides/datasets
- LangSmith: docs.smith.langchain.com/evaluation/datasets
- DeepEval: docs.confident-ai.com/docs/evaluation-datasets
- HuggingFace: huggingface.co/docs/datasets

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_eval_dataset_builder]] | downstream | 0.53 |
| [[eval-dataset-builder]] | downstream | 0.53 |
| [[bld_schema_eval_dataset]] | downstream | 0.46 |
| [[bld_instruction_eval_dataset]] | downstream | 0.43 |
| [[bld_examples_eval_dataset]] | downstream | 0.43 |
| [[p10_lr_eval_dataset_builder]] | downstream | 0.39 |
| [[bld_collaboration_eval_dataset]] | downstream | 0.39 |
| [[p01_kc_eval_dataset]] | sibling | 0.37 |
| [[bld_output_template_eval_dataset]] | downstream | 0.37 |
| [[bld_tools_eval_dataset]] | downstream | 0.36 |
