---
lp: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of signal in the CEX fractal
pattern: every builder must know where its output fits and what it connects to
---

# Architecture: signal in the CEX

## Boundary
`signal` EH: evento runtime atomico emitido por um satellite para informar
status, qualidade e momento.

`signal` NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|--------------|
| handoff | handoff instrui trabalho: contexto, tarefas, scope fence, commit | P12 handoff |
| dispatch_rule | dispatch_rule decide roteamento futuro | P12 dispatch_rule |
| workflow | workflow organiza passos e dependencias de execucao | P12 workflow |
| interface | interface define contrato estavel entre sistemas | P06 validation/schema |

Regra:
- "o que aconteceu agora?" -> `signal`
- "o que o agente deve fazer?" -> `handoff`
- "quem deve receber este tipo de tarefa?" -> `dispatch_rule`

## Position in Runtime Flow

```text
dispatch_rule -> handoff -> execution -> signal -> monitor/next dispatch
```

`signal` sits after execution and before supervisory reaction.
It is feedback, not planning.

## Dependency Graph

```text
signal -> consumed_by -> spawn_monitor / supervisors / wave trackers
signal -> emitted_after -> handoff-driven execution
signal -> may_trigger -> next dispatch or retry policy

signal --independent-- workflow authoring
signal --independent-- routing policy definition
```

## Fractal Position
LP: P12 (Orchestration - "how coordination happens")
Function: COLLABORATE
Scale: L0 runtime event
Smallest collaborative artifact in P12: shorter than handoff, simpler than workflow.
