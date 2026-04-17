---
kind: schema
id: bld_schema_graph_rag_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for graph_rag_config
quality: 9.1
title: "Schema Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for graph_rag_config"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field      | Type        | Required | Default | Notes                              |  
|------------|-------------|----------|---------|------------------------------------|  
| id         | string      | yes      | null    | Must match ID Pattern              |  
| kind       | string      | yes      | null    | Always `graph_rag_config`          |  
| pillar     | string      | yes      | null    | Always `P01`                       |  
| title      | string      | yes      | null    | Human-readable config name         |  
| version    | string      | yes      | null    | Semantic version (e.g., `1.0.0`)   |  
| created    | datetime    | yes      | null    | ISO 8601 timestamp                 |  
| updated    | datetime    | yes      | null    | ISO 8601 timestamp                 |  
| author     | string      | yes      | null    | Creator’s identifier               |  
| domain     | string      | yes      | null    | Always `graph_rag`                 |  
| quality    | null        | yes      | null    | Never self-score; peer review assigns |  
| tags       | array       | yes      | null    | Keywords (e.g., `ontology`, `llm`) |  
| tldr       | string      | yes      | null    | One-sentence config summary        |  
| graph_type | string      | yes      | null    | E.g., `knowledge`, `ontology`      |  
| embedding_model | string | yes      | null    | Model name (e.g., `bert-base`)     |  

### Recommended  
| Field         | Type    | Notes                  |  
|---------------|---------|------------------------|  
| description   | string  | Detailed config purpose|  
| source        | string  | Origin of config data  |  
| license       | string  | Usage permissions      |  
| deprecated    | boolean | Mark if obsolete       |  

## ID Pattern  
^p01_grc_[a-z][a-z0-9_]+.yaml$  

## Body Structure  
1. **Graph Type Configuration**  
   Define graph structure (e.g., directed/undirected).  
2. **Embedding Model Settings**  
   Parameters for embedding generation (e.g., dimensionality).  
3. **RAG Strategy Parameters**  
   Rules for retrieval-augmented generation (e.g., top-k results).  
4. **Indexing Options**  
   Indexing method (e.g., FAISS, HNSW).  
5. **Query Optimization Rules**  
   Constraints for query processing (e.g., max hops).  

## Constraints  
- ID must match ^p01_grc_[a-z][a-z0-9_]+.yaml$  
- Max file size: 4096 bytes  
- `graph_type` must be one of: `knowledge`, `ontology`, `network`  
- `embedding_model` must reference a registered model  
- `version` must follow semantic versioning (X.Y.Z)  
- `quality` field must be assigned by peer review, not self-assigned
