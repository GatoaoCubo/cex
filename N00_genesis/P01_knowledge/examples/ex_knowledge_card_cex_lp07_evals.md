---
id: p01_kc_cex_lp07_evals
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP07 Evals — Quality Measurement for LLM Systems"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp07, evals, scoring, benchmark, golden-test, shokunin]
tldr: "P07 formalizes 6 eval types as first-class citizens: from smoke_eval 30s to golden_test 9.5+"
when_to_use: "Understand how to measure quality in LLM systems and the Shokunin tier standard"
keywords: [evals, scoring-rubric, benchmark, golden-test, smoke-eval]
long_tails:
  - "How to implement quality evaluation for LLM agents"
  - "What are golden tests and scoring rubrics in CEX"
axioms:
  - "ALWAYS measure before promoting (no eval = no pool)"
  - "NEVER self-assign quality score (external evaluation)"
linked_artifacts:
  primary: p01_kc_cex_lp06_schema
  related: [p01_kc_cex_lp05_output, p01_kc_cex_lp08_architecture]
density_score: 1.0
data_source: "https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool"
related:
  - p01_kc_lp07_evals
  - bld_architecture_golden_test
  - bld_architecture_unit_eval
  - p01_kc_cex_function_govern
  - p01_kc_golden_test
  - unit-eval-builder
  - smoke-eval-builder
  - bld_architecture_e2e_eval
  - bld_architecture_scoring_rubric
  - p01_kc_cex_lp11_feedback
---

## Quick Reference

topic: P07 Evals | scope: quality measurement | criticality: high
types: 6 | function: GOVERN | layer: governance

## Key Concepts

- P07 treats evals as first-class types in CEX
- scoring_rubric defines HOW to evaluate (criteria and weights)
- unit_eval tests an individual agent or prompt in isolation
- smoke_eval is a quick sanity check in under 30 seconds
- e2e_eval tests the complete pipeline end to end
- benchmark measures continuous quantitative performance
- golden_test is a quality 9.5+ reference (exemplar)
- Shokunin standard: Master >= 9.5 | Skilled >= 8.0
- No popular framework formalizes evals like this
- DSPy has Metric — the closest, but isolated
- LangChain has Callback for logging, not evaluation
- CrewAI has no formalized eval type
- P07 evaluates P05: quality of the output format
- P07 evaluates P01: quality of the distilled knowledge
- P07 feeds P11: eval results are feedback
- scoring_rubric max 5120 bytes (governance, core: true)
- golden_test max 4096 bytes (governance, core: true)

## Phases

1. Create scoring_rubric with domain criteria
2. Implement smoke_evals for quick sanity (<30s)
3. Write unit_evals for each critical agent
4. Build e2e_evals for complete pipelines
5. Establish benchmarks for continuous metrics
6. Promote artifacts 9.5+ to golden_test reference

## Golden Rules

- ALWAYS have scoring_rubric before evaluating
- NEVER confuse benchmark (measures) with eval (tests)
- ALWAYS run smoke_eval before unit_eval (fail fast)
- NEVER promote to pool without eval >= 8.0 (Shokunin)
- ALWAYS preserve golden_tests as immutable reference

## Comparison

| Eval Type | Speed | Scope | Depth |
|-----------|-------|-------|-------|
| smoke_eval | < 30s | Sanity | Shallow |
| unit_eval | 1-5 min | Isolated | Deep |
| e2e_eval | 5-30 min | Pipeline | Complete |
| benchmark | Continuous | Metrics | Quantitative |
| golden_test | N/A | Reference | Exemplar 9.5+ |
| scoring_rubric | N/A | Criteria | Framework |

## Flow

```
[new artifact]
     |
     v
[smoke_eval: sanity <30s]
     |
pass v              fail --> rewrite
[unit_eval: teste profundo]
     |
pass v              fail --> fix + retry
[scoring_rubric: score final]
     |
     +-------+-------+-------+
     |       |       |       |
   <7.0   7.0-7.9  8.0-9.4  >=9.5
  REJECT  LEARNING SKILLED  MASTER
                     |        |
                   pool    golden_test
```

## References

- source: https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool
- source: https://arxiv.org/abs/2312.07381
- related: p01_kc_cex_lp06_schema
- related: p01_kc_cex_lp05_output
- related: p01_kc_cex_lp08_architecture


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp07_evals]] | sibling | 0.43 |
| [[bld_architecture_golden_test]] | downstream | 0.33 |
| [[bld_architecture_unit_eval]] | downstream | 0.33 |
| [[p01_kc_cex_function_govern]] | sibling | 0.31 |
| [[p01_kc_golden_test]] | sibling | 0.27 |
| [[unit-eval-builder]] | downstream | 0.27 |
| [[smoke-eval-builder]] | downstream | 0.27 |
| [[bld_architecture_e2e_eval]] | downstream | 0.26 |
| [[bld_architecture_scoring_rubric]] | downstream | 0.26 |
| [[p01_kc_cex_lp11_feedback]] | sibling | 0.26 |
