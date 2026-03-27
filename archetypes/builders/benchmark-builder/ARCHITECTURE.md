---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of benchmark in the CEX fractal
---

# Architecture: benchmark in the CEX

## Boundary
benchmark EH: medicao quantitativa de performance (latencia, throughput, custo, qualidade) com metodologia reproduzivel.

benchmark NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| scoring_rubric | rubric DEFINE criterios de qualidade multi-dimensional. benchmark MEDE performance. | P07 scoring_rubric |
| unit_eval | unit_eval TESTA corretude de agente/prompt. benchmark MEDE velocidade/custo. | P07 unit_eval |
| golden_test | golden_test FORNECE exemplo referencia. benchmark FORNECE numeros. | P07 golden_test |
| smoke_eval | smoke_eval VERIFICA sanidade rapida. benchmark MEDE com rigor estatistico. | P07 smoke_eval |
| e2e_eval | e2e_eval TESTA pipeline end-to-end. benchmark MEDE performance quantitativa. | P07 e2e_eval |

Regra: "quao rapido, barato, ou eficiente eh X?" -> benchmark.

## Position in Performance Flow

```text
environment setup -> warmup runs -> benchmark measurement -> percentile analysis -> comparison report
```

benchmark is MEASUREMENT LAYER — captures quantitative performance data that scoring_rubrics and quality_gates reference.

## Dependency Graph

```text
benchmark --produces_for--> scoring_rubric (P07 uses metrics as evaluation input)
benchmark --produces_for--> quality_gate (P11 uses thresholds from benchmark baselines)
benchmark --produces_for--> model_card (P02 uses benchmark data for performance specs)
benchmark <--environment_from-- boot_config (P02 provides runtime configuration)
benchmark --independent-- signal, handoff, knowledge_card
```

## Fractal Position
Pillar: P07 (Evals — how to measure quality)
Function: GOVERN
Scale: L0 (governance artifact)
benchmark is unique in P07 because it provides RAW NUMBERS — the quantitative foundation that other eval types interpret.
