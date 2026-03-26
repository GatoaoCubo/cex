---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of golden_test in the CEX fractal
---

# Architecture: golden_test in the CEX

## Boundary
golden_test EH: caso de teste referencia quality 9.5+ que calibra avaliacao de artefatos.

golden_test NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| unit_eval | unit_eval testa a QUALQUER nivel. golden_test exige 9.5+. | P07 unit_eval |
| smoke_eval | smoke_eval verifica sanidade rapida. golden_test eh referencia curada. | P07 smoke_eval |
| e2e_eval | e2e_eval testa pipeline completo. golden_test testa artefato unico. | P07 e2e_eval |
| benchmark | benchmark mede PERFORMANCE (latencia, custo). golden_test mede QUALIDADE exemplar. | P07 benchmark |
| scoring_rubric | rubric define CRITERIOS. golden_test fornece EXEMPLO concreto. | P07 scoring_rubric |
| few_shot_example | few_shot_example ENSINA pattern (P01). golden_test AVALIA qualidade (P07). | P01 few_shot_example |

Regra: "como eh um artefato perfeito deste tipo?" -> golden_test.

## Position in Evaluation Flow

```text
scoring_rubric (define criteria) -> golden_test (reference example) -> unit_eval (run tests) -> quality_gate (pass/fail)
```

golden_test is CALIBRATION LAYER — provides the ground truth for evaluation.

## Dependency Graph

```text
golden_test <--uses_criteria-- scoring_rubric (P07 defines dimensions)
golden_test <--validates_against-- quality_gate (P11 defines pass/fail)
golden_test --produces_for--> unit_eval (P07 uses as reference)
golden_test --produces_for--> benchmark (P07 uses as quality anchor)
golden_test --independent-- signal, handoff, lifecycle_rule
```

## Fractal Position
Pillar: P07 (Evals — how to measure quality)
Function: GOVERN
Scale: L0 (governance artifact)
golden_test is unique in P07 because it requires quality 9.5+ — the highest bar in the evaluation pillar.
