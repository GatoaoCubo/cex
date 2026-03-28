---
id: diagram-builder-examples
kind: examples
builder: diagram-builder
version: 1.0.0
---

# diagram-builder — EXAMPLES

## Golden Example

INPUT: "Visualize the CEX satellite orchestration architecture"

FRONTMATTER (19 fields):
```yaml
---
id: p08_diag_satellite_orchestration
kind: diagram
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
domain: "orchestration"
quality: null
tags: [diagram, orchestration, satellite, architecture, multi-agent]
tldr: "System-level view of orchestrator orchestrating 6 satellites via handoffs and signals"
scope: "CEX satellite orchestration — orchestrator dispatch to 6 domain satellites"
notation: "ascii"
zoom_level: "system"
components: [orchestrator, researcher, marketer, builder, knowledge-engine, executor, monetizer, Brain, Signal_Bus]
connections: ["orchestrator->satellites: handoff", "satellites->Signal_Bus: complete/error"]
layers: [orchestration, execution, infrastructure]
annotations: ["Max 3 concurrent satellites (RAM limit)", "Signal polling every 15s"]
keywords: [orchestration, satellite, dispatch, signal]
---
```

## Scope
CEX satellite orchestration: how orchestrator dispatches tasks to 6 domain satellites, monitors progress via signals, and consolidates results. System-level view — not individual satellite internals.

## Diagram
```text
          ┌─────────┐
          │ orchestrator  │ (orchestrator)
          └────┬────┘
               │ handoffs
    ┌──┬──┬────┼────┬──┬──┐
    ▼  ▼  ▼    ▼    ▼  ▼  ▼
 [researcher][marketer][builder][knowledge-engine][executor][monetizer]
    └──┴──┴────┬────┴──┴──┘
               ▼
        ┌────────────┐
        │ Signal Bus │ (complete/error)
        └──────┬─────┘
               │ poll 15s
               ▼
        ┌────────────┐
        │   Brain    │ (BM25+FAISS)
        └────────────┘
```

## Legend
- `┌──────┐` = system component
- `▼` / `│` = control/data flow direction
- Solid lines = direct communication channel
- Names inside boxes = component identity + domain

## Components
| Component | Role | Layer |
|-----------|------|-------|
| orchestrator | Orchestrator — decomposes, dispatches, monitors | orchestration |
| researcher/marketer/builder/knowledge-engine/executor/monetizer | Domain satellites (6) | execution |
| Signal Bus | Event transport — complete/error signals | infrastructure |
| Brain | Knowledge retrieval — BM25 + FAISS | infrastructure |

## Connections
| From | To | Type | Data |
|------|-----|------|------|
| orchestrator | satellites | handoff | task + seeds |
| satellites | Signal Bus | signal | status + score |
| Signal Bus | orchestrator | poll | completion |
| Brain | all | query | retrieval |

## Annotations
- Max 3 concurrent satellites (RAM limit — BSOD if >4)
- Signal poll: 15s

## References
- CLAUDE.md SATELLITES table
- records/framework/docs/SPAWN_PLAYBOOK.md

WHY GOLDEN: quality null, id pattern valid, 19 fields, scope defined, actual visual, legend + 7 body sections. See QUALITY_GATES.md.

---

## Anti-Example

INPUT: "Draw the system"

BAD OUTPUT:
```yaml
---
id: system_diagram
kind: drawing
quality: 8.0
---

The system has several components that work together.
orchestrator talks to satellites. Satellites send signals back.
```

FAILURES:
1. id `system_diagram` has no `p08_diag_` prefix -> H02 FAIL
2. kind: "drawing" not "diagram" -> H04 FAIL
3. quality: 8.0 (self-assigned number) -> H05 FAIL
4. Missing: pillar, version, created, updated, author, domain, tags, tldr, scope, notation, zoom_level, components -> H06 FAIL
5. notation not specified -> H09 FAIL
6. No actual diagram in body — only prose description -> S05 FAIL
7. No Legend section -> S04 FAIL
8. Body is filler prose ("several components", "work together") -> S08 FAIL
9. No Components table -> S03 FAIL
10. No body sections: Scope, Diagram, Legend, Components, Connections, Annotations, References -> S07 FAIL
