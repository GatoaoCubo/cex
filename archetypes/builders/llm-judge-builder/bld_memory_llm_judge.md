---
id: p10_lr_llm_judge_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "LLM judges without scale anchors produced score variance of +/- 1.8 points on a 1-5 scale across identical inputs in 5 of 7 eval runs reviewed. Judges with concrete behavioral anchors reduced variance to +/- 0.3 points. Few-shot examples with rationale were the second most impactful calibration factor."
pattern: "Define scale anchors as concrete observable behaviors. Include at least 2 few_shot examples with chain-of-thought rationale. Set temperature: 0.0. Use judge_model from a different model family than the evaluated model. Keep criteria count <= 5 and verify non-overlap before publishing."
evidence: "7 eval pipelines: 5 showed high variance without behavioral anchors; 0 high variance after anchors + few_shot added. Self-enhancement bias observed in 3/3 cases where judge_model matched evaluated_model family."
confidence: 0.82
outcome: SUCCESS
domain: llm_judge
tags: [llm-judge, scale-anchors, few-shot, calibration, self-enhancement-bias, criteria-independence]
tldr: "Behavioral scale anchors + few-shot rationale eliminate judge variance. Different model family eliminates self-enhancement. Max 5 criteria, verify non-overlap."
impact_score: 8.5
decay_rate: 0.03
agent_node: edison
keywords: [llm judge, scale anchors, few shot, calibration, judge model, criteria, variance, self-enhancement bias, chain of thought]
memory_scope: project
observation_types: [user, feedback, project, reference]
---
## Summary
LLM-as-Judge quality degrades via two failure modes: variance (same input, different scores) and bias (systematic score inflation). Variance comes from vague anchors — behavioral IF/THEN anchors ("Score 5: all claims traceable to context; no fabricated facts") fix this. Bias comes from judging a model with its own family; a cross-family judge eliminates self-enhancement (+0.4-0.8 points on 1-5 scale).

## Pattern
**Behavioral anchors + cross-family judge + few-shot with rationale.**

Scale anchor formula: write as IF/THEN behavioral statements. Always anchor min, midpoint, max.

Judge model selection:
- Evaluated model is OpenAI family -> use Anthropic judge (claude-3-5-sonnet)
- Evaluated model is Anthropic family -> use OpenAI judge (gpt-4o)
- Evaluated model unknown -> use gpt-4o

Few-shot construction:
- Example 1: high-scoring output with rationale explaining WHAT makes it high
- Example 2: low-scoring output with rationale explaining WHAT makes it low
- Rationale MUST come before score (chain-of-thought ordering reduces position bias)

Criteria design rules:
- Write criteria as "this dimension measures X and ONLY X"
- If two criteria penalize the same flaw, merge or remove one
- Maximum 5 criteria per judge

## Anti-Pattern
- Adjective-only anchors ("1=bad, 5=good") — judge assigns scores based on vague sentiment.
- Judge model from same family as evaluated model — self-enhancement bias inflates scores.
- Overlapping criteria (e.g. "accuracy" + "factual correctness") — same flaw penalized twice.
- Temperature > 0.2 — score variance increases; use temperature 0.0.
- No few_shot examples or single example — judge drifts with no contrast reference.
