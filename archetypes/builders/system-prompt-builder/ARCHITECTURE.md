---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of system_prompt in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: system_prompt in the CEX

## Boundary
system_prompt EH: identidade persistente do agente — persona, regras ALWAYS/NEVER, formato de saida, e constraints. Lido PRIMEIRO pelo LLM antes de qualquer input do usuario.

system_prompt NAO EH:

| Confusao | Por que NAO | Type correto |
|----------|-------------|-------------|
| action_prompt | action_prompt define TAREFA especifica; system_prompt define IDENTIDADE | P03 action_prompt |
| instruction | instruction eh receita passo-a-passo; system_prompt eh persona | P03 instruction |
| prompt_template | prompt_template tem {{vars}} para reuso; system_prompt eh fixo por agente | P03 prompt_template |
| mental_model | mental_model eh blueprint de design-time; system_prompt eh runtime | P02/P10 mental_model |
| guardrail | guardrail eh restricao de seguranca externa; system_prompt internaliza regras | P11 guardrail |

Regra: "quem este agente EH e como ele RESPONDE?" -> system_prompt.

## Position in Agent Boot Flow

```text
mental_model (P10) --> knowledge_card (P01) --> system_prompt (P03) --> agent (P02)
                                                     ^                      |
                                               guardrail (P11)        action_prompt (P03)
                                                                           |
                                                                      execution
```

system_prompt is IDENTITY LAYER — the bridge between design-time (mental_model) and runtime (agent).

## Dependency Graph

```text
system_prompt <--receives-- knowledge_card (P01) (domain knowledge to inject)
system_prompt <--receives-- mental_model (P10) (routing rules, personality)
system_prompt <--receives-- guardrail (P11) (safety constraints to internalize)
system_prompt --consumed_by--> agent (P02) (loads as first message)
system_prompt --independent-- action_prompt, instruction, prompt_template
```

## Fractal Position
Pillar: P03 (Prompt — how the agent SPEAKS)
Function: BECOME (LLM assumes this identity)
Scale: L0 (core infrastructure — every agent needs one)
system_prompt is the MOST LOADED P03 artifact: 7 PRIMEs + 101 ISO system instructions + 10 Rules files already exist in CODEXA.
