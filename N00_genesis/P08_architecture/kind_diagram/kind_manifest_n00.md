---
id: n00_diagram_manifest
kind: knowledge_card
pillar: P08
nucleus: n00
title: "Diagram -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, diagram, p08, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P08 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A diagram is an architecture diagram rendered in ASCII or Mermaid syntax that visually communicates system topology, data flow, or process sequences. It is injected into builder context (F3 INJECT) to give nuclei a spatial understanding of the system before making structural changes, and is included in documentation for human readers.

## Pillar
P08 -- architecture

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `diagram` |
| pillar | string | yes | Always `P08` |
| title | string | yes | Human-readable diagram name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| diagram_type | enum | yes | flowchart \| sequence \| class \| state \| component \| er |
| format | enum | yes | mermaid \| ascii \| plantuml |
| scope | string | yes | What system or subsystem this depicts |
| body | string | yes | The actual diagram source code |
| description | string | no | Plain-text explanation of the diagram |

## When to use
- Documenting the flow between nuclei during a multi-wave mission
- Visualizing the 8F pipeline or composable-crew topology
- Illustrating data flow through the RAG or memory stack

## Builder
`archetypes/builders/diagram-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind diagram --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: diagram_8f_pipeline
kind: diagram
pillar: P08
nucleus: n03
title: "8F Pipeline Flow"
version: 1.0
quality: null
---
diagram_type: flowchart
format: mermaid
scope: 8F reasoning pipeline
body: |
  graph LR
    F1[CONSTRAIN] --> F2[BECOME] --> F3[INJECT]
    F3 --> F4[REASON] --> F5[CALL] --> F6[PRODUCE]
    F6 --> F7[GOVERN] --> F8[COLLABORATE]
```

## Related kinds
- `component_map` (P08) -- structured data that this diagram visualizes
- `dual_loop_architecture` (P08) -- complex control flows that benefit from diagrams
- `workflow` (P12) -- process flows that diagrams help document
