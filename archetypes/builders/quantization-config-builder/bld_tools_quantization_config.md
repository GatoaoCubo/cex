---
kind: tools
id: bld_tools_quantization_config
pillar: P04
llm_function: CALL
purpose: Tools available for quantization_config production
quality: 8.8
title: "Tools Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, tools]
tldr: "Tools available for quantization_config production"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_knowledge_card_quantization_config
  - quantization-config-builder
  - bld_schema_quantization_config
  - p03_sp_quantization_config_builder
  - bld_tools_vad_config
  - hybrid_review3_n05
  - bld_instruction_quantization_config
  - p10_lr_quantization_config_builder
  - bld_tools_prosody_config
  - bld_architecture_quantization_config
---

## Production Tools
| Tool | Purpose | When |
| :--- | :--- | :--- |
| cex_compile.py | Generate quantized configs | Model compression |
| cex_score.py | Evaluate accuracy metrics | Post-quantization |
| cex_retriever.py | Fetch optimal hyperparams | Config search |
| cex_doctor.py | Debug config mismatches | Deployment prep |
| cex_optimizer.py | Fine-tune bit-width | Optimization loop |

## External References
| Library | Purpose | When |
| :--- | :--- | :--- |
| AutoGPTQ | GPTQ quantization via Python API | GPTQ config validation |
| AutoAWQ | AWQ quantization via Python API | AWQ config validation |
| bitsandbytes | int8/int4 quantization (nf4, fp4) | bitsandbytes config |
| llama.cpp / GGUF | GGUF format generation and inference | GGUF config |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_quantization_config]] | upstream | 0.43 |
| [[quantization-config-builder]] | downstream | 0.41 |
| [[bld_schema_quantization_config]] | downstream | 0.37 |
| [[p03_sp_quantization_config_builder]] | upstream | 0.35 |
| [[bld_tools_vad_config]] | sibling | 0.30 |
| [[hybrid_review3_n05]] | upstream | 0.29 |
| [[bld_instruction_quantization_config]] | upstream | 0.29 |
| [[p10_lr_quantization_config_builder]] | downstream | 0.29 |
| [[bld_tools_prosody_config]] | sibling | 0.29 |
| [[bld_architecture_quantization_config]] | downstream | 0.28 |
