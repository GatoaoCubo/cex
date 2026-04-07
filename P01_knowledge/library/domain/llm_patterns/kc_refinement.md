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
