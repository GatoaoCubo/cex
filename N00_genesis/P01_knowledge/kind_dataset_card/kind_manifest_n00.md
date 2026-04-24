---
id: n00_dataset_card_manifest
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "Dataset Card -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, dataset_card, p01, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_dataset_card
  - bld_schema_eval_dataset
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_eval_metric
  - bld_schema_integration_guide
  - bld_schema_voice_pipeline
  - bld_schema_multimodal_prompt
  - bld_schema_quickstart_guide
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Dataset Card provides structured documentation for a machine learning dataset following Hugging Face and Model Cards for Model Reports conventions. It documents data provenance, format, intended use, known biases, and access instructions. Essential for reproducibility, compliance, and responsible AI practices when training or fine-tuning models.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `dataset_card` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Dataset name and version |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| dataset_size | string | yes | Row count or token count |
| data_format | enum | yes | jsonl\|csv\|parquet\|text\|arrow |
| language | list | yes | Language codes (e.g., [en, pt]) |
| license | string | yes | Data license identifier |
| task_categories | list | yes | ML tasks the dataset supports |
| known_biases | list | no | Documented bias or skew issues |
| source_url | string | no | Origin or download location |

## When to use
- When creating a training or evaluation dataset for fine-tuning
- When sharing a dataset with collaborators or publishing internally
- When auditing data quality for a model training run

## Builder
`archetypes/builders/dataset_card-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind dataset_card --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (typically N04 or N05)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- ML engineers, data scientists
- `{{DOMAIN_CONTEXT}}` -- task domain and data collection methodology

## Example (minimal)
```yaml
---
id: dataset_card_cex_8f_ft_v1
kind: dataset_card
pillar: P01
nucleus: n04
title: "CEX 8F Fine-Tuning Dataset v1"
version: 1.0
quality: null
---
dataset_size: "12,000 examples"
data_format: jsonl
language: [en, pt]
license: proprietary
task_categories: [instruction-following, structured-generation]
```

## Related kinds
- `finetune_config` (P02) -- training job that consumes this dataset
- `embedding_config` (P01) -- when dataset is used to train embeddings
- `knowledge_card` (P01) -- atomic facts extracted from dataset analysis

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_dataset_card]] | downstream | 0.58 |
| [[bld_schema_eval_dataset]] | downstream | 0.49 |
| [[bld_schema_benchmark_suite]] | downstream | 0.48 |
| [[bld_schema_reranker_config]] | downstream | 0.45 |
| [[bld_schema_usage_report]] | downstream | 0.45 |
| [[bld_schema_eval_metric]] | downstream | 0.44 |
| [[bld_schema_integration_guide]] | downstream | 0.44 |
| [[bld_schema_voice_pipeline]] | downstream | 0.44 |
| [[bld_schema_multimodal_prompt]] | downstream | 0.44 |
| [[bld_schema_quickstart_guide]] | downstream | 0.42 |
