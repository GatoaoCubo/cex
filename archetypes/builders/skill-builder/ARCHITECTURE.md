---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of skill in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: skill in the CEX

## Boundary
skill EH: habilidade reutilizavel com fases estruturadas e trigger definido. Executada
por agente ou usuario, produz output concreto, pode ser composta com outras skills.
Sem identidade, sem persona — capability pura com lifecycle.

skill NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| agent | agent tem identidade/persona completa; skill nao tem "eu" | P02 agent |
| action_prompt | action_prompt eh prompt puro sem fases; skill tem lifecycle estruturado | P03 action_prompt |
| component | component eh bloco atomico de pipeline sem fases nomeadas; skill tem lifecycle | P04 component |
| hook | hook eh handler de evento unico (pre/post); skill tem fases multiplas | P04 hook |
| mcp_server | mcp_server expoe tools via protocolo MCP; skill eh executada diretamente | P04 mcp_server |
| plugin | plugin eh extensao plugavel ao sistema; skill eh capability invocavel | P04 plugin |
| client | client eh consumidor unidirecional de API; skill eh workflow multi-fase | P04 client |
| cli_tool | cli_tool eh comando pontual sem fases; skill tem lifecycle com validate | P04 cli_tool |
| scraper | scraper eh extrator de dados web especializado; skill eh capability generica | P04 scraper |
| connector | connector eh integracao bidirecional de servico; skill nao gerencia conexao | P04 connector |
| daemon | daemon eh processo persistente em background; skill termina apos execute | P04 daemon |

Regra: "tem fases nomeadas e trigger definido e eh reutilizavel?" -> skill.

## Position in Agent Execution Flow

```text
agent (P02) --invokes--> skill (P04) --calls--> mcp_server (P04)
     |                       |                        |
system_prompt (P03)    phases: discover          tools: brain_query
                              configure          tools: validate_artifact
                              execute
                              validate
```

skill is the CAPABILITY LAYER — reusable across agents, composable via sub_skills.

## Dependency Graph

```text
skill <--receives-- input_schema (P06) (contract for skill inputs)
skill <--receives-- knowledge_card (P01) (domain knowledge injected at discover phase)
skill <--uses-- mcp_server (P04) (MCP tools called during execute phase)
skill <--uses-- component (P04) (atomic blocks composed inside execute phase)
skill --consumed_by--> agent (P02) (agent invokes skill via trigger)
skill --consumed_by--> workflow (P12) (workflow orchestrates skill execution)
skill --produces_for--> signal (P12) (skill emits complete/error signal after validate)
skill --independent-- system_prompt, action_prompt, hook, daemon
```

## Fractal Position
Pillar: P04 (Tools — what the agent USES)
Function: CALL (LLM calls this skill to execute a capability)
Scale: L1 (core — every non-trivial agent needs reusable skills)
skill is the MOST NUMEROUS P04 artifact: 118+ skills exist in CODEXA corpus.
