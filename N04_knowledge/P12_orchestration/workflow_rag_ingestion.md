---
id: p12_wf_rag_ingestion_n04
kind: workflow
pillar: P12
nucleus: n04
title: "Workflow -- RAG Corpus Ingestion Pipeline"
version: "1.0.0"
quality: 9.1
tags: [workflow, n04, rag, ingestion, corpus, embedding, indexing, P12]
domain: knowledge management
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "End-to-end RAG corpus ingestion workflow: source identification -> document loading -> chunking -> embedding -> vector store upsert -> index validation. Includes error handling, batch processing, and post-ingestion verification."
density_score: null
---

# Workflow: RAG Corpus Ingestion Pipeline

## Overview

This workflow governs how external knowledge enters the N04 semantic corpus.
It is the WRITE side of the read pipeline defined in `memory_architecture_n04.md`.

**Trigger**: new documents available, scheduled refresh, or manual ingestion command
**Output**: documents indexed in pgvector, BM25 index updated, integrity verified

---

## Workflow Steps

```
SOURCE IDENTIFICATION
       |
       v
DOCUMENT LOADING (document_loader_n04.md)
       |
       v
QUALITY FILTERING
       |
       v
CHUNKING (chunk_strategy_knowledge.md)
       |
       v
METADATA ENRICHMENT
       |
       v
EMBEDDING GENERATION
       |
       v
DEDUPLICATION CHECK
       |
       v
VECTOR STORE UPSERT (api_reference_rag_apis.md)
       |
       v
BM25 INDEX UPDATE
       |
       v
POST-INGESTION VERIFICATION
       |
       v
LOG + COMMIT
```

---

## Step Details

### Step 1: Source Identification

Determine source type and corpus namespace:

| Source | Type | Corpus | Trust Level |
|--------|------|--------|-------------|
| CEX .md artifacts | markdown | cex_artifacts | 5 |
| External documentation | html/pdf | external_docs | 3 |
| Research papers | pdf | external_docs | 4 |
| Session transcripts | text | session_memory | 2 |
| User-uploaded files | varies | external_docs | 3 (default) |

### Step 2: Document Loading

Apply `document_loader_n04.md` per source type.

```bash
python _tools/cex_retriever.py --ingest \
  --source {path} \
  --format {markdown|pdf|html|docx|repo} \
  --corpus {corpus_name} \
  --trust-level {1-5}
```

### Step 3: Quality Filtering

Reject documents below quality thresholds:
- PDF: OCR artifact ratio <= 5%
- HTML: text/html ratio >= 0.3 (not mostly markup)
- Markdown: frontmatter must parse without error
- All: min_length = 100 characters

### Step 4: Chunking

Per `chunk_strategy_knowledge.md`:

| Document Type | Strategy | Size | Overlap |
|-------------|---------|------|---------|
| KnowledgeCard | whole document | N/A | N/A |
| ContextDoc | heading-based | 1024 tokens | 0 |
| PDF/HTML/DOCX | sliding window | 512 tokens | 128 tokens |
| Code | function-level | variable | 0 |

### Step 5: Metadata Enrichment

Add: `ingestion_date`, `corpus`, `trust_level`, `token_count`, `language`, `embedding_model`

### Step 6: Embedding Generation

```python
embeddings = openai_client.embeddings.create(
    model="text-embedding-3-small",
    input=[chunk.content for chunk in chunks]
)
```

Batch size: 50 chunks per API call. Rate limit: 500 requests/min (1 batch/2s).

### Step 7: Deduplication Check

Before upsert, check for near-duplicates:
```bash
python _tools/cex_retriever.py --similarity-check \
  --query "{chunk_content}" \
  --threshold 0.97 \
  --corpus {corpus_name}
```

If similarity >= 0.97: skip upsert (exact duplicate), log event.
If similarity 0.92-0.96: flag for review queue.

### Step 8: Vector Store Upsert

Per `api_reference_rag_apis.md` -> `upsert_document` endpoint.

```python
for chunk in deduped_chunks:
    supabase.rpc("upsert_document", {
        "doc_id": str(chunk.id),
        "content": chunk.content,
        "embedding": chunk.embedding,
        "metadata": chunk.metadata
    }).execute()
```

### Step 9: BM25 Index Update

After all upserts:
```bash
python _tools/cex_retriever.py --rebuild-index \
  --corpus {corpus_name}
```

### Step 10: Post-Ingestion Verification

Verify the just-ingested content is retrievable:
```bash
python _tools/cex_retriever.py \
  --query "{representative_query_from_ingested_content}" \
  --corpus {corpus_name} \
  --verify-ingestion
```

PASS: at least 1 result from ingested batch in top-10
FAIL: ingestion failed silently -- check upsert logs

### Step 11: Log + Commit

```bash
# Log ingestion event
echo "{date} | {source} | {n_docs} docs | {corpus}" \
  >> N04_knowledge/P05_output/ingestion_log.md

# Commit for CEX artifact ingestions
git add N04_knowledge/ && \
git commit -m "[N04] ingest: {n_docs} docs from {source} to {corpus}"
```

---

## Error Handling

| Error | Step | Recovery |
|-------|------|---------|
| Low OCR quality | 3 | Skip document, log to P07_evals/ |
| Embedding API rate limit | 6 | Exponential backoff (1s, 2s, 4s) |
| Vector store unavailable | 8 | Fall back to ChromaDB, retry pgvector in 5min |
| Dedup threshold exceeded | 7 | Skip upsert, log duplicate pair |
| Verification fails | 10 | Alert: check step 8 logs, re-run upsert |

---

## Scheduled Runs

| Trigger | Source | Corpus |
|---------|--------|--------|
| After `cex_compile.py --all` | N04_knowledge/ | cex_artifacts |
| Weekly cron (Sunday 02:00) | All CEX nuclei/ | cex_artifacts |
| Monthly (first Sunday) | External curated sources | external_docs |
| Manual trigger | Any | Any |
