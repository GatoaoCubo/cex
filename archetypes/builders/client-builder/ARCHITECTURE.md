---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of client in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: client in the CEX

## Boundary
client EH: consumidor unidirecional de API externa via REST, GraphQL, ou gRPC.
Faz requests, recebe responses, trata erros. Define endpoints, auth, rate limits.
Cada endpoint tem method + path + parameters. Client CONSOME, nunca EXPOE.

client NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| mcp_server | mcp_server EXPOE tools via MCP protocol; client CONSOME API | P04 mcp_server |
| connector | connector eh integracao BIDIRECIONAL; client eh unidirecional (request/response) | P04 connector |
| scraper | scraper extrai de HTML/DOM; client consome API estruturada (JSON/XML) | P04 scraper |
| skill | skill eh habilidade reutilizavel com fases; client eh consumidor de API | P04 skill |
| plugin | plugin eh extensao plugavel ao sistema; client eh consumidor externo | P04 plugin |
| cli_tool | cli_tool eh execucao pontual em terminal; client eh chamada programatica | P04 cli_tool |
| daemon | daemon eh processo background persistente; client eh chamada pontual | P04 daemon |
| hook | hook eh gatilho pre/post evento; client eh consumidor de API | P04 hook |
| component | component eh bloco composavel de pipeline; client eh consumidor externo | P04 component |

Regra: "quem CONSOME API externa via HTTP/gRPC de forma unidirecional?" -> client.

## Position in Agent Tool Flow

```text
knowledge_card (P01) --> agent (P02) --> client (P04) --> external_api
                              |                |
                         skill (P04)      response_data
                              |
                         mcp_server (P04)
```

client is CONSUMER LAYER — the bridge between agent runtime and external APIs.

## Dependency Graph

```text
client <--receives-- env_config (P09) (API keys, base URLs, timeouts)
client <--receives-- guardrail (P11) (rate limits, auth constraints)
client <--receives-- boot_config (P02) (client config injected at agent boot)
client --consumed_by--> agent (P02) (agent calls API via client)
client --consumed_by--> skill (P04) (skills may wrap client calls into phases)
client --independent-- mcp_server, connector, scraper, plugin, daemon
```

## Fractal Position
Pillar: P04 (Tools — what the agent USES)
Function: CALL (agent invokes API at runtime)
Layer: runtime (executes during agent session)
Scale: L2 (per-integration — one client per external API)
client is EXTENSION (not core_24): useful but not required for bootstrapping.
