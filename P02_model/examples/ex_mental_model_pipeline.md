---
id: ex_mental_model_pipeline
kind: mental_model
pillar: P02
title: "Pipeline Mental Model"
tags: [mental_model, pipeline, compilation, phases, 8f]
tldr: "The compilation pipeline thinks in 5 phases: CAPTURE→DECOMPOSE→HYDRATE→COMPILE→ENVELOPE. Each phase transforms state. Maps directly to CEX 8F functions."
references:
  - tpl_mental_model
  - ex_agent_copywriter
quality: 9.0
updated: "2026-04-07"
domain: "model configuration"
version: "1.0.0"
author: n03_builder
created: "2026-04-07"
density_score: 0.91
---

# Pipeline Mental Model

## The 5-Phase Compilation Model
Every artifact production follows the same mental model, regardless of kind:

```
CAPTURE → DECOMPOSE → HYDRATE → COMPILE → ENVELOPE
   F1        F2-F3       F3       F4-F6      F7-F8
```

## Phase Details

| Phase | What Happens | 8F Mapping | Output |
|-------|-------------|------------|--------|
| CAPTURE | Receive intent, load constraints | F1 CONSTRAIN | Bounded problem |
| DECOMPOSE | Break intent into kind + fields | F2 BECOME + F3 INJECT | Structured spec |
| HYDRATE | Inject knowledge, examples, memory | F3 INJECT | Rich context |
| COMPILE | Transform context into artifact | F4 REASON + F6 PRODUCE | Raw artifact |
| ENVELOPE | Validate, package, deliver | F7 GOVERN + F8 COLLABORATE | Shipped artifact |

## Analogy: The Factory
```
Raw material → Blueprint → Assembly → Quality Control → Shipping
  (intent)     (ISOs)     (LLM call)    (hard gates)    (save+commit)
```

## Key Properties
- **Deterministic structure**: Same intent + ISOs always produces same skeleton
- **Stateful**: Each phase reads output of previous phases
- **Bounded**: Constraints limit what can be produced (no unbounded generation)
- **Recoverable**: If COMPILE fails, retry with feedback (don't restart from CAPTURE)
- **Observable**: Each phase logs timing and state for debugging

## When to Use This Model
- Building any CEX artifact (8F pipeline)
- Designing multi-stage LLM workflows
- Creating data transformation pipelines
- Structuring any process with accumulating state

## Anti-patterns
- **Skipping DECOMPOSE**: Going directly from intent to LLM call produces generic output
- **No ENVELOPE**: Shipping without validation leads to broken artifacts
- **Stateless phases**: Each phase must read accumulated state, not just its input
- **Big-bang COMPILE**: Don't try to produce everything in one LLM call — break into stages

## Quality Gate
- [ ] All 5 phases present in pipeline design
- [ ] Each phase has defined input/output
- [ ] State accumulates (not discarded between phases)
- [ ] Validation happens in ENVELOPE, not scattered
