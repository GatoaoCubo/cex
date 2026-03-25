---
id: p01_kc_evolutionary_prompt_optimization
type: knowledge_card
lp: P01
title: "Evolutionary Prompt Optimization — 5 Techniques with Empirical Benchmarks"
version: 2.0.0
created: 2026-02-07
updated: 2026-03-25
author: SHAKA
domain: llm_engineering
quality: null
tags: [prompt-optimization, evolutionary, promptbreeder, elo-rating, llm]
tldr: "5 tecnicas evolucionarias (PromptBreeder, C-Evolve, APE, Tournament, Dual Fitness) elevam fitness de 0.65 para 0.85+ com meta-mutacao e consenso."
when_to_use: "Otimizar prompts sistematicamente com populacoes de candidatos em vez de iteracao manual"
keywords: [prompt_evolution, genetic_algorithm, meta_mutation, elo_rating]
long_tails:
  - "Como usar algoritmos geneticos para otimizar prompts de LLM"
  - "Qual tecnica de prompt evolution tem melhor custo-beneficio"
axioms:
  - "SEMPRE usar dual fitness (task + quality) para evitar overfitting"
  - "NUNCA evoluir prompts sem metricas de fitness quantitativas"
linked_artifacts:
  primary: null
  related: [p01_kc_claude_agent_sdk_patterns]
density_score: null
data_source: "Papers: PromptBreeder 2309.16797, C-Evolve 2509.23331, APE 2211.01910"
---

## Summary

Prompt optimization evolucionaria aplica selecao natural a populacoes de prompts LLM. 5 tecnicas validadas empiricamente elevam fitness baseline de ~0.65 para 0.85+. PromptBreeder (MATH 46.3%, GSM8K 83.5%) supera GPT-4 zero-shot via meta-mutacao self-referential. APE reduz tempo de desenvolvimento 60-80% com +35% accuracy.

## Spec

| Tecnica | Mecanismo | Benchmark | Custo | Self-Ref |
|---------|-----------|-----------|-------|----------|
| PromptBreeder | Meta-mutacao de estrategias | MATH 46.3%, GSM8K 83.5% | Alto | Sim |
| C-Evolve | Ilhas + consenso por votacao | +13.85% Qwen3-8B, +16.09% GPT-4-mini | Alto | Nao |
| APE | LLM gera + avalia candidatos | +35% accuracy, -60-80% dev time | Alto | Nao |
| Tournament | Elo rating via debate multi-agent | 97% F1 (BBH-Navigate), 71-85% win | V.Alto | Nao |
| Dual Fitness | lambda-balance task + critique | Previne overfitting, emergent tools | V.Alto | Sim |

| Fase | Fitness Target | Success Rate |
|------|---------------|--------------|
| Baseline | ~0.65 | ~75% |
| Tier 1 (dual fitness + tournament + LLM mutations) | 0.75+ | 85%+ |
| Full (islands + consensus + meta-mutation) | 0.85+ | 90%+ |

## Patterns

| Trigger | Action |
|---------|--------|
| Fitness estagnada apos 5+ geracoes | Ativar meta-mutacao (PromptBreeder) |
| Convergencia prematura | Usar island populations (C-Evolve, max 5) |
| Cold start sem prompt existente | APE: LLM gera + avalia 5 candidatos |
| Multiplos candidatos empatados | Tournament com Elo (K=32, min 30 matches) |
| Overfitting em task-only metric | Dual fitness: `0.75*task + 0.25*critique` |
| Mutation strategy desconhecida | Track success_rate por estrategia, evolve top-K |

## Anti-Patterns

- Evoluir sem fitness quantitativa de baseline (sem referencia)
- Populacao < 5 candidatos (diversidade insuficiente para selecao)
- Ignorar mutation strategy tracking (nao sabe qual funciona)
- >5 ilhas simultaneas (overhead supera ganho evolutivo)
- Single fitness sem quality critique (overfitting garantido)
- Elo com < 30 comparisons (ratings instaveis, nao convergem)

## Code

<!-- lang: python | purpose: dual fitness function -->
```python
def fitness_dual(pattern, lambda_q=0.25):
    task_perf = pattern.success_rate * 0.4 + pattern.efficiency * 0.2
    quality = llm_critique(f"Rate 0-10: {pattern.value}") / 10
    return (1 - lambda_q) * task_perf + lambda_q * quality
```

<!-- lang: python | purpose: elo tournament selection -->
```python
def tournament(p1, p2, k=32):
    winner = multi_agent_debate(p1.result, p2.result)
    expected = 1 / (1 + 10 ** ((p2.elo - p1.elo) / 400))
    p1.elo += k * ((1 if winner == p1 else 0) - expected)
```

## References

- external: https://arxiv.org/abs/2309.16797 (PromptBreeder)
- external: https://arxiv.org/abs/2509.23331 (C-Evolve)
- external: https://arxiv.org/abs/2211.01910 (APE)
- deepens: p01_kc_claude_agent_sdk_patterns (multi-agent eval orchestration)
