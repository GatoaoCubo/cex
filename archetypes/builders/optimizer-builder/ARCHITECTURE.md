---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of optimizer in the CEX fractal
---

# Architecture: optimizer in the CEX

## Boundary
optimizer EH: ciclo continuo metric>action com thresholds tripartidos (trigger/target/critical),
baseline documentado, e monitoring. Otimiza processos ao longo do tempo com acoes automatizaveis.

optimizer NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|--------------|
| bugloop | bugloop eh ciclo detect-fix-verify para correcao pontual de um artefato. optimizer eh ciclo continuo de melhoria de processo. | P11 bugloop |
| quality_gate | quality_gate eh barreira pass/fail unica em evento de publicacao. optimizer eh ciclo continuo com thresholds e acoes. | P11 quality_gate |
| guardrail | guardrail previne DANOS (safety boundary, hard stop). optimizer busca MELHORIA (metric target, soft actions). | P11 guardrail |
| lifecycle_rule | lifecycle_rule governa ciclo de vida de artefatos (freshness/archive/promote). optimizer governa performance de processos. | P11 lifecycle_rule |
| benchmark | benchmark MEDE passivamente (P07, define criterios de avaliacao). optimizer AGE com base em medicoes. | P07 benchmark |
| scoring_rubric | scoring_rubric define HOW to evaluate. optimizer define WHAT action fires at WHAT threshold. | P07 scoring_rubric |

## Fractal Position
Pillar: P11 (Feedback)
Function: GOVERN
Layer: governance
Scale: L0 (governance artifact)

## Dependency Graph
```
optimizer --reads_metric_from--> validator (P06 implements metric collection)
optimizer --uses_thresholds_from--> scoring_rubric (P07 defines quality dimensions)
optimizer --triggers--> bugloop (P11 fires fix cycle when metric signals defect pattern)
optimizer --independent--> quality_gate (gate is event-driven; optimizer is continuous)
optimizer --independent--> guardrail (guardrail is hard stop; optimizer is soft improvement)
optimizer --independent--> lifecycle_rule (lifecycle is age/staleness; optimizer is performance)
optimizer --produces_history_for--> knowledge_card (improvement.history feeds KC updates)
optimizer --informs--> signal (optimizer state changes emit signals to P12)
```

## Information Flow
```
[live metric source]
        |
        v
[optimizer: compare metric to threshold.trigger]
        |
   above trigger?
        |-- YES --> [fire action (automated or manual approval)]
        |               |
        |               v
        |           [measure result]
        |               |
        |               v
        |           [append improvement.history]
        |
   below target for N cycles?
        |-- YES --> [restore conservative config (tune rollback)]
        |
   above critical?
        |-- YES --> [escalate (scale or page on-call, automated=false)]
```

## Builder Dependencies
| Dependency | Kind | Why |
|------------|------|-----|
| SCHEMA.md | self | field constraints |
| OUTPUT_TEMPLATE.md | self | production format |
| QUALITY_GATES.md | self | validation rules |
| KNOWLEDGE.md | self | threshold patterns, action types |

## Builders That Depend On optimizer-builder
| Builder | Why |
|---------|-----|
| signal-builder | Optimizer state changes emit signals |
| knowledge-card-builder | Improvement history feeds KC updates |
