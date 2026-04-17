---
kind: examples
id: bld_examples_model_registry
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of model_registry artifacts
quality: 8.9
title: "Examples Model Registry"
version: "1.0.0"
author: wave1_builder_gen
tags: [model_registry, builder, examples]
tldr: "Golden and anti-examples of model_registry artifacts"
domain: "model_registry construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
---
kind: model_registry
id: transformer-encoder-xl
version: "2.4.0"
status: production
lifecycle:
  stage: active
  deprecated: false
  last_updated: 2023-10-12
lineage:
  base_model: "transformer-base-v1"
  parent_version: "2.3.9"
  training_pipeline: "pipeline-nlp-v4"
artifacts:
  - type: weights
    uri: "s3://models/transformer-xl/v2.4.0/weights.bin"
  - type: configuration
    uri: "s3://models/transformer-xl/v2.4.0/config.json"
  - type: tokenizer
    uri: "s3://models/transformer-xl/v2.4.0/tokenizer.model"
tags:
  - architecture: transformer
  - task: sequence-classification
  - compute_tier: high
---
Registry entry for the production-grade XL encoder. This version includes updated attention heads for long-context support.

## Anti-Example 1: Confusion with Model Card
---
kind: model_card
id: transformer-encoder-xl
description: A large scale transformer model for text classification.
intended_use: Natural language understanding tasks.
limitations: High memory footprint; not suitable for edge devices.
accuracy_metrics:
  f1_score: 0.92
  precision: 0.91
---
Detailed documentation regarding the model's capabilities and ethical considerations.

## Why it fails
This is a **model_card**, not a **model_registry**. It focuses on the qualitative specification, usage instructions, and performance metrics of a single model instance rather than the versioned artifact tracking, lineage, and URI pointers required for a registry.

## Anti-2: Confusion with Checkpoint
---
kind: checkpoint
id: transformer-encoder-xl-run-882
epoch: 45
loss: 0.0234
learning_rate: 0.00005
optimizer: AdamW
batch_size: 32
gradients: "s3://training-logs/run-882/grads.pt"
---
A snapshot of the model weights at the end of epoch 45 during the training process.

## Why it fails
This is a **checkpoint**, not a **model_registry**. It describes a specific point-in-time training state (hyperparameters, loss, and epoch) rather than a managed, versioned asset intended for deployment and lineage tracking in a production environment.
