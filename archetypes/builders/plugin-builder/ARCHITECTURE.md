---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of plugin in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: plugin in the CEX

## Boundary
plugin EH: extensao plugavel runtime — modulo com interface contract, API surface, lifecycle
management, configuracao, e isolamento que estende o sistema sem modificar o core. O plugin
IMPLEMENTA um contrato e EXPOE metodos que o host pode invocar.

plugin NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| hook | hook INTERCEPTA um evento especifico; plugin EXTENDE com API completa | P04 hook |
| skill | skill tem FASES estruturadas de workflow; plugin tem INTERFACE e API surface | P04 skill |
| mcp_server | mcp_server implementa PROTOCOLO MCP; plugin implementa interface CUSTOM | P04 mcp_server |
| daemon | daemon RODA continuamente em background; plugin eh CARREGADO sob demanda | P04 daemon |
| connector | connector CONECTA a servico externo; plugin EXTENDE sistema interno | P04 connector |
| client | client CONSOME API externa; plugin PROVEE API interna | P04 client |
| cli_tool | cli_tool eh INVOCADO pelo user; plugin eh CARREGADO pelo sistema | P04 cli_tool |
| scraper | scraper COLETA dados da web; plugin EXTENDE sistema interno | P04 scraper |
| component | component eh BLOCO composavel de pipeline; plugin eh PLUGAVEL no host | P04 component |

Regra: "como adicionar esta capacidade como extensao plugavel ao sistema?" -> plugin.

## Position in Extension Flow

```text
host system --> plugin registry --> plugin (P04) --> API surface --> consumers
                    |                    |
               [discovery]          [lifecycle]
               [dependency]         on_load -> on_enable -> on_disable -> on_unload
```

plugin is the EXTENSION LAYER — sits between host system and added capabilities,
providing modular extensibility through interface contracts and managed lifecycle.

## Dependency Graph

```text
plugin <--loaded_by-- host system (plugin registry discovers and loads)
plugin <--configured_by-- config (P09) (runtime configuration)
plugin <--may_depend_on-- plugin (P04) (other plugins as dependencies)
plugin --exposes--> api_surface (methods callable by host/other plugins)
plugin --may_use--> hook (P04) (register hooks during on_load)
plugin --may_use--> mcp_server (P04) (consume MCP tools)
plugin --may_emit--> signal (P12) (report plugin lifecycle events)
plugin --independent-- parser, formatter, knowledge_card, model_card
```

## Fractal Position
Pillar: P04 (Tools — WHAT the agent USES)
Function: EXTEND (add capabilities through pluggable modules)
Layer: runtime (loaded on demand, managed lifecycle)
Scale: L1 (application — plugins extend specific system capabilities)
