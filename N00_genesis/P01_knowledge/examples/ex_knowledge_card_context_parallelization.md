---
id: p01_kc_context_parallelization
kind: knowledge_card
pillar: P01
title: "Context Parallelization — 79% Token Reduction via Specialized Workers"
version: 2.0.0
created: 2026-02-06
updated: 2026-03-25
author: knowledge_agent
domain: architecture
quality: 9.1
tags: [parallelization, token-optimization, multi-agent, context-reduction, spawn]
tldr: "N workers com contexto narrow (2K tokens) substituem 1 agente com contexto full (50K). Reducao 79% tokens, velocidade 3-6x."
when_to_use: "Agente unico carrega >10K tokens de contexto para tarefas que precisam de <3K cada"
keywords: [context_parallelization, token_reduction, multi_agent, fat_adw, spawn]
long_tails:
  - "Como reduzir consumo de tokens em sistema multi-agente"
  - "Qual a diferenca entre contexto full e contexto especializado"
axioms:
  - "NUNCA carregar contexto full quando worker precisa de <20% dele"
  - "SEMPRE medir token savings real vs estimado"
linked_artifacts:
  primary: p01_kc_claude_agent_sdk_patterns
  related: []
density_score: null
data_source: "https://docs.anthropic.com/en/docs/agents-and-tools"
---

## Summary

Agente unico carrega 10K-100K tokens de contexto irrelevante por tarefa. Arquitetura paralela: orchestrator (500 tokens, so routing) + N workers (2K tokens, dominio narrow) + aggregator (merge + quality). Resultado: 79% reducao tokens, velocidade = tempo do worker mais lento (nao soma).

## Spec

| Approach | Tokens/task | Velocidade | Custo relativo |
|----------|-------------|------------|----------------|
| 1 agente x 50K contexto | 50,000 | 1x (serial) | 100% |
| Orch(500) + 5 workers(2K) | 10,500 | 3-6x (paralelo) | 21% |
| **Savings** | **79% reducao** | **3-6x speedup** | **79% economia** |

| Componente | Tokens | Funcao |
|------------|--------|--------|
| Orchestrator | ~500 | Routing logic, sem dominio |
| Worker | ~1K-2K | Contexto narrow, 1 dominio |
| Aggregator | ~500 | Merge results + quality check |

## Patterns

| Trigger | Action |
|---------|--------|
| Agente com >10K contexto | Decompor em workers especializados |
| Tarefas independentes entre si | Parallelizar workers (spawn N) |
| Tarefas dependentes | Pipeline sequencial (A->B->C) |
| Quality check necessario | Aggregator valida merge |

## Anti-Patterns

- Carregar contexto full em cada worker (anula o beneficio)
- Workers com escopo muito amplo (>3K tokens = nao eh narrow)
- Spawn >10 workers simultaneos (RAM/rate limit)
- Nao medir savings real (estimativa ≠ producao)

## Code

<!-- source: pattern generico | lang: python | purpose: worker com contexto narrow -->
```python
# Orchestrator: routing only (~500 tokens)
def orchestrate(task):
    workers = decompose(task)  # split em subtarefas
    results = parallel_run(workers)  # cada worker ~2K tokens
    return aggregate(results)  # merge + quality check

# Worker: contexto narrow, 1 dominio
def worker_marketing(product):
    context = load_domain_context("marketing", max_tokens=2000)
    return llm_call(context + product)  # 2K vs 50K
```

<!-- source: benchmark empirico | lang: yaml | purpose: metricas de referencia -->
```yaml
parallelization_benchmarks:
  max_parallel_workers: 10
  worker_context_size: 1000-2500 tokens
  measured_reduction: 40-80% vs agente unico
  speed_multiplier: 3-6x (tempo do mais lento, nao soma)
  sweet_spot: 3-5 workers (alem de 10 = overhead > ganho)
```

## References

- external: https://docs.anthropic.com/en/docs/agents-and-tools
- external: https://arxiv.org/abs/2304.03442 (CoALA framework)
- deepens: p01_kc_claude_agent_sdk_patterns (handoffs e orquestracao)
- deepens: /skill context_decomposition (como decompor tarefas — a ser criada)
