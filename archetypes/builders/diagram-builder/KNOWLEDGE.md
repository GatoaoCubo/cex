---
id: diagram-builder-knowledge
kind: knowledge
builder: diagram-builder
version: 1.0.0
---

# diagram-builder — KNOWLEDGE

## Foundational

Architecture diagrams trace to engineering blueprints — visual representations of structure to communicate design. In software: UML (1997), C4 model (Brown 2018), arc42, and informal ASCII/Mermaid. A diagram answers "how does this look?" not "what should it do?" or "what parts exist?"

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| UML Component Diagram | Standard component notation | Structured visual syntax |
| C4 Model (Brown 2018) | 4-level zoom: Context/Container/Component/Code | zoom_level field |
| Mermaid.js | Text-to-diagram rendering | Machine notation format |
| arc42 | Architecture documentation template | Scope + boundary approach |
| ASCII art | Universal plain-text visualization | Portable, no tooling required |
| CEX Diagrams | Agent architecture visualization | Domain: multi-satellite system |

## Key Patterns

| Pattern | Rule |
|---------|------|
| SCOPE-FIRST | Define what is visualized before drawing |
| LAYERED | Separate concerns: infra, runtime, content, governance |
| LEGEND | Every non-obvious symbol explained |
| ZOOM | Specify level: system, subsystem, component |
| NOTATION | Consistent within diagram — no mixing |
| CONNECTIONS | Label arrows with relationship type |
| ANNOTATIONS | Explain non-obvious design decisions inline |
| BOUNDARY | Dashed lines for system boundaries |

## Zoom Level Guide

| Level | Components | When to use |
|-------|-----------|-------------|
| system | 10+ components | Full-system overview for newcomers |
| subsystem | 3-10 components | One domain or pillar in detail |
| component | 1-3 components | Deep dive into one component's internals |

## Notation Choice Guide

| Notation | Best for | Avoid when |
|----------|----------|------------|
| ascii | Universal portability, inline in docs, no tool dependency | Large diagrams (>40 lines get unreadable) |
| mermaid | Rendered docs, auto-layout, flowcharts | Plain-text-only environments |

## Boundary vs Nearby Types

| Type | What it is | Why NOT diagram |
|------|------------|-----------------|
| component_map (P08) | Structured inventory | Maps INVENTORY data; diagrams SHOW visually |
| pattern (P08) | Reusable solution | Patterns PRESCRIBE; diagrams DEPICT |
| law (P08) | Operational mandate | Laws GOVERN; diagrams ILLUSTRATE |
| satellite_spec (P08) | Component specification | Specs DEFINE one; diagrams SHOW many |
| workflow (P12) | Execution sequence | Workflows EXECUTE; diagrams REPRESENT |
| dag (P12) | Dependency graph | DAGs define EXECUTION order; diagrams show STRUCTURE |

## CEX Architecture Domains

| Domain | Common diagram types |
|--------|---------------------|
| Orchestration | Satellite dispatch, signal flow, wave execution |
| Knowledge | Ingestion pipeline, brain architecture, index flow |
| Infrastructure | Boot sequence, MCP connections, spawn lifecycle |
| Governance | Quality gate flow, review chain, scoring pipeline |
| Content | Pillar structure, artifact relationships, layer map |
