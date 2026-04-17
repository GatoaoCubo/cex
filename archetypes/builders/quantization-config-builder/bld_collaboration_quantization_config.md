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
