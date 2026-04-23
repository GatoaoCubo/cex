---
kind: knowledge_card
id: bld_knowledge_card_quantization_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for quantization_config production
quality: 9.1
title: "Knowledge Card Quantization Config"
version: "1.0.0"
author: hybrid_review3_n05
tags: [quantization_config, builder, knowledge_card]
tldr: "Domain knowledge for quantization_config production -- GPTQ, AWQ, GGUF, bitsandbytes"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.88
related:
  - bld_schema_quantization_config
  - quantization-config-builder
  - bld_tools_quantization_config
  - p03_sp_quantization_config_builder
  - p10_lr_quantization_config_builder
  - hybrid_review3_n05
  - bld_instruction_quantization_config
  - bld_collaboration_quantization_config
  - kc_quantization_config
  - p09_qg_quantization_config
---

## Domain Overview
Quantization configuration defines the precision reduction strategies applied to model weights
and activations. By mapping high-precision floating-point values (FP32, BF16) to lower-bit
integer formats (INT8, INT4), developers reduce memory footprint and increase inference
throughput on hardware-constrained devices.

Domain: LLM model compression -- NOT data compression (ZIP, zlib, deflate, LZMA).
These are entirely separate domains. quantization_config only covers model weight/activation
precision, never file compression.

## Key Concepts

| Concept | Definition | Source |
|---------|------------|--------|
| Post-Training Quantization (PTQ) | Quantize weights after training, no re-training needed | Frantar et al. 2022 (GPTQ) |
| Quantization-Aware Training (QAT) | Simulate quantization during training for accuracy retention | Bengio et al. 2013 |
| Weight-only quantization | Quantize weights to INT4/INT8; activations stay FP16 | bitsandbytes, GPTQ, AWQ |
| Weight-activation quantization | Quantize both weights and activations | SmoothQuant, ONNX INT8 |
| Per-tensor quantization | Single scale/zero-point for entire tensor | Lower accuracy, higher speed |
| Per-channel quantization | Scale per output channel | Better accuracy than per-tensor |
| Per-group quantization | Scale per group_size consecutive elements | GPTQ/AWQ default |
| Calibration dataset | Small dataset used to compute activation statistics | c4, wikitext2, pile |
| Perplexity (PPL) | Language model quality metric; quantization should minimize PPL increase | Lower = better |

## Algorithm Reference

| Algorithm | Authors | Key Params | Hardware | Use When |
|-----------|---------|------------|----------|----------|
| GPTQ | Frantar et al. 2022 | bits, group_size, desc_act, damp_percent | CUDA (preferred) | GPU deployment, 4-bit target |
| AWQ | Lin et al. 2023 | bits, group_size, zero_point | CUDA, Metal | Activation-aware, good accuracy |
| GGUF | ggerganov / llama.cpp | bits (maps to Q4_K_M etc.) | CPU, Metal, CUDA | Edge/local inference |
| bitsandbytes | Dettmers et al. | bits (4/8), bnb_4bit_quant_type, double_quant | CUDA | Fast prototyping, HuggingFace |
| ONNX INT8 | ONNX Runtime | per-channel vs per-tensor | CPU, GPU | Cross-platform deployment |

## GGUF Quantization Types (llama.cpp naming)
| GGUF Type | Bits (eff.) | Description | Use Case |
|-----------|-------------|-------------|----------|
| Q4_K_M | ~4.5 | 4-bit with K-quant mixed | Recommended 4-bit |
| Q4_0 | 4.0 | Simple 4-bit, no K-quant | Fast, lower quality |
| Q5_K_M | ~5.5 | 5-bit K-quant mixed | Better accuracy than Q4 |
| Q8_0 | 8.0 | 8-bit, near-lossless | Max quality, 2x FP16 size |
| F16 | 16 | No quantization | Baseline reference |

Note: GGML is the legacy format superseded by GGUF. Avoid GGML references in new configs.

## Hardware Compatibility Matrix
| Algorithm | CUDA | ROCm | Metal (Apple) | CPU |
|-----------|------|------|---------------|-----|
| GPTQ | Yes (AutoGPTQ) | Partial | No | No |
| AWQ | Yes (AutoAWQ) | Partial | No | No |
| GGUF | Yes (llama.cpp) | Yes | Yes | Yes |
| bitsandbytes | Yes | Partial | No | No |
| ONNX INT8 | Yes | Yes | Partial | Yes |

## Common Pitfalls

| Pitfall | Symptom | Fix |
|---------|---------|-----|
| Missing calibration_dataset for GPTQ | Poor accuracy, high PPL | Add calibration_dataset: c4 |
| Wrong compute_dtype | OOM or slow inference | Set compute_dtype: bfloat16 |
| group_size too large | Accuracy drop | Reduce to 64 or 32 |
| GGML reference (stale) | Framework errors | Replace with GGUF |
| bits=16 in quantization_config | Not quantization | Remove from config |
| Mixing quant_type and compression settings | Schema violation | Separate configs |

## CEX Integration Notes
- Artifacts live in P09 (Config pillar)
- Naming: p09_qc_{model_name} (e.g., p09_qc_llama3_8b)
- Compiled by: python _tools/cex_compile.py {path}
- Validated by: bld_quality_gate_quantization_config.md (H01-H07 HARD gates)
- Related kinds: compression_config (context compression -- DIFFERENT domain), model_architecture (layer structure)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_quantization_config]] | downstream | 0.53 |
| [[quantization-config-builder]] | downstream | 0.52 |
| [[bld_tools_quantization_config]] | downstream | 0.49 |
| [[p03_sp_quantization_config_builder]] | downstream | 0.44 |
| [[p10_lr_quantization_config_builder]] | downstream | 0.43 |
| [[hybrid_review3_n05]] | sibling | 0.39 |
| [[bld_instruction_quantization_config]] | downstream | 0.38 |
| [[bld_collaboration_quantization_config]] | downstream | 0.35 |
| [[kc_quantization_config]] | sibling | 0.35 |
| [[p09_qg_quantization_config]] | downstream | 0.34 |
