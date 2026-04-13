---
id: kc_prompt_optimizer
kind: knowledge_card
type: kind
pillar: P01
title: "Prompt Optimizer -- Deep Knowledge"
version: 1.0.0
created: "2026-04-13"
updated: "2026-04-13"
author: n03_builder
domain: prompt_optimizer
quality: null
tags: [prompt_optimizer, P03, GOVERN, kind-kc]
tldr: "Automated prompt improvement via iterative scoring, mutation, and selection"
when_to_use: "Building or reviewing prompt_optimizer artifacts"
keywords: [DSPy, APE, OPRO, prompt-tuning, meta-prompting]
feeds_kinds: [prompt_optimizer]
density_score: 0.90
linked_artifacts:
  primary: _tools/cex_prompt_optimizer.py
  related: [P01_knowledge/library/kind/kc_prompt_compiler.md]
---

# Prompt Optimizer

## Spec
```yaml
kind: prompt_optimizer
pillar: P03
llm_function: GOVERN
max_bytes: 5120
naming: p03_po_{{name}}.md
core: false
```

## What It Is

A prompt_optimizer defines **automated prompt improvement**: ingest a seed prompt, run scoring and mutation loops, emit a higher-performing variant. It formalizes the optimization policy -- what to mutate, how to score, when to stop -- so optimization is reproducible rather than ad hoc. Lineage: **DSPy** (compile-time optimization), **APE** (Zhou 2022), **OPRO** (Google 2023, LLMs as optimizers).

## How It Differs From Similar Kinds

| Kind | Distinction |
|------|-------------|
| **prompt_optimizer** (P03) | Improves a prompt via scored iteration |
| prompt_compiler (P03) | Resolves intent into {kind, pillar, nucleus} |
| prompt_template (P03) | Fills {{variables}} for generation |
| optimizer (P11) | Generic optimization; target is not a prompt |
| quality_gate (P07) | Pass/fail threshold only; no improvement loop |

## Optimization Loop

| Stage | Action |
|-------|--------|
| 1 Baseline | Score seed on eval_dataset |
| 2 Mutate | Generate N variants (reword, CoT, few-shot, persona) |
| 3 Evaluate | Score each against scoring_rubric or llm_judge |
| 4 Select | Keep top-k |
| 5 Iterate | Re-mutate from winners until plateau or budget cap |

## Industry References

| System | Concept | Relationship |
|--------|---------|-------------|
| DSPy | teleprompter, MIPROv2 | Direct ancestor: compile signatures into tuned prompts |
| APE (Zhou 2022) | Automatic Prompt Engineer | LLM proposes, LLM scores, iterate |
| OPRO (Google 2023) | LLM as optimizer | Scored trajectories generate next prompt |
| PromptBreeder (DeepMind) | Evolutionary mutation | Genetic-algorithm variant |

## Key Design Decisions

| Decision | Rule |
|----------|------|
| Scoring source | eval_dataset + scoring_rubric OR llm_judge |
| Budget cap | max_iterations + max_tokens required |
| Plateau detection | Stop if delta < threshold for N rounds |
| Winner persistence | Save top variant as prompt_version |

## Anti-Patterns

- No baseline score (cannot detect regression)
- Single metric (overfits, degrades real quality)
- No budget cap (unbounded API cost)
- Mutate on production prompt (breaks live traffic; use shadow eval)
- Ignore variance (one lucky run != true improvement)

## Application Checklist

1. Baseline: seed + eval_dataset + initial score
2. Enumerate mutation strategies; bind scoring; set budget caps
3. Persist winner as prompt_version with score delta
4. Validate body <= 5120 bytes; quality: null
