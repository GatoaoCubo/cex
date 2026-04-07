---
id: p01_kc_cex_lp07_evals
kind: knowledge_card
pillar: P01
title: "CEX LP07 Evals — Quality Measurement for LLM Systems"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp07, evals, scoring, benchmark, golden-test, shokunin]
tldr: "P07 formaliza 6 tipos de eval como cidadaos de 1a classe: de smoke_eval 30s a golden_test 9.5+"
when_to_use: "Entender como medir qualidade em sistemas LLM e o padrao Shokunin de tiers"
keywords: [evals, scoring-rubric, benchmark, golden-test, smoke-eval]
long_tails:
  - "Como implementar avaliacao de qualidade para agentes LLM"
  - "O que sao golden tests e scoring rubrics no CEX"
axioms:
  - "SEMPRE medir antes de promover (sem eval = sem pool)"
  - "NUNCA auto-atribuir quality score (avaliacao externa)"
linked_artifacts:
  primary: p01_kc_cex_lp06_schema
  related: [p01_kc_cex_lp05_output, p01_kc_cex_lp08_architecture]
density_score: 1.0
data_source: "https://docs.anthropic.com/en/docs/test-and-evaluate/eval-tool"
---

## Quick Reference

topic: P07 Evals | scope: quality measurement | criticality: high
types: 6 | function: GOVERN | layer: governance

## Conceitos Chave

- P07 trata evals como tipos de primeira classe no CEX
- scoring_rubric define COMO avaliar (criterios e pesos)
- unit_eval testa agente ou prompt individual isolado
- smoke_eval eh sanidade rapida em menos de 30 segundos
- e2e_eval testa pipeline completo ponta a ponta
- benchmark mede performance quantitativa continua
- golden_test eh referencia quality 9.5+ (exemplar)
- Padrao Shokunin: Master >= 9.5 | Skilled >= 8.0
- Nenhum framework popular formaliza evals assim
- DSPy tem Metric — o mais proximo, mas isolado
- LangChain tem Callback para logging, nao avaliacao
- CrewAI nao tem nenhum tipo de eval formalizado
- P07 avalia P05: qualidade do formato de output
- P07 avalia P01: qualidade do conhecimento destilado
- P07 alimenta P11: resultados de evals sao feedback
- scoring_rubric max 5120 bytes (governance, core: true)
- golden_test max 4096 bytes (governance, core: true)

## Fases

1. Criar scoring_rubric com criterios do dominio
2. Implementar smoke_evals para sanidade rapida (<30s)
3. Escrever unit_evals para cada agente critico
4. Construir e2e_evals para pipelines completos
5. Estabelecer benchmarks para metricas continuas
6. Promover artefatos 9.5+ a golden_test de referencia

## Regras de Ouro

- SEMPRE ter scoring_rubric antes de avaliar
- NUNCA confundir benchmark (mede) com eval (testa)
- SEMPRE rodar smoke_eval antes de unit_eval (fail fast)
- NUNCA promover ao pool sem eval >= 8.0 (Shokunin)
- SEMPRE preservar golden_tests como referencia imutavel

## Comparativo

| Tipo Eval | Velocidade | Escopo | Profundidade |
|-----------|------------|--------|--------------|
| smoke_eval | < 30s | Sanidade | Superficial |
| unit_eval | 1-5 min | Isolado | Profunda |
| e2e_eval | 5-30 min | Pipeline | Completa |
| benchmark | Continuo | Metricas | Quantitativa |
| golden_test | N/A | Referencia | Exemplar 9.5+ |
| scoring_rubric | N/A | Criterios | Framework |

## Flow

```
[artefato novo]
     |
     v
[smoke_eval: sanidade <30s]
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
