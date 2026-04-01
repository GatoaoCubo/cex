---
id: p10_out_benchmark_report
kind: output
pillar: P10
title: "Output: Benchmark Report"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 8.7
tags: [output, n01, benchmark, comparison, features]
tldr: "Feature/price/performance comparison grid across N products."
density_score: 0.91
---

# Output: Benchmark Report

## Template
```markdown
# Benchmark: {{CATEGORY}}
**Date**: {{DATE}} | **Products**: {{COUNT}} | **Criteria**: {{COUNT}}

## Comparison Grid

| Criteria | Weight | {{PRODUCT_A}} | {{PRODUCT_B}} | {{PRODUCT_C}} |
|----------|--------|-------------|-------------|-------------|
| {{FEAT_1}} | {{W}}% | ⭐⭐⭐ | ⭐⭐ | ⭐⭐⭐⭐ |
| {{FEAT_2}} | {{W}}% | ⭐⭐⭐⭐ | ⭐⭐⭐ | ⭐⭐ |
| Price | {{W}}% | {{VALUE}} | {{VALUE}} | {{VALUE}} |
| **Weighted Score** | 100% | {{SCORE}} | {{SCORE}} | {{SCORE}} |

## Winner per Dimension
- Best features: {{PRODUCT}}
- Best price: {{PRODUCT}}
- Best performance: {{PRODUCT}}
- Best overall: {{PRODUCT}}

## Recommendation
{{ACTIONABLE_RECOMMENDATION}}
```
