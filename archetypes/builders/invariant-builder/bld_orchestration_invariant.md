---
kind: collaboration
id: bld_collaboration_invariant
pillar: P08
llm_function: COLLABORATE
purpose: How invariant-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Invariant"
version: "1.0.0"
author: n03_builder
tags: [invariant, builder, examples]
tldr: "Golden and anti-examples for invariant construction, demonstrating ideal structure and common pitfalls."
domain: "invariant construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_quality_gate
  - bld_collaboration_pattern
  - bld_collaboration_builder
  - invariant-builder
  - bld_architecture_kind
  - bld_collaboration_agent
  - bld_collaboration_guardrail
  - bld_collaboration_component_map
  - p03_ins_law
  - bld_collaboration_axiom
---

# Collaboration: invariant-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what operational rule MUST always be followed?"
I formalize inviolable mandates with enforcement mechanisms and exception protocols. I do NOT produce flexible guides (instruction-builder), safety restrictions (guardrail-builder), or abstract truths (axiom-builder).
## Crew Compositions
### Crew: "Governance Pipeline"
```
  1. pattern-builder      -> "proven reusable solution to ground the mandate"
  2. invariant-builder          -> "elevates the pattern to an inviolable operational rule"
  3. quality-gate-builder -> "compliance gate that enforces the invariant at validation time"
```
### Crew: "Architecture Governance"
```
  1. agent-card-builder -> "defines what a agent_group component can do"
  2. invariant-builder            -> "defines what it MUST do — inviolable behavioral mandates"
  3. guardrail-builder      -> "adds runtime safety boundaries that complement the law"
```
### Crew: "Full Governance Package"
```
  1. axiom-builder         -> "establishes abstract truths that give laws their authority"
  2. invariant-builder           -> "codifies operational mandate derived from the axiom"
  3. diagram-builder       -> "visualizes law enforcement flow for the domain"
  4. component-map-builder -> "inventories all components governed by the law"
```
## Handoff Protocol
### I Receive
- seeds: rule statement to formalize, rationale, domain context (quality/security/ops), enforcement scope
- optional: precedent patterns, known exceptions, related instructions to differentiate from
### I Produce
- invariant artifact (Markdown, 19+ frontmatter fields, all 8 body sections, max 4KB)
- committed to: `cex/P08_architecture/examples/p08_law_{number}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- pattern-builder: proven patterns may be elevated to mandatory laws; provides precedent and rationale
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | gates encode law compliance as HARD validation conditions |
| guardrail-builder | translates operational laws into enforceable runtime safety restrictions |
| agent-card-builder | specs reference applicable laws governing each agent_group |
| diagram-builder | may visualize law enforcement flows for the governed domain |
| component-map-builder | maps reference which laws govern each component |
| instruction-builder | references laws to clarify what is mandatory vs flexible guidance |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_quality_gate]] | sibling | 0.46 |
| [[bld_collaboration_pattern]] | sibling | 0.43 |
| [[bld_collaboration_builder]] | sibling | 0.42 |
| [[invariant-builder]] | related | 0.40 |
| [[bld_architecture_kind]] | related | 0.37 |
| [[bld_collaboration_agent]] | sibling | 0.36 |
| [[bld_collaboration_guardrail]] | sibling | 0.36 |
| [[bld_collaboration_component_map]] | sibling | 0.36 |
| [[p03_ins_law]] | upstream | 0.35 |
| [[bld_collaboration_axiom]] | sibling | 0.35 |
