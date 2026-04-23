---
kind: architecture
id: bld_architecture_eval_dataset
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of eval_dataset — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Eval Dataset"
version: "1.0.0"
author: n03_builder
tags: [eval_dataset, builder, examples]
tldr: "Golden and anti-examples for eval dataset construction, demonstrating ideal structure and common pitfalls."
domain: "eval dataset construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_eval_dataset
  - eval-dataset-builder
  - p01_kc_eval_dataset
  - p03_sp_eval_dataset_builder
  - bld_instruction_eval_dataset
  - p11_qg_eval_dataset
  - bld_examples_eval_dataset
  - bld_output_template_eval_dataset
  - bld_schema_eval_dataset
  - bld_knowledge_card_eval_dataset
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| test_case | Single input/expected_output/metadata unit in the collection | eval_dataset | required |
| schema_field | Named field present in every test case (input, expected_output, metadata) | eval_dataset | required |
| split | Named partition of cases (train, test, val) with percentage allocation | eval_dataset | required |
| size | Total case count — integer measure of dataset scale | eval_dataset | required |
| version | Semver identifier — tracks schema changes and data revisions | eval_dataset | required |
| source | Origin of test cases (human, synthetic, scraped, adversarial) | eval_dataset | required |
| framework_adapter | Integration pattern for target eval framework | eval_dataset | optional |
| scoring_rubric | External evaluation criteria applied to dataset cases | P07 | external |
| benchmark | Aggregate performance measurement consuming this dataset | P07 | consumer |
| eval_runner | Runtime that iterates cases and calls model | P02 | consumer |
| model | LLM under evaluation that receives case inputs | P02 | consumer |

## Dependency Graph
```
source          --produces--> test_case
schema_field    --depends-->  test_case
split           --depends-->  test_case
test_case       --produces--> eval_dataset
version         --depends-->  eval_dataset
framework_adapter --depends-> eval_dataset
scoring_rubric  --depends-->  eval_dataset
benchmark       --depends-->  eval_dataset
eval_runner     --depends-->  eval_dataset
model           --depends-->  eval_dataset (via eval_runner)
```
| From | To | Type | Data |
|------|----|------|------|
| source | test_case | produces | raw input/output pairs from origin |
| schema_field | test_case | depends | field contract every case must satisfy |
| split | test_case | depends | partition label assigned to each case |
| test_case | eval_dataset | produces | the collection itself |
| version | eval_dataset | depends | schema change tracking and migration |
| framework_adapter | eval_dataset | depends | loading and push pattern for target framework |
| scoring_rubric | eval_dataset | depends | evaluation criteria applied at run time |
| benchmark | eval_dataset | depends | consumes dataset to produce performance scores |
| eval_runner | eval_dataset | depends | iterates cases, calls model, collects results |

## Boundary Table
| eval_dataset IS | eval_dataset IS NOT |
|----------------|---------------------|
| A collection of >= 1 test cases with shared schema | A single exemplary reference case (that is golden_test) |
| Has declared splits summing to 1.0 | A performance measurement across models (that is benchmark) |
| Defines schema fields: input + expected_output required | Evaluation criteria with weights (that is scoring_rubric) |
| Versioned with semver for schema evolution | A quick sanity check with 1-5 cases (that is smoke_eval) |
| Framework-agnostic spec; adapter specifies integration | A single-function isolated test (that is unit_eval) |
| Source-declared: human/synthetic/scraped/adversarial | The actual data rows (data lives in registry, not spec) |

## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| data | test_case, source | Raw cases and their origin |
| schema | schema_field | Field contract governing every case |
| partitioning | split, size | How cases are divided and counted |
| governance | version, scoring_rubric | Schema evolution and evaluation criteria |
| integration | framework_adapter | Framework-specific loading and push |
| consumers | benchmark, eval_runner, model | Runtime systems that use the dataset |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_eval_dataset]] | downstream | 0.49 |
| [[eval-dataset-builder]] | upstream | 0.49 |
| [[p01_kc_eval_dataset]] | upstream | 0.45 |
| [[p03_sp_eval_dataset_builder]] | upstream | 0.44 |
| [[bld_instruction_eval_dataset]] | upstream | 0.38 |
| [[p11_qg_eval_dataset]] | downstream | 0.37 |
| [[bld_examples_eval_dataset]] | upstream | 0.32 |
| [[bld_output_template_eval_dataset]] | upstream | 0.32 |
| [[bld_schema_eval_dataset]] | upstream | 0.30 |
| [[bld_knowledge_card_eval_dataset]] | upstream | 0.29 |
