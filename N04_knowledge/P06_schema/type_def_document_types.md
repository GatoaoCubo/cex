---
id: p06_td_document_types
kind: type_def
pillar: P06
nucleus: n04
title: "Type Definition -- Document Type Taxonomy"
version: "1.0.0"
quality: 9.1
tags: [type_def, document_types, taxonomy, rag, knowledge_card, n04, P06]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Canonical type definitions for all document types that flow through the N04 RAG pipeline: KnowledgeCard, ContextDoc, RAGSource, Artifact, and their subtypes. Includes field contracts, serialization rules, and retrieval behavior per type."
density_score: null
related:
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - n06_schema_brand_config
  - bld_schema_tagline
  - bld_schema_training_method
  - bld_schema_model_architecture
  - bld_schema_multimodal_prompt
  - bld_schema_dataset_card
  - bld_schema_graph_rag_config
  - p06_is_knowledge_data_model
---

# Type Definition: Document Type Taxonomy

## Overview

Every document in the N04 retrieval pipeline has a type. Types determine:
- Which embedding model and chunking strategy to apply
- How the document is stored and indexed
- What metadata fields are required
- How retrieval results are formatted and scored

---

## Base Type: `Document`

All document types extend this base.

```typescript
interface Document {
  id: string;              // UUID v4
  type: DocumentType;      // enum (see below)
  content: string;         // raw text content
  metadata: Metadata;      // type-specific metadata
  embedding?: float[];     // 1536-dim vector (null until indexed)
  created_at: datetime;
  updated_at: datetime;
  score?: float;           // only present in retrieval results (0.0-1.0)
}
```

---

## Enum: `DocumentType`

```typescript
enum DocumentType {
  KNOWLEDGE_CARD   = "knowledge_card",
  CONTEXT_DOC      = "context_doc",
  RAG_SOURCE       = "rag_source",
  ARTIFACT         = "artifact",
  CONVERSATION     = "conversation",
  CHUNK            = "chunk",
  CITATION         = "citation",
  GLOSSARY_ENTRY   = "glossary_entry",
}
```

---

## Type: `KnowledgeCard`

Primary knowledge unit. Typed, peer-reviewed, compiled.

```typescript
interface KnowledgeCard extends Document {
  type: DocumentType.KNOWLEDGE_CARD;
  metadata: {
    kind: string;          // from 257-kind taxonomy
    pillar: string;        // P01-P12
    nucleus: string;       // n01-n07
    domain: string;
    quality: float | null; // null until peer-reviewed
    version: string;       // semver
    tldr: string;          // <= 200 chars
    tags: string[];
    compiled_path?: string; // path to .yaml compiled version
  };
}
```

**Chunking**: 512-token sliding window, 128-token overlap
**Embedding**: text-embedding-3-small (1536 dim)
**Storage**: pgvector `cex_artifacts` namespace
**Retrieval weight**: 1.2x boost (highest quality signal)

---

## Type: `ContextDoc`

Longer-form operational documentation: guides, specs, runbooks.

```typescript
interface ContextDoc extends Document {
  type: DocumentType.CONTEXT_DOC;
  metadata: {
    title: string;
    kind: string;           // context_doc, contributor_guide, quickstart_guide, etc.
    pillar: string;
    audience: string;       // "developer" | "operator" | "agent"
    version: string;
    toc?: string[];         // table of contents (section headings)
  };
}
```

**Chunking**: 1024-token semantic chunks (split on H2/H3 boundaries)
**Embedding**: text-embedding-3-small
**Storage**: pgvector `cex_artifacts` namespace
**Retrieval weight**: 1.0x (standard)

---

## Type: `RAGSource`

External data source registered for ingestion into the corpus.

```typescript
interface RAGSource extends Document {
  type: DocumentType.RAG_SOURCE;
  metadata: {
    source_url?: string;
    source_type: string;   // "web", "pdf", "repo", "database", "api"
    ingestion_date: datetime;
    refresh_interval?: string; // ISO 8601 duration (e.g., "P7D" for weekly)
    corpus: string;        // target corpus namespace
    license?: string;
    trust_level: integer;  // 1 (low) to 5 (high) -- affects retrieval weight
  };
}
```

**Chunking**: adaptive (PDF: 256-token; code: function-level; web: paragraph)
**Embedding**: text-embedding-3-small
**Storage**: pgvector `external_docs` namespace
**Retrieval weight**: trust_level / 5.0 (max 1.0x)

---

## Type: `Artifact`

Any CEX typed artifact file (not necessarily a KC -- includes agents, configs, schemas).

```typescript
interface Artifact extends Document {
  type: DocumentType.ARTIFACT;
  metadata: {
    kind: string;          // any of 257 CEX kinds
    pillar: string;
    nucleus: string;
    path: string;          // relative path in repo
    quality: float | null;
    compiled_yaml_path?: string;
  };
}
```

**Chunking**: whole document (artifacts are small enough, max 8KB)
**Embedding**: text-embedding-3-small
**Storage**: pgvector `cex_artifacts` namespace
**Retrieval weight**: 1.0x

---

## Type: `Conversation`

Session transcript or summarized conversation memory.

```typescript
interface Conversation extends Document {
  type: DocumentType.CONVERSATION;
  metadata: {
    session_id: string;
    nucleus: string;
    turn_count: integer;
    summary?: string;       // compressed representation
    learnings?: string[];   // extracted facts for memory persistence
    date: datetime;
  };
}
```

**Chunking**: by turn (one chunk per exchange)
**Embedding**: text-embedding-3-small
**Storage**: pgvector `session_memory` namespace
**Retrieval weight**: 0.8x (recency-boosted if < 24h old)

---

## Type: `Chunk`

Atomic retrieval unit. Produced by the chunking pipeline from any parent document.

```typescript
interface Chunk extends Document {
  type: DocumentType.CHUNK;
  metadata: {
    parent_id: string;      // source document ID
    parent_type: DocumentType;
    chunk_index: integer;   // position in parent
    token_count: integer;
    overlap_tokens: integer;
    heading_context?: string; // nearest H2/H3 above this chunk
  };
}
```

**Chunking**: N/A (is the chunk)
**Embedding**: text-embedding-3-small
**Storage**: pgvector alongside parent namespace
**Retrieval weight**: inherits parent weight

---

## Type: `Citation`

Source reference for provenance tracking.

```typescript
interface Citation extends Document {
  type: DocumentType.CITATION;
  metadata: {
    title: string;
    authors?: string[];
    url?: string;
    doi?: string;
    publication_date?: datetime;
    cited_by: string[];     // list of document IDs that cite this
    kind: "citation";
  };
}
```

**Embedding**: title + abstract only (if available)
**Storage**: pgvector `citations` namespace

---

## Type Hierarchy

```
Document (base)
  |-- KnowledgeCard     (P01 primary type, highest retrieval weight)
  |-- ContextDoc        (P05 documentation, semantic chunks)
  |-- RAGSource         (external ingested data, trust-weighted)
  |-- Artifact          (any CEX artifact, whole-doc embedding)
  |-- Conversation      (session memory, recency-boosted)
  |-- Chunk             (atomic retrieval unit, inherits parent)
  |-- Citation          (provenance, title+abstract only)
  |-- GlossaryEntry     (vocabulary, short, whole-doc embedding)
```

---

## Serialization Rules

| Rule | Requirement |
|------|------------|
| IDs | UUID v4, lowercase, no hyphens in storage keys |
| Dates | ISO 8601 UTC (e.g., `2026-04-17T00:00:00Z`) |
| Embeddings | 1536-dim float array, stored as JSONB in pgvector |
| Content encoding | UTF-8 |
| Metadata | flat JSON (no nesting beyond 1 level) |
| Quality field | float 0.0-10.0 or null (never string "null") |

---

## Cross-References

| Type | Builder | Schema |
|------|---------|--------|
| KnowledgeCard | `knowledge-card-builder` | `kc_structure_contract.md` |
| RAGSource | `rag-source-builder` | `rag_source_knowledge.md` |
| Artifact | any kind builder | frontmatter schema per kind |
| Chunk | chunking pipeline | `chunk_strategy_knowledge.md` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_model_registry]] | related | 0.48 |
| [[bld_schema_experiment_tracker]] | related | 0.45 |
| [[n06_schema_brand_config]] | related | 0.39 |
| [[bld_schema_tagline]] | related | 0.38 |
| [[bld_schema_training_method]] | related | 0.37 |
| [[bld_schema_model_architecture]] | related | 0.36 |
| [[bld_schema_multimodal_prompt]] | related | 0.36 |
| [[bld_schema_dataset_card]] | related | 0.34 |
| [[bld_schema_graph_rag_config]] | related | 0.33 |
| [[p06_is_knowledge_data_model]] | related | 0.33 |
