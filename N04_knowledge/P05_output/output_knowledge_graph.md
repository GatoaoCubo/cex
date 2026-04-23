---
id: p10_out_knowledge_graph
kind: output
pillar: P10
title: "Output: Knowledge Graph"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.1
tags: [output, n04, knowledge-graph, entity, relationship, visualization]
tldr: "Entity-relationship map of KCs: nodes (KCs) + edges (feeds_kinds, linked_artifacts)."
density_score: 0.91
related:
  - p06_arch_knowledge_graph
  - bld_collaboration_knowledge_graph
  - bld_architecture_kind
  - bld_collaboration_kind
  - p10_out_taxonomy_map
  - bld_examples_graph_rag_config
  - p10_entity_cex_system
  - p10_out_gap_report
  - bld_instruction_kind
  - p01_kc_knowledge_card
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

## Usage Patterns

| Scenario | When to use | Output focus |
|----------|-------------|--------------|
| Nucleus handoff | N04 → N07 knowledge map | Cluster density + missing links |
| Builder discovery | Find related KCs for artifact | Kind KC → Domain KC paths |
| Quality audit | Check KC coverage gaps | Entity types + orphaned nodes |
| RAG optimization | Identify retrieval clusters | High-edge-count subgraphs |

## Anti-Patterns

| DON'T | WHY | DO instead |
|-------|-----|-----------|
| Map all 2184 KCs at once | Cognitive overload | Focus on 1 domain cluster (≤20 nodes) |
| Show every relationship | Visual noise | Filter by relationship strength |
| Generate without purpose | Wasted computation | Target specific gap analysis |
| Static snapshots | Stale quickly | Live queries via cex_retriever.py |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_arch_knowledge_graph]] | upstream | 0.29 |
| [[bld_collaboration_knowledge_graph]] | downstream | 0.29 |
| [[bld_architecture_kind]] | upstream | 0.27 |
| [[bld_collaboration_kind]] | downstream | 0.23 |
| [[p10_out_taxonomy_map]] | sibling | 0.23 |
| [[bld_examples_graph_rag_config]] | upstream | 0.22 |
| [[p10_entity_cex_system]] | related | 0.21 |
| [[p10_out_gap_report]] | sibling | 0.21 |
| [[bld_instruction_kind]] | upstream | 0.21 |
| [[p01_kc_knowledge_card]] | upstream | 0.21 |
