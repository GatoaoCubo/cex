---
kind: collaboration
id: bld_collaboration_component_map
pillar: P12
llm_function: COLLABORATE
purpose: How component-map-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
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
