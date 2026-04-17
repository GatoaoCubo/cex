---
id: p10_lr_eval_dataset_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "Eval datasets without declared splits caused 5 out of 8 evaluation pipelines to use all cases as test data, including cases originally intended for validation. Datasets without schema_fields declarations required consumers to read source code to understand the data shape, adding 30-60 min of onboarding per pipeline integration. Datasets where splits did not sum to 1.0 (floating-point drift) caused silent data leakage in 3 train/test workflows."
pattern: "Declare splits explicitly with values summing to 1.0. Use eval-only (test: 1.0) as default for pure evaluation datasets. List schema_fields in frontmatter exactly matching ## Schema section names. Keep quality: null always."
evidence: "8 evaluation pipelines reviewed: 5 used wrong splits when splits were absent; 3 had data leakage from float drift; 0 issues when splits were explicit and verified to sum to 1.0. Schema field documentation reduced integration time from 45min avg to 8min avg."
confidence: 0.75
outcome: SUCCESS
domain: eval_dataset
tags: [eval-dataset, splits, schema-fields, data-leakage, framework-integration]
tldr: "Explicit splits summing to 1.0 prevent data leakage. schema_fields in frontmatter reduce integration time. Eval-only is the safe default. quality: null always."
impact_score: 8.0
decay_rate: 0.04
agent_group: edison
keywords: [eval dataset, splits, schema fields, expected output, data leakage, braintrust, langsmith, deepeval, huggingface, versioning]
memory_scope: project
observation_types: [user, feedback, project, reference]
llm_function: INJECT
quality: 8.9
title: Memory ISO - eval_dataset
density_score: 0.96
---
## Summary
Eval datasets are consumed by automated evaluation pipelines, not just humans. The difference between a dataset that integrates cleanly and one that causes silent failures comes down to three spec-time decisions: split declaration, schema_fields enumeration, and size accuracy. All three are invisible during happy-path exploration and catastrophic when absent in automated evaluation. Float split values drifting from 1.0 by as little as 0.001 cause silent case omission in some frameworks.
## Pattern
**Explicit splits + schema_fields + eval-only default.**

Split declaration rules:
- Always declare splits explicitly — never leave splits absent
- Default for pure evaluation: `test: 1.0` (no train, no val)
- Verify float arithmetic: `0.7 + 0.2 + 0.1 = 1.0` (not 0.9999999)
- Use 3 decimal places max; round to avoid float drift

Schema_fields rules:
- Minimum required: `input`, `expected_output`
- Each field in schema_fields MUST have a ## Schema subsection in body
- Document framework adapter field name differences (Braintrust: `expected` not `expected_output`)

Size rules:
- Always integer — "a few hundred" is not acceptable
- Size must match total cases across all splits

Versioning rules:
- `1.0.0` initial; `1.x.0` new field (backward-compatible); `2.0.0` breaking change; `1.0.x` data correction
## Anti-Pattern
- Omitting splits entirely: pipeline assumes all-test; training contamination risk.
- Float drift in splits: 0.7 + 0.2 + 0.1 = 0.9999999 in some languages — always verify sum.
- Missing expected_output from schema_fields: cannot compute automated metrics.
- Putting actual test case rows in the artifact body: spec bloat; data belongs in registry.
- Confusing eval_dataset with golden_test: a golden_test is ONE exemplary case; eval_dataset is a COLLECTION.
- Framework field name mismatch undocumented (Braintrust `expected` vs spec `expected_output`).
