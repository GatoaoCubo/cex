---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of dispatch_rule in the CEX fractal
pattern: every builder must know where its output fits and what it connects to
---

# Architecture: dispatch_rule in the CEX

## Boundary
`dispatch_rule` EH: politica de roteamento que mapeia keywords/scope para um
satellite especifico, com fallback, priority e confidence_threshold. Decide
QUEM recebe um tipo de tarefa antes da execucao comecar.

`dispatch_rule` NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|--------------|
| handoff | handoff instrui trabalho: contexto completo, tarefas, scope fence, commit | P12 handoff |
| signal | signal reporta o que acabou de acontecer: status + quality + timestamp | P12 signal |
| workflow | workflow organiza passos sequenciais/paralelos com dependencias | P12 workflow |
| dag | dag modela grafo aciclico de dependencias entre tasks | P12 dag |
| spawn_config | spawn_config configura como lanccar satellites (modo, slots, timeout) | P12 spawn_config |
| crew | crew define grupo multi-agente com protocolo de coordenacao | P12 crew |
| router (P02) | router P02 faz roteamento complexo task>model multi-step com context | P02 router |

Regra:
- "quem deve receber este tipo de tarefa?" -> `dispatch_rule`
- "o que o agente deve fazer?" -> `handoff`
- "o que aconteceu?" -> `signal`
- "quais passos executar em sequencia?" -> `workflow`
- "como lancar N satellites?" -> `spawn_config`

## Position in Runtime Flow

```text
[input/task] -> dispatch_rule selects satellite -> handoff instructs satellite
             -> satellite executes -> signal reports -> monitor/next dispatch
```

`dispatch_rule` sits at the entry point of orchestration, before any work begins.
It is routing policy, not execution context.

## Dependency Graph

```text
dispatch_rule --> consumed_by --> orchestrator (STELLA, spawn_grid)
dispatch_rule --> consumed_by --> spawn_solo routing layer
dispatch_rule --> consumed_by --> auto-orchestrator wave queue

dispatch_rule --> precedes --> handoff (rule selects; handoff instructs)
dispatch_rule --> precedes --> spawn_config (rule selects; config launches)
dispatch_rule --> informed_by --> signal (completion signals may update priority)

dispatch_rule --independent-- workflow authoring
dispatch_rule --independent-- dag structure definition
dispatch_rule --independent-- crew protocol definition
dispatch_rule --independent-- knowledge_card, system_prompt, validator
```

## Fractal Position
Pillar: P12 (Orchestration — "how coordination happens")
Function: REASON
Scale: L0 routing policy record
Lightest routing artifact in P12: smaller than workflow, simpler than crew,
more specific than spawn_config.

## Relationship to STELLA Routing Table
STELLA_RULES.md contains an inline routing table (keywords -> satellite).
`dispatch_rule` artifacts are the formalized, versioned, machine-readable
equivalent of those inline table rows. They extend STELLA routing with:
- explicit priority ordering for conflict resolution
- confidence_threshold for ambiguous matches
- fallback satellite for availability failures
- optional routing_strategy for semantic matching
- conditions for AND-gating beyond keyword match

## Scaling Pattern
Single scope -> single `dispatch_rule` file.
Full system coverage -> one file per domain scope in `P12_orchestration/compiled/`.
Conflict resolution: higher `priority` wins when two rules match same input.
