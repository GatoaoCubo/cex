---
id: diagram-builder-memory
kind: memory
builder: diagram-builder
version: 1.0.0
---

# diagram-builder — MEMORY

## Common Mistakes

| # | Mistake | Gate | Fix |
|---|---------|------|-----|
| 1 | quality set to a number instead of null | H05 | Always null — never score yourself |
| 2 | Body is prose instead of actual visual | S05 | Draw actual ASCII/Mermaid characters |
| 3 | No legend — symbols unexplained | S04 | Always include Legend section |
| 4 | Mixing ASCII and Mermaid in same diagram | H09 | Pick one notation, stay consistent |
| 5 | Confusing diagram with component_map | boundary | Ask: "visual or data inventory?" |
| 6 | Components unlabeled or ambiguous | S03 | Every box gets a name and brief role |
| 7 | Scope too broad — trying to show everything | S08 | Pick zoom level, cut to fit |
| 8 | zoom_level missing | S02 | Always specify: system/subsystem/component |
| 9 | id missing `p08_diag_` prefix | H02 | Pattern: `p08_diag_{scope_slug}` |
| 10 | Diagram too large (>4096 bytes) | constraint | Zoom in or split into two diagrams |

## Visualization Pattern Catalog

| Domain | Common diagrams | Key boundary |
|--------|----------------|-------------|
| Orchestration | Satellite dispatch, signal flow, wave execution | vs workflow (P12) |
| Knowledge | Ingestion pipeline, brain architecture, index flow | vs dag (P12) |
| Infrastructure | Boot sequence, MCP connections, spawn lifecycle | vs component_map (P08) |
| Governance | Quality gate flow, review chain, scoring pipeline | vs law (P08) |
| Content | Pillar structure, artifact relationships, layer map | vs satellite_spec (P08) |

## ASCII Box-Drawing Quick Reference

| Symbol | Use |
|--------|-----|
| `┌─────┐` | Box top |
| `│     │` | Box side |
| `└─────┘` | Box bottom |
| `→` `←` | Horizontal flow |
| `▼` `▲` | Vertical flow |
| `├` `┤` | Branch join |
| `┬` `┴` | T-junction |
| `┼` | Cross junction |

## Mermaid Quick Reference

```
graph TD
  A[Component A] --> B[Component B]
  B -->|label| C[Component C]
  subgraph Layer
    D[Inner]
  end
```

## Production Counter

0 artifacts produced.
