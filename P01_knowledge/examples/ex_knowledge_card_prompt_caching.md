---
id: p01_kc_prompt_caching
type: knowledge_card
lp: P01
title: Prompt Caching Patterns for LLM Cost Optimization
version: 1.0.0
created: 2026-03-24
updated: 2026-03-24
author: EDISON
domain: llm_engineering
quality: 9.5
tags: [prompt-caching, cost-optimization, latency, anthropic, openai, context-reuse]
tldr: Prompt caching reutiliza prefixos pre-processados entre chamadas LLM, reduzindo custo em ate 90% e latencia em 85% para contextos repetitivos acima de 1024 tokens
when_to_use: Quando sistema LLM repete contexto longo (system prompts, RAG chunks, few-shot) entre chamadas
keywords: [prompt-caching, cache-control, context-reuse, token-cost, prefill-optimization]
long_tails:
  - Como configurar prompt caching na API da Anthropic para reduzir custos
  - Qual o tamanho minimo de prefixo para ativar cache em APIs LLM
axioms:
  - SEMPRE coloque conteudo estatico (system prompt, few-shot) ANTES do conteudo dinamico (user query)
  - NUNCA cache contexto que muda a cada request — invalida o cache e AUMENTA custo
linked_artifacts:
  adw: null
  agent: p02_agent_llm_application_specialist
  hop: null
density_score: 0.91
---

# Prompt Caching Patterns for LLM Cost Optimization

## Quick Reference
```yaml
topic: prompt_caching
scope: LLM API optimization (Anthropic, OpenAI, Google)
owner: EDISON
criticality: high
```

## Key Concepts
- **Cache-Control Header**: Anthropic usa `cache_control: {type: "ephemeral"}` no ultimo bloco cacheavel; TTL = 5 min
- **Prefix Matching**: Cache ativa quando prefixo do prompt e identico byte-a-byte ao request anterior
- **Minimum Tokens**: Anthropic exige >= 1024 tokens no prefixo; OpenAI >= 1024 tokens (auto, sem config)
- **Pricing Split**: Anthropic — cache write 1.25x base, cache read 0.1x base (90% economia no hit)
- **OpenAI Auto-Cache**: Ativado automaticamente para prefixos >= 1024 tokens, 50% desconto no hit, sem config

## Strategy Phases
1. **Audit**: Identificar prompts com >50% conteudo estatico (system + few-shot + RAG fixo)
2. **Reorder**: Mover conteudo estatico para inicio do prompt, dinamico para final
3. **Annotate**: Adicionar cache breakpoints (Anthropic: `cache_control`) no ultimo bloco estatico
4. **Monitor**: Medir cache hit rate via headers (`x-cache-creation-input-tokens` vs `x-cache-read-input-tokens`)
5. **Tune**: Ajustar TTL e granularidade — prompts com >80% hit rate sao candidatos a cache permanente

## Golden Rules
- ORDENE: estatico primeiro (system > few-shot > RAG > tools) e dinamico por ultimo (user query)
- AGRUPE: poucos blocos grandes cacheaveis > muitos blocos pequenos (overhead de cache por bloco)
- METRIZE: cache_hit_rate = cache_read_tokens / (cache_read + cache_creation + uncached) — target >= 80%
- INVALIDE com cuidado: qualquer byte diferente no prefixo = cache miss = custo de write

## Flow
```text
[Request N] -> [Hash Prefix] -> [Cache Lookup]
                                    |
                          HIT: read cached KV  (0.1x cost, ~85% faster)
                          MISS: compute + store (1.25x cost, normal speed)
                                    |
                              [Append Dynamic] -> [Generate] -> [Response]
```

## Comparativo
| Provider | Min Tokens | Config | Write Cost | Read Cost | TTL |
|----------|-----------|--------|------------|-----------|-----|
| Anthropic | 1024 | Explicit (cache_control) | 1.25x | 0.1x | 5 min |
| OpenAI | 1024 | Automatic (zero config) | 1.0x | 0.5x | 5-60 min |
| Google | 32768 | Explicit (cached_content) | 1.0x | 0.25x | configurable |

## References
- Related artifact: p02_agent_llm_application_specialist (production LLM patterns)
- Related artifact: p01_kc_rag_fundamentals (RAG context reuse patterns)
