---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of connector in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: connector in the CEX

## Boundary
connector EH: integracao bidirecional com servico externo via REST, WebSocket, gRPC,
ou MQTT. Envia dados outbound E recebe dados inbound (webhooks, streams, pub/sub).
Define endpoints com direcao, data mapping, transform rules, e health check.
Connector INTEGRA, nunca apenas CONSOME.

connector NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| client | client eh unidirecional (request/response); connector eh bidirecional | P04 client |
| mcp_server | mcp_server expoe tools via protocolo MCP; connector integra servico externo | P04 mcp_server |
| scraper | scraper extrai de HTML/DOM; connector usa APIs estruturadas bidirecionais | P04 scraper |
| skill | skill eh habilidade reutilizavel com fases; connector eh bridge de servico | P04 skill |
| plugin | plugin eh extensao plugavel; connector eh integracao externa especifica | P04 plugin |
| cli_tool | cli_tool eh execucao pontual em terminal; connector eh integracao persistente | P04 cli_tool |
| daemon | daemon eh processo background generico; connector define spec de integracao | P04 daemon |
| hook | hook eh gatilho pre/post evento pontual; connector eh bridge de servico continuo | P04 hook |
| component | component eh bloco composavel de pipeline; connector eh bridge externo | P04 component |

Regra: "quem INTEGRA servico externo BIDIRECIONALMENTE (envia E recebe)?" -> connector.

## Position in Integration Flow

```text
knowledge_card (P01) --> agent (P02) --> connector (P04) <--> external_service
                              |                |
                         client (P04)     webhooks_in
                         (one-way)        (events)
```

connector is BRIDGE LAYER — bidirectional data exchange between CEX runtime and external services.

## Dependency Graph

```text
connector <--receives-- env_config (P09) (API keys, service URLs, secrets)
connector <--receives-- guardrail (P11) (rate limits, auth constraints)
connector <--receives-- boot_config (P02) (connector config injected at boot)
connector --consumed_by--> agent (P02) (agent uses connector for bidirectional ops)
connector --consumed_by--> workflow (P12) (workflows orchestrate connector calls)
connector --consumed_by--> skill (P04) (skills may wrap connector into phases)
connector --independent-- mcp_server, scraper, plugin, daemon, cli_tool
```

## Fractal Position
Pillar: P04 (Tools — what the agent USES)
Function: CALL (agent invokes connector at runtime)
Layer: runtime (executes during agent session)
Scale: L2 (per-integration — one connector per external service)
connector is EXTENSION (not core_24): bidirectional integration, useful but not required for bootstrap.
