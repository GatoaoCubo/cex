---
kind: architecture
id: bld_architecture_diagram
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of diagram — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Diagram"
version: "1.0.0"
author: n03_builder
tags: [diagram, builder, examples]
tldr: "Golden and anti-examples for diagram construction, demonstrating ideal structure and common pitfalls."
domain: "diagram construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| notation_format | Output format: ASCII art or Mermaid syntax | diagram-builder | required |
| diagram_type | Classification: flow, layered, dependency, sequence, topology | diagram-builder | required |
| visual_body | The rendered diagram content (ASCII block or Mermaid code) | diagram-builder | required |
| legend | Key explaining symbols, line styles, and node types used | diagram-builder | required |
| layer_boundaries | Explicit visual separators between architectural layers | diagram-builder | required |
| annotations | Inline labels explaining non-obvious connections or components | diagram-builder | optional |
| source_reference | Pointer to the component_map or pattern being visualized | diagram-builder | optional |
| metadata | diagram id, version, scope, author, created date | diagram-builder | required |
| alt_text | Plain-language description for accessibility and indexing | diagram-builder | optional |
## Dependency Graph
```
component_map (P08) --provides_data--> diagram (structured inventory becomes visual)
pattern (P08) --illustrated_by--> diagram (pattern solution may be shown visually)
law (P08) --illustrated_by--> diagram (enforcement flow may be diagrammed)
diagram --produces_for--> documentation (external consumers: docs, READMEs, specs)
diagram --referenced_by--> agent_card (P08) (specs may embed diagram reference)
knowledge_index (P10) --indexes--> diagram (stored and retrieved via semantic search)
signal (P12) --independent-- diagram (diagram is static, not runtime)
connector (P04) --independent-- diagram (diagram visualizes, does not integrate)
```
| From | To | Type | Data |
|------|----|------|------|
| component_map | diagram | data_flow | component names, roles, relationships |
| pattern | diagram | data_flow | solution structure to visualize |
| law | diagram | data_flow | enforcement flow to illustrate |
| diagram | documentation | produces | visual representation for human readers |
| diagram | agent_card | referenced_by | spec cites diagram for structure overview |
| knowledge_index | diagram | indexes | diagram stored for semantic retrieval |
## Boundary Table
| diagram IS | diagram IS NOT |
|------------|----------------|
| A visual representation: shows structure as ASCII or Mermaid | A component_map — component_map is structured tabular inventory, not visual |
| Communicates architecture to human readers | A pattern — pattern prescribes a reusable solution approach |
| Derived from structured data (component_map, pattern) | A law — law mandates behavior rules and constraints |
| Static artifact: created once, consumed by documentation | A dag — dag defines execution ordering, not visual structure |
| Includes legend, layer boundaries, and annotations | A workflow — workflow executes sequences at runtime |
| Supports two notations: ASCII (portable) and Mermaid (renderable) | A agent_card — agent_card defines a component, diagram shows the system |
| Indexed and retrievable via semantic search | A signal — signals are runtime events, diagrams are authoring-time artifacts |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Input | component_map, pattern, law | Source data and structure that the diagram visualizes |
| Authoring | notation_format, diagram_type, metadata | Define what kind of diagram to produce and how |
| Visual Content | visual_body, layer_boundaries, annotations | The actual rendered diagram with structural markup |
| Readability | legend, alt_text | Aid interpretation for human readers and search indexers |
| Reference | source_reference | Trace diagram back to its authoritative source artifact |
| Distribution | documentation, agent_card, knowledge_index | Consumers that embed, reference, or index the diagram |
