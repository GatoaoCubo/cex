---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of instruction in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: instruction in the CEX

## Boundary
instruction EH: receita operacional passo-a-passo com prerequisites, validation, e rollback. Executada por um agente ou humano para completar uma tarefa especifica.

instruction NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| action_prompt | action_prompt eh prompt conversacional com input/output definidos | P03 action_prompt |
| system_prompt | system_prompt define identidade, nao passos de execucao | P03 system_prompt |
| workflow | workflow orquestra multiplos agentes; instruction eh single-agent | P12 workflow |
| skill | skill tem lifecycle phases e trigger; instruction eh one-shot | P04 skill |
| handoff | handoff despacha tarefa para satelite; instruction detalha execucao | P12 handoff |

Regra: "quais sao os passos EXATOS para executar esta tarefa?" -> instruction.

## Position in Execution Flow

```text
system_prompt (P03) --> agent loads identity
action_prompt (P03) --> agent receives task
instruction (P03) -----> agent follows steps <-- dependencies (P04)
                              |
                         validation
                              |
                    signal (P12) complete
```

instruction is EXECUTION LAYER — the detailed recipe between receiving a task and reporting completion.

## Dependency Graph

```text
instruction <--receives-- action_prompt (P03) (task context to decompose into steps)
instruction <--receives-- knowledge_card (P01) (domain knowledge for step details)
instruction --consumed_by--> agent (P02) (follows steps to execute)
instruction --referenced_by--> skill (P04) (skill phases may reference instructions)
instruction --independent-- system_prompt, workflow, signal
```

## Fractal Position
Pillar: P03 (Prompt — how the agent SPEAKS/ACTS)
Function: PRODUCE (following these steps produces the outcome)
Scale: L0 (core infrastructure — 213 ISO instructions + 255 handoffs already exist)
instruction is the MOST NUMEROUS P03 artifact in CODEXA, reflecting its operational nature.
