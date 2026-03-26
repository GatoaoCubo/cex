---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of agent in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: agent in the CEX

## Boundary
agent EH: entidade executora runtime — persona + capabilities + iso_vectorstore. O agente BECOMES
sua identidade quando carregado, possui ferramentas concretas, pertence a um satelite, e produz
outputs verificaveis. A definicao completa inclui 10+ ISO files no iso_vectorstore.

agent NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| skill | skill eh habilidade executavel (phases + trigger); agent EH identidade persistente | P04 skill |
| system_prompt | system_prompt define como o agente FALA; agent define QUEM ELE EH | P03 system_prompt |
| mental_model (P02) | mental_model eh blueprint estatico de design-time; agent eh entidade runtime | P02 mental_model |
| mental_model (P10) | mental_model P10 eh estado de sessao efemero; agent eh definicao permanente | P10 mental_model |
| model_card | model_card descreve o LLM subjacente; agent descreve QUEM usa o LLM | P02 model_card |
| boot_config | boot_config define como o agente INICIALIZA por provider; agent define O QUE ele eh | P02 boot_config |
| router | router define regras de roteamento task-to-satellite; agent EH o destino do routing | P02 router |
| fallback_chain | fallback_chain define sequencia de modelos alternativos; agent nao define fallback de modelo | P02 fallback_chain |
| iso_package | iso_package eh o bundle portable distribuivel; agent eh a definicao canonizada no repo | P02 iso_package |
| axiom | axiom eh principio imutavel de governanca; agent tem constraints mas eh editavel | P02 axiom |
| lens | lens eh perspectiva especializada sobre dominio; agent tem identidade completa executavel | P02 lens |

Regra: "quem este agente EH, o que pode fazer, e como esta estruturado?" -> agent.

## Position in Agent Boot Flow

```text
knowledge_card (P01) --> system_prompt (P03) --> agent (P02) --> skill (P04)
       |                        |                    |               |
  domain facts           identity + rules      capabilities    executavel
                                                    |
                              mental_model (P02) ---+--- router (P02)
                              (design blueprint)         (routing rules)
```

agent is RUNTIME IDENTITY LAYER — bridges design-time specs (mental_model, system_prompt)
with execution (skills, tools, downstream agents).

## Dependency Graph

```text
agent <--receives-- system_prompt (P03) (identity and rules)
agent <--receives-- knowledge_card (P01) (domain knowledge)
agent <--receives-- mental_model (P02) (routing and decisions)
agent <--receives-- model_card (P02) (LLM capabilities)
agent <--receives-- boot_config (P02) (initialization per provider)
agent --produces--> iso_package (P02) (portable bundle)
agent --produces--> skill (P04) (reusable capabilities)
agent --consumed_by--> router (P02) (routing destination)
agent --consumed_by--> workflow (P12) (orchestration node)
agent --consumed_by--> spawn_config (P12) (spawn target)
agent --independent-- model_card, lens, fallback_chain
```

## Fractal Position
Pillar: P02 (Model — QUEM o agente EH)
Function: BECOME (LLM assumes this identity and capabilities)
Layer: runtime (executes with state, produces outputs)
Scale: L0 (core infrastructure — every agentic system needs agent definitions)
iso_vectorstore: 10 required ISO files minimum per agent (MANIFEST, QUICK_START, PRIME,
INSTRUCTIONS, ARCHITECTURE, OUTPUT_TEMPLATE, EXAMPLES, ERROR_HANDLING, UPLOAD_KIT, SYSTEM_INSTRUCTION)
