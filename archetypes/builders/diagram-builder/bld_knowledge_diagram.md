---
kind: knowledge_card
id: bld_knowledge_card_diagram
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for diagram production — architecture visualization
sources: UML, C4 Model (Brown 2018), Mermaid.js, arc42, ASCII art conventions
quality: 9.1
title: "Knowledge Card Diagram"
version: "1.0.0"
author: n03_builder
tags: [diagram, builder, examples]
tldr: "Golden and anti-examples for diagram construction, demonstrating ideal structure and common pitfalls."
domain: "diagram construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: diagram
## Executive Summary
Diagrams are visual representations of system architecture using ASCII art or Mermaid notation. They answer "how does this look structurally?" — showing components, layers, connections, and boundaries. Diagrams differ from component maps (structured data inventories), patterns (prescriptive solutions), and workflows (execution sequences).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P08 (architecture) |
| Frontmatter fields | 19+ |
| Quality gates | 9 HARD + 10 SOFT |
| Notation formats | ASCII art, Mermaid |
| Zoom levels | system (10+), subsystem (3-10), component (1-3) |
| Required elements | legend, boundary markers, labeled connections |
## Patterns
- **Scope-first**: define what is visualized before drawing — prevents scope creep
- **Zoom level selection**: match detail to audience
| Level | Components | Audience |
|-------|-----------|----------|
| System | 10+ | Newcomers, stakeholders |
| Subsystem | 3-10 | Domain specialists |
| Component | 1-3 | Engineers deep-diving |
- **Notation selection**: choose based on environment
| Notation | Best for | Avoid when |
|----------|----------|------------|
| ASCII | Universal portability, inline docs | Large diagrams (>40 lines) |
| Mermaid | Rendered docs, auto-layout | Plain-text-only environments |
- **Layered separation**: infrastructure, runtime, content, governance on separate visual layers
- **Legend requirement**: every non-obvious symbol must be explained in legend
- **Labeled connections**: arrows without labels are ambiguous — always annotate with relationship type
- **Boundary markers**: dashed lines for system boundaries, solid for component boundaries
| Source | Concept | Application |
|--------|---------|-------------|
| UML | Standard component notation | Structured visual syntax |
| C4 Model | 4-level zoom | zoom_level field selection |
| Mermaid.js | Text-to-diagram rendering | Machine-renderable notation |
| arc42 | Architecture documentation | Scope + boundary approach |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No legend | Readers guess symbol meanings; miscommunication |
| Unlabeled arrows | Ambiguous relationships; "what flows here?" |
| Missing scope definition | Diagram tries to show everything; becomes unreadable |
| Mixed notations | ASCII + Mermaid in same diagram; inconsistent rendering |
| Diagram without accompanying text | Visual alone lacks rationale for design decisions |
| Too many components (>15 per diagram) | Overwhelming; split into zoom levels |
## Application
1. Define scope: what system/subsystem is being visualized
2. Select zoom level: system, subsystem, or component
3. Choose notation: ASCII for portability, Mermaid for rendered docs
4. Draw layers: separate infrastructure, runtime, content, governance
5. Label all connections and add legend for non-obvious symbols
6. Validate: scope is defined, legend present, all arrows labeled
## References
- UML: component and deployment diagram specifications
- Brown 2018: C4 Model for Software Architecture
- Mermaid.js: text-based diagramming and visualization
- arc42: architecture documentation template
