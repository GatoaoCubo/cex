---
id: "p08_diag_{{SCOPE_SLUG}}"
kind: diagram
8f: F4_reason
pillar: P08
version: 1.0.0
title: Template - Diagram
tags: [template, diagram, visual, mermaid, ascii]
tldr: Visual diagram (Mermaid or ASCII) showing structure, data flow, or sequences. Embedded in markdown.
quality: 9.0
updated: "2026-04-07"
domain: "system architecture"
author: n03_builder
created: "2026-04-07"
density_score: 0.97
related:
  - bld_architecture_diagram
  - p01_kc_diagram
  - p11_qg_diagram
  - diagram-builder
  - bld_collaboration_diagram
  - bld_config_diagram
  - bld_instruction_diagram
  - p03_sp_diagram_builder
  - bld_knowledge_card_diagram
  - bld_tools_diagram
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
1. [ ] Diagram has title
2. [ ] Arrows are labeled
3. [ ] Both Mermaid + ASCII provided
4. [ ] Matches textual description

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `diagram` |
| Pillar | P08 |
| Domain | system architecture |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_diagram]] | related | 0.49 |
| [[p01_kc_diagram]] | related | 0.48 |
| [[p11_qg_diagram]] | downstream | 0.47 |
| [[diagram-builder]] | related | 0.45 |
| [[bld_collaboration_diagram]] | downstream | 0.43 |
| [[bld_config_diagram]] | related | 0.42 |
| [[bld_instruction_diagram]] | related | 0.42 |
| [[p03_sp_diagram_builder]] | upstream | 0.34 |
| [[bld_knowledge_card_diagram]] | upstream | 0.32 |
| [[bld_tools_diagram]] | related | 0.28 |
