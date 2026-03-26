---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary and position of guardrail in the CEX fractal
---

# Architecture: guardrail in the CEX

## Boundary
guardrail EH: restricao de seguranca externa aplicada a agentes para prevenir danos.

guardrail NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| quality_gate | gate garante QUALIDADE com score. guardrail previne DANO. | P11 quality_gate |
| bugloop | bugloop CORRIGE bugs em ciclo. guardrail PREVINE acoes perigosas. | P11 bugloop |
| lifecycle_rule | lifecycle_rule gerencia FRESHNESS. guardrail gerencia SAFETY. | P11 lifecycle_rule |
| optimizer | optimizer MELHORA metricas. guardrail RESTRINGE comportamento. | P11 optimizer |
| permission | permission controla ACESSO (read/write). guardrail controla ACAO (safe/unsafe). | P09 permission |
| law | law define regra OPERACIONAL arquitetural. guardrail define restricao de SEGURANCA. | P08 law |

Regra: "o que este agente NUNCA deve fazer, e o que acontece se tentar?" -> guardrail.

## Position in Safety Flow

```text
law (operational rule) -> guardrail (safety boundary) -> permission (access control) -> enforcement (runtime check)
```

guardrail is SAFETY LAYER — external constraints that agents cannot override themselves.

## Dependency Graph

```text
guardrail <--derives_from-- law (P08 provides operational principles)
guardrail <--complemented_by-- permission (P09 controls access scope)
guardrail --enforced_by--> hook (P04 implements pre/post checks)
guardrail --monitored_by--> quality_gate (P11 tracks compliance)
guardrail --independent-- knowledge_card, signal, scoring_rubric
```

## Fractal Position
Pillar: P11 (Feedback — how to improve)
Function: CONSTRAIN
Scale: L0 (governance artifact)
guardrail is unique in P11 because it uses CONSTRAIN function (not GOVERN) — it restricts behavior rather than measuring quality.
