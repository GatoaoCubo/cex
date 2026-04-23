---
kind: collaboration
id: bld_collaboration_interface
pillar: P12
llm_function: COLLABORATE
purpose: How interface-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Interface"
version: "1.0.0"
author: n03_builder
tags: [interface, builder, examples]
tldr: "Golden and anti-examples for interface construction, demonstrating ideal structure and common pitfalls."
domain: "interface construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_input_schema
  - interface-builder
  - bld_collaboration_component_map
  - bld_collaboration_builder
  - bld_collaboration_validation_schema
  - bld_collaboration_client
  - p03_sp_interface_builder
  - bld_collaboration_golden_test
  - bld_collaboration_dispatch_rule
  - bld_collaboration_action_prompt
---

# Collaboration: interface-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what is the formal contract between these two agents/systems?"
I do not define unilateral input schemas. I do not build runtime signals.
I specify bilateral integration contracts so agents and systems interoperate reliably.
## Crew Compositions
### Crew: "Integration Design"
```
  1. component-map-builder -> "inventory of components that need interfaces"
  2. interface-builder -> "bilateral contracts between components"
  3. client-builder -> "client implementations against interfaces"
  4. connector-builder -> "bidirectional integrations via interfaces"
```
### Crew: "Contract Stack"
```
  1. input-schema-builder -> "unilateral input contracts"
  2. interface-builder -> "bilateral integration contracts"
  3. e2e-eval-builder -> "validation that contracts are honored"
```
## Handoff Protocol
### I Receive
- seeds: party A name, party B name, methods/operations list
- optional: versioning strategy, deprecation policy, mock specifications
### I Produce
- interface artifact (.md + .yaml frontmatter)
- committed to: `cex/P06/examples/p06_interface_{a}_{b}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- input-schema-builder: provides unilateral schemas that compose into bilateral contracts
- component-map-builder: identifies which components need interfaces
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| client-builder | Implements outbound side of the interface |
| connector-builder | Implements bidirectional side of the interface |
| e2e-eval-builder | Tests that interface contracts are honored end-to-end |
| dispatch-rule-builder | Routes to targets defined by interface contracts |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_input_schema]] | sibling | 0.53 |
| [[interface-builder]] | upstream | 0.47 |
| [[bld_collaboration_component_map]] | sibling | 0.45 |
| [[bld_collaboration_builder]] | sibling | 0.41 |
| [[bld_collaboration_validation_schema]] | sibling | 0.40 |
| [[bld_collaboration_client]] | sibling | 0.40 |
| [[p03_sp_interface_builder]] | upstream | 0.37 |
| [[bld_collaboration_golden_test]] | sibling | 0.35 |
| [[bld_collaboration_dispatch_rule]] | sibling | 0.34 |
| [[bld_collaboration_action_prompt]] | sibling | 0.34 |
