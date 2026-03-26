---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of router in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: router in the CEX

## Boundary
router EH: logica de decisao de roteamento runtime — route tables com patterns, confidence thresholds,
fallback routes, e escalation policies. O router DECIDE para onde uma task vai baseado em analise
do input, nao simplesmente mapeia keywords.

router NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| dispatch_rule | dispatch_rule mapeia keyword-satellite sem logica; router ANALISA e DECIDE com confidence | P12 dispatch_rule |
| workflow | workflow orquestra SEQUENCIA de steps; router decide UM destino | P12 workflow |
| agent | agent EH a entidade executora; router DIRECIONA para o agent | P02 agent |
| fallback_chain | fallback_chain define degradacao de MODELO; router define escolha de DESTINO | P02 fallback_chain |
| mental_model | mental_model eh blueprint de decisoes; router eh regra concreta de roteamento | P02 mental_model |
| dag | dag define grafo de dependencias; router define ponto unico de decisao | P12 dag |

Regra: "para onde esta task deve ir?" -> router.

## Position in Dispatch Flow

```text
task_input --> router (P02) --> agent (P02) --> skill (P04) --> output
                  |                                    ^
                  v                                    |
            dispatch_rule (P12) ----fallback--->  fallback_chain (P02)
            (simple keyword map)              (model degradation)
```

router is the DECISION LAYER — sits between task input and agent execution,
applying pattern matching, confidence scoring, and fallback logic.

## Dependency Graph

```text
router <--receives-- dispatch_rule (P12) (keyword hints for pattern matching)
router <--receives-- model_card (P02) (model capabilities inform routing)
router --produces_for--> agent (P02) (selected destination receives task)
router --produces_for--> workflow (P12) (routing within orchestration)
router --produces_for--> spawn_config (P12) (satellite selection for spawn)
router --independent-- knowledge_card, system_prompt, signal
```

## Fractal Position
Pillar: P02 (Model — WHO makes decisions)
Function: DECIDE (routing logic applied at runtime)
Layer: runtime (executes per-task, stateless decision)
Scale: L0 (infrastructure — every multi-agent system needs routing)
