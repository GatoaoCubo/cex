---
id: p01_kc_cex_function_call
kind: knowledge_card
pillar: P01
title: "CEX Function CALL — Tool Invocation Beyond Text Generation"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, call, tools, mcp, function-calling, plugin]
tldr: "CALL invoca ferramentas externas (APIs, MCPs, CLIs) via 8 tipos — expande LLM alem de texto"
when_to_use: "Entender como LLMs usam ferramentas e a fronteira entre CALL (instrumento) e COLLABORATE (agente)"
keywords: [call, tools, mcp, function-calling, plugin, skill, connector]
long_tails:
  - "Qual a diferenca entre CALL e COLLABORATE no CEX"
  - "Quais os 8 tipos de ferramentas na taxonomia CEX"
axioms:
  - "SEMPRE usar REASON antes de CALL em cadeias complexas"
  - "NUNCA confundir CALL (ferramenta passiva) com COLLABORATE (agente ativo)"
linked_artifacts:
  primary: p01_kc_cex_function_reason
  related: [p01_kc_cex_function_become, p01_kc_cex_function_inject]
density_score: null
data_source: "https://arxiv.org/abs/2307.16789"
---

## Summary

CALL invoca ferramentas externas para expandir capacidades do LLM alem de geracao de texto. O LLM seleciona a ferramenta, formata argumentos (function calling), executa e recebe resultado no contexto. Com 8 tipos (10% do CEX), cobre de funcoes atomicas (function_tool) a servidores MCP bidirecionais. Fronteira critica: CALL usa instrumentos passivos sem identidade; COLLABORATE conversa com agentes ativos com goals e memoria.

## Spec

| Tipo | LP | Complexidade | Funcao | Detalhe |
|------|-----|-------------|--------|---------|
| function_tool | P04 | Baixa | Funcao atomica | Schema tipado, invocacao direta |
| cli_tool | P04 | Baixa | Comando CLI | Invocacao unica sem wrapper |
| connector | P04 | Media | API client | SDK wrapper, retry, auth |
| plugin | P04 | Media | Extensao modular | Adiciona capacidade sem alterar core |
| component | P04 | Media | Unidade pipeline | I/O tipado, composavel (Haystack) |
| scraper | P04 | Media | Extrator web | HTML/JSON parsing, anti-bot |
| skill | P04 | Alta | Receita reusavel | Steps, quality gate, exemplos |
| mcp_server | P04 | Alta | Protocolo MCP | Bidirecional, stateful, stdio/sse |

Hierarquia de complexidade: function_tool < cli_tool < connector < skill < MCP.
function_tool e a forma minima: schema JSON + funcao pura.
MCP e a forma maxima: protocolo bidirecional com estado persistente.
Fronteira critica: CALL (ferramenta passiva, sem identidade) vs
COLLABORATE (agente ativo, com goals, memoria, persona).
LangChain separa Tool de Agent. CrewAI confirma Tool vs Agent.

## Code

<!-- lang: python | purpose: MCP tool invocation -->
```python
# function_tool: forma mais simples de CALL
@function_tool
def get_price(product_id: str) -> float:
    return db.query(f"SELECT price FROM products WHERE id=?", product_id)

# mcp_server: protocolo bidirecional com estado
mcp = MCPServer("brain", transport="stdio")
result = mcp.call("brain_query", {"query": "agent for research"})
# tool (passivo, sem goals) != agent (ativo, com identidade)
```

## Patterns

| Trigger | Action |
|---------|--------|
| Operacao atomica simples | function_tool com schema tipado |
| Capacidade existe como CLI | cli_tool sem wrapper |
| Integracao com servico externo | connector como API client |
| Extensao sem modificar entidade | plugin modular |
| Pipeline com interface padrao | component com I/O tipado |
| Capacidade padronizada e reutilizavel | skill com steps e quality gate |
| Acesso bidirecional com estado | mcp_server (MCP protocol) |

## Anti-Patterns

- Agent com 20+ tools sem especialistas (dividir)
- CALL sem REASON previo (acao sem planejamento)
- Confundir tool (passivo) com agent (ativo, com goals)
- MCP para operacao stateless simples (use function_tool)
- Skill sem quality gate (nao validavel)
- Connector sem retry/timeout (falha silenciosa)

## References

- source: https://arxiv.org/abs/2307.16789
- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_function_reason
- related: p01_kc_cex_function_become
