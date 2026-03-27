---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of handoff in the CEX fractal
pattern: every builder must know where its output fits and what it connects to
---

# Architecture: handoff in the CEX

## Boundary
`handoff` EH: instrucao completa de delegacao que empacota tarefa, contexto,
escopo e regras de commit para um satelite executar autonomamente.

`handoff` NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|--------------|
| action_prompt | action_prompt eh prompt conversacional com persona e formato de resposta | P03 action_prompt |
| signal | signal eh evento atomico de status (complete, error, progress) | P12 signal |
| dispatch_rule | dispatch_rule define roteamento keyword-satelite | P12 dispatch_rule |
| workflow | workflow organiza steps com error handling e runtime state | P12 workflow |
| dag | dag define grafo de dependencias estatico entre tasks | P12 dag |
| spawn_config | spawn_config define parametros de boot (modelo, flags, MCP) | P12 spawn_config |
| crew | crew define protocolo de coordenacao multi-agente | P12 crew |

Regra:
- "o que o satelite deve fazer?" -> `handoff`
- "o que aconteceu?" -> `signal`
- "quem deve receber este tipo de tarefa?" -> `dispatch_rule`

## Position in Execution Flow

```text
dispatch_rule selects satellite -> handoff instructs work -> execution -> signal reports
```

`handoff` sits between routing decision and execution.
It is instruction, not feedback.

## Dependency Graph

```text
handoff <--receives-- dispatch_rule (P12)
dispatch_rule --> selects satellite --> handoff provides execution brief

handoff <--receives-- dag (P12)
dag --> defines dependency structure --> one handoff per node

handoff --produces_for--> signal (P12)
execution completes --> signal emitted --> signal_writer called from handoff Signal section

handoff --produces_for--> workflow (P12)
workflow may include handoffs as steps in larger orchestration flow

handoff --produces_for--> spawn_config (P12)
spawn_config may derive satellite/model params from handoff metadata

handoff --independent-- brain_index
handoff --independent-- axiom
handoff --independent-- component_map
handoff --independent-- chain
```

## Fractal Position
Pillar: P12 (Orchestration - "how coordination happens")
Function: COLLABORATE
Scale: L1 delegation instruction
Central coordination artifact in P12: richer than signal, more actionable than dag.

handoff is DELEGATION LAYER — actionable execution instructions.
