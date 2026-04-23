---
kind: tools
id: bld_tools_inference_config
pillar: P04
llm_function: CALL
purpose: Tools available for inference_config production
quality: null
title: "Inference Config Builder - Tools ISO"
version: "1.0.0"
author: n03_builder
tags: [inference_config, builder, tools]
tldr: "Tools available for inference config production."
domain: "model inference"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_inference_config
---

# Tools: inference-config-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile artifact to YAML | Phase 3 | ACTIVE |
| cex_score.py | Score artifact quality | Phase 3 | ACTIVE |
| cex_retriever.py | Find similar configs | Phase 1 | ACTIVE |
| cex_doctor.py | Health check | Phase 3 | ACTIVE |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions |
| vLLM docs | vllm.readthedocs.io | vLLM serving framework |
| llama.cpp | github.com/ggerganov/llama.cpp | GGUF quantization specs |
| Ollama docs | ollama.com/docs | Local model serving |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Permitted |
| DENIED | (none) | -- |
