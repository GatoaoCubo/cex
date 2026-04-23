---
id: p10_ma_n04_knowledge
kind: memory_architecture
pillar: P10
nucleus: n04
title: "Memory Architecture -- N04 Knowledge Nucleus"
version: "1.0.0"
quality: 9.2
tags: [memory_architecture, n04, rag, episodic, semantic, procedural, working_memory, P10]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Full memory system design for N04: working memory (context window), episodic (session transcripts), semantic (vector store), and procedural (task procedures). Includes storage backends, read/write pipelines, eviction policies, and tier matrix."
density_score: null
related:
  - bld_knowledge_card_memory_architecture
  - bld_output_template_memory_architecture
  - memory-architecture-builder
  - p01_kc_memory_scope
  - p03_sp_memory_architecture_builder
  - atom_22_memory_taxonomy
  - bld_examples_memory_scope
  - bld_instruction_memory_architecture
  - bld_schema_memory_architecture
  - bld_knowledge_card_memory_scope
---

# Memory Architecture: N04 Knowledge Nucleus

## Overview

N04 (Knowledge Gluttony) operates as the enterprise memory layer for CEX. Its sin lens
demands that EVERYTHING be remembered, indexed, and retrievable. This architecture
implements 4 memory layers spanning hot (context window) to cold (vector corpus),
with pipelines that ensure nothing is lost.

Reference architectures: MemGPT/Letta (hierarchical paging), Zep (temporal graphs),
mem0 (selective extraction), LangMem (session compression).

---

## Memory Layers

| Layer | Backend | Retention | Tier Required | Active? |
|-------|---------|-----------|---------------|---------|
| Working | Context window (200K tokens) | Session duration | FREE | Always |
| Episodic | Supabase pgvector `session_memory` | 90 days | PRO | Yes |
| Semantic | Supabase pgvector `cex_artifacts` | Permanent | FREE | Always |
| Procedural | Markdown files in P10_memory/ | Permanent | FREE | Always |

---

## Storage Backends

### Working Memory (Layer 1)
- **Backend**: Claude context window (200K tokens)
- **Contents**: current task, recent tool outputs, loaded KCs, active artifacts
- **Management**: `cex_prompt_layers.py` controls what enters working memory
- **Overflow**: trigger semantic lookup when context > 80% capacity
- **Paging protocol**: MemGPT-style -- compress least-recent content, archive to episodic

### Episodic Memory (Layer 2)
- **Backend**: pgvector `session_memory` namespace
- **Contents**: session transcripts, per-session learning records, conversation summaries
- **Indexing**: embedding per session summary + per-turn key facts
- **Retention**: 90-day TTL with importance decay (used sessions extend TTL)
- **Access**: semantic search across session history for relevant prior context

### Semantic Memory (Layer 3) -- PRIMARY
- **Backend**: pgvector `cex_artifacts` namespace + `external_docs` namespace
- **Contents**: all 3381+ CEX ISOs, compiled KCs, artifacts, external ingested documents
- **Indexing**: text-embedding-3-small (1536 dim), BM25 index (sparse)
- **Retrieval**: hybrid (dense + sparse), reranked via cross-encoder
- **Scale**: 2184 documents at last index (cex_retriever.py TF-IDF as fallback)
- **Updates**: triggered on `cex_compile.py` run (new/updated artifacts auto-indexed)

### Procedural Memory (Layer 4)
- **Backend**: Markdown files in `N04_knowledge/P10_memory/`
- **Contents**: how-to protocols, standard operating procedures, decision patterns
- **Examples**: `procedural_memory_n04.md` (this session), ingestion workflows, scoring procedures
- **Access**: loaded explicitly at session start via `cex_prompt_layers.py`
- **Updates**: append-only; versioned via git

---

## Read Pipeline (Retrieval)

```
User/Agent Query
      |
      v
1. CONSTRAIN -- parse query via input_schema_knowledge_query.md
      |
      v
2. WORKING MEMORY CHECK -- is answer already in context? (O(1) lookup)
      |
      | Miss
      v
3. PROCEDURAL LOOKUP -- does this match a known procedure? (exact match)
      |
      | Miss
      v
4. EPISODIC LOOKUP -- did we encounter this in a recent session? (semantic search)
      |
      | Miss
      v
5. SEMANTIC SEARCH -- corpus search (hybrid: dense + BM25)
   |-- dense: text-embedding-3-small cosine similarity
   |-- sparse: BM25 TF-IDF on cex_retriever.py (2184 docs)
   |-- merge: Reciprocal Rank Fusion (RRF)
      |
      v
6. RERANK -- cross-encoder reranking (top-20 -> top-10)
      |
      v
7. INJECT -- assemble context passages into working memory
      |
      v
8. RESPOND -- generate with grounded context
```

---

## Write Pipeline (Memory Formation)

```
After each significant generation
      |
      v
1. EXTRACT -- identify facts, entities, procedures worth persisting
      |
      v
2. CLASSIFY -- which memory layer is appropriate?
   |-- new fact about the world -> semantic (new KC or update existing)
   |-- session learning -> episodic (learning_record)
   |-- new procedure -> procedural (new .md in P10_memory/)
   |-- entity encountered -> entity_memory update
      |
      v
3. DEDUPLICATE -- check if fact already exists (similarity search, threshold 0.95)
      |
      v
4. PERSIST
   |-- semantic: cex_compile.py -> auto-index via post-tool hook
   |-- episodic: append to session learning_record
   |-- procedural: write to P10_memory/{procedure_name}.md
   |-- entity: update entity_memory file
      |
      v
5. SIGNAL (if cross-nucleus relevant) -- write_signal to N07
```

---

## Eviction Policy

| Layer | Strategy | Trigger |
|-------|----------|---------|
| Working | LRU + importance score | > 80% context window used |
| Working | Compress + archive | Session end |
| Episodic | TTL (90 days) + usage extension | Background cron (daily) |
| Episodic | Importance decay | Score < 0.2 after 30 days |
| Semantic | Never evicted | Permanent corpus (versioned in git) |
| Procedural | Never evicted | Superseded procedures marked deprecated |

**Importance Score**: composite of (retrieval frequency, recency, cross-nucleus citations)

---

## Commercial Tier Matrix

| Feature | FREE | PRO | ENTERPRISE |
|---------|------|-----|-----------|
| Working memory | 200K tokens | 200K tokens | 1M tokens |
| Semantic corpus | 2184 docs | Unlimited | Unlimited + private |
| Episodic retention | Session only | 90 days | 2 years |
| Episodic search | No | Yes | Yes + temporal graph |
| Procedural memory | 20 files | Unlimited | Unlimited + versioned |
| Auto-indexing | Manual | On compile | Real-time |
| Reranking | TF-IDF | Cross-encoder | Cross-encoder + LLM |
| Multi-corpus | No | 3 corpora | Unlimited |

---

## Integration Points

| Artifact | Role |
|---------|------|
| `consolidation_policy_n04.md` | When to merge/compress episodic memories |
| `procedural_memory_n04.md` | What N04 knows HOW to do (Layer 4 content) |
| `knowledge_memory_index.md` | Index of semantic corpus |
| `retriever_n04.md` | Implementation of the read pipeline (Layer 3) |
| `document_loader_n04.md` | Implementation of the write pipeline (ingestion) |
| `cex_memory_types.py` | 4-type taxonomy: correction/preference/convention/context |
| `cex_memory_age.py` | Freshness caveats + linear decay for episodic layer |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_memory_architecture]] | upstream | 0.50 |
| [[bld_output_template_memory_architecture]] | upstream | 0.48 |
| [[memory-architecture-builder]] | related | 0.45 |
| [[p01_kc_memory_scope]] | upstream | 0.40 |
| [[p03_sp_memory_architecture_builder]] | upstream | 0.39 |
| [[atom_22_memory_taxonomy]] | related | 0.37 |
| [[bld_examples_memory_scope]] | upstream | 0.36 |
| [[bld_instruction_memory_architecture]] | upstream | 0.35 |
| [[bld_schema_memory_architecture]] | upstream | 0.33 |
| [[bld_knowledge_card_memory_scope]] | upstream | 0.32 |
