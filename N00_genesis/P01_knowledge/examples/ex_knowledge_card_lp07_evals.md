---
id: p01_kc_lp07_evals
kind: knowledge_card
pillar: P01
title: "P07 Evals: Como Medir Qualidade"
version: 1.0.0
created: 2026-03-23
updated: 2026-03-23
author: builder_agent
domain: meta-construction
quality: 9.0
tags: [evals, testing, benchmark, quality, golden_test]
tldr: "P07 define 6 tipos de avaliacao (unit_eval, smoke_eval, e2e_eval, benchmark, golden_test, scoring_rubric) que medem qualidade de agentes e prompts — max 4096 bytes"
when_to_use: "Quando precisar criar testes, benchmarks ou rubrics de avaliacao no CEX"
keywords: [unit_eval, smoke_eval, e2e_eval, benchmark, golden_test, scoring_rubric]
long_tails:
  - "como criar um golden test no CEX"
  - "quais tipos de avaliacao existem em P07"
axioms:
  - "Golden test exige quality 9.5+ — eh o padrao de excelencia contra o qual tudo se mede"
linked_artifacts:
  agent: null
  skill: null
density_score: 0.86
related:
  - p01_kc_cex_lp07_evals
  - smoke-eval-builder
  - p01_kc_cex_function_govern
  - unit-eval-builder
  - bld_collaboration_smoke_eval
  - e2e-eval-builder
  - bld_collaboration_unit_eval
  - bld_architecture_e2e_eval
  - bld_architecture_unit_eval
  - p07_e2e_cex_forge_pipeline
---

# P07 Evals: Como Medir Qualidade

## Executive Summary
P07 governa medicao de qualidade no CEX com 6 tipos de avaliacao que cobrem desde testes rapidos (smoke_eval < 30s) ate benchmarks completos de latencia/custo/qualidade. Golden tests (9.5+) servem como referencia absoluta, e scoring rubrics definem criterios (5D, 12LP, custom).

## Spec Table
| Campo | Valor | Nota |
|-------|-------|------|
| Tipos | 6 | unit_eval, smoke_eval, e2e_eval, benchmark, golden_test, scoring_rubric |
| unit_eval max_bytes | 4096 | Teste unitario de agente/prompt |
| smoke_eval max_bytes | 3072 | Sanidade rapida < 30s |
| golden_test quality | 9.5+ | Referencia absoluta |
| scoring_rubric max_bytes | 3072 | 5D, 12LP ou custom |
| benchmark metrics | 3 | latencia, custo, qualidade |

## Patterns
- Smoke eval como gate rapido antes de e2e (< 30s, fail fast)
- Golden tests como corpus de referencia para regressao
- Scoring rubric define criterios explicitamente — sem julgamento subjetivo
- Benchmark com 3 eixos: latencia (ms), custo ($), qualidade (score)
- Unit eval por agente/prompt garante granularidade de debug

## Anti-Patterns
- Golden test com quality < 9.5: contamina o corpus de referencia
- Benchmark sem baseline: medicao sem ponto de comparacao
- Scoring rubric vago ("boa qualidade"): impossivel de reproduzir
- Smoke eval > 30s: perde proposito de sanidade rapida

## Application
No CEX, P07 alimenta o quality gate de P11 (Feedback). O forge gera exemplos de eval que validam os proprios artefatos gerados, criando um ciclo: forge > artefato > eval > feedback > forge melhorado.

## References
- P07_evals/_schema.yaml (fonte de verdade)
- P11_feedback/_schema.yaml (quality_gate consumer)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp07_evals]] | sibling | 0.39 |
| [[smoke-eval-builder]] | downstream | 0.33 |
| [[p01_kc_cex_function_govern]] | sibling | 0.32 |
| [[unit-eval-builder]] | downstream | 0.31 |
| [[bld_collaboration_smoke_eval]] | downstream | 0.30 |
| [[e2e-eval-builder]] | downstream | 0.27 |
| [[bld_collaboration_unit_eval]] | downstream | 0.27 |
| [[bld_architecture_e2e_eval]] | downstream | 0.27 |
| [[bld_architecture_unit_eval]] | downstream | 0.25 |
| [[p07_e2e_cex_forge_pipeline]] | downstream | 0.25 |
