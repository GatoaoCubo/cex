---
id: p10_out_benchmark_report
kind: output
pillar: P10
title: "Output: Benchmark Report"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: research-intelligence
quality: 9.0
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

## Scoring Methodology

**Star Rating Scale**: 1⭐ = Poor | 2⭐⭐ = Fair | 3⭐⭐⭐ = Good | 4⭐⭐⭐⭐ = Excellent | 5⭐⭐⭐⭐⭐ = Best-in-class

**Weight Distribution**: Core features (40-50%) | Price (20-30%) | Performance (15-25%) | Support/UX (10-15%)

## Common Criteria Examples

| Category | Core Criteria | Weight Range |
|----------|---------------|--------------|
| **Software Tools** | Feature completeness, ease of use, integrations, pricing | 30%, 25%, 25%, 20% |
| **SaaS Platforms** | Functionality, scalability, security, cost per user | 35%, 20%, 25%, 20% |
| **Hardware** | Performance, build quality, price, warranty | 40%, 20%, 25%, 15% |

**Anti-patterns**: Equal weights (dilutes decision), >7 criteria (analysis paralysis), subjective scoring without clear rubrics.