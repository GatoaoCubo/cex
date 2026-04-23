---
kind: instruction
id: bld_instruction_quantization_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for quantization_config
quality: 8.8
title: "Instruction Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, instruction]
tldr: "Step-by-step production process for quantization_config"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p09_qg_quantization_config
  - bld_schema_quantization_config
  - bld_knowledge_card_quantization_config
  - hybrid_review3_n05
  - quantization-config-builder
  - bld_tools_quantization_config
  - bld_output_template_quantization_config
  - bld_instruction_golden_test
  - p10_lr_quantization_config_builder
  - p03_sp_quantization_config_builder
---

## Phase 1: RESEARCH
1. Analyze target model weight distribution and dynamic range.
2. Evaluate bit-width trade-offs (INT8, FP8, NF4, INT4).
3. Compare compression algorithms (AWQ, GPTQ, bitsandbytes).
4. Assess hardware kernel compatibility (CUDA, ROCm, Triton).
5. Determine perplexity loss tolerance for specific tasks.
6. Identify optimal calibration dataset for scale estimation.

## Phase 2: COMPOSE
1. Initialize artifact structure using bld_output_template_quantization_config.md.
2. Map quantization parameters to types in bld_schema_quantization_config.md.
3. Define 'bits' parameter based on precision research.
4. Configure 'group_size' for weight-clustering density.
5. Specify 'quant_type' (e.g., 'nf4') per bld_schema_quantization_config.md.
6. Implement 'desc_act' settings for activation scaling (GPTQ only).
7. Set 'zero_point' and 'scale' calculation logic.
8. Define 'compute_dtype' for dequantization kernels.
9. Set id following naming convention from bld_config_quantization_config.md (p09_qc_*).

## Phase 3: VALIDATE
- [ ] Verify all keys strictly match bld_schema_quantization_config.md definitions.
- [ ] Check id follows p09_qc_* pattern (HARD gate H02).
- [ ] Confirm quant_type in {GPTQ, AWQ, GGUF, int8, int4, nf4} (HARD gate H04).
- [ ] Confirm bits in {2, 3, 4, 8} (HARD gate H05).
- [ ] Confirm calibration_dataset present for GPTQ/AWQ methods (HARD gate H07).
- [ ] Validate structural integrity against bld_output_template_quantization_config.md.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p09_qg_quantization_config]] | downstream | 0.44 |
| [[bld_schema_quantization_config]] | downstream | 0.33 |
| [[bld_knowledge_card_quantization_config]] | upstream | 0.31 |
| [[hybrid_review3_n05]] | upstream | 0.30 |
| [[quantization-config-builder]] | downstream | 0.26 |
| [[bld_tools_quantization_config]] | downstream | 0.25 |
| [[bld_output_template_quantization_config]] | downstream | 0.24 |
| [[bld_instruction_golden_test]] | sibling | 0.22 |
| [[p10_lr_quantization_config_builder]] | downstream | 0.22 |
| [[p03_sp_quantization_config_builder]] | related | 0.22 |
