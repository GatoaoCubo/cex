---
kind: quality_gate
id: p01_qg_graph_rag_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for graph_rag_config
quality: 9.0
title: "Quality Gate Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for graph_rag_config"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_graph_rag_config
  - graph-rag-config-builder
  - bld_collaboration_knowledge_graph
  - kc_graph_rag_config
  - p03_sp_graph_rag_config_builder
  - knowledge-graph-builder
  - bld_instruction_graph_rag_config
  - p01_kc_knowledge_graph
  - bld_architecture_knowledge_graph
  - p10_mem_graph_rag_config_builder
---

## Quality Gate

## Definition
(Table: metric, threshold, operator, scope)
| metric | threshold | operator | scope |
|---|---|---|---|
| Schema Validity | 1 | equals | All files |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML frontmatter |
| H02 | ID matches pattern ^p01_grc_[a-z][a-z0-9_]+.yaml$ | ID does not match schema pattern |
| H03 | kind field matches 'graph_rag_config' | kind field not 'graph_rag_config' |
| H04 | graph_type field present | Missing graph_type |
| H05 | embedding_model field valid | Invalid or missing embedding_model |
| H06 | retrieval_strategy field valid | Invalid or missing retrieval_strategy |
| H07 | knowledge_sources field present | Missing knowledge_sources |
| H08 | query_transformer field valid | Invalid or missing query_transformer |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Schema Completeness | 0.20 | 100% required fields present |
| D02 | Configuration Validity | 0.20 | Valid parameters and values |
| D03 | Graph Model Fidelity | 0.15 | Correct community detection and entity extraction config |
| D04 | Retrieval Strategy Quality | 0.15 | Multi-hop, hybrid vector+graph strategy defined |
| D05 | Scalability | 0.10 | Configurable traversal depth and query latency thresholds |
| D06 | Usability | 0.10 | Clear documentation and parameters |
| D07 | Documentation | 0.10 | Usage guides and examples present |

## Actions
| Score | Action |
|---|---|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |

## Bypass
(Table: conditions, approver, audit trail)
| conditions | approver | audit trail |
|---|---|---|
| Critical production issue requiring immediate deployment | CTO | Change management system log |

## Examples

## Golden Example
```markdown
---
title: "Graph RAG Configuration for Legal Document Analysis"
kind: graph_rag_config
---
**Graph Database**: Neo4j (version 5.19.0)
**Vector Store**: Pinecone (index: "legal-docs-2024")
**RAG Components**:
- **LLM**: GPT-4 (OpenAI) for query refinement and answer generation
- **Graph Traversal**: BFS with depth limit 3 for entity relationship exploration
- **Node Types**:
  - `Case`: Properties include `case_id`, `court`, `date`
  - `Entity`: Properties include `name`, `type` (person, organization)
  - `Citation`: Links `Case` nodes via `CITES` relationships
**Edge Types**:
- `RELATED_TO`: Connects entities mentioned in the same document
- `REFERRED_IN`: Links cases to cited legal precedents
**Query Flow**:
1. User input → 2. Vector search in Pinecone → 3. Graph traversal → 4. LLM answer synthesis
**Traversal Constraints**:
- Max hops: 3
- Filter: Only include nodes with `relevance_score > 0.7`
```

## Anti-Example 1: Confusing config with knowledge graph data
```markdown
---
title: "Legal Knowledge Graph"
kind: graph_rag_config
---
**Nodes**:
- `Case_1234`: {court: "Supreme Court", date: "2022-05-15"}
- `Entity_5678`: {name: "John Doe", type: "person"}
**Edges**:
- `Case_1234` --[CITES]--> `Case_9876`
## Why it fails
This example describes actual graph data (nodes/edges) instead of the architecture configuration. It violates the boundary by acting as a knowledge graph instance rather than defining how the RAG system interacts with the graph.
```

## Anti-Example 2: Missing critical components
```markdown
---
title: "Minimal Graph RAG Setup"
kind: graph_rag_config
---
**Graph Database**: Neo4j
**Vector Store**: Not specified
**Traversal**: DFS without depth limits
## Why it fails
The configuration omits essential components like the vector store integration and lacks explicit RAG pipeline details. Without a defined vector store and traversal constraints, the system cannot effectively retrieve or synthesize answers from the graph.
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
