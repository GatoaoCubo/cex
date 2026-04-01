---
id: p10_out_knowledge_graph
kind: output
pillar: P10
title: "Output: Knowledge Graph"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: null
tags: [output, n04, knowledge-graph, entity, relationship, visualization]
tldr: "Entity-relationship map of KCs: nodes (KCs) + edges (feeds_kinds, linked_artifacts)."
density_score: 0.91
---

# Output: Knowledge Graph

## Template
```markdown
# Knowledge Graph: {{DOMAIN}}
**Nodes**: {{KC_COUNT}} | **Edges**: {{LINK_COUNT}} | **Date**: {{DATE}}

## Entity Types
| Type | Count | Example |
|------|-------|---------|
| Kind KC | {{N}} | kc_agent, kc_workflow |
| Domain KC | {{N}} | kc_chain_of_thought |
| Platform KC | {{N}} | kc_supabase |

## Key Relationships
| From | → | To | Relationship |
|------|---|-----|-------------|
| kc_agent | feeds | agent-builder | Kind KC → Builder |
| kc_tool_use | links | kc_mcp_server_patterns | Domain cross-ref |

## Clusters (densely connected groups)
1. **LLM Patterns**: CoT ↔ self-healing ↔ autonomy ↔ refinement
2. **Operations**: zero-touch ↔ error-recovery ↔ quality-gates ↔ testing
3. **Brand**: archetypes ↔ voice ↔ visual ↔ positioning
```
