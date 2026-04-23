---
kind: collaboration
id: bld_collaboration_diagram
pillar: P12
llm_function: COLLABORATE
purpose: How diagram-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Diagram"
version: "1.0.0"
author: n03_builder
tags: [diagram, builder, examples]
tldr: "Golden and anti-examples for diagram construction, demonstrating ideal structure and common pitfalls."
domain: "diagram construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Collaboration: diagram-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how does this system look structurally?"
I do not inventory data. I do not prescribe solutions.
I visualize architecture so stakeholders can understand system structure at a glance.
## Crew Compositions
### Crew: "Architecture Documentation"
```
  1. component-map-builder -> "structured component inventory"
  2. diagram-builder -> "visual architecture diagram (ASCII/Mermaid)"
  3. context-doc-builder -> "domain context for documentation"
```
### Crew: "System Overview"
```
  1. dag-builder -> "dependency graph data"
  2. diagram-builder -> "visual representation of dependencies"
  3. glossary-entry-builder -> "legend terms and definitions"
```
## Handoff Protocol
### I Receive
- seeds: system name, components to visualize, diagram type (flow, layered, sequence)
- optional: component-map output, notation preference (ASCII, Mermaid), layer boundaries
### I Produce
- diagram artifact (.md with ASCII or Mermaid notation)
- committed to: `cex/P08/examples/p08_diagram_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- component-map-builder: provides structured data to visualize
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| context-doc-builder | May embed diagrams in domain documentation |
| knowledge-card-builder | May reference diagrams for visual context |
