---
id: p02_agent_gateway
kind: agent
pillar: P02
title: Gateway Agent - Entry Point para Usuarios
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
domain: orchestration
quality: 9.1
tags: [gateway, router, mentor, intent-detection, handoff, entry-point]
tldr: Ponto de entrada unico - combina mentor (loop interativo) + router (semantic intent detection) com handoff para 5 workflows automaticos
when_to_use: Frontend chat, onboarding de usuarios, routing de intents
when_not_to_use: Tarefas diretas de agent_group (usar agent_group dispatch), admin tasks
keywords: [gateway, router, mentor, semantic-router, intent-detection]
long_tails:
  - como criar entry point unico para sistema multi-agente
  - como rotear intents do usuario para workflows automaticos
axioms:
  - Gateway NUNCA executa tasks (mentor OU router, nunca builder)
  - Intent ambiguo = perguntar (nao adivinhar routing)
density_score: 0.87
---

# Gateway Agent - Entry Point para Usuarios

## Architecture

```
+----------------------------------------------------------+
|                    GATEWAY_AGENT                           |
+----------------------------------------------------------+
|  INTENT DETECTOR                                          |
|  Comandos: -anuncio, -pesquisa, -photo, -combo           |
|  Keywords: anunciar, pesquisar, foto, completo            |
+----------------------------------------------------------+
|         |                              |                  |
|    MENTOR MODE                    ROUTER MODE             |
|     (loop)                        (handoff)               |
|                                       |                   |
|                              SEMANTIC_ROUTER (1-5)        |
|                   1        2       3       4       5      |
|                Pesquisa Anuncio  Combo   Photo  Gateway   |
|                (auto)   (auto) (pipeline)(auto)  (loop)   |
+----------------------------------------------------------+
```

## When to Use

| Cenario | Usar? | Alternativa |
|---------|-------|-------------|
| Frontend chat (organizationapp.com) | SIM | - |
| Routing de intents do usuario | SIM | - |
| Onboarding e duvidas | SIM | - |
| Agent_group dispatch direto | NAO | orchestrator |
| Admin/infra tasks | NAO | operations_agent |

## Capabilities

| # | Capability | Descricao |
|---|-----------|-----------|
| 1 | Mentor mode | Loop interativo para duvidas e orientacao |
| 2 | Intent detection | Keywords + comandos diretos (confianca 0.8+) |
| 3 | Semantic routing | Router 1-5 (pesquisa/anuncio/combo/photo/else) |
| 4 | Handoff | Transferencia de contexto para sub-workflows |
| 5 | Deploy-ready | System prompt + Knowledge Base + Workflow Config prontos |

## Intent Routing

| Output | Intent | Trigger |
|--------|--------|---------|
| 1 | PESQUISA | `-pesquisa [produto]` ou "pesquisar, mercado, concorrentes" |
| 2 | ANUNCIO | `-anuncio [produto]` ou "anunciar, listing, copy" |
| 3 | COMBO | `-combo [produto]` ou "completo, tudo, full" |
| 4 | FOTO | `-photo [produto]` ou "foto, imagem, visual" |
| 5 | ELSE | Qualquer outro → volta para mentor loop |

## Deploy Artifacts

| Artifact | Tokens | Purpose |
|----------|--------|---------|
| GATEWAY_SYSTEM_PROMPT.txt | ~1500 | System prompt do agent |
| SEMANTIC_ROUTER.txt | ~500 | Classificador 1-5 (temp=0, max=1 token) |
| KNOWLEDGE_BASE.json | ~2500 | Code Interpreter knowledge |
| KNOWLEDGE_ECOMMERCE.md | ~3000 | Vector Store knowledge |
| WORKFLOW_CONFIG.json | ~200 | Config n8n/Make |

## Integration

```yaml
upstream:
  - USER: "Input do usuario via chat"
  - orchestrator: "Routing interno do sistema"
downstream:
  - pesquisa-agent: "Intent 1 → pesquisa automatica"
  - anuncio-agent: "Intent 2 → criacao de anuncio"
  - photo-agent: "Intent 4 → geracao de fotos"
pipeline:
  - combo: "Intent 3 → pesquisa > anuncio (sequential)"
```

## Anti-Patterns

- Gateway executando research/marketing: viola papel de router — delegar para specialists
- Intent detection sem confianca threshold: routing errado — exigir >= 0.8 ou perguntar
- Semantic router com temperature > 0: output nao-deterministico — usar temperature=0
- Sem fallback (intent 5): usuario fica preso — sempre ter mentor loop como default

## Quality Gates

- System prompt < 2000 tokens (latencia)
- Intent classification accuracy >= 90%
- Handoff inclui full context (nao perder informacao)
- Custo/conversa < $0.05 USD
- Latencia < 3s/resposta

## References

- `records/agents/gateway/README.md` (fonte original)
- Deploy: OpenAI Agent Builder (gpt-4o + gpt-4o-mini router)
- Status: Production-Ready para organizationapp.com
