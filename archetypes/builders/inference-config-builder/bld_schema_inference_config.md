---
kind: schema
id: bld_schema_inference_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for inference_config
quality: null
title: "Inference Config Builder - Schema ISO"
version: "1.0.0"
author: n03_builder
tags: [inference_config, builder, schema]
tldr: "Schema for inference config artifacts -- fields, types, and constraints."
domain: "model inference"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_output_inference_config
  - bld_eval_inference_config
---

# Schema: inference_config

## Frontmatter Fields

| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_ic_{slug}) | YES | - | Namespace compliance |
| kind | literal "inference_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| model_id | string | YES | - | Model to serve |
| framework | enum | YES | - | vllm, tgi, ollama, tensorrt, llama_cpp |
| quantization | enum | YES | "fp16" | fp16, int8, int4, gguf_q4, gguf_q5, gguf_q8 |
| batch_strategy | enum | REC | "continuous" | continuous, static, dynamic |
| max_concurrent | integer | REC | 8 | Max concurrent requests |
| vram_budget_gb | float | REC | - | GPU memory budget |
| ttft_target_ms | float | REC | - | Time-to-first-token target |
| throughput_target | float | REC | - | Tokens per second target |
| domain | string | YES | - | Target domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "inference" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern

Regex: `^p09_ic_[a-z][a-z0-9_]+$`

## Body Structure (required sections)

1. `## Framework` -- serving framework and configuration
2. `## Quantization` -- level, format, quality impact
3. `## Batching` -- strategy and concurrency
4. `## Hardware` -- GPU, VRAM, fallback
5. `## Performance Targets` -- latency and throughput

## Constraints

- naming: p09_ic_{config_slug}.md
- framework MUST be one of: vllm, tgi, ollama, tensorrt, llama_cpp
- vram_budget_gb MUST be positive float
- quality: null always
