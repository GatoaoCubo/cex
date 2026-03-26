---
# TEMPLATE: Benchmark (P07 Evals)
# Valide contra P07_evals/_schema.yaml (types.benchmark)
# Max 4096 bytes

id: p07_bm_{{METRIC_SLUG}}
kind: benchmark
pillar: P07
title: "Benchmark: {{METRIC_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Benchmark: {{METRIC_NAME}}

## Benchmark Frame
| Property | Value |
|----------|-------|
| Target | {{TARGET_SYSTEM}} |
| Metric | {{LATENCY|COST|QUALITY|THROUGHPUT}} |
| Load | {{LOAD_PROFILE}} |
| Budget | {{TARGET_THRESHOLD}} |

## Method
1. {{SETUP_ENVIRONMENT}}
2. {{RUN_MEASUREMENT}}
3. {{RECORD_RESULTS}}

## Results Table
| Run | Value | Pass |
|-----|-------|------|
| 1 | {{VALUE_1}} | {{yes|no}} |
| 2 | {{VALUE_2}} | {{yes|no}} |
| 3 | {{VALUE_3}} | {{yes|no}} |

## Interpretation
- Good when: {{GOOD_RESULT_RULE}}
- Investigate when: {{BAD_RESULT_RULE}}
