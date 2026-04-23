---
id: p01_kc_optimizer
kind: knowledge_card
type: kind
pillar: P11
title: "Optimizer — Deep Knowledge for optimizer"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: research_agent
domain: optimizer
quality: 9.1
tags: [optimizer, P11, GOVERN, kind-kc]
tldr: "Metric-driven continuous improvement loop that adjusts prompts, parameters, or agent behavior based on measured outcomes"
when_to_use: "Building, reviewing, or reasoning about optimizer artifacts"
keywords: [optimization, metrics, continuous-improvement]
feeds_kinds: [optimizer]
density_score: null
related:
  - p03_ins_optimizer
  - p03_sp_optimizer_builder
  - optimizer-builder
  - bld_collaboration_optimizer
  - bld_architecture_optimizer
  - p11_qg_optimizer
  - bld_memory_optimizer
  - p01_kc_reward_signal
  - bld_knowledge_card_optimizer
  - action-prompt-builder
---

# Optimizer

## Spec
```yaml
kind: optimizer
pillar: P11
llm_function: GOVERN
max_bytes: 4096
naming: p11_opt_{{target}}.md + .yaml
core: false
```

## What It Is
An optimizer is a metric→action specification that continuously monitors a target metric and applies tuning actions when the metric drifts from target. It defines the metric source, evaluation frequency, action strategy, and convergence criteria. It is NOT bugloop (P11 — corrects discrete failures; optimizer improves continuous metrics) nor benchmark (P07 — passive measurement without action).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | LangSmith feedback loop + LCEL composition | Traces → human/automated feedback → prompt revision |
| LlamaIndex | `RetrieverEvaluator` + re-indexing pipeline | Eval retrieval quality → adjust chunk_size, top_k |
| CrewAI | `AgentPlanner` + task parameter tuning | Pre-task planner adjusts task descriptions based on past outcomes |
| DSPy | `MIPROv2`, `BootstrapFewShot`, `SIMBA` | Native optimizer suite; Bayesian instruction + demo optimization |
| Haystack | Custom pipeline evolution component | No native; build eval → tune → redeploy pipeline |
| OpenAI | Fine-tuning API + evals API | Systematic fine-tune cycles guided by evals scores |
| Anthropic | Prompt engineering + evals pipeline | Constitutional AI feedback; custom eval → prompt iteration |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| target_metric | string | required | Must be measurable and actionable; vague metrics produce no improvement |
| target_value | float | required | Optimization ceiling; prevents over-tuning |
| action_strategy | enum | prompt_revision | prompt_revision/param_tuning/example_addition/model_swap |
| eval_frequency | string | on_batch | on_batch/daily/on_commit — frequent eval = faster convergence but higher cost |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Prompt revision loop | Quality score drifts below target | metric: quality_score < 7.5 → action: revise system_prompt with failure examples |
| Few-shot bootstrapping | Low example count limiting accuracy | metric: accuracy < 0.80 → action: add_bootstrapped_examples via DSPy |
| Param sweep | Retrieval precision low | metric: precision@5 < 0.70 → action: sweep chunk_size [256,512,1024] |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Optimizing without baseline | No way to measure improvement | Establish baseline score before first optimization run |
| Continuous optimization on production traffic | A/B test interference; live degradation risk | Optimize on eval set; promote to prod only after convergence |
| Optimizing multiple metrics simultaneously | Metric conflict causes oscillation | Prioritize one primary metric; others as constraints |

## Integration Graph
```
[benchmark] --> [optimizer] --> [action_prompt]
[reward_signal] --^       |
                     [learning_record]
```

## Decision Tree
- IF target_metric below target_value THEN trigger action_strategy
- IF action produces score improvement >= 0.5 THEN commit change + record in learning_record
- IF 3 consecutive actions show no improvement THEN escalate to human review
- DEFAULT: Optimize prompt first (cheapest); only swap model if prompt revision fails

## Quality Criteria
- GOOD: Has target_metric, target_value, action_strategy, eval_frequency, convergence_criteria
- GREAT: Baseline documented; action history tracked; convergence detection prevents over-tuning
- FAIL: No baseline; optimizes vague metric; no convergence criteria; runs on live production traffic

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_optimizer]] | upstream | 0.36 |
| [[p03_sp_optimizer_builder]] | upstream | 0.35 |
| [[optimizer-builder]] | related | 0.34 |
| [[bld_collaboration_optimizer]] | related | 0.34 |
| [[bld_architecture_optimizer]] | upstream | 0.33 |
| [[p11_qg_optimizer]] | related | 0.32 |
| [[bld_memory_optimizer]] | upstream | 0.28 |
| [[p01_kc_reward_signal]] | sibling | 0.28 |
| [[bld_knowledge_card_optimizer]] | sibling | 0.27 |
| [[action-prompt-builder]] | upstream | 0.27 |
