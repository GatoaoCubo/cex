---
pillar: P08
llm_function: CONSTRAIN
purpose: Boundary, relationships, and position of scraper in the CEX fractal
pattern: every builder must know WHERE its output fits and what it CONNECTS to
---

# Architecture: scraper in the CEX

## Boundary
scraper EH: extrator de dados web que coleta informacao de paginas HTML/DOM.
Usa CSS selectors ou XPath para localizar campos, trata paginacao, respeita rate limits.
Cada selector extrai um campo especifico. scraper EXTRAI dados nao-estruturados da web.

scraper NAO EH:

| Confusao | Por que NAO | Tipo correto |
|----------|-------------|-------------|
| client | client consome API estruturada (JSON/XML); scraper extrai de HTML/DOM | P04 client |
| connector | connector integra bidirecional; scraper eh somente leitura (extract) | P04 connector |
| parser | parser extrai de output LLM/texto; scraper extrai de web pages | P05 parser |
| mcp_server | mcp_server expoe tools via protocol; scraper consome web pages | P04 mcp_server |
| skill | skill eh habilidade com fases; scraper eh extrator pontual | P04 skill |
| plugin | plugin eh extensao plugavel; scraper eh extrator independente | P04 plugin |
| cli_tool | cli_tool processa input local; scraper acessa web remota | P04 cli_tool |
| daemon | daemon persiste em background; scraper executa e termina | P04 daemon |
| hook | hook eh gatilho pre/post evento; scraper eh invocado explicitamente | P04 hook |
| component | component eh bloco de pipeline; scraper eh extrator web standalone | P04 component |

Regra: "quem extrai dados de paginas web via selectors HTML/DOM?" -> scraper.

## Position in Agent Tool Flow

```text
knowledge_card (P01) --> agent (P02) --> scraper (P04) --> web_page
                              |                |
                         skill (P04)      extracted_data
                              |
                         client (P04) --> api
```

scraper is EXTRACTION LAYER — collects unstructured web data for agents.

## Dependency Graph

```text
scraper <--receives-- env_config (P09) (proxy config, API keys for anti-bot)
scraper <--receives-- guardrail (P11) (rate limits, robots.txt compliance)
scraper <--receives-- path_config (P09) (output directory, cache paths)
scraper --consumed_by--> agent (P02) (agent triggers scrape for data collection)
scraper --produces_for--> knowledge_card (P01) (scraped data becomes knowledge)
scraper --independent-- mcp_server, connector, daemon, plugin, hook
```

## Fractal Position
Pillar: P04 (Tools — what the agent USES)
Function: CALL (agent invokes scraper at runtime)
Layer: runtime (executes during agent session)
Scale: L2 (per-target — one scraper per web source)
scraper is EXTENSION (not core_24): useful but not required for bootstrapping.
