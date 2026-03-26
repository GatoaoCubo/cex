---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of workflow in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: workflow in the CEX

## Boundary
workflow EH: orquestracao runtime de agentes+tools+signals em steps sequenciais/paralelos. Define QUEM faz O QUE, em que ORDEM, com quais DEPENDENCIAS.

workflow NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| chain | chain eh sequencia de PROMPTS (texto->texto) sem agentes | P03 chain |
| dag | dag eh grafo de dependencias sem semantica de execucao | P12 dag |
| dispatch_rule | dispatch_rule roteia por keyword, nao orquestra | P12 dispatch_rule |
| handoff | handoff eh instrucao de tarefa unica para 1 satelite | P12 handoff |
| crew | crew define COMO agentes colaboram (protocolo), workflow define QUANDO | P12 crew |

Regra: "quais agentes rodam em que ordem, com que dependencias e signals?" -> workflow.

## Position in Orchestration Flow

```text
dispatch_rule (P12) --> handoff (P12) --> spawn_config (P12) --> workflow (P12)
                                                                      |
                                                    step_1 [sat_A] --> step_2 [sat_B]
                                                         |                   |
                                                    signal (P12)        signal (P12)
                                                                             |
                                                                     workflow_complete
```

workflow is ORCHESTRATION LAYER — the highest-level runtime coordinator.

## Dependency Graph

```text
workflow <--receives-- handoff (P12) (task instructions per step)
workflow <--receives-- spawn_config (P12) (how to launch each satellite)
workflow <--receives-- signal (P12) (completion/error events from steps)
workflow <--receives-- chain (P03) (may embed as prompt substep)
workflow --consumed_by--> STELLA (orchestrator reads workflow to dispatch)
workflow --independent-- boot_config, env_config, mental_model
```

## Fractal Position
Pillar: P12 (Orchestration — how it COORDINATES)
Function: PRODUCE (creates execution plan for multi-agent missions)
Scale: L0 (core 24 — every multi-step mission needs a workflow)
workflow is the TOP-LEVEL orchestration artifact: ~240 ADW files in CODEXA are implicit workflows.
