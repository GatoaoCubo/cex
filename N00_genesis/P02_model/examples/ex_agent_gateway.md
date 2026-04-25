---
id: p02_agent_gateway
kind: agent
8f: F2_become
pillar: P02
title: Gateway Agent - Entry Point for Users
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: builder_agent
domain: orchestration
quality: 9.1
tags: [gateway, router, mentor, intent-detection, handoff, entry-point]
tldr: Single entry point - combines mentor (interactive loop) + router (semantic intent detection) with handoff to 5 automatic workflows
when_to_use: Frontend chat, user onboarding, intent routing
when_not_to_use: Direct agent_group tasks (use agent_group dispatch), admin tasks
keywords: [gateway, router, mentor, semantic-router, intent-detection]
long_tails:
  - how to create a single entry point for a multi-agent system
  - how to route user intents to automatic workflows
axioms:
  - Gateway NEVER executes tasks (mentor OR router, never builder)
  - Ambiguous intent = ask (do not guess routing)
density_score: 0.87
related:
  - p01_kc_input_intent_resolution
  - p01_kc_routing_resilience
  - p04_ct_cex_8f_motor
  - p02_agent_pesquisa
  - p02_agent_web_researcher
  - ex_dispatch_rule_research
  - p01_kc_router
  - router-builder
  - p03_pv_pesquisa_system_v2
  - p01_kc_dispatch_rule
---

# Gateway Agent - Entry Point for Users

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

| Scenario | Use? | Alternative |
|----------|------|-------------|
| Frontend chat (organizationapp.com) | YES | - |
| User intent routing | YES | - |
| Onboarding and questions | YES | - |
| Direct agent_group dispatch | NO | orchestrator |
| Admin/infra tasks | NO | operations_agent |

## Capabilities

| # | Capability | Description |
|---|-----------|-------------|
| 1 | Mentor mode | Interactive loop for questions and guidance |
| 2 | Intent detection | Keywords + direct commands (confidence 0.8+) |
| 3 | Semantic routing | Router 1-5 (research/listing/combo/photo/else) |
| 4 | Handoff | Context transfer to sub-workflows |
| 5 | Deploy-ready | System prompt + Knowledge Base + Workflow Config ready |

## Intent Routing

| Output | Intent | Trigger |
|--------|--------|---------|
| 1 | PESQUISA | `-pesquisa [produto]` ou "pesquisar, mercado, concorrentes" |
| 2 | ANUNCIO | `-anuncio [produto]` ou "anunciar, listing, copy" |
| 3 | COMBO | `-combo [produto]` ou "completo, tudo, full" |
| 4 | FOTO | `-photo [produto]` ou "foto, imagem, visual" |
| 5 | ELSE | Any other → returns to mentor loop |

## Deploy Artifacts

| Artifact | Tokens | Purpose |
|----------|--------|---------|
| GATEWAY_SYSTEM_PROMPT.txt | ~1500 | Agent system prompt |
| SEMANTIC_ROUTER.txt | ~500 | Classifier 1-5 (temp=0, max=1 token) |
| KNOWLEDGE_BASE.json | ~2500 | Code Interpreter knowledge |
| KNOWLEDGE_ECOMMERCE.md | ~3000 | Vector Store knowledge |
| WORKFLOW_CONFIG.json | ~200 | Config n8n/Make |

## Integration

```yaml
upstream:
  - USER: "User input via chat"
  - orchestrator: "Internal system routing"
downstream:
  - pesquisa-agent: "Intent 1 → automatic research"
  - anuncio-agent: "Intent 2 → listing creation"
  - photo-agent: "Intent 4 → photo generation"
pipeline:
  - combo: "Intent 3 → pesquisa > anuncio (sequential)"
```

## Anti-Patterns

- Gateway executing research/marketing: violates router role — delegate to specialists
- Intent detection without confidence threshold: wrong routing — require >= 0.8 or ask
- Semantic router with temperature > 0: non-deterministic output — use temperature=0
- No fallback (intent 5): user gets stuck — always have mentor loop as default

## Quality Gates

- System prompt < 2000 tokens (latency)
- Intent classification accuracy >= 90%
- Handoff includes full context (no information loss)
- Cost/conversation < $0.05 USD
- Latency < 3s/response

## References

- `records/agents/gateway/README.md` (original source)
- Deploy: OpenAI Agent Builder (gpt-4o + gpt-4o-mini router)
- Status: Production-Ready for organizationapp.com

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_input_intent_resolution]] | upstream | 0.30 |
| [[p01_kc_routing_resilience]] | upstream | 0.28 |
| [[p04_ct_cex_8f_motor]] | downstream | 0.28 |
| [[p02_agent_pesquisa]] | sibling | 0.26 |
| [[p02_agent_web_researcher]] | sibling | 0.24 |
| [[ex_dispatch_rule_research]] | downstream | 0.23 |
| [[p01_kc_router]] | related | 0.22 |
| [[router-builder]] | related | 0.21 |
| [[p03_pv_pesquisa_system_v2]] | downstream | 0.21 |
| [[p01_kc_dispatch_rule]] | downstream | 0.20 |
