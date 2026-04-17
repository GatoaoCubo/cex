---
kind: examples
id: bld_examples_dataset_card
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of dataset_card artifacts
quality: 8.9
title: "Examples Dataset Card"
version: "1.0.0"
author: wave1_builder_gen
tags: [dataset_card, builder, examples]
tldr: "Golden and anti-examples of dataset_card artifacts"
domain: "dataset_card construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

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
