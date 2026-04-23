---
id: p01_kc_claude_model_capabilities_2026
kind: knowledge_card
pillar: P01
title: "Claude Model Capabilities 2026 — Opus 4.6, Sonnet 4.6, Haiku 4.5 Specs"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: llm_engineering
quality: 9.1
tags: [claude, models, pricing, context-window, model-selection, api]
tldr: "3 tiers: Opus 4.6 ($5/$25 MTok, 200K/1M ctx), Sonnet 4.6 ($3/$15, balanced), Haiku 4.5 ($1/$5, fastest). Routing correto economiza 50-80%."
when_to_use: "Selecionar modelo Claude para API calls ou configurar model router com custo otimo"
keywords: [model_selection, opus, sonnet, haiku, pricing, context_window]
long_tails:
  - "Qual modelo Claude usar para cada tipo de tarefa"
  - "Quanto custa cada modelo Claude por milhao de tokens"
axioms:
  - "NUNCA usar Opus 4.1 ($15/$75) quando Opus 4.6 ($5/$25) eh melhor e mais barato"
  - "SEMPRE rotear tarefas simples para Haiku (economia 80% vs Opus)"
linked_artifacts:
  primary: null
  related: [p01_kc_claude_agent_sdk_patterns, p01_kc_claude_server_tools]
density_score: null
data_source: "https://docs.anthropic.com/en/docs/about-claude/models"
related:
  - p02_mc_claude_opus_4
  - spec_infinite_bootstrap_loop
  - self_audit_n03_builder_20260408
  - bld_examples_model_card
  - p02_mp_anthropic
  - p02_fb_model_cascade
  - p12_dr_keyword_agent_group
  - output_sdk_validation_audit
  - bld_examples_model_provider
  - bld_knowledge_card_effort_profile
---

## Summary

Familia Claude 2026: Opus 4.6 (mais inteligente, 128K output), Sonnet 4.6 (equilibrio custo/inteligencia), Haiku 4.5 (mais rapido, $1/$5 MTok). Todos suportam 200K context com 1M beta para Opus/Sonnet. Extended thinking disponivel nos 3 tiers. Model routing correto economiza 50-80%.

## Spec

| Spec | Opus 4.6 | Sonnet 4.6 | Haiku 4.5 |
|------|----------|------------|-----------|
| API ID | claude-opus-4-6 | claude-sonnet-4-6 | claude-haiku-4-5-20251001 |
| Context | 200K (1M beta) | 200K (1M beta) | 200K |
| Max Output | 128K tokens | 64K tokens | 64K tokens |
| Input $/MTok | $5 | $3 | $1 |
| Output $/MTok | $25 | $15 | $5 |
| Extended Thinking | Sim (adaptive) | Sim (manual+adaptive) | Sim |
| Knowledge Cutoff | May 2025 | Aug 2025 | Feb 2025 |

| 1M Context Beta | Detalhe |
|----------------|---------|
| Header | `context-1m-2025-08-07` |
| Modelos | Opus 4.6, Sonnet 4.6, Sonnet 4.5, Sonnet 4 |
| Pricing >200K | Input 2x, Output 1.5x |
| Requisito | Usage tier 4 |

| Legacy (evitar) | Preco Input/Output | Status |
|-----------------|-------------------|--------|
| Opus 4.1 | $15/$75 MTok | Ativo mas 3x mais caro que 4.6 |
| Haiku 3 | Deprecado | Retirement: 2026-04-19 |

## Patterns

| Trigger | Action |
|---------|--------|
| Orquestracao complexa, agent coding | Opus 4.6 |
| Tarefas padrao, workhorse | Sonnet 4.6 (melhor custo/inteligencia) |
| Classificacao, tagging, bulk ops | Haiku 4.5 ($1 MTok input) |
| Contexto >200K tokens | Ativar 1M beta header + tier 4 |
| Custo alto com Opus em tudo | Router: simples->Haiku, padrao->Sonnet, complexo->Opus |

## Anti-Patterns

- Usar Opus 4.1 ($15/$75) quando 4.6 ($5/$25) existe e supera
- Enviar >200K tokens sem 1M beta header (erro de validacao)
- Haiku 3 para novos projetos (retirement abril 2026)
- Opus para tarefas de classificacao simples (5x custo sem ganho)
- Assumir truncamento silencioso (Claude 4+ retorna erro)

## Code

<!-- lang: python | purpose: model router por complexidade -->
```python
ROUTER = {
    "classify": "claude-haiku-4-5-20251001",     # $1/$5
    "standard": "claude-sonnet-4-6-20250514",    # $3/$15
    "complex":  "claude-opus-4-6-20250514",      # $5/$25
}

def select_model(task_complexity: str) -> str:
    return ROUTER.get(task_complexity, ROUTER["standard"])
```

<!-- lang: python | purpose: 1M context beta -->
```python
response = client.messages.create(
    model="claude-sonnet-4-6-20250514",
    max_tokens=8192,
    betas=["context-1m-2025-08-07"],
    messages=[{"role": "user", "content": long_context}]  # >200K tokens
)
```

## References

- external: https://docs.anthropic.com/en/docs/about-claude/models
- deepens: p01_kc_claude_agent_sdk_patterns (model per agent config)
- deepens: p01_kc_claude_server_tools (server-side tool specs)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_mc_claude_opus_4]] | downstream | 0.52 |
| [[spec_infinite_bootstrap_loop]] | related | 0.39 |
| [[self_audit_n03_builder_20260408]] | sibling | 0.35 |
| [[bld_examples_model_card]] | downstream | 0.34 |
| [[p02_mp_anthropic]] | downstream | 0.33 |
| [[p02_fb_model_cascade]] | downstream | 0.31 |
| [[p12_dr_keyword_agent_group]] | downstream | 0.31 |
| [[output_sdk_validation_audit]] | related | 0.29 |
| [[bld_examples_model_provider]] | downstream | 0.28 |
| [[bld_knowledge_card_effort_profile]] | sibling | 0.27 |
