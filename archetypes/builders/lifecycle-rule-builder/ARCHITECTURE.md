```yaml
---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of lifecycle_rule in the CEX fractal
---
```

# Architecture: lifecycle_rule in the CEX

## Boundary
lifecycle_rule EH: regra declarativa de ciclo de vida que governa QUANDO artefatos mudam de estado (freshness, archive, promote, sunset).

lifecycle_rule NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| hook | hook EXECUTA codigo em eventos. lifecycle_rule DECLARA politica de estados. | P04 hook |
| runtime_rule | runtime_rule gerencia SISTEMA (timeouts, retries). lifecycle_rule gerencia ARTEFATO (freshness, archive). | P09 runtime_rule |
| quality_gate | quality_gate mede QUALIDADE num ponto. lifecycle_rule gerencia ESTADO ao longo do tempo. | P11 quality_gate |
| guardrail | guardrail previne DANO. lifecycle_rule gerencia FRESHNESS. | P11 guardrail |
| bugloop | bugloop CORRIGE bugs em ciclo. lifecycle_rule TRANSICIONA estados por tempo/criterio. | P11 bugloop |
| optimizer | optimizer MELHORA metricas continuamente. lifecycle_rule GOVERNA transicoes discretas. | P11 optimizer |

Regra: "quando este artefato deve mudar de estado, e quem decide?" -> lifecycle_rule.

## Position in Governance Flow

```text
artifact produced -> quality_gate (pass?) -> active -> lifecycle_rule (stale?) -> review -> promote/archive/sunset
```

lifecycle_rule is GOVERNANCE LAYER — declarative time-based policies applied after initial quality approval.

## Dependency Graph

```text
lifecycle_rule <--receives-- quality_gate (P11) — initial quality score determines entry state
lifecycle_rule <--informed_by-- scoring_rubric (P07) — criteria for promote/demote decisions
lifecycle_rule --enforced_by--> hook (P04) — cron/event hooks execute transitions
lifecycle_rule --monitored_by--> signal (P12) — state changes emit signals
lifecycle_rule --independent-- knowledge_card, guardrail, system_prompt
```

## Fractal Position
Pillar: P11 (Feedback — how to improve)
Function: GOVERN
Scale: L0 (governance artifact)
lifecycle_rule is unique in P11 because it operates on TIME dimension — all other P11 types operate on QUALITY or SAFETY dimensions.
