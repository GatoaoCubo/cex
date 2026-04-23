---
kind: collaboration
id: bld_collaboration_component_map
pillar: P12
llm_function: COLLABORATE
purpose: How component-map-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Component Map"
version: "1.0.0"
author: n03_builder
tags: [component_map, builder, examples]
tldr: "Golden and anti-examples for component map construction, demonstrating ideal structure and common pitfalls."
domain: "component map construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_diagram
  - component-map-builder
  - bld_collaboration_builder
  - p03_sp_component_map_builder
  - bld_collaboration_dispatch_rule
  - bld_collaboration_dag
  - bld_architecture_kind
  - bld_collaboration_interface
  - bld_collaboration_context_doc
  - bld_collaboration_memory_scope
---

# Collaboration: component-map-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the parts of this system and how do they connect?"
I do not visualize diagrams. I do not prescribe solutions.
I inventory components structurally so architects can understand system topology.
## Crew Compositions
### Crew: "Architecture Documentation"
```
  1. component-map-builder -> "structured inventory of components and connections"
  2. diagram-builder -> "visual representation of the architecture"
  3. context-doc-builder -> "domain context for stakeholders"
```
### Crew: "System Analysis"
```
  1. component-map-builder -> "component inventory with dependencies"
  2. interface-builder -> "formal contracts between components"
  3. dag-builder -> "execution dependency graph"
```
## Handoff Protocol
### I Receive
- seeds: system name, scope boundary, component list or discovery criteria
- optional: existing architecture docs, ownership mapping, health status
### I Produce
- component_map artifact (.md + .yaml frontmatter)
- committed to: `cex/P08/examples/p08_component_map_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Component maps start from system analysis.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| diagram-builder | Visualizes the component inventory as architecture diagrams |
| interface-builder | Defines contracts between mapped components |
| dag-builder | Models execution dependencies between mapped components |
| dispatch-rule-builder | Routes tasks to components identified in the map |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_diagram]] | sibling | 0.48 |
| [[component-map-builder]] | upstream | 0.44 |
| [[bld_collaboration_builder]] | sibling | 0.40 |
| [[p03_sp_component_map_builder]] | upstream | 0.40 |
| [[bld_collaboration_dispatch_rule]] | sibling | 0.39 |
| [[bld_collaboration_dag]] | sibling | 0.39 |
| [[bld_architecture_kind]] | upstream | 0.36 |
| [[bld_collaboration_interface]] | sibling | 0.35 |
| [[bld_collaboration_context_doc]] | sibling | 0.33 |
| [[bld_collaboration_memory_scope]] | sibling | 0.33 |
