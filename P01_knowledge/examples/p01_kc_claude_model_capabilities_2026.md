---
id: p01_kc_claude_model_capabilities_2026
type: knowledge_card
lp: P01
title: "Claude Model Capabilities 2026 — Opus 4.6, Sonnet 4.6, Haiku 4.5 Specs"
version: 2.0.0
created: 2026-02-23
updated: 2026-03-25
author: PYTHA
domain: llm_engineering
quality: null
tags: [claude, models, pricing, context-window, model-selection, api]
tldr: "3 tiers: Opus 4.6 ($5/$25 MTok, 128K out), Sonnet 4.6 ($3/$15, balanced), Haiku 4.5 ($1/$5, fastest). Routing correto economiza 50-80%."
when_to_use: "Selecionar modelo Claude para API calls ou configurar model router com custo otimo"
keywords: [model_selection, opus, sonnet, haiku, pricing, context_window]
long_tails:
  - "Qual modelo Claude usar para cada tipo de tarefa em 2026"
  - "Quanto custa cada modelo Claude por milhao de tokens"
axioms:
  - "NUNCA usar Opus 4.1 ($15/$75) quando Opus 4.6 ($5/$25) eh superior"
  - "SEMPRE rotear tarefas simples para Haiku (economia 80% vs Opus)"
linked_artifacts:
  primary: null
  related: [p01_kc_claude_agent_sdk_patterns, p01_kc_claude_server_tools]
density_score: null
data_source: "https://docs.anthropic.com/en/docs/about-claude/models"
---

## Summary

Familia Claude 2026: Opus 4.6 (mais inteligente, 128K output max), Sonnet 4.6 (melhor custo/inteligencia), Haiku 4.5 (mais rapido, $1/$5 MTok). Todos suportam 200K context e extended thinking. 1M beta para Opus/Sonnet com pricing 2x/1.5x. Opus 4.6 custa 66% menos que Opus 4.1 com performance superior. Routing correto economiza 50-80%.

## Spec

| Spec | Opus 4.6 | Sonnet 4.6 | Haiku 4.5 |
|------|----------|------------|-----------|
| API ID | claude-opus-4-6 | claude-sonnet-4-6 | claude-haiku-4-5-20251001 |
| Context | 200K (1M beta) | 200K (1M beta) | 200K |
| Max Output | 128K tokens | 64K tokens | 64K tokens |
| Input $/MTok | $5 | $3 | $1 |
| Output $/MTok | $25 | $15 | $5 |
| Extended Thinking | Adaptive only | Manual + Adaptive | Yes |
| Knowledge Cutoff | May 2025 | Aug 2025 | Feb 2025 |
| Training Cutoff | Aug 2025 | Jan 2026 | Jul 2025 |

| 1M Context Beta | Detalhe |
|----------------|---------|
| Header | `context-1m-2025-08-07` |
| Modelos | Opus 4.6, Sonnet 4.6, Sonnet 4.5, Sonnet 4 |
| Pricing >200K | Input 2x, Output 1.5x |
| Requisito | Usage tier 4 organization |

| Legacy (evitar) | Preco In/Out | Status |
|-----------------|-------------|--------|
| Opus 4.5 (20251101) | $5/$25 | Disponivel |
| Opus 4.1 (20250805) | $15/$75 | 3x mais caro que 4.6, inferior |
| Sonnet 4.5 (20250929) | $3/$15 | Disponivel |
| Haiku 3 | Deprecado | Retirement: 2026-04-19 |

## Patterns

| Trigger | Action |
|---------|--------|
| Orquestracao complexa, agent coding | Opus 4.6 (mais inteligente) |
| Tarefas padrao, workhorse diario | Sonnet 4.6 (melhor custo/inteligencia) |
| Classificacao, tagging, bulk ops | Haiku 4.5 ($1/$5, mais rapido) |
| Contexto >200K tokens | Ativar 1M beta header + tier 4 |
| Fleet cost alto com Opus em tudo | Router: simples->Haiku, padrao->Sonnet, complexo->Opus |
| Output estruturado com raciocinio | Sonnet 4.6 (manual + adaptive thinking) |

## Anti-Patterns

- Opus 4.1 a $15/$75 quando 4.6 a $5/$25 existe e supera
- Enviar >200K tokens sem 1M beta header (erro de validacao)
- Haiku 3 em novos projetos (retirement 2026-04-19)
- Todo trafego para Opus (50-80% desperdicio em tasks simples)
- Assumir truncamento silencioso (Claude 4+ retorna erro)
- Budget_tokens manual em Opus 4.6 (so aceita adaptive thinking)

## Code

<!-- lang: python | purpose: model router por complexidade -->
```python
ROUTER = {
    "classify": "claude-haiku-4-5-20251001",     # $1/$5
    "standard": "claude-sonnet-4-6-20250514",    # $3/$15
    "complex":  "claude-opus-4-6-20250514",      # $5/$25
}

def select_model(complexity: str) -> str:
    return ROUTER.get(complexity, ROUTER["standard"])
```

<!-- lang: python | purpose: 1M context beta activation -->
```python
response = client.messages.create(
    model="claude-sonnet-4-6-20250514",
    max_tokens=8192,
    betas=["context-1m-2025-08-07"],
    messages=[{"role": "user", "content": long_context}]
)
```

## References

- external: https://docs.anthropic.com/en/docs/about-claude/models
- deepens: p01_kc_claude_server_tools (server-side tool per model)
- deepens: p01_kc_claude_agent_sdk_patterns (agent model config)
