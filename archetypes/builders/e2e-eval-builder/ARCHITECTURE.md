---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of e2e_eval in the CEX fractal
---

# Architecture: e2e_eval in the CEX

## Boundary
e2e_eval EH: teste end-to-end que verifica pipeline completo do input inicial ao output final, testando integracao entre multiplos agentes/stages.

e2e_eval NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| unit_eval | unit_eval testa agente ISOLADO. e2e_eval testa PIPELINE completo. | P07 unit_eval |
| smoke_eval | smoke_eval verifica sanidade rapida (<30s). e2e_eval testa fluxo completo. | P07 smoke_eval |
| benchmark | benchmark mede PERFORMANCE (latencia, custo). e2e_eval verifica CORRETUDE de pipeline. | P07 benchmark |
| golden_test | golden_test eh referencia quality 9.5+ de artefato unico. e2e_eval testa integracao. | P07 golden_test |
| scoring_rubric | scoring_rubric define CRITERIOS. e2e_eval APLICA verificacao em pipeline. | P07 scoring_rubric |
| workflow | workflow DEFINE o fluxo (P12). e2e_eval TESTA o fluxo (P07). | P12 workflow |

Regra: "o pipeline completo produz resultado correto?" -> e2e_eval.

## Position in Evaluation Flow

```text
smoke_eval (quick sanity) -> unit_eval (individual tests) -> e2e_eval (pipeline test) -> quality_gate (pass/fail)
```

e2e_eval is the INTEGRATION LAYER — verifies that components work together correctly.

## Dependency Graph

```text
e2e_eval <--composes-- unit_eval (P07 individual tests feed pipeline test)
e2e_eval <--requires_pass-- smoke_eval (P07 smoke must pass first)
e2e_eval <--tests-- workflow (P12 defines the pipeline being tested)
e2e_eval --produces_for--> quality_gate (P11 uses e2e results for pass/fail)
e2e_eval --produces_for--> benchmark (P07 aggregates pipeline metrics)
e2e_eval --independent-- golden_test, scoring_rubric, lifecycle_rule
```

## Fractal Position
Pillar: P07 (Evals — how to measure quality)
Function: GOVERN
Scale: L0 (governance artifact)
e2e_eval is the most comprehensive eval in P07 — tests complete pipeline integration.
