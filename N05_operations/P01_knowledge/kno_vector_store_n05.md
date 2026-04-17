---
id: kno_vector_store_n05
kind: vector_store
pillar: P01
nucleus: N05
title: "N05 Operations Vector Store"
version: "1.0.0"
quality: null
tags: [n05, operations, vector_store, gating_wrath, pgvector, retrieval, evidence]
---
<!-- 8F: F1=vector_store/P01 F2=vector-store-builder F3=nucleus_def_n05+P01_schema+kc_vector_store+examples+W1 config F4=pgvector backend with auditable namespaces
     F5=shell+apply_patch+cex_compile F6=approx-6KB dense markdown F7=self-check frontmatter+8F+80L+properties+ascii F8=N05_operations/P01_knowledge/kno_vector_store_n05.md -->

# N05 Operations Vector Store

## Intent

N05 needs a vector backend that fits operational reality:

- observable
- backed up
- easy to gate
- compatible with strict metadata filtering

For this nucleus, the vector store is not an isolated ML toy. It is part of deploy and incident operations.

## Properties

| Property | Value |
|----------|-------|
| Kind | `vector_store` |
| Pillar | `P01` |
| Nucleus | `N05` |
| Backend | `pgvector` |
| Collection model | `schema_plus_namespace` |
| Distance metric | `cosine` |
| Index type | `hnsw` |
| Dimension contract | `1536` |
| Failure stance | `reject_on_contract_violation` |

## Primary Decision

Use `pgvector` on PostgreSQL as the default N05 vector store.

Why this fits Gating Wrath:

- operational teams already know how to back up, inspect, and restore Postgres
- metadata filtering is first-class and auditable
- schema constraints can enforce dimension and namespace contracts
- one operational platform can hold vectors, metadata, and index health facts together

N05 values auditability over fashionable separation.

## Storage Layout

Use one logical table family with namespace isolation:

- `n05_knowledge_chunks`
- `n05_memory_chunks`
- `n05_index_audit`

Suggested namespaces:

- `ops_runbook`
- `ops_ci`
- `ops_deploy`
- `ops_schema`
- `ops_memory`

Each row should include:

- vector
- source path
- kind
- pillar
- nucleus
- document class
- environment
- service
- created_at
- updated_at
- source_hash

## Index Parameters

| Parameter | Value | Reason |
|-----------|-------|--------|
| distance metric | `cosine` | matches normalized embeddings |
| index type | `hnsw` | good recall/latency balance |
| m | `16` | moderate graph density |
| ef_construction | `128` | stable build quality |
| ef_search | `64` | reasonable runtime recall |
| vacuum policy | `scheduled` | prevents drift after churn |

## Contract Rules

Hard database rules should enforce:

1. vector dimension must equal `1536`
2. namespace must be one of the approved N05 namespaces
3. `nucleus` must equal `N05`
4. `source_hash` must be present for every row
5. `updated_at` must be set on insert and update

If a write violates the contract, the transaction fails. This is the correct behavior.

## Why Not Other Defaults

| Backend | Reason it is not primary |
|---------|--------------------------|
| FAISS | very fast, but weaker operational auditability and backup ergonomics |
| Pinecone | managed, but adds external dependency and weaker in-stack inspection |
| Chroma | easy local dev, less aligned with production governance |
| Qdrant | strong option, but N05 already operates around Postgres-heavy workflows |

This is not a claim that pgvector is universally best. It is best for this nucleus and this governance posture.

## Query Pattern

The store should support:

- vector similarity
- metadata prefiltering
- namespace isolation
- freshness-aware ordering
- rebuild audits by source hash

Operationally important query filters:

- `environment = staging`
- `service = api`
- `document_class = deploy_log`
- `kind = learning_record`

## Failure Modes

| Failure mode | Symptom | Mitigation |
|--------------|---------|------------|
| dimension mismatch | insert errors or invalid neighbors | db constraint and preflight validation |
| mixed namespace data | wrong evidence in gate decision | approved namespace enum |
| stale rows after source change | retriever cites obsolete rule | source_hash diff and rebuild queue |
| no audit table | impossible rebuild provenance | keep `n05_index_audit` entries |
| missing metadata filters | semantic false positives | enforce filter path in retriever |

## Operations Playbook

Normal cycle:

1. ingest chunk batch
2. verify dimensions and metadata
3. upsert into namespace
4. record audit row with build id and source hashes
5. vacuum/analyze on schedule

Incident cycle:

1. detect suspicious retrieval drift
2. inspect audit table for last rebuild and model id
3. compare source hashes to current corpus
4. isolate affected namespace
5. rebuild only the broken namespace unless model changed globally

## Backup and Recovery

Postgres-native backup is a major reason for this choice.

Required posture:

- daily logical backup of vector tables and audit metadata
- WAL-based recovery aligned with the rest of operations data
- namespace-scoped restore plan for accidental corruption

If the audit table cannot prove what model and source set produced the vectors, recovery is incomplete.

## Validation Checklist

- vector dimension pinned to `1536`
- namespace present and valid
- source hash recorded
- metadata filters usable without full table scan
- audit rows written for every rebuild
- warm query latency acceptable for top_k `6`

## Integration

This store is paired with:

- `kno_embedder_provider_n05.md` for vector generation
- `kno_retriever_config_n05.md` for hybrid query behavior
- `mem_knowledge_index_n05.md` for rebuild cadence and sparse companion index

The store is intentionally boring, inspectable, and enforceable. That is an operational strength, not a weakness.
