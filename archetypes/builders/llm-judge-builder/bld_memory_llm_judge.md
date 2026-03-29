---
id: p10_lr_llm_judge_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "LLM judges without scale anchors produced score variance of +/- 1.8 points on a 1-5 scale across identical inputs in 5 of 7 eval runs reviewed. Judges with concrete behavioral anchors (not just low/mid/high labels) reduced variance to +/- 0.3 points. Few-shot examples with rationale were the second most impactful calibration factor."
pattern: "Define scale anchors as concrete observable behaviors. Include at least 2 few_shot examples with chain-of-thought rationale. Set temperature: 0.0. Use judge_model from a different model family than the evaluated model. Keep criteria count <= 5 and verify non-overlap before publishing."
evidence: "7 eval pipelines: 5 showed high variance without behavioral anchors; 0 high variance after anchors + few_shot added. Self-enhancement bias observed in 3/3 cases where judge_model matched evaluated_model family."
confidence: 0.82
outcome: SUCCESS
domain: llm_judge
tags: [llm-judge, scale-anchors, few-shot, calibration, self-enhancement-bias, criteria-independence]
tldr: "Behavioral scale anchors + few-shot rationale eliminate judge variance. Different model family eliminates self-enhancement. Max 5 criteria, verify non-overlap."
impact_score: 8.5
decay_rate: 0.03
satellite: edison
keywords: [llm judge, scale anchors, few shot, calibration, judge model, criteria, variance, self-enhancement bias, chain of thought]
---

## Summary
LLM-as-Judge quality degrades in two distinct failure modes: variance (same input, different scores across runs) and bias (systematic distortion favoring certain outputs). Both are invisible during development and expensive to discover in production.
Variance is caused by vague scale anchors. When anchors say "1=poor, 3=average, 5=excellent", the judge maps its own interpretation of "excellent" — which shifts across contexts. When anchors say "5=all claims directly supported by retrieved context; no fabricated facts detected", the judge has a behavioral checklist to apply consistently.
Bias is caused by mismatched judge-evaluated model pairing. A model evaluating its own family's outputs systematically inflates scores by 0.4-0.8 points on likert 1-5 scales (self-enhancement bias). Using a judge from a different provider family eliminates this.

## Pattern
**Behavioral anchors + cross-family judge + few-shot with rationale.**

Scale anchor formula:
- Write anchors as IF/THEN behavioral statements
- "Score 5: IF all claims are traceable to the provided context AND no unsupported assertions are present"
- "Score 1: IF the output contradicts the context OR introduces facts absent from context"
- Always anchor minimum, midpoint, and maximum — adjacent scores derive from there

Judge model selection:
- Evaluated model is OpenAI family -> use Anthropic judge (claude-3-5-sonnet)
- Evaluated model is Anthropic family -> use OpenAI judge (gpt-4o)
- Evaluated model unknown -> use gpt-4o (most consistent calibration in literature)

Few-shot construction:
- Example 1: a genuinely high-scoring output with rationale explaining WHAT makes it high
- Example 2: a genuinely low-scoring output with rationale explaining WHAT makes it low
- Rationale MUST come before score (chain-of-thought ordering reduces position bias)
- Do not use borderline examples as the only few-shot — include the extremes first

Criteria design rules:
- Write criteria as "this dimension measures X and ONLY X"
- If two criteria would both penalize the same flaw, merge or remove one
- Maximum 5 criteria per judge — split into multiple judges if more coverage needed

## Anti-Pattern
- Adjective-only anchors ("1=bad, 5=good") — judge assigns scores based on vague sentiment, not behavior.
- Judge model from same family as evaluated model — self-enhancement bias inflates scores systematically.
- Overlapping criteria (e.g. "accuracy" + "factual correctness") — same flaw penalized twice, inflating failure signal.
- Temperature > 0.2 — score variance increases; deterministic evaluation requires temperature 0.0.
- No few_shot examples — judge drifts on edge cases with no behavioral reference point.
- Single few-shot example — one example sets an anchor at one end only; judge has no contrast reference.
- Criteria count > 5 — cognitive overload causes later criteria to receive less attention from the judge.
- Omitting chain_of_thought: true — judges that score without reasoning show 2-3x higher variance on ambiguous inputs.

## Context
The 2048-byte body limit for llm_judge accommodates the few_shot section, which is the highest-value content in the artifact. Budget bytes accordingly: frontmatter (~600) + Overview (~100) + Criteria (~400) + Scale (~200) + Few-Shot (~700) = ~2000. The few-shot rationale is not decoration — it is the primary calibration signal for the judge model at inference time. Every byte spent on rationale clarity directly reduces scoring variance in production.
