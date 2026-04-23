---
id: p07_llm_judge
kind: llm_judge
pillar: P07
version: 1.0.0
title: "Template — LLM Judge"
tags: [template, llm, judge, evaluation, rubric]
tldr: "An LLM-based evaluator that scores outputs against a rubric. Defines the judge prompt, scoring dimensions, calibration method, and bias mitigation."
quality: 9.1
updated: "2026-04-07"
domain: "evaluation and testing"
author: n03_builder
created: "2026-04-07"
density_score: 0.89
related:
  - bld_knowledge_card_llm_judge
  - p01_kc_llm_judge
  - p10_lr_llm_judge_builder
  - bld_collaboration_llm_judge
  - llm-judge-builder
  - bld_knowledge_card_judge_config
  - bld_output_template_llm_judge
  - n01_atom_26_evaluation_taxonomy
  - judge-config-builder
  - p01_kc_reward_signal
---

# LLM Judge: [JUDGE_NAME]

## Purpose
[WHAT outputs this judge evaluates — artifact quality, response accuracy, safety compliance]

## Judge Configuration
```yaml
model: [claude-sonnet-4-6 | gpt-4o]
temperature: 0.0          # Deterministic scoring
max_tokens: 500           # Enough for scores + rationale
cost_per_eval: ~$0.005    # Budget awareness
```

## Scoring Prompt
```
You are an expert evaluator. Score the following output on these dimensions.
For each dimension, provide a score (1-5) and a 1-sentence rationale.

## Output to Evaluate
{output}

## Scoring Dimensions
1. **Accuracy** (1-5): Is the content factually correct?
2. **Structure** (1-5): Does it follow the expected format?
3. **Completeness** (1-5): Are all required elements present?
4. **Clarity** (1-5): Is it easy to understand?

Respond in JSON: {"accuracy": {"score": N, "rationale": "..."}, ...}
```

## Calibration
- **Anchor examples**: Include 3 pre-scored examples (low/mid/high) in prompt
- **Inter-rater agreement**: Compare LLM judge vs human scores on 20 samples
- **Target kappa**: ≥ 0.7 (substantial agreement)

## Bias Mitigation

| Bias | Mitigation |
|------|-----------|
| Position bias | Randomize output order in comparative evals |
| Verbosity bias | Include word count in scoring criteria |
| Self-preference | Never judge own model's output |
| Anchoring | Randomize score scale presentation |

## Quality Gate
- [ ] Judge model different from generator model
- [ ] Temperature = 0 (deterministic)
- [ ] Calibration examples included
- [ ] Output format is structured (JSON/YAML)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_llm_judge]] | upstream | 0.41 |
| [[p01_kc_llm_judge]] | related | 0.40 |
| [[p10_lr_llm_judge_builder]] | downstream | 0.39 |
| [[bld_collaboration_llm_judge]] | downstream | 0.38 |
| [[llm-judge-builder]] | related | 0.36 |
| [[bld_knowledge_card_judge_config]] | upstream | 0.32 |
| [[bld_output_template_llm_judge]] | upstream | 0.29 |
| [[n01_atom_26_evaluation_taxonomy]] | upstream | 0.29 |
| [[judge-config-builder]] | related | 0.29 |
| [[p01_kc_reward_signal]] | downstream | 0.29 |
