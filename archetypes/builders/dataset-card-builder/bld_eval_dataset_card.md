---
kind: quality_gate
id: p01_qg_dataset_card
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for dataset_card
quality: 8.9
title: "Quality Gate Dataset Card"
version: "1.0.0"
author: wave1_builder_gen
tags: [dataset_card, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for dataset_card"
domain: "dataset_card construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_dataset_card
  - p01_kc_dataset_card
  - p11_qg_eval_dataset
  - p09_qg_marketplace_app_manifest
  - eval-dataset-builder
  - dataset-card-builder
  - bld_collaboration_dataset_card
  - p01_qg_reranker_config
  - p03_sp_dataset_card_builder
  - p06_qg_edit_format
---
## Quality Gate
## Definition
| metric | threshold | operator | scope |
|--------|-----------|----------|-------|
| Doc Completeness | 100% | == | Metadata & Schema |
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML Syntax | Parse Error |
| H02 | ID Pattern | Regex Mismatch |
| H03 | Kind Match | Not 'dataset_card' |
| H04 | Schema Presence | Missing definition |
| H05 | License Field | Null or Empty |
| H06 | Version Format | Non-SemVer |
| H07 | Owner Identity | Unassigned |
## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Metadata Depth | 0.15 | Field coverage % |
| D02 | Schema Clarity | 0.15 | Type accuracy |
| D03 | Lineage Trace | 0.10 | Upstream links |
| D04 | Usage Limits | 0.10 | Constraint detail |
| D05 | Privacy Flags | 0.15 | PII identification |
| D06 | Stat Summary | 0.10 | Distribution info |
| D07 | Style Consistency| 0.05 | Format adherence |
| D08 | Bias/Error Notes | 0.10 | Known issue depth |
| D09 | Interoperability | 0.10 | Format compatibility|
## Actions
| Score | Action |
|-------
## Examples
## Golden Example
---
id: movie_reviews_v2
type: dataset_card
version: 2.1
---
# MovieReview-Clean
## Summary
A curated dataset of 50,000 English-language movie reviews for sentiment analysis.
## Data Collection
Data was scraped from public IMDB forums between 2022 and 2023. All PII was removed during ingestion.
## Data Structure
- `review_text`: string (The raw text of the review)
- `label`: integer (0 for negative, 1 for positive)
- `timestamp`: datetime (Date of the review)
## Limitations
The dataset contains a bias toward modern films (post-2010) and does not represent non-English cinema.
## Usage
Intended for training binary classifiers for sentiment detection.
## Why it fails:
(N/A - This is the correct format)
## Anti-Example 1: Including evaluation metrics (eval_dataset)
---
id: sentiment_model_eval
type: eval_dataset
---
# Model Performance Report
The BERT-base model achieved an F1-score of 0.89 on the test split.
## Metrics
- Accuracy: 91%
- Precision: 0.88
- Recall: 0.90
## Why it fails:
This is an `eval_dataset` artifact. It focuses on model performance, metrics, and evaluation results rather than documenting the structure, provenance, and features of the underlying dataset.
## Anti-Example 2: Providing factual information (knowledge_card)
---
id: photosynthesis_info
type: knowledge_card
---
# Photosynthesis
Photosynthesis is the process used by plants and other organisms to convert light energy into chemical energy.
## Key Components
- Chlorophyll
- Sunlight
- Carbon Dioxide
## Why it fails:
This is a `knowledge_card`. It provides general factual information and encyclopedic knowledge about a topic, rather than documenting a structured dataset's metadata, features, or collection methods.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
