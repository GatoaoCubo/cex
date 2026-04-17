---
id: kc_knowledge_vocabulary
kind: knowledge_card
pillar: P01
nucleus: n04
title: "Knowledge Card -- N04 Controlled Vocabulary"
version: "1.0.0"
quality: null
tags: [vocabulary, controlled_vocabulary, rag, knowledge, taxonomy, n04, P01]
domain: knowledge management
type: controlled_vocabulary
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "N04 controlled vocabulary: 21 canonical terms for knowledge management and RAG architecture. CEX-to-industry mapping, domain application, anti-patterns. Loaded at F2b SPEAK before any artifact generation."
density_score: null
---

# Knowledge Card: N04 Controlled Vocabulary

## About This KC

N04's language model. Loaded at every session via F2b SPEAK.
Ensures N04 uses canonical industry terms in ALL artifacts, never inventing synonyms.
Cross-nucleus shared terms (kind, pillar, 8F) are NOT redefined here -- they are in N00_genesis.

---

## Canonical Terms

| Term | Definition | N04 Application | Anti-Pattern |
|------|-----------|----------------|-------------|
| `retrieval_augmented_generation` (RAG) | LLM augmented with retrieved external context at inference time | N04's primary architecture: query -> retrieve -> generate | "search-augmented LLM", "context-injected AI" |
| `dense_retrieval` | Embedding-based similarity search (bi-encoder, cosine distance) | Layer 3 primary retrieval in N04 memory architecture | "semantic search" (imprecise), "vector search" |
| `sparse_retrieval` | Term-frequency-based search (BM25, TF-IDF, inverted index) | BM25 component of N04 hybrid retrieval | "keyword search" (less precise), "exact match" |
| `BM25` (Best Match 25) | Probabilistic sparse retrieval: TF-IDF with saturation (k1) and length normalization (b) | N04 sparse retriever, always-available fallback | "keyword search", "TF-IDF search" (BM25 is a specific algorithm) |
| `FAISS` (Facebook AI Similarity Search) | CPU/GPU ANN library for dense vector indexing | Used internally by some N04 tools; pgvector uses HNSW separately | "vector database" (FAISS is a library, not a DB) |
| `cosine_similarity` | Similarity metric: dot product of L2-normalized vectors (range: -1 to 1) | Primary distance metric in N04 pgvector configuration | "cosine distance" (sim = 1 - distance), "dot product" (unnormalized) |
| `embedding_space` | High-dimensional vector space where semantically similar documents cluster | The space N04 operates in for dense retrieval | "AI dimension", "vector space" (correct but less specific) |
| `document_chunking` | Splitting large documents into smaller segments for indexing | Applied by N04 document_loader for PDFs, HTML, long context_docs | "splitting", "segmentation" (correct but vague) |
| `context_window_management` | Techniques to fit relevant content within LLM context limits (200K for N04) | N04 working memory management, LRU eviction, compression | "token management", "prompt trimming" (too vague) |
| `knowledge_graph` | Graph structure where nodes are entities and edges are typed relationships | N04 graph retrieval mode; kno_knowledge_graph_n04.md | "entity network", "relationship map" |
| `ontology` | Formal specification of concepts and relationships in a domain | N04 taxonomy design capability; formal ontologies (OWL, RDF) | "taxonomy" (taxonomy = hierarchy only; ontology = full semantics) |
| `taxonomy` | Hierarchical classification of concepts (is-a relationships only) | CEX 257-kind taxonomy; pillar hierarchy P01-P12 | "ontology" (ontology is more expressive than taxonomy) |
| `folksonomy` | User-generated, non-hierarchical tagging system | Tag fields in CEX frontmatter (flat tags[], not controlled hierarchy) | "taxonomy" (folksonomies are emergent, not designed) |
| `knowledge_engineering` | Discipline of building knowledge bases and expert systems | N04's overall domain; KC creation, taxonomy design, RAG architecture | "knowledge management" (KE is technical discipline; KM is organizational) |
| `information_architecture` | Organization, structure, and labeling of knowledge for findability | Pillar P01-P12 structure; nucleus routing; kind taxonomy | "information design" (less specific), "knowledge organization" |
| `technical_writing` | Disciplined writing for technical audiences: accuracy, clarity, structure | All KC and context_doc output from N04 | "documentation" (writing is the act; documentation is the output) |
| `semantic_search` | Search using meaning/concept similarity (not just keywords) | Dense retrieval component of N04 hybrid search | "AI search" (imprecise), "intelligent search" |
| `lexical_search` | Search using exact or near-exact term matching | Sparse retrieval (BM25) component of N04 hybrid search | "keyword search" (lexical is the technical term) |
| `hybrid_retrieval` | Combining dense (semantic) and sparse (lexical) retrieval, fused by RRF | N04 default retrieval mode -- always hybrid unless specified | "mixed search", "combined search" |
| `reciprocal_rank_fusion` (RRF) | Score fusion algorithm: rank(d) = sum(1/(k+rank_i(d))); k=60 standard | N04 fusion algorithm for hybrid dense+sparse results | "score averaging", "weighted combination" (different algorithms) |
| `knowledge_distillation` | Compressing a corpus of facts into a smaller, denser representation | N04 consolidation: multiple KCs -> memory_summary; session -> learning_record | "summarization" (distillation implies information preservation, not just reduction) |

---

## Cross-Nucleus Shared Terms (DO NOT REDEFINE)

These terms are defined in N00_genesis and apply identically in N04:
- `8F pipeline` (F1-F8): canonical N04 reasoning protocol
- `kind`: atomic artifact type from the 257-kind taxonomy
- `pillar`: P01-P12 domain grouping
- `nucleus`: N00-N07 operational agent
- `quality_gate`: F7 GOVERN validation
- `signal`: F8 COLLABORATE completion notification
- `GDP` (Guided Decision Protocol): user-decides-what, LLM-decides-how

---

## Domain-Specific Extensions (N04 introduces)

| New Term | Definition | Maps to Industry Standard |
|----------|-----------|--------------------------|
| `knowledge_corpus` | The complete indexed knowledge base N04 manages | "knowledge base" in KM; "corpus" in NLP |
| `knowledge_quality_score` (KQS) | N04 composite retrieval quality metric (0.0-1.0) | Composite eval metric (domain-specific) |
| `procedural_memory` | N04 layer for storing task SOPs and how-to knowledge | "procedural knowledge" in cognitive science |
| `gluttony_scan` | N04 post-task scan for gaps to fill (sin lens in action) | "knowledge gap analysis" |
| `context_assembly` | Loading relevant artifacts into working memory for a task | "prompt assembly", "context stuffing" |

---

## Anti-Pattern Register

Terms N04 must NEVER use:

| Banned Term | Use Instead | Reason |
|-------------|-------------|--------|
| "AI search" | `semantic_search` or `hybrid_retrieval` | Too vague |
| "smart search" | `hybrid_retrieval` | Marketing language, not technical |
| "vector database" | `pgvector`, `ChromaDB`, `Pinecone` (specific) | Too generic |
| "knowledge base" | `knowledge_corpus` (N04-specific) or `RAG corpus` | Overloaded term |
| "research card" | `knowledge_card` | Invented synonym (kind drift) |
| "intel doc" | `knowledge_card` | Invented synonym (kind drift) |
| "context injection" | `retrieval_augmented_generation` | Imprecise (injection is just one step) |
