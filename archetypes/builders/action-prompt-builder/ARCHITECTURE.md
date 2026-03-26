---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of action_prompt in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: action_prompt in the CEX

## Boundary
action_prompt EH: prompt de acao task-focused com input/output definidos, injetado em runtime para executar uma tarefa especifica. Conversacional, denso, focado em resultado.

action_prompt NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| system_prompt | system_prompt define IDENTIDADE; action_prompt define TAREFA | P03 system_prompt |
| instruction | instruction eh receita com prerequisites/rollback; action_prompt eh prompt conciso | P03 instruction |
| prompt_template | prompt_template tem {{vars}} para reuso generico; action_prompt eh especifico | P03 prompt_template |
| user_prompt | user_prompt eh mensagem crua sem I/O tipado; action_prompt tem contrato | P03 user_prompt |
| chain | chain eh sequencia de prompts; action_prompt eh atomico | P03 chain |

Regra: "que prompt injeto para o agente executar ESTA tarefa especifica?" -> action_prompt.

## Position in Runtime Flow

```text
system_prompt (P03) --> agent loads identity
                             |
action_prompt (P03) -------> agent receives task with typed I/O
                             |
                        [execution]
                             |
                    output (validated) --> signal (P12) or next action_prompt
```

action_prompt is TASK INJECTION LAYER — the bridge between orchestration (dispatch) and execution (agent doing work).

## Dependency Graph

```text
action_prompt <--receives-- knowledge_card (P01) (domain context for task)
action_prompt <--receives-- output_schema (P05/P06) (output format spec)
action_prompt <--constrained_by-- system_prompt (P03) (identity constrains what tasks fit)
action_prompt --consumed_by--> agent (P02) (executes the task)
action_prompt --referenced_by--> chain (P03) (chains compose action_prompts)
action_prompt --independent-- instruction, workflow, signal
```

## Fractal Position
Pillar: P03 (Prompt — how the agent SPEAKS/ACTS)
Function: INJECT (injected into conversation at runtime)
Scale: L0 (core infrastructure — 287 HOPs + 255 handoffs are action_prompt-like)
action_prompt is the MOST DYNAMIC P03 artifact: created per-task, consumed once, results validated.
