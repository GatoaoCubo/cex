---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of mcp_server in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: mcp_server in the CEX

## Boundary
mcp_server EH: servidor MCP que expoe tools e resources para agentes LLM consumirem.
Implementa o Model Context Protocol (Anthropic) via transport stdio, SSE, ou HTTP.
Cada tool tem nome + JSON-Schema parameters. Cada resource tem URI template + content-type.

mcp_server NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| skill | skill eh habilidade reutilizavel com fases; mcp_server eh servidor de protocolo | P04 skill |
| connector | connector eh integracao bidirecional de servico; mcp_server expoe via MCP protocol | P04 connector |
| client | client CONSOME API; mcp_server EXPOE tools (provider, nao consumer) | P04 client |
| plugin | plugin eh extensao plugavel ao sistema; mcp_server eh servidor de protocolo independente | P04 plugin |
| cli_tool | cli_tool eh execucao pontual em linha de comando; mcp_server persiste e aceita conexoes | P04 cli_tool |
| scraper | scraper extrai dados web pontualmente; mcp_server expoe capacidades via protocolo | P04 scraper |
| daemon | daemon eh processo background sem protocol layer; mcp_server tem protocol MCP | P04 daemon |
| hook | hook eh gatilho pre/post evento; mcp_server eh servidor persistente de tools | P04 hook |
| component | component eh bloco composavel de pipeline; mcp_server eh servidor de protocolo | P04 component |

Regra: "quem expoe tools via MCP para agentes consumirem?" -> mcp_server.

## Position in Agent Tool Flow

```text
knowledge_card (P01) --> agent (P02) --> mcp_server (P04) --> external_service
                              |                |
                         skill (P04)    resources_provided
                              |
                         connector (P04)
```

mcp_server is TOOL LAYER — the bridge between agent runtime and external capabilities.

## Dependency Graph

```text
mcp_server <--receives-- boot_config (P02) (MCP config injected at agent boot)
mcp_server <--receives-- env_config (P09) (API keys, endpoints, transport config)
mcp_server <--receives-- guardrail (P11) (rate limits, auth constraints)
mcp_server --consumed_by--> agent (P02) (agent calls tools via MCP protocol)
mcp_server --produces_for--> skill (P04) (skills may wrap mcp_server tool calls)
mcp_server --independent-- connector, client, plugin, daemon
```

## Fractal Position
Pillar: P04 (Tools — what the agent USES)
Function: CALL (agent invokes tools at runtime)
Layer: runtime (executes during agent session)
Scale: L1 (infrastructure — shared across agents, not per-task)
mcp_server is CORE (in core_24): foundational for any agentic system needing external tools.
