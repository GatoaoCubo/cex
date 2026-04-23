---
id: p01_kc_evolutionary_prompt_optimization
kind: knowledge_card
pillar: P01
title: "Evolutionary Prompt Optimization — 5 Techniques with Empirical Benchmarks"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: llm_engineering
quality: 9.1
tags: [prompt-optimization, evolutionary, promptbreeder, elo-rating, llm]
tldr: "5 tecnicas evolucionarias (PromptBreeder, C-Evolve, APE, Tournament, Vision-Language) elevam fitness de 0.65 para 0.85+ com meta-mutacao e consenso."
when_to_use: "Otimizar prompts sistematicamente em vez de iteracao manual — especialmente com populacoes de candidatos"
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
related:
  - bld_knowledge_card_prompt_technique
---

## Summary

Prompt optimization evolucionaria aplica algoritmos geneticos a populacoes de prompts. 5 tecnicas validadas empiricamente elevam fitness baseline de ~0.65 para 0.85+. PromptBreeder (MATH 46.3%) evolui as proprias estrategias de mutacao. APE reduz tempo de dev 60-80%.

## Spec

| Tecnica | Mecanismo | Benchmark | Custo | Self-Referential |
|---------|-----------|-----------|-------|------------------|
| PromptBreeder | Meta-mutacao de estrategias | MATH 46.3%, GSM8K 83.5% | Alto | Sim |
| C-Evolve | Ilhas + consenso por votacao | +13.85% Qwen3-8B, +16.09% GPT-4-mini | Alto | Nao |
| APE | LLM gera + avalia candidatos | +35% accuracy, -60-80% dev time | Alto | Nao |
| Tournament | Elo rating via debate multi-agent | 97% F1 (BBH-Navigate) | Muito alto | Nao |
| Vision-Language | Dual fitness (task + critique) | Previne overfitting, emergent tool use | Muito alto | Sim |

| Fase | Fitness Target | Success Rate |
|------|---------------|--------------|
| Baseline | ~0.65 | ~75% |
| Tier 1 (dual fitness + tournament + LLM mutations) | 0.75+ | 85%+ |
| Full (islands + consensus + meta-mutation) | 0.85+ | 90%+ |

## Patterns

| Trigger | Action |
|---------|--------|
| Fitness estagnada apos 5 geracoes | Ativar meta-mutacao (PromptBreeder) |
| Prompts convergindo prematuramente | Usar island populations (C-Evolve) |
| Sem tempo para tuning manual | APE: LLM gera 5 variacoes dos top performers |
| Multiplos candidatos empatados | Tournament com Elo rating (K=32) |
| Overfitting em task metric | Dual fitness: 0.75*task + 0.25*quality_critique |

## Anti-Patterns

- Evoluir sem fitness quantitativa (viés de confirmacao)
- Populacao < 5 candidatos (diversidade insuficiente)
- Ignorar mutation strategy tracking (nao sabe o que funciona)
- >10 ilhas simultaneas (overhead > ganho evolutivo)
- Single fitness function sem quality critique (overfitting)

## Code

<!-- lang: python | purpose: dual fitness function -->
```python
def fitness_dual(pattern, lambda_q=0.25):
    task_perf = pattern.success_rate * 0.4 + pattern.efficiency * 0.2
    quality = llm_critique(f"Rate 0-10: {pattern.value}") / 10
    return (1 - lambda_q) * task_perf + lambda_q * quality
```

<!-- lang: python | purpose: elo tournament -->
```python
def tournament(p1, p2, k=32):
    winner = multi_agent_debate(p1.result, p2.result)
    expected = 1 / (1 + 10 ** ((p2.elo - p1.elo) / 400))
    p1.elo += k * (1 - expected) if winner == p1 else k * (0 - expected)
```

## References

- external: https://arxiv.org/abs/2309.16797 (PromptBreeder)
- external: https://arxiv.org/abs/2509.23331 (C-Evolve)
- external: https://arxiv.org/abs/2211.01910 (APE)
- deepens: p01_kc_claude_agent_sdk_patterns (multi-agent orchestration)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_prompt_technique]] | sibling | 0.16 |
