---
kind: collaboration
id: bld_orchestration_retrieval_evaluator
pillar: P12
llm_function: COLLABORATE
purpose: How retrieval-evaluator-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: null
title: "Retrieval Evaluator Builder - Orchestration ISO"
version: "1.0.0"
author: n03_builder
tags: [retrieval_evaluator, builder, collaboration]
tldr: "Crew collaboration protocol for retrieval evaluator: role, handoffs, and dependencies."
domain: "retrieval evaluation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_retrieval_evaluator
  - bld_architecture_retrieval_evaluator
---

# Collaboration: retrieval-evaluator-builder

## My Role in Crews

I am a SPECIALIST. I answer ONE question: "how do we measure retrieval quality for this system?"
I do not build retrieval logic. I do not configure indexes.
I define evaluation methodology so retrieval systems can be measured and compared.

## Crew Compositions

### Crew: "RAG Quality Assurance"
```
1. retrieval-evaluator-builder -> "evaluation metrics and methodology"
2. benchmark-suite-builder -> "bundled evaluation suite"
3. regression-check-builder -> "automated regression detection"
```

### Crew: "Search System Evaluation"
```
1. retrieval-evaluator-builder -> "retrieval quality metrics"
2. golden-test-builder -> "gold standard test cases"
3. eval-metric-builder -> "individual metric definitions"
```

## Handoff Protocol

### I Receive
- seeds: target system, use case (QA, search, recommendation), domain
- optional: existing metrics, query set, baseline system

### I Produce
- retrieval_evaluator artifact (.md with YAML frontmatter)
- committed to: P07_evals/examples/p07_re_{slug}.md

### I Signal
- signal: complete (with quality score)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None -- independent builder (layer 0). Evaluators are defined from requirements.

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| benchmark-suite-builder | Bundles evaluators into comprehensive suites |
| regression-check-builder | Uses evaluator thresholds for automated checks |
