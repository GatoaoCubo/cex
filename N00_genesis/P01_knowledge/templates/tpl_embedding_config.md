---
id: "p01_emb_"PLACEHOLDER""
kind: embedding_config
pillar: P01
version: 1.0.0
title: Template - Embedding Config
tags: [template, embedding, vector, model, config]
tldr: "Configures embedding model for vector search: model, dimensions, chunking, batch size, runtime."
quality: 9.0
model_name: PLACEHOLDER
dimensions: PLACEHOLDER
chunk_size: PLACEHOLDER
updated: "2026-04-07"
domain: "knowledge management"
author: n04_knowledge
created: "2026-04-07"
density_score: 0.98
---

# Embedding Config: [NAME]

## Purpose
[WHAT this embedding_config does]
## Configuration
```yaml
model: [text-embedding-3-small | nomic-embed-text | mxbai-embed-large]
dimensions: [256 | 384 | 768 | 1536]
chunk_size: [512 | 1024 | 2048]
overlap: [0 | 64 | 128]

batch_size: [100 | 500 | 1000]
runtime: [api | ollama | local]
```
## Model Comparison
| Model | Dims | Local | Cost | MTEB |
|-------|------|-------|------|------|
| text-embedding-3-small | 1536 | no | $0.02/1M | 62.3 |
| nomic-embed-text | 768 | yes | $0 | 62.4 |
| mxbai-embed-large | 1024 | yes | $0 | 63.6 |
## Chunking
1. `chunk_size`: Max tokens per chunk (must be <= model input limit)
2. `overlap`: Tokens shared between chunks (prevents boundary loss)
3. `batch_size`: Embeddings per API call (tune for throughput vs memory)
## Quality Gate
1. [ ] Dimensions match vector store config
2. [ ] Chunk size <= model max input
3. [ ] Overlap < chunk_size / 2
4. [ ] Runtime specified (api vs local)

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `embedding_config` |
| Pillar | P01 |
| Domain | knowledge management |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |
