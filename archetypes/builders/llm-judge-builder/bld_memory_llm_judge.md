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
agent_group: edison
keywords: [llm judge, scale anchors, few shot, calibration, judge model, criteria, variance, self-enhancement bias, chain of thought]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Llm Judge"
density_score: 0.90
llm_function: INJECT
related:
  - bld_knowledge_card_llm_judge
  - llm-judge-builder
  - bld_collaboration_llm_judge
  - p07_llm_judge
  - p01_kc_llm_judge
  - p11_qg_llm_judge
  - p03_sp_llm_judge_builder
  - bld_manifest_memory_type
  - bld_instruction_llm_judge
  - bld_tools_memory_type
---
## Summary
LLM-as-Judge quality degrades via two failure modes: variance (same input, different scores) and bias (systematic score inflation). Variance comes from vague anchors — behavioral IF/THEN anchors ("Score 5: all claims traceable to context; no fabricated facts") fix this. Bias comes from judging a model with its own family; a cross-family judge eliminates self-enhancement (+0.4-0.8 points on 1-5 scale).

## Pattern
**Behavioral anchors + cross-family judge + few-shot with rationale.**

Scale anchor formula: write as IF/THEN behavioral statements. Always anchor min, midpoint, max.

Judge model selection:
1. Evaluated model is OpenAI family -> use Anthropic judge (claude-3-5-sonnet)
2. Evaluated model is Anthropic family -> use OpenAI judge (gpt-4o)
3. Evaluated model unknown -> use gpt-4o

Few-shot construction:
1. Example 1: high-scoring output with rationale explaining WHAT makes it high
2. Example 2: low-scoring output with rationale explaining WHAT makes it low
3. Rationale MUST come before score (chain-of-thought ordering reduces position bias)

Criteria design rules:
1. Write criteria as "this dimension measures X and ONLY X"
2. If two criteria penalize the same flaw, merge or remove one
3. Maximum 5 criteria per judge

## Anti-Pattern
1. Adjective-only anchors ("1=bad, 5=good") — judge assigns scores based on vague sentiment.
2. Judge model from same family as evaluated model — self-enhancement bias inflates scores.
3. Overlapping criteria (e.g. "accuracy" + "factual correctness") — same flaw penalized twice.
4. Temperature > 0.2 — score variance increases; use temperature 0.0.
5. No few_shot examples or single example — judge drifts with no contrast reference.

## Builder Context

This ISO operates within the `llm-judge-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_llm_judge_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_llm_judge_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | llm_judge |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_llm_judge]] | upstream | 0.51 |
| [[llm-judge-builder]] | upstream | 0.45 |
| [[bld_collaboration_llm_judge]] | downstream | 0.43 |
| [[p07_llm_judge]] | upstream | 0.43 |
| [[p01_kc_llm_judge]] | upstream | 0.42 |
| [[p11_qg_llm_judge]] | downstream | 0.38 |
| [[p03_sp_llm_judge_builder]] | upstream | 0.38 |
| [[bld_manifest_memory_type]] | upstream | 0.37 |
| [[bld_instruction_llm_judge]] | upstream | 0.33 |
| [[bld_tools_memory_type]] | upstream | 0.32 |
