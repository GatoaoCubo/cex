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
quality: 9.1
tags: [prompt_optimizer, P03, GOVERN, kind-kc]
tldr: "Automated prompt improvement via iterative scoring, mutation, and selection"
when_to_use: "Building or reviewing prompt_optimizer artifacts"
keywords: [DSPy, APE, OPRO, prompt-tuning, meta-prompting]
feeds_kinds: [prompt_optimizer]
density_score: 0.90
linked_artifacts:
  primary: _tools/cex_prompt_optimizer.py
  related: [P01_knowledge/library/kind/kc_prompt_compiler.md]
related:
  - bld_tools_prompt_optimizer
  - bld_knowledge_card_prompt_optimizer
  - bld_examples_prompt_optimizer
  - bld_instruction_prompt_optimizer
  - bld_output_template_prompt_optimizer
  - p03_qg_prompt_optimizer
  - p01_kc_optimizer
  - prompt-version-builder
  - bld_knowledge_card_prompt_version
  - p01_kc_prompt_version
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

- **prompt_compiler** resolves intent (F1); prompt_optimizer improves prompts (F7)
- **prompt_template** fills {{variables}}; prompt_optimizer rewrites the template itself
- **optimizer** (P11) is generic; prompt_optimizer targets prompt text specifically
- **quality_gate** only accepts/rejects; prompt_optimizer iterates to improve

## Optimization Loop

1. **Baseline**: score seed on eval_dataset
2. **Mutate**: generate N variants (reword, CoT, few-shot, persona)
3. **Evaluate**: score each against scoring_rubric or llm_judge
4. **Select + Iterate**: keep top-k, re-mutate until plateau or budget cap

## Industry References

- **DSPy** (Stanford): `teleprompter`, `MIPROv2` -- direct ancestor, compiles signatures into tuned prompts
- **APE** (Zhou 2022): LLM proposes, LLM scores, iterate
- **OPRO** (Google 2023): LLM as optimizer over prompt text via scored trajectories
- **PromptBreeder** (DeepMind): evolutionary / genetic-algorithm variant of the same loop

## Key Design Decisions

- **Scoring source**: eval_dataset + scoring_rubric, or llm_judge (deterministic first)
- **Budget cap**: max_iterations + max_tokens required (prevents unbounded cost)
- **Plateau detection**: stop if delta < threshold for N rounds
- **Winner persistence**: save top variant as prompt_version (audit + rollback)

## Anti-Patterns

- No baseline score (cannot detect regression)
- Single metric (overfits, degrades real quality)
- No budget cap (unbounded API cost)
- Mutate on production prompt (breaks live traffic; use shadow eval)
- Ignore variance (one lucky run != true improvement)

## Application Checklist

1. Baseline: seed + eval_dataset + initial score; enumerate mutations; bind scoring; set budget caps
2. Persist winner as prompt_version with score delta; validate body <= 5120 bytes; quality: null

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_prompt_optimizer]] | downstream | 0.36 |
| [[bld_knowledge_card_prompt_optimizer]] | sibling | 0.32 |
| [[bld_examples_prompt_optimizer]] | downstream | 0.27 |
| [[bld_instruction_prompt_optimizer]] | downstream | 0.26 |
| [[bld_output_template_prompt_optimizer]] | downstream | 0.24 |
| [[p03_qg_prompt_optimizer]] | downstream | 0.23 |
| [[p01_kc_optimizer]] | sibling | 0.23 |
| [[prompt-version-builder]] | downstream | 0.23 |
| [[bld_knowledge_card_prompt_version]] | sibling | 0.22 |
| [[p01_kc_prompt_version]] | sibling | 0.22 |
