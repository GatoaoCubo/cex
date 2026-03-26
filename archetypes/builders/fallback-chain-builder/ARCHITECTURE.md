---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of fallback_chain in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: fallback_chain in the CEX

## Boundary
fallback_chain EH: sequencia de degradacao graceful de modelo runtime — steps ordenados do mais
capaz ao menos capaz, com timeouts, quality thresholds, circuit breakers, e cost controls.
Garante que o sistema continua funcionando mesmo quando o modelo primario falha.

fallback_chain NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| chain (P03) | chain sequencia PROMPTS (texto-texto); fallback_chain degrada MODELOS | P03 chain |
| workflow (P12) | workflow orquestra STEPS de agentes; fallback_chain troca MODELO mantendo a task | P12 workflow |
| router (P02) | router decide DESTINO da task; fallback_chain decide qual MODELO usar | P02 router |
| agent (P02) | agent eh entidade executora; fallback_chain configura RESILIENCIA do modelo | P02 agent |
| model_card (P02) | model_card descreve UM modelo; fallback_chain SEQUENCIA multiplos modelos | P02 model_card |
| boot_config (P02) | boot_config inicializa UM provider; fallback_chain transiciona entre providers | P02 boot_config |

Regra: "se este modelo falhar, qual usar em seguida?" -> fallback_chain.

## Position in Resilience Flow

```text
router (P02) --> agent (P02) --> model_card (P02) --> LLM call
                                       |
                                  [timeout/error/low quality]
                                       |
                                       v
                              fallback_chain (P02)
                              step 1: opus (primary)
                              step 2: sonnet (degraded)
                              step 3: haiku (minimum)
                                       |
                                  [circuit breaker]
                                       v
                                  signal (P12) error
```

fallback_chain is the RESILIENCE LAYER — activates when primary model fails,
providing graceful degradation instead of hard failure.

## Dependency Graph

```text
fallback_chain <--receives-- model_card (P02) (model specs for each step)
fallback_chain <--receives-- router (P02) (routing failures may trigger fallback)
fallback_chain --produces_for--> agent (P02) (provides resilient model selection)
fallback_chain --produces_for--> boot_config (P02) (model configuration per step)
fallback_chain --produces_for--> signal (P12) (emits degradation/circuit-breaker events)
fallback_chain --independent-- knowledge_card, system_prompt, skill, workflow
```

## Fractal Position
Pillar: P02 (Model — WHO handles resilience)
Function: DEGRADE (graceful capability reduction under failure)
Layer: runtime (activates on error/timeout, stateful across retries)
Scale: L0 (infrastructure — every production system needs fallback)
