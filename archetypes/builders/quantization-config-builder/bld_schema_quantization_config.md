---
kind: schema
id: bld_schema_quantization_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for quantization_config
quality: 9.1
title: "Schema Quantization Config"
version: "1.0.0"
author: hybrid_review3_n05
tags: [quantization_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for quantization_config"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.87
---

## Frontmatter Fields

### Required
| Field | Type | Required | Default | Notes |
| :--- | :--- | :--- | :--- | :--- |
| id | string | Y | - | Naming: p09_qc_{{model_name}} |
| kind | string | Y | quantization_config | Must be exactly "quantization_config" |
| pillar | string | Y | P09 | Config pillar |
| title | string | Y | - | Human-readable descriptor |
| version | string | Y | 1.0.0 | SemVer |
| created | string | Y | - | ISO 8601 date |
| updated | string | Y | - | ISO 8601 date |
| quality | null | Y | null | Never self-score |

### Optional
| Field | Type | Required | Default | Notes |
| :--- | :--- | :--- | :--- | :--- |
| tags | list | N | [] | Free-form labels |
| domain | string | N | - | e.g., "model compression" |
| author | string | N | - | Generating tool or nucleus |

## Body Fields

### Required Body Fields
| Field | Type | Allowed Values | Notes |
| :--- | :--- | :--- | :--- |
| quant_type | string | GPTQ, AWQ, GGUF, int8, int4, nf4 | Quantization algorithm |
| bits | int | 2, 3, 4, 8 | Bit-width for quantized weights |
| group_size | int | 32, 64, 128, -1 | -1 = per-column (no grouping) |

### Recommended Body Fields
| Field | Type | Notes |
| :--- | :--- | :--- |
| compute_dtype | string | float16, bfloat16 -- dtype for dequantization kernels |
| calibration_dataset | string | Required for GPTQ/AWQ. Common: c4, wikitext2, pile |
| target_device | string | cuda, rocm, metal, cpu |
| desc_act | bool | GPTQ-specific: activation-order quantization |
| zero_point | bool | AWQ-specific: asymmetric quantization |
| double_quant | bool | bitsandbytes-specific: double quantization |

## Method-Specific Field Profiles

### GPTQ (Frantar et al., 2022)
| Field | Required | Notes |
| :--- | :--- | :--- |
| bits | Y | Typically 4 |
| group_size | Y | 128 standard |
| desc_act | Y | Activation-order quantization (Hessian-based) |
| damp_percent | N | Dampening for Hessian approximation (default 0.01) |
| calibration_dataset | Y | Used for Hessian estimation |

### AWQ (Lin et al., 2023)
| Field | Required | Notes |
| :--- | :--- | :--- |
| bits | Y | Typically 4 |
| group_size | Y | 128 standard |
| zero_point | Y | true = asymmetric |
| calibration_dataset | Y | Activation-aware scale search |

### GGUF (llama.cpp / ggerganov)
| Field | Required | Notes |
| :--- | :--- | :--- |
| bits | Y | Maps to GGUF type: 4=Q4_K_M, 8=Q8_0 |
| gguf_type | N | Explicit GGUF type string, e.g., Q4_K_M |
| target_device | Y | Typically cpu or cuda |

### bitsandbytes (Dettmers et al.)
| Field | Required | Notes |
| :--- | :--- | :--- |
| bits | Y | 4 (nf4/fp4) or 8 (LLM.int8()) |
| bnb_4bit_quant_type | N | nf4 or fp4 |
| double_quant | N | Double quantization reduces memory further |
| compute_dtype | Y | bfloat16 recommended |

## Naming Convention
```
id: p09_qc_{{model_name}}
Examples:
  p09_qc_llama3_8b
  p09_qc_mistral_7b_gptq
  p09_qc_phi3_awq
```

## Boundary
- IN SCOPE: weight quantization, activation quantization, calibration, precision config
- OUT OF SCOPE: context compression (compression_config), KV-cache pruning, model architecture (num_layers, hidden_size), token pruning
