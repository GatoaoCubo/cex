---
kind: instruction
id: bld_instruction_quantization_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for quantization_config
quality: null
title: "Instruction Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, instruction]
tldr: "Step-by-step production process for quantization_config"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH
1. Analyze target model weight distribution and dynamic range.
2. Evaluate bit-width trade-offs (INT8, FP8, NF4, INT4).
3. Compare compression algorithms (AWQ, GPTQ, bitsandbytes).
4. Assess hardware kernel compatibility (CUDA, ROCm, Triton).
5. Determine perplexity loss tolerance for specific tasks.
6. Identify optimal calibration dataset for scale estimation.

## Phase 2: COMPOSE
1. Initialize artifact structure using OUTPUT_TEMPLATE.md.
2. Map quantization parameters to types in SCHEMA.md.
3. Define 'bits' parameter based on precision research.
4. Configure 'group_size' for weight-clustering density.
5. Specify 'quant_type' (e.g., 'nf4') per SCHEMA.md.
6. Implement 'desc_act' settings for activation scaling.
7. Set 'zero_point' and 'scale' calculation logic.
8. Define 'compute_dtype' for dequantization kernels.
9. Finalize the JSON/YAML block for the CONSTRAIN function.

## Phase 3: VALIDATE
- [ ] Verify all keys strictly match SCHEMA.md definitions.
- [ ] Check bit-width compatibility with target hardware.
- [ ] Ensure numerical ranges for scales are within bounds.
- [ ] Confirm no unsupported quantization methods are listed.
- [ ] Validate structural integrity against OUTPUT_TEMPLATE.md.
