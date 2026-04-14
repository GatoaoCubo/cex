---
kind: quality_gate
id: p09_qg_quantization_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for quantization_config
quality: null
title: "Quality Gate Quantization Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [quantization_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for quantization_config"
domain: "quantization_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Accuracy Retention | >= 0.98 | >= | Model Weights |
| Compression Ratio | > 2.0x | > | Model Size |
| Bit-width Range | 4 to 16 | range | Precision |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML Validity | Syntax Error |
| H02 | ID Pattern | Non-conforming ID |
| H03 | Kind Match | Kind != quantization_config |
| H04 | Bit-width Range | Value < 4 or > 16 |
| H05 | Backend Support | Unsupported Backend |
| H06 | Required Fields | Missing dtype or scale |
| H07 | Schema Integrity | Schema Mismatch |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Accuracy Loss | 0.25 | < 1% loss = 1.0 |
| D02 | Size Reduction | 0.15 | > 4x reduction = 1.0 |
| D03 | Latency Delta | 0.15 | < 5% increase = 1.0 |
| D04 | Memory Usage | 0.10 | < 10% reduction = 1.0 |
| D05 | Quant Error | 0.10 | MSE < 1e-4 = 1.0 |
| D06 | Compatibility | 0.10 | Multi-device = 1.0 |
| D07 | Calibration | 0.10 | High precision = 1.0 |
| D08 | Hardware Fit | 0.05 | Optimized = 1.0 |

## Actions
| Score | Action |
|-------|--------|
| >=9.5 | GOLDEN: Auto-promote |
| >=8.0 | PUBLISH: Deploy to Registry |
| >=7.0 | REVIEW: Manual QA Required |
| <7.0  | REJECT: Block Deployment |

##
