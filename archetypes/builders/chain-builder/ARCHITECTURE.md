---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of chain in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: chain in the CEX

## Boundary
chain EH: sequencia de prompts encadeados onde output A eh input B — pipeline de texto puro, sem agentes, sem tools, sem signals.

chain NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| workflow | workflow orquestra agentes+tools+signals em runtime | P12 workflow |
| dag | dag define dependencias entre tasks sem semantica de execucao | P12 dag |
| chain_of_thought | CoT eh tecnica de raciocinio INTRA-prompt, nao pipeline | P03 chain_of_thought |
| instruction | instruction eh receita passo-a-passo para um agente | P03 instruction |
| action_prompt | action_prompt eh prompt de tarefa unica | P03 action_prompt |

Regra: "quais prompts rodam em que ordem e como dados fluem entre eles?" -> chain.

## Position in Prompt Pipeline

```text
knowledge_card (P01) --> system_prompt (P03) --> chain (P03) --> output_schema (P05)
                                                   |
                                            step_1 --> step_2 --> step_N
                                                          |
                                                   [text only, no agents]
```

chain is COMPOSITION LAYER — text-to-text transformations chained sequentially.

## Dependency Graph

```text
chain <--receives-- system_prompt (P03) (identity context for step prompts)
chain <--receives-- output_schema (P05/P06) (typed contracts between steps)
chain <--receives-- knowledge_card (P01) (domain knowledge injected into steps)
chain --consumed_by--> workflow (P12) (may embed chains as prompt substeps)
chain --independent-- signal, spawn_config, dispatch_rule, handoff
```

## Fractal Position
Pillar: P03 (Prompt — how the agent SPEAKS)
Function: PRODUCE (creates structured output through step composition)
Scale: L0 (core 24 — chains are fundamental to any multi-step LLM system)
chain is the MULTI-STEP composition primitive: ~240 ADW files in CODEXA already function as implicit chains.
