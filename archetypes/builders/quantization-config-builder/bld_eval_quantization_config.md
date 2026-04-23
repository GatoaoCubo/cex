---
kind: quality_gate
id: p09_qg_quantization_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for quantization_config
quality: 9.0
title: "Quality Gate Quantization Config"
version: "1.0.0"
author: hybrid_review3_n05
tags: [quantization_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for quantization_config"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_examples_quantization_config
  - bld_schema_quantization_config
  - bld_instruction_quantization_config
  - hybrid_review3_n05
  - bld_output_template_quantization_config
  - bld_config_quantization_config
  - bld_knowledge_card_quantization_config
  - p11_qg_input_schema
  - p11_qg_chunk_strategy
  - p11_qg_kind_builder
---

## Quality Gate
## HARD Gates
Gates check ARTIFACT STRUCTURE -- not runtime model accuracy or inference speed.

| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML validity | Any syntax error in frontmatter or body |
| H02 | ID pattern | id does not match p09_qc_* naming convention |
| H03 | Kind field | kind != quantization_config |
| H04 | quant_type value | quant_type not in {GPTQ, AWQ, GGUF, int8, int4, nf4} |
| H05 | bits value | bits not in {2, 3, 4, 8} |
| H06 | Required fields | Missing any of: quant_type, bits, group_size |
| H07 | Calibration field | GPTQ/AWQ artifact missing calibration_dataset field |

## SOFT Scoring
All dimensions evaluate ARTIFACT completeness and correctness.
Weights sum: 0.30 + 0.20 + 0.20 + 0.15 + 0.15 = 1.00

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Field completeness | 0.30 | All required fields present + typed = 1.0; each missing field -0.15 |
| D02 | Method specificity | 0.20 | Method-specific params documented (e.g., desc_act for GPTQ, zero_point for AWQ) = 1.0 |
| D03 | Hardware target | 0.20 | target_device or hardware_target field present and non-empty = 1.0 |
| D04 | Calibration documented | 0.15 | calibration_dataset field present with dataset name = 1.0; absent = 0.0 |
| D05 | CEX naming | 0.15 | id follows p09_qc_* pattern = 1.0; any deviation = 0.0 |

## Actions
| Score | Action |
|-------|--------|
| >=9.5 | GOLDEN: Auto-promote to examples library |
| >=8.0 | PUBLISH: Accept artifact |
| >=7.0 | REVIEW: Return with specific field gaps listed |
| <7.0  | REJECT: Rebuild from bld_output_template |

## Examples
## Golden Example
---
kind: quantization_config
version: "1.2"
---
method: "bitsandbytes"
bits: 4
compute_dtype: "bfloat16"
bnb_4bit_quant_type: "nf4"
bnb_4bit_use_double_quant: true
bnb_4bit_compute_dtype: "bfloat16"

## Anti-Example 1: Including context compression settings
---
kind: quantization_config
---
bits: 4
compression_config:
  method: "token_pruning"
  reduction_ratio: 0.5
context_window_compression: true

## Why it fails
This example violates the boundary by including `compression_config` and context-related settings. The `quantization_config` should only contain parameters related to weight/activation precision (bits, types, methods), not settings for compressing the context window or token sequences.

## Anti-Example 2: Including model architecture parameters
---
kind: quantization_config
---
bits: 8
num_layers: 32
hidden_size: 4096
vocab_size: 32000
attention_heads: 32

## Why it fails
This example incorrectly includes `model_architecture` parameters such as `num_layers`, `hidden_size`, and `vocab_size`. These parameters define the structural topology of the model and belong in a separate architecture configuration, not within the quantization settings.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
