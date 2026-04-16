---
kind: examples
id: bld_examples_experiment_tracker
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of experiment_tracker artifacts
quality: 8.8
title: "Examples Experiment Tracker"
version: "1.0.0"
author: wave1_builder_gen
tags: [experiment_tracker, builder, examples]
tldr: "Golden and anti-examples of experiment_tracker artifacts"
domain: "experiment_tracker construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
---
kind: experiment_tracker
metadata:
  project_name: "transformer-layer-scaling"
  experiment_group: "width-vs-depth-study"
  total_runs: 3
runs:
  - run_id: "run_alpha"
    timestamp: "2023-11-01T08:00:00Z"
    configuration:
      layers: 6
      hidden_dim: 512
      heads: 8
    results:
      perplexity: 12.4
      training_loss: 0.85
      throughput_tokens_sec: 1200
  - run_id: "run_beta"
    timestamp: "2023-11-01T14:30:00Z"
    configuration:
      layers: 12
      hidden_dim: 512
      heads: 8
    results:
      perplexity: 10.2
      training_loss: 0.72
      throughput_tokens_sec: 850
  - run_id: "run_gamma"
    timestamp: "2023-11-02T09:15:00Z"
    configuration:
      layers: 12
      hidden_dim: 768
      heads: 12
    results:
      perplexity: 9.8
      training_loss: 0.68
      throughput_tokens_sec: 600
---

## Anti-Example 1: Single experiment configuration
---
kind: experiment_config
parameters:
  learning_rate: 0.0001
  batch_size: 32
  optimizer: "adamw"
---
## Why it fails
This is an `experiment_config`. It only contains the settings for a single execution. An `experiment_tracker` must contain a collection of multiple runs to allow for comparison and historical tracking.

## Anti-Example 2: Evaluation benchmark
---
kind: benchmark_suite
dataset: "GLUE_benchmark"
model_version: "v2.1-final"
evaluation_metrics:
  mnli_accuracy: 0.88
  sst2_accuracy: 0.92
  cola_score: 0.65
---
## Why it fails
This is a `benchmark`. It focuses on the static evaluation of a specific model version against a fixed dataset. An `experiment_tracker` should focus on the iterative process of changing parameters and observing the resulting changes in performance across different attempts.
