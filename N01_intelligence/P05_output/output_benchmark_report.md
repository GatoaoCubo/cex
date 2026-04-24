---
id: p10_out_benchmark_report
kind: output
8f: F6_produce
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
related:
  - p08_pat_pricing_framework
  - pricing_optimization_memory
  - bld_memory_scoring_rubric
  - benchmark-builder
  - p01_kc_benchmark
  - p03_sp_scoring_rubric_builder
  - bld_knowledge_card_scoring_rubric
  - bld_collaboration_benchmark
  - bld_output_template_llm_judge
  - p11_qg_benchmark
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p08_pat_pricing_framework]] | upstream | 0.21 |
| [[pricing_optimization_memory]] | related | 0.20 |
| [[bld_memory_scoring_rubric]] | related | 0.19 |
| [[benchmark-builder]] | upstream | 0.18 |
| [[p01_kc_benchmark]] | upstream | 0.18 |
| [[p03_sp_scoring_rubric_builder]] | upstream | 0.17 |
| [[bld_knowledge_card_scoring_rubric]] | upstream | 0.16 |
| [[bld_collaboration_benchmark]] | downstream | 0.16 |
| [[bld_output_template_llm_judge]] | upstream | 0.16 |
| [[p11_qg_benchmark]] | downstream | 0.16 |
