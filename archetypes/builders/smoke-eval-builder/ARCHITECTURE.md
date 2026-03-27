---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of smoke_eval in the CEX fractal
---

# Architecture: smoke_eval in the CEX

## Boundary
smoke_eval EH: teste rapido de sanidade (<30s) que verifica se componentes basicos funcionam antes de prosseguir.

smoke_eval NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| unit_eval | unit_eval testa corretude com profundidade. smoke_eval so verifica sanidade. | P07 unit_eval |
| e2e_eval | e2e_eval testa pipeline completo. smoke_eval testa componentes isolados rapidamente. | P07 e2e_eval |
| benchmark | benchmark mede PERFORMANCE (latencia, custo). smoke_eval verifica FUNCIONAMENTO basico. | P07 benchmark |
| golden_test | golden_test exige quality 9.5+. smoke_eval eh binario (pass/fail). | P07 golden_test |
| scoring_rubric | scoring_rubric define CRITERIOS. smoke_eval APLICA checks rapidos. | P07 scoring_rubric |
| quality_gate | quality_gate BLOQUEIA com score (P11). smoke_eval DETECTA falha rapida (P07). | P11 quality_gate |

Regra: "isto funciona minimamente?" -> smoke_eval.

## Position in Evaluation Flow

```text
smoke_eval (quick sanity) -> unit_eval (deep test) -> e2e_eval (pipeline) -> quality_gate (pass/fail)
```

smoke_eval is the FIRST LINE OF DEFENSE — catches obvious failures before investing in deeper tests.

## Dependency Graph

```text
smoke_eval <--derives_checks-- unit_eval (P07 extracts fast checks from deep tests)
smoke_eval --gates--> unit_eval (P07 skip deep tests if smoke fails)
smoke_eval --gates--> e2e_eval (P07 skip pipeline if smoke fails)
smoke_eval --alerts--> signal (P12 notifies on failure)
smoke_eval --independent-- golden_test, scoring_rubric, lifecycle_rule
```

## Fractal Position
Pillar: P07 (Evals — how to measure quality)
Function: GOVERN
Scale: L0 (governance artifact)
smoke_eval is the fastest eval in P07 — maximum 30 seconds, first to run in any test pipeline.
