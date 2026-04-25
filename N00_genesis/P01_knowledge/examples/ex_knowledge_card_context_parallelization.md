---
id: p01_kc_context_parallelization
kind: knowledge_card
8f: F3_inject
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
when_to_use: "Single agent loads >10K tokens of context for tasks that need <3K each"
keywords: [context_parallelization, token_reduction, multi_agent, fat_adw, spawn]
long_tails:
  - "How to reduce token consumption in multi-agent system"
  - "What is the difference between full context and specialized context"
axioms:
  - "NEVER load full context when worker needs <20% of it"
  - "ALWAYS measure real token savings vs estimated"
linked_artifacts:
  primary: p01_kc_claude_agent_sdk_patterns
  related: []
density_score: null
data_source: "https://docs.anthropic.com/en/docs/agents-and-tools"
related:
  - KC_N05_UVICORN_PRODUCTION
  - p01_kc_token_budgeting
  - p01_kc_claude_agent_sdk_patterns
  - p02_memory_scope
  - p01_kc_plan_driven_dev
  - SPEC_01_coordinator_protocol
  - p12_wf_brand_propagation
  - p01_kc_brand_tokens_pipeline
---

## Summary

Single agent loads 10K-100K tokens of irrelevant context per task. Parallel architecture: orchestrator (500 tokens, routing only) + N workers (2K tokens, narrow domain) + aggregator (merge + quality). Result: 79% token reduction, speed = time of the slowest worker (not sum).

## Spec

| Approach | Tokens/task | Speed | Relative cost |
|----------|-------------|-------|---------------|
| 1 agent x 50K context | 50,000 | 1x (serial) | 100% |
| Orch(500) + 5 workers(2K) | 10,500 | 3-6x (parallel) | 21% |
| **Savings** | **79% reducao** | **3-6x speedup** | **79% economia** |

| Component | Tokens | Function |
|-----------|--------|----------|
| Orchestrator | ~500 | Routing logic, no domain |
| Worker | ~1K-2K | Narrow context, 1 domain |
| Aggregator | ~500 | Merge results + quality check |

## Patterns

| Trigger | Action |
|---------|--------|
| Agent with >10K context | Decompose into specialized workers |
| Mutually independent tasks | Parallelize workers (spawn N) |
| Dependent tasks | Sequential pipeline (A->B->C) |
| Quality check needed | Aggregator validates merge |

## Anti-Patterns

- Loading full context in each worker (negates the benefit)
- Workers with overly broad scope (>3K tokens = not narrow)
- Spawn >10 simultaneous workers (RAM/rate limit)
- Not measuring real savings (estimate != production)

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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[KC_N05_UVICORN_PRODUCTION]] | sibling | 0.23 |
| [[p01_kc_token_budgeting]] | sibling | 0.20 |
| [[p01_kc_claude_agent_sdk_patterns]] | sibling | 0.20 |
| [[p02_memory_scope]] | downstream | 0.17 |
| [[p01_kc_plan_driven_dev]] | sibling | 0.17 |
| [[SPEC_01_coordinator_protocol]] | related | 0.16 |
| [[p12_wf_brand_propagation]] | downstream | 0.15 |
| [[p01_kc_brand_tokens_pipeline]] | sibling | 0.15 |
