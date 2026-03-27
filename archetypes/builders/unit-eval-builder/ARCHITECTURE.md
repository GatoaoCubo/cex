---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of unit_eval in the CEX fractal
---

# Architecture: unit_eval in the CEX

## Boundary
unit_eval EH: teste unitario que verifica corretude de agente/prompt individual com assertions mapeadas a gates.

unit_eval NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| smoke_eval | smoke_eval testa sanidade rapida (<30s, sem profundidade). unit_eval testa corretude com assertions. | P07 smoke_eval |
| e2e_eval | e2e_eval testa pipeline completo (multiplos agentes). unit_eval testa agente isolado. | P07 e2e_eval |
| benchmark | benchmark mede PERFORMANCE (latencia, custo). unit_eval verifica CORRETUDE. | P07 benchmark |
| golden_test | golden_test exige quality 9.5+. unit_eval testa a qualquer nivel. | P07 golden_test |
| scoring_rubric | scoring_rubric define CRITERIOS. unit_eval APLICA criterios via assertions. | P07 scoring_rubric |
| few_shot_example | few_shot_example ENSINA pattern (P01). unit_eval VERIFICA corretude (P07). | P01 few_shot_example |

Regra: "este agente produz saida correta para esta entrada?" -> unit_eval.

## Position in Evaluation Flow

```text
scoring_rubric (define criteria) -> golden_test (reference example) -> unit_eval (run tests) -> quality_gate (pass/fail)
```

unit_eval is the VERIFICATION LAYER — runs assertions against actual agent output.

## Dependency Graph

```text
unit_eval <--uses_criteria-- scoring_rubric (P07 defines dimensions)
unit_eval <--uses_reference-- golden_test (P07 provides expected quality)
unit_eval --produces_for--> quality_gate (P11 uses results for pass/fail)
unit_eval --produces_for--> benchmark (P07 aggregates test results)
unit_eval --independent-- signal, handoff, lifecycle_rule
```

## Fractal Position
Pillar: P07 (Evals — how to measure quality)
Function: GOVERN
Scale: L0 (governance artifact)
unit_eval is the workhorse of P07 — most frequent eval type, testing individual correctness.
