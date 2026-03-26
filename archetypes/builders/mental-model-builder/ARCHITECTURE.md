---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of mental_model (P02) in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: mental_model in the CEX

## Boundary
mental_model (P02) EH: blueprint estatico de design-time que codifica routing rules,
decision trees, priorities, heuristics, e domain maps de um agente — identidade
cognitiva permanente, versionada, parte do design do agente.

mental_model (P02) NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| mental_model (P10) | P10 eh estado de sessao efemero/mutavel; P02 eh design permanente | P10 mental_model |
| agent | agent eh identidade completa (persona + capabilities + iso); mental_model eh como PENSA | P02 agent |
| router | router define task-to-satellite routing externo; mental_model guia decisoes internas | P02 router |
| model_card | model_card spec do LLM; mental_model eh logica do agente que USA o LLM | P02 model_card |
| boot_config | boot_config define init params por provider; mental_model define cognition | P02 boot_config |
| iso_package | iso_package empacota para distribuir; mental_model eh um componente interno | P02 iso_package |
| fallback_chain | fallback_chain define modelo A->B->C; mental_model define logica de decisao | P02 fallback_chain |
| lens | lens eh perspectiva sobre dominio; mental_model eh mapa cognitivo completo | P02 lens |
| axiom | axiom eh principio imutavel de governanca; mental_model eh editavel e versionado | P02 axiom |
| system_prompt (P03) | system_prompt define como o agente FALA; mental_model define como PENSA | P03 system_prompt |

Regra: "como este agente roteia, decide, e prioriza?" -> mental_model (P02).

## Position in Agent Design Flow

```text
knowledge_card (P01) --> mental_model (P02) --> agent (P02) --> boot_config (P02)
        |                        |                   |                |
  domain facts          cognitive map          full identity     init params
                               |
              routing_rules + decision_tree + priorities
```

mental_model (P02) is COGNITIVE DESIGN LAYER — bridges domain knowledge
with agent identity by defining how the agent reasons and routes.

## Dependency Graph

```text
mental_model <--receives-- knowledge_card (P01) (domain facts inform routing)
mental_model <--receives-- agent (P02) (agent identity scopes decisions)
mental_model --produces_for--> agent (P02) (cognitive component of identity)
mental_model --produces_for--> boot_config (P02) (routing informs boot constraints)
mental_model --consumed_by--> router (P02) (routing rules feed dispatch)
mental_model --consumed_by--> workflow (P12) (decision logic in orchestration)
mental_model --independent-- model_card, iso_package, fallback_chain, lens
```

## Fractal Position
Pillar: P02 (Model — QUEM o agente EH)
Function: BECOME (agent internalizes this cognitive map)
Layer: spec (static design-time artifact, not runtime)
Scale: L0 (core infrastructure — every agent with routing needs a mental model)
Unique: only P02 kind with structured decision_tree and routing_rules objects.
Critical overlap: P10 mental_model — always verify pillar before building.
