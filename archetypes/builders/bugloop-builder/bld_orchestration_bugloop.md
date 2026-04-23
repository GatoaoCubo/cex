---
kind: collaboration
id: bld_collaboration_bugloop
pillar: P12
llm_function: COLLABORATE
purpose: How bugloop-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Bugloop"
version: "1.0.0"
author: n03_builder
tags: [bugloop, builder, examples]
tldr: "Golden and anti-examples for bugloop construction, demonstrating ideal structure and common pitfalls."
domain: "bugloop construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bugloop-builder
  - bld_collaboration_quality_gate
  - bld_collaboration_e2e_eval
  - bld_collaboration_benchmark
  - bld_collaboration_guardrail
  - bld_collaboration_builder
  - bld_collaboration_golden_test
  - bld_collaboration_axiom
  - p03_sp_bugloop_builder
  - bld_collaboration_memory_scope
---

# Collaboration: bugloop-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the automatic detect-fix-verify loop for this system?"
I do not define quality gates. I do not score rubrics.
I design automated correction cycles so systems self-heal without manual intervention.
## Crew Compositions
### Crew: "Self-Healing System"
```
  1. benchmark-builder -> "performance thresholds for detection triggers"
  2. bugloop-builder -> "detect-fix-verify correction cycle"
  3. guardrail-builder -> "safety boundaries for auto-fix scope"
```
### Crew: "Governance Enforcement"
```
  1. axiom-builder -> "immutable rules to enforce"
  2. bugloop-builder -> "correction loop for axiom violations"
  3. e2e-eval-builder -> "end-to-end verification after fix"
```
## Handoff Protocol
### I Receive
- seeds: detection trigger pattern, target system/agent, fix strategy type
- optional: max_attempts, escalation target, rollback policy
### I Produce
- bugloop artifact (.md + .yaml frontmatter)
- committed to: `cex/P11/examples/p11_bugloop_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- benchmark-builder: provides thresholds that trigger detection
- axiom-builder: provides invariant rules that define "correct" state
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| e2e-eval-builder | Validates that bugloop fixes pass full pipeline |
| daemon-builder | Background processes may host bugloop execution |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bugloop-builder]] | upstream | 0.50 |
| [[bld_collaboration_quality_gate]] | sibling | 0.47 |
| [[bld_collaboration_e2e_eval]] | sibling | 0.46 |
| [[bld_collaboration_benchmark]] | sibling | 0.44 |
| [[bld_collaboration_guardrail]] | sibling | 0.44 |
| [[bld_collaboration_builder]] | sibling | 0.43 |
| [[bld_collaboration_golden_test]] | sibling | 0.41 |
| [[bld_collaboration_axiom]] | sibling | 0.39 |
| [[p03_sp_bugloop_builder]] | upstream | 0.37 |
| [[bld_collaboration_memory_scope]] | sibling | 0.37 |
