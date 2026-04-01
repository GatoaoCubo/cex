---
id: "p08_diag_{{SCOPE_SLUG}}"
kind: diagram
pillar: P08
version: 1.0.0
title: Template - Diagram
tags: [template, diagram, visual, mermaid, ascii]
tldr: Visual diagram (Mermaid or ASCII) showing structure, data flow, or sequences. Embedded in markdown.
quality: 8.6
---

# Diagram: [NAME]

## Purpose
[WHAT this diagram does]
## Diagram Types
| Type | Syntax | Best For |
|------|--------|----------|
| Flowchart | `graph TD` | Process flow |
| Sequence | `sequenceDiagram` | API calls |
| Class | `classDiagram` | Data models |
| State | `stateDiagram-v2` | Lifecycle |
## Example
```mermaid
graph LR
    A[Intent] --> B[F1]
    B --> C[F2]
    C --> D[F3]
    D --> E[F6]
    E --> F{F7}
    F -->|pass| G[F8]
    F -->|fail| E
```
## ASCII Fallback
```
Intent -> [F1] -> [F2] -> [F3] -> [F6] -> [F7] -> [F8]
                                     ^       |fail
                                     +-------+
```
## Quality Gate
- [ ] Diagram has title
- [ ] Arrows are labeled
- [ ] Both Mermaid + ASCII provided
- [ ] Matches textual description
