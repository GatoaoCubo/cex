---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of scoring_rubric in the CEX fractal
---

# Architecture: scoring_rubric in the CEX

## Boundary
scoring_rubric EH: framework de avaliacao com dimensoes ponderadas, thresholds por tier, e calibracao.

scoring_rubric NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| unit_eval | unit_eval EXECUTA teste. rubric DEFINE criterios. | P07 unit_eval |
| smoke_eval | smoke_eval verifica sanidade rapida. rubric define framework completo. | P07 smoke_eval |
| e2e_eval | e2e_eval testa pipeline. rubric define como avaliar. | P07 e2e_eval |
| benchmark | benchmark mede PERFORMANCE. rubric mede QUALIDADE multi-dimensional. | P07 benchmark |
| golden_test | golden_test fornece EXEMPLO concreto. rubric fornece CRITERIOS. | P07 golden_test |
| quality_gate | gate BLOQUEIA publicacao. rubric DEFINE como pontuar. | P11 quality_gate |

Regra: "quais dimensoes e pesos usar para avaliar este tipo?" -> scoring_rubric.

## Position in Evaluation Flow

```text
scoring_rubric (define criteria) -> golden_test (calibrate with examples) -> unit_eval (run tests) -> quality_gate (enforce pass/fail)
```

scoring_rubric is CRITERIA LAYER — defines the evaluation framework that all other P07 types use.

## Dependency Graph

```text
scoring_rubric --produces_for--> golden_test (P07 uses criteria for rationale)
scoring_rubric --produces_for--> quality_gate (P11 uses dimensions for SOFT gates)
scoring_rubric --produces_for--> unit_eval (P07 uses criteria for assertions)
scoring_rubric <--calibrated_by-- golden_test (P07 provides reference examples)
scoring_rubric --independent-- signal, handoff, knowledge_card
```

## Fractal Position
Pillar: P07 (Evals — how to measure quality)
Function: GOVERN
Scale: L0 (governance artifact)
scoring_rubric is unique in P07 because it defines the evaluation FRAMEWORK — the meta-level that all other eval types reference.
