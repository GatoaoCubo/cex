---
kind: instruction
id: bld_prompt_inference_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for inference_config
quality: null
title: "Inference Config Builder - Prompt ISO"
version: "1.0.0"
author: n03_builder
tags: [inference_config, builder, instruction]
tldr: "Prompt engineering for inference config: structure template, token budget, style constraints, and role framing for inference-time parameters: temperature, top_p, sampling strategy, stop sequences, penalties."
domain: "model inference"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_inference_config
  - bld_schema_inference_config
---

# Instructions: How to Produce an inference_config

## Phase 1: RESEARCH

1. Identify the model to serve (architecture, parameter count, format)
2. Determine hardware constraints (GPU model, VRAM, CPU/RAM)
3. Define latency targets: time-to-first-token, tokens/sec, p99
4. Select serving framework: vLLM, TGI, Ollama, TensorRT-LLM, llama.cpp
5. Determine quantization level based on quality vs memory trade-off
6. Check existing inference_config artifacts to avoid duplication

## Phase 2: COMPOSE

1. Read SCHEMA -- source of truth for all fields
2. Fill all frontmatter fields; set quality: null
3. Write Framework section: serving framework, version, configuration
4. Write Quantization section: level, format, quality impact
5. Write Batching section: strategy, max concurrent, queue depth
6. Write Hardware section: GPU model, VRAM budget, fallback
7. Write Performance section: latency targets, throughput targets

## Phase 3: VALIDATE

1. Check HARD gates: YAML parses, id matches, kind correct
2. Verify framework specified
3. Verify quantization level defined
4. Verify latency targets set with numeric values
5. Verify VRAM budget does not exceed hardware
6. Cross-check: this is INFERENCE CONFIG, not training or model architecture

## Token Budget

| Component | Allocation | Notes |
|-----------|-----------|-------|
| System prompt | 15%% | Builder identity + sin lens |
| Context (ISOs) | 40%% | 12 ISOs loaded per builder |
| Domain knowledge | 25%% | KCs + examples + memory |
| Generation headroom | 20%% | Artifact output space |

## Style Constraints

| Dimension | Guideline |
|-----------|-----------|
| Voice | Technical, precise, builder-appropriate |
| Structure | Tables over prose; data over description |
| Density | >= 0.85; every sentence adds information |
| References | Use canonical kind names, not synonyms |

## Properties

| Property | Value |
|----------|-------|
| Kind | `prompt` |
| Pillar | P03 |
| Domain | inference config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
