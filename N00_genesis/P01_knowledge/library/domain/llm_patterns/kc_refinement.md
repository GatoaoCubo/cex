---
id: p01_kc_refinement
kind: knowledge_card
type: domain
pillar: P01
title: "Iterative Refinement — Multi-Pass Output Improvement"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: llm_patterns
quality: 9.0
tags: [refinement, iteration, multi-pass, quality]
tldr: "First draft is never final. Generate → critique → revise per dimension. Structure pass, accuracy pass, voice pass, polish pass."
when_to_use: "Long-form content, brand-sensitive output, technical documentation"
keywords: [refinement, iteration, multi-pass, critique, revision]
density_score: 0.91
updated: "2026-04-07"
related:
  - p01_kc_iterative_refinement_skill
  - p07_gt_stripe_pipeline
  - p01_kc_distillation_pipeline
  - p01_kc_anti_file_storage
  - bld_examples_golden_test
  - bld_examples_mental_model
  - p01_kc_knowledge_distillation
  - p01_kc_pattern_extraction
  - n01_hybrid_review_wave1
  - bld_examples_invariant
---

# Iterative Refinement

## The Pattern
```
DRAFT → PASS 1 (structure) → PASS 2 (accuracy) → PASS 3 (voice) → PASS 4 (polish) → SHIP
```

## When to Use vs Skip

| Use | Skip |
|-----|------|
| >2000 words | Short factual answers |
| Brand-sensitive | Code (tests validate better) |
| Technical docs | Time-critical output |
| Multi-audience | Simple Q&A |

## CEX Integration
1. 8F F6→F7→F6 = 2-pass refinement
2. `cex_score.py` = peer-review (different LLM critiques)
3. Brand audit = domain-specific refinement pass

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_iterative_refinement_skill]] | sibling | 0.48 |
| [[p07_gt_stripe_pipeline]] | downstream | 0.29 |
| [[p01_kc_distillation_pipeline]] | sibling | 0.28 |
| [[p01_kc_anti_file_storage]] | sibling | 0.25 |
| [[bld_examples_golden_test]] | downstream | 0.24 |
| [[bld_examples_mental_model]] | downstream | 0.24 |
| [[p01_kc_knowledge_distillation]] | sibling | 0.24 |
| [[p01_kc_pattern_extraction]] | sibling | 0.24 |
| [[n01_hybrid_review_wave1]] | related | 0.23 |
| [[bld_examples_invariant]] | downstream | 0.23 |
