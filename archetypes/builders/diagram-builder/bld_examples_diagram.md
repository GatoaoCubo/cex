---
pillar: P00
id: bld_examples_diagram
kind: examples
builder: diagram-builder
version: 1.0.0
quality: 9.1
title: "Examples Diagram"
author: n03_builder
tags: [diagram, builder, examples]
tldr: "Golden and anti-examples for diagram construction, demonstrating ideal structure and common pitfalls."
domain: "diagram construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
llm_function: GOVERN
---
# diagram-builder — EXAMPLES
## Golden Example
INPUT: "Visualize the CEX agent_group orchestration architecture"
FRONTMATTER (19 fields):
```yaml
id: p08_diag_agent_group_orchestration
kind: diagram
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
domain: "orchestration"
quality: 8.9
tags: [diagram, orchestration, agent_group, architecture, multi-agent]
tldr: "System-level view of orchestrator orchestrating 6 agent_groups via handoffs and signals"
scope: "CEX agent_group orchestration — dispatch to 6 domain agent_groups"
notation: "ascii"
zoom_level: "system"
components: [orchestrator, researcher, marketer, builder, knowledge-engine, executor, monetizer, Brain, Signal_Bus]
connections: ["orchestrator->agent_groups: handoff", "agent_groups->Signal_Bus: complete/error"]
layers: [orchestration, execution, infrastructure]
annotations: ["Max 3 concurrent agent_groups (RAM limit)", "Signal polling every 15s"]
keywords: [orchestration, agent_group, dispatch, signal]
```
## Scope
CEX agent_group orchestration: how orchestrator dispatches tasks to 6 domain agent_groups, monitors progress via signals, and consolidates results. System-level view — not individual agent_group internals.
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
| researcher/marketer/builder/knowledge-engine/executor/monetizer | Domain agent_groups (6) | execution |
| Signal Bus | Event transport — complete/error signals | infrastructure |
| Brain | Knowledge retrieval — BM25 + FAISS | infrastructure |
## Connections
| From | To | Type | Data |
|------|-----|------|------|
| orchestrator | agent_groups | handoff | task + seeds |
| agent_groups | Signal Bus | signal | status + score |
| Signal Bus | orchestrator | poll | completion |
| Brain | all | query | retrieval |
## Annotations
- Max 3 concurrent agent_groups (RAM limit — BSOD if >4)
- Signal poll: 15s
## References
- CLAUDE.md AGENT_GROUPS table
- records/framework/docs/SPAWN_PLAYBOOK.md
WHY GOLDEN: quality null, id pattern valid, 19 fields, scope defined, actual visual, legend + 7 body sections. See QUALITY_GATES.md.
## Anti-Example
INPUT: "Draw the system"
BAD OUTPUT:
```yaml
id: system_diagram
kind: drawing
quality: 8.0
The system has several components that work together.
orchestrator talks to agent_groups. Agent_groups send signals back.
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
