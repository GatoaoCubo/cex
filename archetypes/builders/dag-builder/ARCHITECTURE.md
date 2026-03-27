---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of dag in the CEX fractal
pattern: every builder must know where its output fits and what it connects to
---

# Architecture: dag in the CEX

## Boundary
`dag` EH: grafo aciclico estatico de dependencias entre tasks, definindo
ordem de execucao e paralelismo possivel para um pipeline ou missao.

`dag` NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|--------------|
| workflow | workflow executa steps com error handling e runtime state | P12 workflow |
| component_map | component_map inventaria componentes com ownership e health | P08 component_map |
| chain | chain sequencia prompts texto-a-texto | P03 chain |
| spawn_config | spawn_config define parametros de boot de satelite | P12 spawn_config |
| signal | signal reporta eventos runtime atomicos | P12 signal |
| handoff | handoff instrui trabalho com contexto, tarefas e scope fence | P12 handoff |
| dispatch_rule | dispatch_rule define roteamento keyword-satelite | P12 dispatch_rule |
| crew | crew define protocolo de coordenacao multi-agente | P12 crew |

Regra:
- "o que depende do que?" -> `dag`
- "como executar passo a passo?" -> `workflow`
- "quais componentes existem?" -> `component_map`

## Position in Pipeline Design

```text
requirements -> dag (dependency spec) -> workflow (runtime execution) -> signal (feedback)
```

`dag` sits before execution, defining structure that workflows implement.
It is planning, not execution.

## Dependency Graph

```text
dag <--receives-- requirements / mission briefs
dag --produces_for--> workflow (P12) — execution implements DAG structure
dag --produces_for--> handoff (P12) — one handoff per DAG node
dag --produces_for--> spawn_config (P12) — parallelism informs spawn mode

dag --> consumed_by --> workflow engines / orchestrators / spawn_grid
dag --> informs --> execution_order / parallelism decisions
dag --> may_trigger --> handoff creation (one per node)

dag --independent-- signal emission
dag --independent-- dispatch_rule policy
dag --independent-- brain_index configuration
dag --independent-- crew coordination protocol
```

## Fractal Position
Pillar: P12 (Orchestration - "how coordination happens")
Function: PRODUCE
Scale: L1 pipeline spec
Static structure artifact in P12: more complex than signal, more abstract than workflow.

dag is STRUCTURE LAYER — static dependency specification.
