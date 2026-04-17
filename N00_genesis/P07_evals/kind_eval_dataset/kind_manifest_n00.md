---
id: n00_eval_dataset_manifest
kind: knowledge_card
pillar: P07
nucleus: n00
title: "Eval Dataset -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, eval_dataset, p07, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P07 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Eval dataset defines a curated collection of test cases with inputs, expected outputs, and metadata for evaluating an LLM agent or pipeline. It specifies the sampling strategy, labeling methodology, difficulty distribution, and versioning policy. Eval datasets are the foundational data artifact that all other P07 eval kinds consume.

## Pillar
P07 -- Evals

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `eval_dataset` |
| pillar | string | yes | Always `P07` |
| title | string | yes | Domain + "Eval Dataset" |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| size | int | yes | Number of test cases |
| split | object | yes | train/val/test split ratios |
| difficulty_distribution | object | yes | easy/medium/hard case percentages |
| labeling_method | enum | yes | human / llm_assisted / automated / golden |
| data_format | enum | yes | jsonl / csv / parquet / hf_dataset |

## When to use
- Creating the test data for a new eval, benchmark, or LLM judge
- Building a gold-standard dataset for a specific capability (reasoning, code, safety)
- Curating a domain-specific dataset for fine-tuning or few-shot evaluation

## Builder
`archetypes/builders/eval_dataset-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind eval_dataset --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- N01 intelligence curates; N05 operations stores and versions
- `{{SIN_LENS}}` -- Analytical Envy: maximum coverage, minimum redundancy
- `{{TARGET_AUDIENCE}}` -- eval frameworks, benchmarks, and LLM judges consuming the data
- `{{DOMAIN_CONTEXT}}` -- task type, domain, labeling resources, coverage requirements

## Example (minimal)
```yaml
---
id: eval_dataset_cex_8f_intent_resolution
kind: eval_dataset
pillar: P07
nucleus: n01
title: "CEX 8F Intent Resolution Eval Dataset"
version: 1.0
quality: null
---
size: 500
split: {train: 0.0, val: 0.2, test: 0.8}
difficulty_distribution: {easy: 0.3, medium: 0.5, hard: 0.2}
labeling_method: human
data_format: jsonl
```

## Related kinds
- `golden_test` (P07) -- highest-quality cases from the eval dataset
- `benchmark` (P07) -- uses this dataset as its test harness
- `llm_judge` (P07) -- consumes this dataset for automated evaluation
