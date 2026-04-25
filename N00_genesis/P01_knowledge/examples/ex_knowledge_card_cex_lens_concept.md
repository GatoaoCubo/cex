---
id: p01_kc_cex_lens_concept
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Lens — Cognitive Perspective That Refracts All Input"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lens, perspective, cognitive-filter, agent_group]
tldr: "Lens is a cognitive perspective that filters ALL perception and production — same input, radically different outputs per lens"
when_to_use: "Understand how agent_groups process the same input in distinct ways"
keywords: [lens, cognitive-perspective, refraction, prismatic-model]
long_tails:
  - "How lenses differentiate agent_groups that receive the same input"
  - "What is the difference between lens and role in multi-agent systems"
axioms:
  - "ALWAYS define lens in mental_model before assigning tasks"
  - "NEVER treat lens as a simple role (lens colors ALL perception)"
linked_artifacts:
  primary: p01_kc_cex_function_become
  related: [p01_kc_cex_fractal_architecture, p01_kc_cex_boundary_concept]
density_score: null
data_source: null
related:
  - bld_memory_lens
  - bld_architecture_lens
  - lens-builder
  - p03_sp_lens_builder
  - p11_qg_lens
  - bld_collaboration_lens
  - p03_ins_lens
  - bld_schema_lens
  - bld_tools_lens
  - p01_kc_lens
---

## Summary

Lens is the most original concept in CEX. Unlike "role" (functional role), lens is a cognitive perspective that filters ALL perception and production of an entity. Implemented as a P02 artifact in each agent_group's mental_model.yaml. Prismatic model: same input (white light) passes through 6 lenses and produces 6 refractions. The LensEngine orchestrates automatic routing, execution by specific lens, and multi-lens pipelines.

## Spec

| Satellite | Lens | Example Input | Refracted Output |
|-----------|------|---------------|-----------------|
| research_agent | Analytical Envy | "BT headphones market" | Comparative table, 15 competitors, sources |
| marketing_agent | Creative Lust | "BT headphones market" | 5 emotional triggers, sales copy |
| knowledge_agent | Knowledge Gluttony | "BT headphones market" | KC indexed by category, price, channel |
| commercial_agent | Strategic Greed | "BT headphones market" | Margin by range, most profitable channel |
| builder_agent | Inventive Pride | "BT headphones market" | Scraper prototype, React component |
| operations_agent | Gating Wrath | "BT headphones market" | Deploy pipeline, E2E tests, monitoring |

Closest industry concept: "Role" (MetaGPT), "backstory" (CrewAI). Difference: role describes function, lens colors ALL perception.

Implementation: `lens` field in `mental_model.yaml`. LensEngine orchestrates 3 modes: automatic routing to most suitable lens, execution with configurable intensity, sequential multi-lens pipeline.

Prismatic model: 6 lenses + seventh consciousness (user/orchestrator). Lens combinations are compositional — 2 lenses in sequence produce a result that neither would produce alone.

## Patterns

| Trigger | Action |
|---------|--------|
| Same input needs multiple perspectives | Route to 2+ agent_groups with distinct lenses |
| Generic output without personality | Check if lens is defined |
| Satellite produces unexpected output | Check if lens is aligned with task |
| New agent_group being created | Define lens BEFORE tools and knowledge |
| Pipeline needs progressive refinement | Chain lenses in sequence |

## Anti-Patterns

- Treating lens as descriptive role (it is cognitive, not functional)
- Two agent_groups with identical lenses (total redundancy)
- Omitting lens and depending only on instructions (generic output)
- Changing lens mid-session (perspective incoherence)
- Ignoring prismatic model for multi-perspective tasks

## References

- related: p01_kc_cex_function_become
- related: p01_kc_cex_fractal_architecture
- related: p01_kc_cex_boundary_concept

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_memory_lens]] | downstream | 0.53 |
| [[bld_architecture_lens]] | downstream | 0.52 |
| [[lens-builder]] | downstream | 0.49 |
| [[p03_sp_lens_builder]] | downstream | 0.45 |
| [[p11_qg_lens]] | downstream | 0.44 |
| [[bld_collaboration_lens]] | downstream | 0.42 |
| [[p03_ins_lens]] | downstream | 0.42 |
| [[bld_schema_lens]] | downstream | 0.42 |
| [[bld_tools_lens]] | downstream | 0.41 |
| [[p01_kc_lens]] | sibling | 0.40 |
