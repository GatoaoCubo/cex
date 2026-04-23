---
kind: config
id: bld_config_inference_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions and constraints for inference_config
quality: null
title: "Inference Config Builder - Config ISO"
version: "1.0.0"
author: n03_builder
tags: [inference_config, builder, config]
tldr: "Production config for inference config: naming, paths, and constraints."
domain: "model inference"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_schema_inference_config
---

# Config: inference_config Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | p09_ic_{config_slug}.md | p09_ic_llama3_vllm.md |
| Builder directory | kebab-case | inference-config-builder/ |
| Frontmatter fields | snake_case | batch_strategy, vram_budget_gb |

## File Paths

1. Output: P09_config/examples/p09_ic_{slug}.md
2. Compiled: P09_config/compiled/p09_ic_{slug}.yaml

## Size Limits

1. Body: max 2048 bytes
2. Density: >= 0.85

## Common Quantization Levels

| Level | Memory Savings | Quality Impact | Use Case |
|-------|---------------|----------------|----------|
| fp16 | 2x vs fp32 | None | Default production |
| int8 | 4x vs fp32 | <1% loss | Memory-constrained |
| int4/gguf_q4 | 8x vs fp32 | 2-5% loss | Edge deployment |
| gguf_q5 | 6x vs fp32 | 1-2% loss | Quality/size balance |
