---
kind: collaboration
id: bld_orchestration_inference_config
pillar: P12
llm_function: COLLABORATE
purpose: How inference-config-builder works in crews
quality: null
title: "Inference Config Builder - Orchestration ISO"
version: "1.0.0"
author: n03_builder
tags: [inference_config, builder, collaboration]
tldr: "Orchestration protocol for inference config: workflow integration, handoff signals, dependency management, and cross-nucleus coordination for inference-time parameters: temperature, top_p, sampling strategy, stop sequences, penalties."
domain: "model inference"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_inference_config
---

# Collaboration: inference-config-builder

## My Role in Crews

I am a SPECIALIST. I answer: "how to serve this model in production?"
I do not train models. I do not configure tokenizers.

## Crew Compositions

### Crew: "Model Deployment Stack"
```
1. tokenizer-config-builder -> "tokenizer for input processing"
2. inference-config-builder -> "serving framework and optimization"
3. rate-limit-config-builder -> "API rate limiting"
```

## Handoff Protocol

### I Receive
- seeds: model ID, hardware specs, latency targets, throughput requirements

### I Produce
- inference_config artifact (.md with YAML frontmatter)

### I Signal
- signal: complete (with quality score)

## Builders I Depend On

| Builder | Why |
|---------|-----|
| tokenizer-config-builder | Tokenizer config needed for input processing |
| distillation-config-builder | Distilled model may require specific serving config |

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| rate-limit-config-builder | Needs serving capacity for rate limit calculation |

## Integration Points

| Point | Direction | Protocol |
|-------|-----------|----------|
| F8 COLLABORATE | outbound | signal_writer.write_signal() |
| F3 INJECT | inbound | Receives upstream artifacts via handoff |
| model_provider | upstream | Must exist before inference config production |
| thinking_config | upstream | Must exist before inference config production |
| streaming_config | upstream | Must exist before inference config production |

## Dependencies

| Dependency | Required | Purpose |
|-----------|----------|---------|
| model_provider | yes | Upstream artifact for inference config |
| thinking_config | yes | Upstream artifact for inference config |
| streaming_config | yes | Upstream artifact for inference config |

## Properties

| Property | Value |
|----------|-------|
| Kind | `orchestration` |
| Pillar | P12 |
| Domain | inference config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
