---
id: "p01_emb_"PLACEHOLDER""
kind: embedding_config
pillar: P01
version: 1.0.0
title: Template - Embedding Config
tags: [template, embedding, vector, model, config]
tldr: "Configures embedding model for vector search: model, dimensions, chunking, batch size, runtime."
quality: 8.6
model_name: PLACEHOLDER
dimensions: PLACEHOLDER
chunk_size: PLACEHOLDER
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
- `chunk_size`: Max tokens per chunk (must be <= model input limit)
- `overlap`: Tokens shared between chunks (prevents boundary loss)
- `batch_size`: Embeddings per API call (tune for throughput vs memory)
## Quality Gate
- [ ] Dimensions match vector store config
- [ ] Chunk size <= model max input
- [ ] Overlap < chunk_size / 2
- [ ] Runtime specified (api vs local)
