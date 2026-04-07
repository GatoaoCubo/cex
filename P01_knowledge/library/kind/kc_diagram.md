---
id: p01_kc_diagram
kind: knowledge_card
type: kind
pillar: P08
title: "Diagram — Deep Knowledge for diagram"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: diagram
quality: 9.1
tags: [diagram, P08, INJECT, kind-kc, architecture]
tldr: "diagram is a versioned visual representation of architecture in ASCII or Mermaid — terminal-safe, diff-friendly, and auto-decaying-resistant unlike binary image formats."
when_to_use: "Building, reviewing, or reasoning about diagram artifacts"
keywords: [architecture_diagram, mermaid, ASCII_art]
feeds_kinds: [diagram]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
---

# Diagram

## Spec
```yaml
kind: diagram
pillar: P08
llm_function: INJECT
max_bytes: 4096
naming: p08_diag_{{scope}}.md
core: false
```

## What It Is
A diagram is a visual architecture representation in ASCII or Mermaid syntax — showing system structure, data flow, or interaction sequences. It is NOT a component_map (structured YAML data about connections), NOT a pattern (which prescribes a reusable solution without visualization as its primary purpose).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | LCEL chain diagrams | Runnable \| Runnable \| Runnable ASCII flow |
| LlamaIndex | Workflow event diagrams | StartEvent → Step → StopEvent flows |
| CrewAI | Crew process diagrams | Sequential/hierarchical agent flow visualization |
| DSPy | Module forward() data flow | Input → ChainOfThought → Output data path |
| Haystack | Pipeline DAG | Component boxes with connect() arrows, official viz |
| OpenAI | Assistants API flow | User → Thread → Run → tool_calls loop diagram |
| Anthropic | Agentic loop diagram | Request → tool_use → tool_result → repeat cycle |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| format | enum | ascii | ascii (always renders) vs mermaid (needs renderer) |
| scope | string | required | system/agent_group/flow — tighter scope = clearer diagram |
| direction | enum | LR | LR (left-right) for flows; TB (top-bottom) for hierarchy |
| detail_level | enum | medium | low (overview) / medium (standard) / high (all edges) |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| System overview | Top-level agent_group interconnect | ASCII boxes + labeled arrows between orchestrator/research_agent/operations_agent |
| Flow diagram | Step-by-step execution path | Mermaid flowchart LR for spawn → execute → signal |
| Sequence diagram | Time-ordered message exchange | Mermaid sequenceDiagram for TSP handshake |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| PNG/SVG in repo | Binary diagrams go stale, can't diff, bloat git | Use ASCII or Mermaid text only |
| No legend | Unlabeled shapes are ambiguous to new readers | Always include node type legend |
| Mixed detail levels | Mixing system + component detail confuses scope | Split into separate diagrams per level |

## Integration Graph
```
component_map, agent_card --> [diagram] --> decision_record, pattern
                                   |
                              workflow, law, context_doc
```

## Decision Tree
- IF terminal-only audience or README rendering THEN ASCII diagram
- IF GitHub/Notion rendered markdown viewer THEN Mermaid flowchart
- IF timing or sequence is critical THEN Mermaid sequenceDiagram
- DEFAULT: ASCII for static architecture, Mermaid for dynamic flows

## Quality Criteria
- GOOD: format specified, scope labeled, all nodes named, direction set
- GREAT: legend included, direction optimized for content type, linked to component_map
- FAIL: binary image format (PNG/SVG), no labels on nodes or edges, undefined scope
