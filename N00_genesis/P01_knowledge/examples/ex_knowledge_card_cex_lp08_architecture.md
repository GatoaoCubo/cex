---
id: p01_kc_cex_lp08_architecture
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP08 Architecture — Structure and Scale for LLM Systems"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp08, architecture, patterns, laws, multi-agent, scaling]
tldr: "P08 defines 5 meta-artifacts that govern structure: agent_card, pattern, law, diagram, component_map"
when_to_use: "Understand how LLM systems scale via formal architecture and meta-artifacts"
keywords: [architecture, agent_group, pattern, law, diagram, component-map]
long_tails:
  - "How to scale a multi-agent LLM system with architecture"
  - "What is the difference between pattern and law in CEX"
axioms:
  - "ALWAYS have component_map before adding components"
  - "NEVER violate a law (inviolable, different from instruction)"
linked_artifacts:
  primary: p01_kc_cex_lp07_evals
  related: [p01_kc_cex_lp06_schema]
density_score: 1.0
data_source: "https://arxiv.org/abs/2308.08155"
related:
  - p01_kc_lp08_architecture
  - component-map-builder
  - diagram-builder
  - pattern-builder
  - bld_architecture_component_map
  - bld_architecture_diagram
  - p01_kc_cex_lp11_feedback
  - bld_architecture_pattern
  - p01_kc_cex_lp09_config
  - invariant-builder
---

## Quick Reference

topic: P08 Architecture | scope: system structure | criticality: high
types: 5 | function: BECOME + GOVERN | layer: spec + governance

## Key Concepts

- P08 is about STRUCTURE, not task execution
- P08 types are meta-artifacts (describe artifacts)
- agent_card defines a complete department with MCPs
- pattern is a reusable pattern (e.g.: continuous batching)
- law is an inviolable system rule (not an instruction)
- diagram visualizes architecture (ASCII or Mermaid)
- component_map maps connections between components
- No mainstream framework has equivalent types
- LLM systems grow without a blueprint — P08 is the blueprint
- agent_card max 4096 bytes (spec layer, core: true)
- pattern uses llm_function INJECT (informs, does not enforce)
- law uses llm_function CONSTRAIN (enforces, inviolable)
- P08 constrains all LPs: defines what is possible
- P08 is informed by P07: metrics reveal gaps
- P08 evolves with P11: architecture adapts to feedback
- Dominant function: BECOME (defines) + GOVERN (governs)
- MetaGPT and CrewAI have no formal meta-artifacts

## Phases

1. Map existing components via component_map
2. Define inviolable system laws (constraints)
3. Document emerging reusable patterns
4. Specify agent_cards per functional domain
5. Create diagrams for team visual communication
6. Review architecture when P07 evals reveal gaps

## Golden Rules

- ALWAYS document WHY for each law (not just WHAT)
- NEVER create agent_group without formal agent_card
- ALWAYS update component_map when adding a component
- NEVER treat pattern as law (pattern is a recommendation)
- ALWAYS separate diagram (visual) from component_map (data)

## Comparison

| Type | Rigidity | Scope | Example |
|------|----------|-------|---------|
| law | Inviolable | Entire system | "Never hardcode brand" |
| pattern | Recommended | Reusable | Continuous batching |
| agent_card | Mandatory | 1 department | research_agent research spec |
| diagram | Informational | Visual | Pipeline Mermaid |
| component_map | Structural | Connections | Agent-to-agent graph |

## Flow

```
[P08: Architecture Layer]
         |
    +----+----+----+----+
    |    |    |    |    |
  laws  pats  sats diag cmap
    |    |    |    |    |
    v    v    v    v    v
[CONSTRAIN] [INJECT] [BECOME]
    |          |        |
    v          v        v
 governs    informs   defines
    |          |        |
    +-----+----+--------+
          |
          v
   [operational system]
          |
          v
   [P07 evals feedback loop]
```

## References

- source: https://arxiv.org/abs/2308.08155
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_lp07_evals
- related: p01_kc_cex_lp06_schema


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp08_architecture]] | sibling | 0.42 |
| [[component-map-builder]] | downstream | 0.35 |
| [[diagram-builder]] | downstream | 0.34 |
| [[pattern-builder]] | downstream | 0.30 |
| [[bld_architecture_component_map]] | downstream | 0.27 |
| [[bld_architecture_diagram]] | downstream | 0.26 |
| [[p01_kc_cex_lp11_feedback]] | sibling | 0.24 |
| [[bld_architecture_pattern]] | downstream | 0.24 |
| [[p01_kc_cex_lp09_config]] | sibling | 0.24 |
| [[invariant-builder]] | downstream | 0.23 |
