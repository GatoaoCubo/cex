---
kind: examples
id: bld_examples_graph_rag_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of graph_rag_config artifacts
quality: 9.0
title: "Examples Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, examples]
tldr: "Golden and anti-examples of graph_rag_config artifacts"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
