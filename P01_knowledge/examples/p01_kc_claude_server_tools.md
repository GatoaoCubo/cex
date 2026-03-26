---
id: p01_kc_claude_server_tools
kind: knowledge_card
pillar: P01
title: "Claude Server Tools — Code Execution, Web Search, Memory (API Specs)"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: EDISON
domain: llm_engineering
quality: null
tags: [claude, server-tools, code-execution, web-search, memory, api]
tldr: "4 server tools executam na infra Anthropic sem implementacao client-side: code_execution (sandbox Python), web_search, web_fetch, memory (KV persistente)."
when_to_use: "Integrar ferramentas server-side em workflows API ou decidir entre server tools vs client tools"
keywords: [server_tools, code_execution, web_search, web_fetch, memory_tool]
long_tails:
  - "Como usar code execution tool na API do Claude"
  - "Qual a diferenca entre server tools e client tools no Claude"
axioms:
  - "SEMPRE definir max_uses em web_search para controlar custos"
  - "NUNCA usar sandbox de code execution para storage persistente"
linked_artifacts:
  primary: null
  related: [p01_kc_claude_agent_sdk_patterns]
density_score: null
data_source: "https://docs.anthropic.com/en/docs/agents-and-tools/tool-use"
---

## Summary

Server tools executam na infraestrutura Anthropic dentro do sampling loop. Zero implementacao client-side — basta especificar no request. 4 tools: code execution (sandbox Python isolado), web search (busca real-time), web fetch (conteudo de URLs), memory (KV persistente cross-session). Ate 10 iteracoes por response.

## Spec

| Tool | Type ID | Capacidade | Limite |
|------|---------|------------|--------|
| Code Execution | `code_execution_20250522` | Python sandbox, numpy/pandas/matplotlib | Sem rede, efemero |
| Web Search | `web_search_20250305` | Busca real-time, multi-query | Cobranca por busca |
| Web Fetch | `web_fetch_20250305` | HTML/text/PDF de URLs | Size + timeout limits |
| Memory | `memory_20250501` | KV persistente cross-session | Workspace-scoped |

| Parametro Web Search | Funcao |
|---------------------|--------|
| max_uses | Limita buscas por request (controle de custo) |
| allowed_domains | Whitelist de dominios |
| blocked_domains | Blacklist de dominios |

| Fluxo | Detalhe |
|-------|---------|
| Include tool em `tools[]` | Versioned type string |
| Claude decide usar | Dentro do response generation |
| Server executa | Ate 10 iteracoes por response |
| `pause_turn` | Se limite atingido, reenviar para continuar |

## Patterns

| Trigger | Action |
|---------|--------|
| Analise de dados no response | code_execution: Python sandbox |
| Informacao real-time necessaria | web_search + web_fetch em sequencia |
| Estado entre sessoes | memory: store/retrieve KV |
| `stop_reason: pause_turn` | Reenviar response como assistant message |
| Server + client tools juntos | Claude orquestra a sequencia automaticamente |

## Anti-Patterns

- Implementar web search client-side quando server tool faz automatico
- Web search sem max_uses (custos API sem controle)
- Usar sandbox para storage persistente (efemero, perde entre calls)
- Memory tool para documentos grandes (projetado para KV estruturado)
- Ignorar pause_turn (resposta incompleta sem continuacao)

## Code

<!-- lang: python | purpose: server tools na API request -->
```python
response = client.messages.create(
    model="claude-sonnet-4-6-20250514",
    max_tokens=4096,
    tools=[
        {"type": "code_execution_20250522"},
        {"type": "web_search_20250305", "max_uses": 3,
         "allowed_domains": ["docs.anthropic.com"]},
    ],
    messages=[{"role": "user", "content": "Analyze this data..."}]
)
# Se stop_reason == "pause_turn": reenviar para Claude continuar
```

<!-- lang: python | purpose: handling pause_turn -->
```python
if response.stop_reason == "pause_turn":
    messages.append({"role": "assistant", "content": response.content})
    response = client.messages.create(
        model="claude-sonnet-4-6-20250514", messages=messages, tools=tools
    )
```

## References

- external: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use
- deepens: p01_kc_claude_agent_sdk_patterns (client-side tool orchestration)
