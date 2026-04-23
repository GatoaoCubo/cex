---
kind: collaboration
id: bld_collaboration_handoff
pillar: P12
llm_function: COLLABORATE
purpose: How handoff-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Handoff"
version: "1.0.0"
author: n03_builder
tags: [handoff, builder, examples]
tldr: "Golden and anti-examples for handoff construction, demonstrating ideal structure and common pitfalls."
domain: "handoff construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_dispatch_rule
  - handoff-builder
  - bld_collaboration_handoff_protocol
  - bld_collaboration_instruction
  - bld_collaboration_context_doc
  - bld_collaboration_action_prompt
  - bld_collaboration_dag
  - bld_collaboration_builder
  - bld_architecture_handoff
  - p03_sp_handoff_builder
---

# Collaboration: handoff-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what should the target do, with what context, and how should it commit?"
I do not define routing rules. I do not model dependencies.
I package delegation instructions so remote executors have everything needed to complete a task.
## Crew Compositions
### Crew: "Full Dispatch Setup"
```
  1. dispatch-rule-builder -> "routing rules (who receives)"
  2. dag-builder -> "execution order (when to execute)"
  3. handoff-builder -> "delegation instructions (what to do)"
```
### Crew: "Task Delegation"
```
  1. context-doc-builder -> "domain context for the executor"
  2. instruction-builder -> "step-by-step recipe"
  3. handoff-builder -> "packaged delegation with scope fence and commit rules"
```
## Handoff Protocol
### I Receive
- seeds: target executor, task description, scope fence (allowed/forbidden paths)
- optional: context documents, seed keywords, commit template, quality threshold
### I Produce
- handoff artifact (.md with context, tasks, scope fence, commit, signal sections)
- committed to: `cex/P12/examples/p12_handoff_{mission}_{target}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- dispatch-rule-builder: provides routing decision that determines handoff target
- context-doc-builder: provides domain context embedded in the handoff
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| dag-builder | Models handoff dependencies in execution graphs |
| e2e-eval-builder | Tests that handoff execution produces correct results |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_dispatch_rule]] | sibling | 0.57 |
| [[handoff-builder]] | related | 0.52 |
| [[bld_collaboration_handoff_protocol]] | sibling | 0.51 |
| [[bld_collaboration_instruction]] | sibling | 0.43 |
| [[bld_collaboration_context_doc]] | sibling | 0.43 |
| [[bld_collaboration_action_prompt]] | sibling | 0.42 |
| [[bld_collaboration_dag]] | sibling | 0.42 |
| [[bld_collaboration_builder]] | sibling | 0.40 |
| [[bld_architecture_handoff]] | upstream | 0.39 |
| [[p03_sp_handoff_builder]] | upstream | 0.39 |
