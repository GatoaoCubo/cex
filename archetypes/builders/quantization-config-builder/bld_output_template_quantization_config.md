---
kind: output_template
id: bld_output_template_quantization_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for quantization_config production
quality: 8.9
title: "Output Template Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, output_template]
tldr: "Template with vars for quantization_config production"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Field Guidance

| Placeholder | Type | Allowed Values | Example |
|-------------|------|----------------|---------|
| `{{id}}` | string | p09_qc_* naming pattern | p09_qc_llama3_8b |
| `{{version}}` | string | SemVer | 1.0.0 |
| `{{method}}` | string | GPTQ, AWQ, GGUF, bitsandbytes | bitsandbytes |
| `{{bits}}` | int | 2, 3, 4, 8 | 4 |
| `{{dtype}}` | string | float16, bfloat16, float32 | bfloat16 |
| `{{group_size}}` | int | 32, 64, 128 (GPTQ/AWQ); -1 for per-column | 128 |
| `{{scale_type}}` | string | symmetric, asymmetric | symmetric |
| `{{zero_point}}` | bool | true (asymmetric), false (symmetric) | false |
| `{{arch}}` | string | cuda, rocm, metal, cpu | cuda |
| `{{opt_level}}` | string | O1, O2, O3 (speed vs accuracy tradeoff) | O2 |

## Template

```yaml
---
id: {{id}}
kind: quantization_config
pillar: P09
version: {{version}}
---

quant_type: {{method}}
bits: {{bits}}
compute_dtype: {{dtype}}

parameters:
  group_size: {{group_size}}
  scale_type: {{scale_type}}
  zero_point: {{zero_point}}

hardware_target:
  architecture: {{arch}}
  optimization_level: {{opt_level}}

calibration_dataset: c4  # Required for GPTQ/AWQ. Options: c4, wikitext2, pile
```
