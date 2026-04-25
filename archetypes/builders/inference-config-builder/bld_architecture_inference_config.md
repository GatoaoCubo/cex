---
kind: architecture
id: bld_architecture_inference_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of inference_config
quality: null
title: "Inference Config Builder - Architecture ISO"
version: "1.0.0"
author: n03_builder
tags: [inference_config, builder, architecture]
tldr: "Architecture context for inference config: components and boundary."
domain: "model inference"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_inference_config
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| model_id | Model being served | inference-config-builder | required |
| framework | Serving framework | inference-config-builder | required |
| quantization | Compression level | inference-config-builder | required |
| batch_strategy | Request batching approach | inference-config-builder | required |
| kv_cache | Key-value cache configuration | inference-config-builder | optional |
| hardware | GPU and memory specs | inference-config-builder | required |

## Dependency Graph

```
tokenizer_config (P09) --consumed_by--> inference_config (input processing)
distillation_config (P02) --produces--> model --served_by--> inference_config
inference_config --consumed_by--> api_client (P04)
inference_config --independent-- embedding_config (P01)
```

## Boundary Table

| inference_config IS | inference_config IS NOT |
|--------------------|------------------------|
| Serving configuration: framework, quantization, batching | A distillation_config -- that trains the model |
| Defines how a model runs in production | A tokenizer_config -- that configures tokenization |
| Specifies hardware and performance targets | A model_provider -- that manages model hosting |

## Component Boundaries

Inference-time generation parameters. NOT model_provider (which model to call) nor thinking_config (extended reasoning budget) nor streaming_config (transport streaming).

| Boundary | In Scope | Out of Scope |
|----------|----------|-------------|
| Kind scope | inference config | Adjacent kinds |
| Dependencies | model_provider, thinking_config, streaming_config | Transitive deps |

## Interfaces

| Interface | Direction | Contract |
|-----------|-----------|----------|
| Schema (P06) | upstream | Validates structure |
| Output (P05) | downstream | Produces artifacts |
| Config (P09) | lateral | Constrains production |

## Properties

| Property | Value |
|----------|-------|
| Kind | `architecture` |
| Pillar | P08 |
| Domain | inference config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
