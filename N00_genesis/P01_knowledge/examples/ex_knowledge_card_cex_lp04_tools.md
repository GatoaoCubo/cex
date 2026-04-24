---
id: p01_kc_cex_lp04_tools
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP04 Tools — O Que a LLM Usa (10 Tipos de Ferramenta)"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp04, tools, call, skill, mcp, hook, plugin]
tldr: "P04 Tools agrupa 10 tipos de ferramenta que estendem o LLM alem de texto via funcao CALL"
when_to_use: "Classificar artefatos de tooling ou entender como P04 conecta o LLM ao mundo externo"
keywords: [skill, mcp-server, hook, plugin, connector, daemon, component, cli-tool]
long_tails:
  - "Quais tipos de ferramenta existem no CEX"
  - "Diferenca entre skill e component no CEX"
axioms:
  - "SEMPRE registrar tools no agent antes de usar"
  - "NUNCA expor tool sem permissao explicita (P09 governa)"
linked_artifacts:
  primary: p01_kc_cex_lp03_prompt
  related: [p01_kc_cex_lp02_model, p01_kc_cex_lp01_knowledge]
density_score: 1.0
data_source: "https://arxiv.org/abs/2305.16504"
related:
  - p01_kc_cex_function_call
  - p01_kc_lp04_tools
  - api-client-builder
  - mcp-server-builder
  - p01_kc_mcp_server
  - cli-tool-builder
  - p01_kc_cex_lp03_prompt
  - p01_kc_cex_lp02_model
  - p01_kc_cex_lp01_knowledge
  - db-connector-builder
---

## Quick Reference

topic: LP04 Tools | scope: 10 tipos de artefato | criticality: high
funcao_llm: CALL (+ GOVERN para hook/daemon)
analogia: caixa de ferramentas

## Conceitos Chave

- P04 responde: "que ferramentas externas posso invocar?"
- skill eh o tipo core (habilidade rica com fases e trigger)
- Funcao dominante CALL: LLM invoca tool durante geracao
- mcp_server expoe tools + resources via protocolo MCP
- hook executa codigo em evento pre/post (GOVERN, nao CALL)
- component eh menor unidade composavel de pipeline
- Sem P04 o LLM so gera texto; com P04 interage com mundo
- P04 eh constrangido por P02 (identidade define tools)
- client eh consumidor unidirecional de API externa
- connector eh bidirecional (client eh unidirecional)
- daemon persiste em background (cli_tool executa e termina)
- scraper extrai dados web (nao confundir com client/API)
- plugin eh extensao plugavel sem fases estruturadas
- XAgent (Tsinghua): tools em Docker isolado = seguranca
- ToolBench cataloga 16.000+ APIs reais com benchmarks
- P04 interage com P09 (permissoes) e P07 (avaliacao)

## Fases

1. Registro: declarar tool no agent ou mcp_server
2. Permissao: P09 Config governa acesso e limites
3. Invocacao: LLM decide CALL durante geracao (ReAct loop)
4. Execucao: tool roda e retorna resultado ao contexto
5. Monitoramento: P07 Evals testa e avalia performance

## Regras de Ouro

- SEMPRE declarar tools antes de usar (registro explicito)
- SEMPRE isolar tools em containers quando possivel
- NUNCA dar acesso irrestrito a tools (least privilege)
- NUNCA usar daemon quando cli_tool basta (complexidade)
- SEMPRE preferir mcp_server sobre connector para novos tools

## Comparativo

| Tipo | Proposito | Persistente | Core |
|------|-----------|-------------|------|
| skill | Habilidade com fases + trigger | nao | sim |
| mcp_server | Servidor MCP (tools + resources) | sim | sim |
| hook | Pre/post processing em evento | nao | sim |
| plugin | Extensao plugavel | sim | nao |
| client | Cliente unidirecional de API | nao | nao |
| cli_tool | Ferramenta de linha de comando | nao | nao |
| scraper | Extrator de dados web | nao | nao |
| connector | Conector bidirecional externo | nao | nao |
| daemon | Processo background persistente | sim | nao |
| component | Bloco atomico de pipeline | nao | nao |

## Flow

```
[Agent (P02)] -- registra --> [skill / mcp_server / tool]
       |
[user_prompt (P03)] -- trigger --> [CALL decision]
       |
[ReAct loop] -- Thought --> Action --> Observation
       |                       |
       |              [tool executa]
       |                       |
       +<-- resultado volta ao contexto
       |
[Output (P05)] -- informado por tool results
```

## References

- source: https://arxiv.org/abs/2305.16504
- source: https://arxiv.org/abs/2307.16789
- deepens: p01_kc_cex_lp03_prompt
- related: p01_kc_cex_lp02_model


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_function_call]] | sibling | 0.32 |
| [[p01_kc_lp04_tools]] | sibling | 0.28 |
| [[api-client-builder]] | downstream | 0.25 |
| [[mcp-server-builder]] | downstream | 0.25 |
| [[p01_kc_mcp_server]] | sibling | 0.24 |
| [[cli-tool-builder]] | downstream | 0.24 |
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.24 |
| [[p01_kc_cex_lp02_model]] | sibling | 0.24 |
| [[p01_kc_cex_lp01_knowledge]] | sibling | 0.23 |
| [[db-connector-builder]] | downstream | 0.21 |
