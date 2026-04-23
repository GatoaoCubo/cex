---
kind: collaboration
id: bld_collaboration_llm_judge
pillar: P12
llm_function: COLLABORATE
purpose: How llm-judge-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Llm Judge"
version: "1.0.0"
author: n03_builder
tags: [llm_judge, builder, examples]
tldr: "Golden and anti-examples for llm judge construction, demonstrating ideal structure and common pitfalls."
domain: "llm judge construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - llm-judge-builder
  - p01_kc_llm_judge
  - p03_sp_llm_judge_builder
  - judge-config-builder
  - bld_architecture_llm_judge
  - bld_collaboration_judge_config
  - bld_collaboration_quality_gate
  - bld_collaboration_eval_dataset
  - bld_collaboration_golden_test
  - p07_llm_judge
---

# Collaboration: llm-judge-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "which model evaluates, on what criteria, at what scale, with what calibration examples?"
I do not define pipeline blocking logic. I do not define evaluation datasets. I do not define scoring formulas without an LLM.
I configure LLM-as-Judge artifacts so downstream systems can invoke automated quality evaluation.

## Crew Compositions
### Crew: "Eval Pipeline"
```
  1. llm-judge-builder    -> "judge configuration (model + criteria + scale + few_shot)"
  2. quality-gate-builder -> "pipeline gate that reads judge score and blocks/passes"
  3. dataset-builder      -> "eval corpus supplying (input, output) pairs to the judge"
```

### Crew: "RAG Quality Stack"
```
  1. llm-judge-builder      -> "faithfulness + relevance judge (RAGAS-aligned)"
  2. scoring-rubric-builder -> "criteria framework without model (human review rubric)"
  3. benchmark-builder      -> "comparative performance measurement across RAG variants"
```

### Crew: "Automated QA"
```
  1. llm-judge-builder    -> "multi-criteria quality judge"
  2. quality-gate-builder -> "threshold gate — blocks if judge score < pass_threshold"
  3. learning-record-builder -> "captures judge calibration learnings over time"
```

## Handoff Protocol
### I Receive
- seeds: evaluation domain, what outputs to judge, available ground truth (yes/no)
- optional: target framework (Braintrust/DeepEval/RAGAS/Promptfoo/OpenAI Evals), scale preference, criteria list
- optional: existing few_shot examples or calibration data

### I Produce
- llm_judge artifact (.md + .yaml frontmatter)
- committed to: `cex/P07_evals/examples/p07_judge_{slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None — independent builder (layer 0). LLM judges can be defined standalone.

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | Gates consume judge scores to make pass/fail pipeline decisions |
| benchmark-builder | Benchmarks use judges to score responses across eval datasets |
| dataset-builder | Eval datasets are consumed by judges — paired artifact relationship |
| learning-record-builder | Captures calibration patterns and bias observations from judge runs |

## Boundary Enforcement
| If user asks for... | Route to... | Reason |
|--------------------|-------------|--------|
| Criteria without a judge model | scoring-rubric-builder | scoring_rubric is criteria-only; llm_judge requires judge_model |
| Pipeline blocker based on score threshold | quality-gate-builder (P11) | quality_gate blocks execution; llm_judge only produces a score |
| Comparative system performance measurement | benchmark-builder | benchmark measures across systems; llm_judge evaluates single outputs |
| Formula-based metric (no LLM) | metric-builder | metric is formula-only; llm_judge requires LLM invocation |
| Eval corpus of test cases | dataset-builder | dataset is the corpus; llm_judge is the evaluator config |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[llm-judge-builder]] | upstream | 0.61 |
| [[p01_kc_llm_judge]] | upstream | 0.49 |
| [[p03_sp_llm_judge_builder]] | upstream | 0.43 |
| [[judge-config-builder]] | upstream | 0.42 |
| [[bld_architecture_llm_judge]] | upstream | 0.42 |
| [[bld_collaboration_judge_config]] | sibling | 0.40 |
| [[bld_collaboration_quality_gate]] | sibling | 0.40 |
| [[bld_collaboration_eval_dataset]] | sibling | 0.39 |
| [[bld_collaboration_golden_test]] | sibling | 0.37 |
| [[p07_llm_judge]] | upstream | 0.36 |
