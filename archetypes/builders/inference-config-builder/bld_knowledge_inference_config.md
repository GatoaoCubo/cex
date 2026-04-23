---
kind: knowledge_card
id: bld_knowledge_inference_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for inference_config production -- model serving and inference optimization
sources: vLLM, TGI, GGUF quantization, KV-cache literature, speculative decoding
quality: null
title: "Inference Config Builder - Knowledge ISO"
version: "1.0.0"
author: n03_builder
tags: [inference_config, builder, knowledge]
tldr: "Domain knowledge for inference config: serving frameworks, quantization, batching, KV-cache, and latency optimization."
domain: "model inference"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_inference_config
  - bld_schema_inference_config
---

# Domain Knowledge: inference_config

## Executive Summary

Inference configs define how a trained model is served for production predictions. They specify the serving framework, quantization level, batch strategy, KV-cache configuration, hardware requirements, and latency targets. An inference_config is a P09 artifact -- it configures MODEL SERVING, not training or architecture.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P09 (config) |
| Frameworks | vLLM, TGI, Ollama, TensorRT-LLM, llama.cpp |
| Quantization | FP16, INT8, INT4, GGUF (Q4_K_M, Q5_K_M, Q8_0) |
| Batching | continuous, static, dynamic |
| Key metrics | tokens/sec, time-to-first-token, p99 latency |

## Patterns

- **Quantization trade-off** -- INT4 halves memory, ~2% quality loss; INT8 is quality-neutral for most tasks
- **Continuous batching** -- serves multiple requests simultaneously; maximizes GPU utilization
- **KV-cache** -- stores key/value tensors for past tokens; reduces recomputation but uses VRAM
- **Speculative decoding** -- uses smaller draft model to predict tokens, verified by main model; 2-3x speedup
- **GGUF format** -- CPU-friendly quantized format; Q4_K_M is the quality/size sweet spot

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| No quantization strategy | Full FP32 wastes memory and limits throughput |
| Ignoring TTFT | Time-to-first-token matters more than throughput for interactive use |
| No memory budget | Model + KV-cache exceeds VRAM = OOM crash |
| Static batch only | Underutilizes GPU between requests; latency spikes |
| No fallback model | Primary model unavailable = total service outage |
