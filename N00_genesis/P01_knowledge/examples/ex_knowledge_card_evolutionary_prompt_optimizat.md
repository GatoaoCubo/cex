---
id: p01_kc_evolutionary_prompt_optimization
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Evolutionary Prompt Optimization — 5 Techniques with Empirical Benchmarks"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: llm_engineering
quality: 9.1
tags: [prompt-optimization, evolutionary, promptbreeder, elo-rating, llm]
tldr: "5 evolutionary techniques (PromptBreeder, C-Evolve, APE, Tournament, Vision-Language) raise fitness from 0.65 to 0.85+ with meta-mutation and consensus."
when_to_use: "Systematically optimize prompts instead of manual iteration — especially with candidate populations"
keywords: [prompt_evolution, genetic_algorithm, meta_mutation, elo_rating]
long_tails:
  - "How to use genetic algorithms to optimize LLM prompts"
  - "Which prompt evolution technique has the best cost-benefit ratio"
axioms:
  - "ALWAYS use dual fitness (task + quality) to avoid overfitting"
  - "NEVER evolve prompts without quantitative fitness metrics"
linked_artifacts:
  primary: null
  related: [p01_kc_claude_agent_sdk_patterns]
density_score: null
data_source: "Papers: PromptBreeder 2309.16797, C-Evolve 2509.23331, APE 2211.01910"
related:
  - bld_knowledge_card_prompt_technique
---

## Summary

Evolutionary prompt optimization applies genetic algorithms to prompt populations. 5 empirically validated techniques raise baseline fitness from ~0.65 to 0.85+. PromptBreeder (MATH 46.3%) evolves its own mutation strategies. APE reduces dev time 60-80%.

## Spec

| Technique | Mechanism | Benchmark | Cost | Self-Referential |
|-----------|-----------|-----------|------|------------------|
| PromptBreeder | Strategy meta-mutation | MATH 46.3%, GSM8K 83.5% | High | Yes |
| C-Evolve | Islands + consensus by voting | +13.85% Qwen3-8B, +16.09% GPT-4-mini | High | No |
| APE | LLM generates + evaluates candidates | +35% accuracy, -60-80% dev time | High | No |
| Tournament | Elo rating via multi-agent debate | 97% F1 (BBH-Navigate) | Very high | No |
| Vision-Language | Dual fitness (task + critique) | Prevents overfitting, emergent tool use | Very high | Yes |

| Fase | Fitness Target | Success Rate |
|------|---------------|--------------|
| Baseline | ~0.65 | ~75% |
| Tier 1 (dual fitness + tournament + LLM mutations) | 0.75+ | 85%+ |
| Full (islands + consensus + meta-mutation) | 0.85+ | 90%+ |

## Patterns

| Trigger | Action |
|---------|--------|
| Fitness stagnated after 5 generations | Activate meta-mutation (PromptBreeder) |
| Prompts converging prematurely | Use island populations (C-Evolve) |
| No time for manual tuning | APE: LLM generates 5 variations of top performers |
| Multiple tied candidates | Tournament with Elo rating (K=32) |
| Overfitting on task metric | Dual fitness: 0.75*task + 0.25*quality_critique |

## Anti-Patterns

- Evolving without quantitative fitness (confirmation bias)
- Population < 5 candidates (insufficient diversity)
- Ignoring mutation strategy tracking (cannot tell what works)
- >10 simultaneous islands (overhead > evolutionary gain)
- Single fitness function without quality critique (overfitting)

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
