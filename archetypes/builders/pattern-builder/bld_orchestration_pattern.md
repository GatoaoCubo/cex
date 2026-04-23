---
kind: collaboration
id: bld_collaboration_pattern
pillar: P08
llm_function: COLLABORATE
purpose: How pattern-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Pattern"
version: "1.0.0"
author: n03_builder
tags: [pattern, builder, examples]
tldr: "Golden and anti-examples for pattern construction, demonstrating ideal structure and common pitfalls."
domain: "pattern construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_learning_record
  - pattern-builder
  - bld_collaboration_builder
  - bld_collaboration_agent
  - bld_collaboration_knowledge_card
  - bld_collaboration_invariant
  - bld_collaboration_system_prompt
  - bld_collaboration_quality_gate
  - bld_architecture_kind
  - bld_collaboration_agent_card
---

# Collaboration: pattern-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the named, reusable solution for this recurring problem?"
I formalize architecture patterns with problem, solution, forces, consequences, and applicability. I do NOT write inviolable rules (invariant-builder), draw visual diagrams (diagram-builder), or define executable workflows (workflow-builder).
## Crew Compositions
### Crew: "Architecture Documentation Suite"
```
  1. pattern-builder       -> "formalizes the reusable solution with forces and consequences"
  2. diagram-builder       -> "produces visual representation of the pattern structure"
  3. invariant-builder           -> "encodes non-negotiable constraints the pattern must respect"
```
### Crew: "Knowledge Base Construction"
```
  1. learning-record-builder  -> "captures what worked in forctice"
  2. pattern-builder          -> "formalizes recurring solution from learning records"
  3. knowledge-card-builder   -> "assembles pattern into searchable brain card"
```
### Crew: "Agent Design Documentation"
```
  1. pattern-builder          -> "captures recurring agent interaction pattern"
  2. agent-card-builder   -> "references applicable patterns in agent_group spec"
  3. instruction-builder      -> "turns the pattern into step-by-step agent instructions"
```
## Handoff Protocol
### I Receive
- seeds: pattern name, recurring problem description, known solution examples
- optional: related patterns, known anti-patterns, applicability constraints
### I Produce
- pattern artifact (Markdown, max 4KB, density >= 0.80)
- committed to: `cex/P08/examples/p08_pat_{name}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- learning-record-builder: repeated learning records reveal recurring patterns worth formalizing
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| invariant-builder | proven patterns may become mandatory inviolable laws |
| agent-card-builder | agent_group specs reference applicable patterns |
| instruction-builder | translates pattern solution into executable agent steps |
| knowledge-card-builder | ingests patterns as core knowledge artifacts |
| axiom-builder | universal patterns may crystallize into system axioms |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_learning_record]] | sibling | 0.42 |
| [[pattern-builder]] | related | 0.39 |
| [[bld_collaboration_builder]] | sibling | 0.39 |
| [[bld_collaboration_agent]] | sibling | 0.39 |
| [[bld_collaboration_knowledge_card]] | sibling | 0.38 |
| [[bld_collaboration_invariant]] | sibling | 0.36 |
| [[bld_collaboration_system_prompt]] | sibling | 0.36 |
| [[bld_collaboration_quality_gate]] | sibling | 0.35 |
| [[bld_architecture_kind]] | related | 0.35 |
| [[bld_collaboration_agent_card]] | sibling | 0.33 |
