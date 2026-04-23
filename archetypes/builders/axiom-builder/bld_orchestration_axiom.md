---
kind: collaboration
id: bld_collaboration_axiom
pillar: P12
llm_function: COLLABORATE
purpose: How axiom-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Axiom"
version: "1.0.0"
author: n03_builder
tags: [axiom, builder, examples]
tldr: "Golden and anti-examples for axiom construction, demonstrating ideal structure and common pitfalls."
domain: "axiom construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - axiom-builder
  - bld_collaboration_guardrail
  - p03_sp_axiom_builder
  - bld_collaboration_knowledge_card
  - bld_collaboration_bugloop
  - bld_collaboration_builder
  - bld_collaboration_invariant
  - bld_architecture_axiom
  - p01_kc_axiom
  - bld_collaboration_learning_record
---

# Collaboration: axiom-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the permanent, immutable rule that governs this domain?"
I do not write operational laws. I do not define safety guardrails.
I formalize fundamental truths so governance builders can reference immutable principles.
## Crew Compositions
### Crew: "Governance Foundation"
```
  1. axiom-builder -> "immutable fundamental rules"
  2. guardrail-builder -> "safety boundaries derived from axioms"
  3. bugloop-builder -> "correction cycles that enforce axiom compliance"
```
### Crew: "Knowledge Formalization"
```
  1. knowledge-card-builder -> "domain facts and research"
  2. axiom-builder -> "permanent truths distilled from facts"
  3. glossary-entry-builder -> "term definitions referenced by axioms"
```
## Handoff Protocol
### I Receive
- seeds: domain name, candidate rule statement, justification
- optional: existing laws for boundary check, related axioms
### I Produce
- axiom artifact (.md + .yaml frontmatter, max 3KB, density >= 0.80)
- committed to: `cex/P10/examples/p10_axiom_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- knowledge-card-builder: provides factual basis for axiom formalization
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| guardrail-builder | Safety boundaries reference axioms as justification |
| bugloop-builder | Correction cycles check axiom compliance |
| golden-test-builder | Calibration references axiom constraints |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[axiom-builder]] | upstream | 0.50 |
| [[bld_collaboration_guardrail]] | sibling | 0.49 |
| [[p03_sp_axiom_builder]] | upstream | 0.47 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.46 |
| [[bld_collaboration_bugloop]] | sibling | 0.44 |
| [[bld_collaboration_builder]] | sibling | 0.43 |
| [[bld_collaboration_invariant]] | sibling | 0.42 |
| [[bld_architecture_axiom]] | upstream | 0.41 |
| [[p01_kc_axiom]] | upstream | 0.41 |
| [[bld_collaboration_learning_record]] | sibling | 0.40 |
