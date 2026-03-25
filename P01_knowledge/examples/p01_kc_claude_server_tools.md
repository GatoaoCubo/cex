---
id: p01_kc_claude_server_tools
type: knowledge_card
lp: P01
title: "Claude Server Tools — Code Execution, Web Search, Memory (API Specs)"
version: 2.0.0
created: 2026-02-23
updated: 2026-03-25
author: PYTHA
domain: llm_engineering
quality: null
tags: [claude, server-tools, code-execution, web-search, memory, api]
tldr: "4 server tools executam na infra Anthropic sem implementacao client-side: code_execution (sandbox Python), web_search, web_fetch, memory (KV persistente). Max 10 iteracoes/response."
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
  related: [p01_kc_claude_agent_sdk_patterns, p01_kc_claude_model_capabilities_2026]
density_score: null
data_source: "https://docs.anthropic.com/en/docs/agents-and-tools/tool-use"
---

## Summary

Server tools executam na infraestrutura Anthropic dentro do sampling loop. Zero implementacao client-side — especificar no request basta. 4 tools: code execution (Python sandbox isolado com numpy/pandas/matplotlib), web search (busca real-time com domain filtering), web fetch (conteudo de URLs), memory (KV persistente cross-session). Limite: 10 iteracoes por response, `pause_turn` para continuar.

## Spec

| Tool | Type ID | Capacidade | Limite |
|------|---------|------------|--------|
| Code Execution | `code_execution_20250522` | Python sandbox, numpy/pandas/matplotlib | Sem rede, efemero |
| Web Search | `web_search_20250305` | Busca real-time, multi-query | Cobranca por busca |
| Web Fetch | `web_fetch_20250305` | HTML/text/PDF de URLs | Size + timeout limits |
| Memory | `memory_20250501` | KV persistente cross-session | Workspace-scoped |

| Parametro (web_search) | Funcao |
|------------------------|--------|
| max_uses | Limita buscas por request (controle de custo) |
| allowed_domains | Whitelist de dominios permitidos |
| blocked_domains | Blacklist de dominios bloqueados |

| Execution Flow | Detalhe |
|----------------|---------|
| 1. Include tool em `tools[]` | Versioned type string |
| 2. Claude decide usar | Dentro do response generation |
| 3. Server executa | Ate 10 iteracoes por response |
| 4. Limite atingido | `stop_reason: pause_turn`, reenviar para continuar |

## Patterns

| Trigger | Action |
|---------|--------|
| Analise de dados inline | code_execution com pandas/matplotlib |
| Informacao real-time necessaria | web_search + web_fetch sequencial |
| Estado cross-session necessario | memory: store/retrieve KV estruturado |
| Custo de search preocupa | max_uses=3 (limita buscas por request) |
| `stop_reason: pause_turn` | Reenviar response como assistant message |
| Server + client tools juntos | Claude auto-orquestra a sequencia |

## Anti-Patterns

- Implementar search/fetch client-side quando server tool ja faz
- Web search sem max_uses definido (custo API sem controle)
- Sandbox como storage persistente (efemero, perde entre calls)
- Memory tool para documentos grandes (projetado para KV, nao docs)
- Ignorar pause_turn stop_reason (perde resultado incompleto)
- Re-implementar file processing quando sandbox tem pandas/numpy

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
```

<!-- lang: python | purpose: handling pause_turn continuation -->
```python
if response.stop_reason == "pause_turn":
    messages.append({"role": "assistant", "content": response.content})
    response = client.messages.create(
        model="claude-sonnet-4-6-20250514",
        messages=messages, tools=tools
    )
```

## References

- external: https://docs.anthropic.com/en/docs/agents-and-tools/tool-use
- deepens: p01_kc_claude_agent_sdk_patterns (client-side tool orchestration)
- deepens: p01_kc_claude_model_capabilities_2026 (model compatibility per tool)
