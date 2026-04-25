---
id: p01_kc_cex_lp11_feedback
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP11 Feedback — Continuous Improvement Loop for LLM Systems"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp11, feedback, quality-gate, bugloop, guardrail, optimizer]
tldr: "P11 defines 5 types of continuous improvement: quality_gate, bugloop, lifecycle_rule, guardrail, optimizer"
when_to_use: "Understand how LLM systems implement self-correction and continuous improvement"
keywords: [feedback, quality-gate, bugloop, guardrail, optimizer, lifecycle-rule]
long_tails:
  - "How to implement self-healing in multi-agent LLM systems"
  - "What is the difference between guardrail P11 and permission P09 in CEX"
axioms:
  - "ALWAYS close the loop: detect, correct, verify"
  - "NEVER confuse guardrail (safety) with permission (access)"
linked_artifacts:
  primary: p01_kc_cex_lp10_memory
  related: [p01_kc_cex_lp07_evals]
density_score: 1.0
data_source: "https://arxiv.org/abs/2303.11366"
related:
  - p01_kc_lp11_feedback
  - bugloop-builder
  - optimizer-builder
  - guardrail-builder
  - bld_architecture_guardrail
  - bld_architecture_quality_gate
  - bld_architecture_bugloop
  - bld_collaboration_bugloop
  - bld_architecture_self_improvement_loop
  - bld_collaboration_guardrail
---

## Quick Reference

topic: P11 Feedback | scope: continuous improvement | criticality: high
types: 5 | function: GOVERN + CONSTRAIN | layer: governance

## Key Concepts

- P11 is the boss's review: detects, corrects, improves
- quality_gate is a barrier with numeric score (pass/fail)
- bugloop executes automatic cycle detect > fix > verify
- lifecycle_rule governs freshness, archive and promote
- guardrail is a security boundary (safety, not access)
- optimizer maps metric > action for continuous improvement
- P11 closes the loop: GOVERN detects, P11 corrects
- Reflexion, Self-Refine and DSPy are expressions of P11
- SWE-Agent and Voyager demonstrate automatic self-healing
- quality_gate is NOT validator (P06) nor rubric (P07)
- bugloop is NOT unit_eval (P07, manual test)
- guardrail is NOT permission (P09, access control)
- lifecycle_rule is NOT hook (P04, executable code)
- optimizer is NOT benchmark (P07, passive measurement)
- P11 improves P03: feedback optimizes prompts iteratively
- P11 updates P01: feedback generates new knowledge
- P11 uses P07: evaluation metrics are input
- Dominant function: GOVERN (improvement) + CONSTRAIN (safety)

## Phases

1. Define quality_gates with thresholds per artifact
2. Implement bugloops for critical modules (detect>fix)
3. Create lifecycle_rules (freshness 30d, archive 90d)
4. Establish security guardrails (safety boundaries)
5. Configure optimizers with metrics and automatic actions
6. Connect P07 evals as input for feedback loop

## Golden Rules

- ALWAYS have quality_gate before promoting to pool
- NEVER confuse guardrail with permission (safety vs access)
- ALWAYS verify after correcting (complete bugloop)
- NEVER self-assign quality score (external validator)
- ALWAYS document WHY for each guardrail (context)

## Comparison

| Type | Nature | Trigger | Example |
|------|--------|---------|---------|
| quality_gate | Barrier | Score < threshold | KC score >= 8.0 for pool |
| bugloop | Cycle | Error detected | detect > fix > verify loop |
| lifecycle_rule | Rule | Time/state | Archive KCs > 90 days |
| guardrail | Restriction | Dangerous action | Block delete in production |
| optimizer | Process | Low metric | Prompt rewrite if score < 7 |

## Flow

```
[P11: Feedback Layer]
         |
    +----+----+----+----+
    |    |    |    |    |
   qg   bl   lc   gr  opt
    |    |    |    |    |
    v    v    v    v    v
 [GOVERN]  [GOVERN] [CONSTRAIN]
    |         |         |
    v         v         v
 barrier   cycle    safety
    |         |         |
    +----+----+---------+
         |
         v
  [P07 evals as input]
         |
         v
  [P01 knowledge updated]
         |
         v
  [P03 prompts optimized]
```

## References

- source: https://arxiv.org/abs/2303.11366
- source: https://arxiv.org/abs/2310.11511
- related: p01_kc_cex_lp10_memory
- related: p01_kc_cex_lp07_evals


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp11_feedback]] | sibling | 0.45 |
| [[bugloop-builder]] | downstream | 0.36 |
| [[optimizer-builder]] | downstream | 0.31 |
| [[guardrail-builder]] | downstream | 0.28 |
| [[bld_architecture_guardrail]] | downstream | 0.26 |
| [[bld_architecture_quality_gate]] | downstream | 0.25 |
| [[bld_architecture_bugloop]] | downstream | 0.24 |
| [[bld_collaboration_bugloop]] | downstream | 0.24 |
| [[bld_architecture_self_improvement_loop]] | downstream | 0.24 |
| [[bld_collaboration_guardrail]] | downstream | 0.24 |
