---
id: reward_signal_n01
kind: reward_signal
pillar: P11
nucleus: n01
title: "N01 Research Quality Reward Signal"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [reward_signal, quality_feedback, n01, rl_feedback, analytical_envy, quality_optimization]
tldr: "Reward signal definition for N01 research quality optimization: composite signal from eval_framework (D1-D5) + bias audit + stakeholder satisfaction. Used by self_improvement_loop to guide artifact evolution direction."
density_score: 0.88
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P11/reward_signal F2 become=reward-signal-builder F3 inject=eval_framework_n01+bias_audit_n01+self_improvement_loop_n01+learning_record_n01 F4 reason=the self-improvement loop needs a clear optimization target -- reward signal defines what "better" means for N01 research F5 call=cex_compile F6 produce=reward_signal_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P11_feedback/ -->

## Purpose

The self_improvement_loop_n01 must optimize in a DIRECTION.
Without a defined reward signal, "better" is undefined.

This artifact defines the composite reward signal that N01 maximizes:
- What dimensions matter (eval_framework D1-D5)
- How they combine (weighted sum)
- What additional signals add context (bias, freshness, utility)
- What the reward floor and ceiling look like

## Reward Signal Components

| Component | Source | Weight | Scale |
|-----------|--------|--------|-------|
| D1 Source Quality | eval_framework_n01 | 25% | 0-10 |
| D2 Analytical Depth | eval_framework_n01 | 25% | 0-10 |
| D3 Comparative Coverage | eval_framework_n01 | 25% | 0-10 |
| D4 Claim Confidence | eval_framework_n01 | 15% | 0-10 |
| D5 Actionability | eval_framework_n01 | 10% | 0-10 |
| Bias penalty | bias_audit_n01 | modifier | -2 to 0 |
| Freshness bonus | source date check | modifier | -1 to +1 |
| Hallucination penalty | llm_judge_n01 | modifier | -3 to 0 |

## Reward Formula

```
base_score = (D1*0.25 + D2*0.25 + D3*0.25 + D4*0.15 + D5*0.10)

bias_penalty = max(0, 6 - bias_audit_score) * (-0.4)
  # bias_audit < 6 = up to -2.0 penalty

freshness_mod = +0.5 if all_sources < 30d else (0 if all_sources < 90d else -0.5)

hallucination_penalty = (-1.5 * hallucination_rate)
  # 10% hallucination rate = -0.15 penalty

reward = base_score + bias_penalty + freshness_mod + hallucination_penalty
reward = clamp(reward, 0, 10)
```

## Reward Thresholds

| Reward Value | Status | Self-Improvement Action |
|-------------|--------|------------------------|
| >= 9.5 | Elite | use as few-shot example; no action |
| 9.0 - 9.4 | Published | monitor for staleness only |
| 8.0 - 8.9 | Improve | queue for next loop iteration |
| 6.0 - 7.9 | Fix | immediate improvement target |
| < 6.0 | Reject | rebuild from scratch |

## Reward Signal History (Example)

| Artifact | Prev Reward | New Reward | Delta | Primary Improvement |
|----------|------------|-----------|-------|---------------------|
| kc_anthropic_analysis.md | 7.2 | 9.1 | +1.9 | D3 (added 3 competitors) |
| kc_llm_pricing.md | 8.1 | 9.4 | +1.3 | D1 (added primary sources) |
| kc_market_sizing.md | 6.8 | 8.8 | +2.0 | D2+D3 (depth + comparison) |

## Analytical Envy Reward Boost

N01 Analytical Envy gives D3 Comparative Coverage an Envy Multiplier:

```
if D3_score >= 9.0:
    envy_bonus = +0.3  # comparing BETTER than competitors
elif D3_score <= 5.0:
    envy_penalty = -0.5  # Analytical Envy is violated
```

No other nucleus has this multiplier. D3 is the differentiator.

## Comparison: Reward Signal Approaches

| Signal | Captures | Analytical Envy | N01 Fit |
|--------|----------|----------------|---------|
| RAGAS composite | RAG accuracy | no | partial |
| Human rating | holistic quality | partially | impractical |
| This composite | D1-D5 + bias + freshness + hallucination | yes (D3 weighted) | optimal |
| BLEU/ROUGE | text similarity | no | wrong metric for research |
