---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of knowledge_card artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: knowledge-card-builder

## Golden Example

INPUT: "Destila conhecimento sobre prompt caching para otimizar custos LLM"

OUTPUT:
```yaml
---
id: p01_kc_prompt_caching
kind: knowledge_card
pillar: P01
title: "Prompt Caching Patterns for LLM Cost Optimization"
version: "1.0.0"
created: "2026-03-24"
updated: "2026-03-24"
author: "EDISON"
domain: llm_engineering
quality: null
tags: [prompt-caching, cost-optimization, latency, anthropic, openai, knowledge]
tldr: "Prompt caching reutiliza prefixos pre-processados entre chamadas LLM, reduzindo custo em ate 90% e latencia em 85%"
when_to_use: "Quando sistema LLM repete contexto longo entre chamadas"
keywords: [prompt-caching, cache-control, context-reuse]
long_tails:
  - Como configurar prompt caching na API da Anthropic
  - Tamanho minimo de prefixo para ativar cache em LLMs
axioms:
  - SEMPRE coloque conteudo estatico ANTES do dinamico
  - NUNCA cache contexto que muda a cada request
linked_artifacts:
  primary: null
  related: [p01_kc_rag_fundamentals]
density_score: 0.91
data_source: "https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching"
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
- **Cache-Control**: Anthropic `cache_control: {kind: "ephemeral"}`; TTL 5 min
- **Prefix Matching**: cache hit when prefix identical byte-a-byte
- **Minimum Tokens**: Anthropic >= 1024; OpenAI >= 1024 (auto)
- **Pricing Split**: write 1.25x base, read 0.1x (90% savings on hit)

## Strategy Phases
1. **Audit**: identify prompts with >50% static content
2. **Reorder**: static first (system > few-shot > RAG), dynamic last
3. **Annotate**: add cache breakpoints on last static block
4. **Monitor**: measure hit rate via response headers
5. **Tune**: target >= 80% hit rate, adjust granularity

## Golden Rules
- ORDENE: static first, dynamic last (always)
- AGRUPE: few large cacheable blocks > many small ones
- METRIZE: hit_rate = read / (read + creation + uncached)
- INVALIDE com cuidado: 1 byte diff = full cache miss

## Flow
```text
[Request] -> [Hash Prefix] -> [Cache Lookup]
                                   |
                         HIT: 0.1x cost, 85% faster
                         MISS: 1.25x cost, normal speed
                                   |
                             [Generate] -> [Response]
```

## Comparativo
| Provider | Min Tokens | Config | Write | Read | TTL |
|----------|-----------|--------|-------|------|-----|
| Anthropic | 1024 | Explicit | 1.25x | 0.1x | 5 min |
| OpenAI | 1024 | Automatic | 1.0x | 0.5x | 5-60 min |
| Google | 32768 | Explicit | 1.0x | 0.25x | config |

## References
- Source: https://docs.anthropic.com/en/docs/build-with-claude/prompt-caching
- Related: p01_kc_rag_fundamentals (context reuse patterns)
```

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p01_kc_ pattern (H03 pass)
- kind: knowledge_card (H04 pass)
- 13 required fields present (H06 pass)
- tags: list >= 3 (H07 pass)
- body 200-5120 bytes (H08 pass)
- No internal paths (H09 pass)
- author not STELLA (H10 pass)
- 7 sections >= 3 lines (S06, S08 pass)
- Bullets <= 80 chars (S10 pass)
- Tables + code blocks + external URL (S11-S13 pass)
- linked_artifacts with primary+related (S20 pass)

## Anti-Example

INPUT: "Documenta prompt caching"

BAD OUTPUT:
```yaml
---
id: prompt_caching_knowledge
kind: knowledge_card
title: Prompt Caching
author: STELLA
quality: 9.0
tags: "caching, llm"
---
This document describes how prompt caching works.
In summary, it saves money. As mentioned before, caching is good.
See records/core/docs/caching.md for details.
```

FAILURES:
1. id: no `p01_kc_` prefix -> H03 FAIL
2. lp: missing -> H06 FAIL
3. author: STELLA -> H10 FAIL
4. quality: self-assigned 9.0 -> H05 FAIL
5. tags: string not list -> H07 FAIL
6. body: <200 bytes -> H08 FAIL
7. internal path: records/ -> H09 FAIL
8. filler: "this document", "in summary", "as mentioned" -> S09 FAIL
9. no sections, no tables, no code -> S06, S11, S12 FAIL
10. no axioms, no keywords, no long_tails -> S16-S18 FAIL
