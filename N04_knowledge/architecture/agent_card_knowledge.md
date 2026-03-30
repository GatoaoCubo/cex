---
id: n04_ac_knowledge
kind: agent_card
pillar: P08_architecture
version: "2.0.0"
created: "2024-03-30"
updated: "2024-03-30"
author: "N04 Knowledge Nucleus"
name: "N04 Knowledge Nucleus"
role: "The core agent for the CEX knowledge lifecycle, managing ingestion, semantic indexing, RAG, and taxonomy."
model: "gemini-2.5-pro"
mcps: [vector_db, document_loaders, embedding_apis]
domain_area: "knowledge-management-rag"
boot_sequence:
  - "LOAD_IDENTITY (n04_agent_knowledge)"
  - "LOAD_SYSTEM_PROMPT (n04_sp_knowledge)"
  - "INITIALIZE_TOOLS (semantic_search, knowledge_graph_builder, consolidate)"
  - "CONNECT_MCPS (vector_db, embedding_apis)"
  - "AWAIT_DISPATCH"
constraints:
  - "NEVER operate outside the knowledge architecture domain."
  - "NEVER respond without citing sources from the knowledge base."
  - "ALWAYS prioritize retrieval accuracy and data integrity."
dispatch_keywords": [knowledge, rag, index, search, distill, taxonomy, embed, chunk]
tools: [chunk_optimizer, semantic_search, knowledge_graph_builder, consolidate]
dependencies: [N03_engineering, P01_knowledge]
scaling:
  max_concurrent: 5
  timeout_minutes: 60
  memory_limit_mb: 8192
monitoring:
  health_check: "self_diagnose(test_query='what is RAG?')"
  signal_on_complete: true
  alert_on_failure: true
runtime: "gemini-cli"
mcp_config_file: ".mcp-n04.json"
flags: ["--large-context-window", "--high-accuracy-retrieval"]
domain: "RAG, Knowledge Graphs, Semantic Search, Taxonomy"
quality: null
tags: [agent_card, n04, knowledge, architecture, p08]
tldr: "Deployment specification for the N04 Knowledge Nucleus, running on Gemini 2.5-pro."
---

## Role
The N04 Knowledge Nucleus is the specialized agent responsible for the end-to-end CEX knowledge pipeline. It architects and maintains the systems for data ingestion, processing, indexing, and retrieval, forming the foundation of the CEX RAG strategy.

## Model & Runtime
- **Model**: `gemini-2.5-pro`
  - **Reasoning**: Chosen for its massive 1M context window, ideal for large-scale document ingestion and synthesis, and its advanced reasoning for architectural tasks. Accessed via a Google subscription.
- **Runtime**: `gemini-cli`
  - **Reasoning**: The native command-line interface for interacting with the Gemini model, providing the necessary control and scripting capabilities for an agent of this type.

## MCPs & Tools (Future State)
N04's capabilities will be augmented by a suite of specialized Micro-Capability Products (MCPs) and internal tools.
- **MCPs**:
  - `vector_db`: A dedicated vector database for storing and querying billions of embeddings at scale.
  - `document_loaders`: A collection of connectors for ingesting data from diverse sources (e.g., git repositories, websites, Notion).
  - `embedding_apis`: A managed service for generating text embeddings using various models.
- **Tools**:
  - `semantic_search`: Performs vector search against the `vector_db` MCP.
  - `knowledge_graph_builder`: Constructs and traverses the graph of interconnected Knowledge Cards.
  - `chunk_optimizer`: Analyzes retrieval metrics to suggest better chunking strategies.
  - `consolidate`: Merges and deduplicates redundant information into a single canonical source.

## Boot Sequence
The agent's activation follows a strict, layered protocol:
1.  **LOAD_IDENTITY**: Ingests its core identity from `n04_agent_knowledge.md`.
2.  **LOAD_SYSTEM_PROMPT**: Adopts the rules and persona from `n04_sp_knowledge.md`.
3.  **INITIALIZE_TOOLS**: Activates its suite of knowledge management tools.
4.  **CONNECT_MCPS**: Establishes secure connections to its dependent MCPs.
5.  **AWAIT_DISPATCH**: Enters a ready state, awaiting tasks from the CEX orchestrator.

## Scaling & Resource Allocation
- **Concurrency**: Can handle up to 5 concurrent knowledge processing tasks.
- **Resources**: Allocated a significant memory limit (`8192MB`) and a long timeout (`60 minutes`) to handle complex ingestion and indexing jobs.

## Constraints & Governance
- N04's operational domain is strictly limited to knowledge architecture. It will hand off implementation tasks to N03 and will not engage in generative tasks outside of knowledge synthesis.
- All retrieved information must be accompanied by source links to the relevant Knowledge Card(s), ensuring traceability and trust.
