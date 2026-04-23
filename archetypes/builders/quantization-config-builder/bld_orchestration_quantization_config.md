---
kind: collaboration
id: bld_collaboration_quantization_config
pillar: P12
llm_function: COLLABORATE
purpose: How quantization_config-builder works in crews with other builders
quality: 8.9
title: "Collaboration Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, collaboration]
tldr: "How quantization_config-builder works in crews with other builders"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p03_sp_quantization_config_builder
  - quantization-config-builder
  - bld_architecture_kind
  - kind-builder
  - p10_lr_quantization_config_builder
  - kc_quantization_config
  - bld_collaboration_model_card
  - bld_collaboration_response_format
  - bld_collaboration_builder
  - bld_collaboration_prompt_technique
---

## Crew Role
Defines precision parameters (bit-width, dtype, scaling) to optimize
model inference speed and memory footprint without altering architecture.

## Receives From
| Builder | What | Format |
| :--- | :--- | :--- |
| model_architecture-builder | Target precision/dtype | JSON |
| hardware_profiler | Supported bit-widths | Schema |
| optimization_strategist | Accuracy/Latency targets | YAML |

## Produces For
| Builder | What | Format |
| :--- | :--- | :--- |
| quantization_engine | Quantization parameters | JSON |
| model_converter | Quantization mapping | YAML |
| deployment_orchestrator | Quantization metadata | JSON |

## Boundary
- Does NOT define model layers or weights (model_architecture-builder).
- Does NOT handle context/KV cache compression (compression_config-builder).
- Does NOT manage weight pruning (pruning_config-builder).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_quantization_config_builder]] | upstream | 0.39 |
| [[quantization-config-builder]] | upstream | 0.35 |
| [[bld_architecture_kind]] | upstream | 0.30 |
| [[kind-builder]] | upstream | 0.30 |
| [[p10_lr_quantization_config_builder]] | upstream | 0.29 |
| [[kc_quantization_config]] | upstream | 0.27 |
| [[bld_collaboration_model_card]] | sibling | 0.27 |
| [[bld_collaboration_response_format]] | sibling | 0.25 |
| [[bld_collaboration_builder]] | sibling | 0.24 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.23 |
