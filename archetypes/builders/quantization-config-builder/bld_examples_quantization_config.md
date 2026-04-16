---
kind: examples
id: bld_examples_quantization_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of quantization_config artifacts
quality: 8.8
title: "Examples Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, examples]
tldr: "Golden and anti-examples of quantization_config artifacts"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Golden Example
---
kind: quantization_config
version: "1.2"
---
method: "bitsandbytes"
bits: 4
compute_dtype: "bfloat16"
bnb_4bit_quant_type: "nf4"
bnb_4bit_use_double_quant: true
bnb_4bit_compute_dtype: "bfloat16"

## Anti-Example 1: Including context compression settings
---
kind: quantization_config
---
bits: 4
compression_config:
  method: "token_pruning"
  reduction_ratio: 0.5
context_window_compression: true

## Why it fails
This example violates the boundary by including `compression_config` and context-related settings. The `quantization_config` should only contain parameters related to weight/activation precision (bits, types, methods), not settings for compressing the context window or token sequences.

## Anti-Example 2: Including model architecture parameters
---
kind: quantization_config
---
bits: 8
num_layers: 32
hidden_size: 4096
vocab_size: 32000
attention_heads: 32

## Why it fails
This example incorrectly includes `model_architecture` parameters such as `num_layers`, `hidden_size`, and `vocab_size`. These parameters define the structural topology of the model and belong in a separate architecture configuration, not within the quantization settings.
