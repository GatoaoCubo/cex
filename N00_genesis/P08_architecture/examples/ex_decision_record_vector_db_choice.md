---
id: p08_adr_vector_db_choice
kind: decision_record
pillar: P08
title: "ADR-007: Choose Qdrant over Pinecone for Vector Database"
status: accepted
context: "organization needs a vector database for brain_query FAISS replacement at scale. Must be self-hosted for data sovereignty and cost control."
decision: "Use Qdrant (self-hosted Docker) as the primary vector database"
consequences:
  positive:
    - "Full control over data — no external API calls for embeddings storage"
    - "No per-query pricing — fixed infrastructure cost (~$20/mo on Railway)"
    - "Supports filtering, payload storage, and hybrid search natively"
    - "Rust-based — low memory footprint, handles 1M+ vectors on 2GB RAM"
  negative:
    - "Self-managed infrastructure — updates, backups, monitoring are our responsibility"
    - "No managed dashboard — monitoring via Prometheus/Grafana or API"
    - "Smaller community than Pinecone — fewer tutorials, slower Stack Overflow answers"
version: 1.0.0
created: 2026-03-29
author: builder_agent
quality: 9.1
tags: [adr, vector-database, qdrant, pinecone, self-hosted, architecture]
related:
  - knowledge-index-builder
  - bld_knowledge_card_knowledge_index
  - bld_examples_component_map
  - bld_architecture_retriever
  - bld_examples_knowledge_index
  - p01_kc_knowledge_index
  - p04_plug_brain_search
  - retriever-builder
  - p10_bi_organization_brain
  - bld_knowledge_card_vector_store
---

# ADR-007: Vector Database Selection

## Status
**Accepted** — 2026-03-29

## Context

organization's brain_query currently uses FAISS for vector search (140MB index, ~1,957 pool artifacts). This works for local development but has limitations:

1. **No persistence** — index must be rebuilt on every fresh clone (~20 min)
2. **No filtering** — cannot filter by pillar, agent_group, or quality score during search
3. **No real-time updates** — adding a new KC requires full index rebuild
4. **Single-machine** — cannot share index across Railway API + local dev

We need a vector database that supports:
- Self-hosted deployment (data sovereignty requirement — pool artifacts contain proprietary business knowledge)
- Hybrid search (vector + keyword, replacing current BM25+FAISS dual system)
- Metadata filtering (by pillar, agent_group, quality score, kind)
- Real-time upsert without full rebuild
- Affordable at our scale (2K-10K documents, 768-dim vectors)

## Options Evaluated

### Option A: Pinecone (Managed)
| Aspect | Assessment |
|--------|------------|
| Hosting | Cloud-managed (AWS us-east-1) |
| Pricing | Free tier: 100K vectors. Starter: $70/mo for 1M vectors |
| Hybrid search | Sparse-dense vectors supported |
| Filtering | Metadata filtering with JSON operators |
| Latency | ~50ms p95 (network round-trip to US) |
| Setup | 5 min (API key + SDK) |
| **Concern** | Data leaves our infrastructure. Vendor lock-in. $70/mo for <10K vectors is overpaying. |

### Option B: Qdrant (Self-hosted)
| Aspect | Assessment |
|--------|------------|
| Hosting | Docker on Railway ($5-20/mo depending on RAM) |
| Pricing | Open source, infrastructure cost only |
| Hybrid search | Native sparse+dense, BM25-equivalent built in |
| Filtering | Rich payload filtering (nested JSON, geo, datetime) |
| Latency | ~5ms p95 (same Railway network, no external hop) |
| Setup | 30 min (Docker, collection schema, initial load) |
| **Concern** | Self-managed backups. Must monitor health ourselves. |

### Option C: ChromaDB (Self-hosted)
| Aspect | Assessment |
|--------|------------|
| Hosting | Docker or embedded Python |
| Pricing | Open source |
| Hybrid search | Basic keyword + vector |
| Filtering | Metadata where clauses |
| Latency | ~15ms p95 |
| Setup | 15 min |
| **Concern** | Python-based — higher memory, slower at scale. No native sparse vectors. Single-node only (no replication). |

### Option D: Keep FAISS + BM25
| Aspect | Assessment |
|--------|------------|
| Hosting | Local files |
| Pricing | Free |
| **Concern** | All 4 original problems remain unsolved. |

## Decision

**Use Qdrant self-hosted on Railway.**

Deciding factors:
1. **10x lower latency** — 5ms vs 50ms (same-network vs cross-internet)
2. **80% cheaper** — ~$10/mo vs $70/mo at our scale
3. **Data sovereignty** — pool artifacts never leave our infrastructure
4. **Native hybrid search** — replaces both FAISS and BM25 with single system
5. **Rust performance** — 2GB RAM handles 1M vectors; we have <10K

## Implementation Plan

```
Phase 1 (Week 1): Deploy Qdrant on Railway
  - Docker image: qdrant/qdrant:v1.8.4
  - Collection: organization_brain, 768-dim, cosine distance
  - Initial load: migrate FAISS index -> Qdrant collection

Phase 2 (Week 2): Integrate with brain_query
  - Replace hybrid_search() to call Qdrant instead of FAISS+BM25
  - Add metadata filters: pillar, agent_group, quality, kind
  - Benchmark: must match or beat current 88% top-3 accuracy

Phase 3 (Week 3): Real-time sync
  - On KC create/update: upsert to Qdrant via post-commit hook
  - Remove build_indexes_ollama.py rebuild requirement
  - Add health check to /api/v2/health
```

## Consequences

### Positive
- Single search system instead of BM25+FAISS dual maintenance
- Real-time index updates — new KCs searchable in <1s
- Metadata filtering enables scoped queries ("agents in P02 with quality >= 8.0")
- 10x latency improvement for Railway API search endpoint
- No vendor lock-in — Qdrant is open source, data exportable as JSON

### Negative
- Infrastructure responsibility: backups, updates, monitoring
- Team must learn Qdrant query DSL (though similar to Elasticsearch)
- Migration risk: must validate accuracy parity before cutover
- Additional Railway service adds ~$10/mo to infrastructure cost

### Risks
| Risk | Mitigation |
|------|-----------|
| Qdrant service crashes | Railway auto-restart + daily snapshot backups |
| Accuracy regression after migration | A/B test against FAISS for 1 week before cutover |
| Qdrant version upgrade breaks API | Pin version, test upgrades in staging first |
| Scale beyond single node | Unlikely at <10K docs; Qdrant supports clustering if needed |

## References
- Qdrant docs: https://qdrant.tech/documentation/
- FAISS current setup: `records/core/brain/mcp-organization-brain/build_indexes_ollama.py`
- Brain search: `records/core/brain/mcp-organization-brain/vector_search.py`
- Related: p01_kc_bm25_search (current BM25 implementation)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[knowledge-index-builder]] | downstream | 0.33 |
| [[bld_knowledge_card_knowledge_index]] | upstream | 0.32 |
| [[bld_examples_component_map]] | related | 0.30 |
| [[bld_architecture_retriever]] | downstream | 0.28 |
| [[bld_examples_knowledge_index]] | upstream | 0.28 |
| [[p01_kc_knowledge_index]] | downstream | 0.28 |
| [[p04_plug_brain_search]] | upstream | 0.27 |
| [[retriever-builder]] | upstream | 0.27 |
| [[p10_bi_organization_brain]] | downstream | 0.27 |
| [[bld_knowledge_card_vector_store]] | upstream | 0.27 |
