---
id: p01_emb_nomic_embed_text
kind: embedding_config
8f: F3_inject
pillar: P01
title: "Example — Nomic Embed Text Configuration"
model_name: nomic-embed-text
dimensions: 768
chunk_size: 2048
tags: [embedding, nomic, ollama, local, vector]
tldr: "Local embedding config using nomic-embed-text via Ollama. 768 dimensions, 2048 token chunks, 128 overlap. Runs on localhost, ~24ms per text."
quality: 9.0
related:
  - p01_emb_openai_text_embedding_3_small
  - bld_examples_embedding_config
  - bld_knowledge_card_embedding_config
  - n01_emb_text_embedding_4
  - p04_tool_embedding_batch
  - p06_schema_embedding
  - bld_config_embedding_config
  - p01_kc_rag_chunking_strategies
  - bld_instruction_embedding_config
  - p10_lr_embedding_config_builder
---

# Embedding Config: nomic-embed-text

## Model Details
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Model | nomic-embed-text | Open-source, runs locally via Ollama |
| Dimensions | 768 | Good balance: quality vs storage |
| Max input tokens | 8192 | Handles long documents |
| Runtime | Ollama localhost:11434 | No API costs, full privacy |
| License | Apache 2.0 | Commercial use allowed |

## Chunking Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Chunk size | 2048 tokens | Within model's 8192 limit, good granularity |
| Overlap | 128 tokens | ~6% overlap, preserves cross-boundary context |
| Min chunk | 100 tokens | Avoids noise from tiny fragments |
| Max chunks/file | 10 | Caps index size per document |
| Boundary | sentence | Splits at sentence boundaries |

## Performance
| Metric | Value |
|--------|-------|
| Latency (single) | ~24ms per text |
| Batch size | 500 (optimal throughput) |
| Full reindex time | ~20 min for CEX corpus |
| Index size | ~140 MB (gitignored) |
| Memory (model loaded) | ~1.5 GB |

## Usage
```bash
# Full reindex
python build_indexes_ollama.py --scope all

# Single file
python build_indexes_ollama.py --file P01_knowledge/library/kind/kc_agent.md

# Verify
python -c "import chromadb; c = chromadb.Client(); print(c.list_collections())"
```

## Comparison to Alternatives
| Model | Dim | Local | Cost | Quality (MTEB) |
|-------|-----|-------|------|----------------|
| **nomic-embed-text** | **768** | **yes** | **$0** | **62.4** |
| text-embedding-3-small | 1536 | no | $0.02/1M | 62.3 |
| text-embedding-3-large | 3072 | no | $0.13/1M | 64.6 |
| mxbai-embed-large | 1024 | yes | $0 | 63.6 |

## Quality Gate
- [ ] Ollama running with model loaded: `ollama list | grep nomic`
- [ ] Chunk size ≤ model max input (8192)
- [ ] Index is gitignored (regenerable)
- [ ] Batch size tuned for hardware (500 = 12 GB RAM sweet spot)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_emb_openai_text_embedding_3_small]] | related | 0.41 |
| [[bld_examples_embedding_config]] | downstream | 0.40 |
| [[bld_knowledge_card_embedding_config]] | related | 0.38 |
| [[n01_emb_text_embedding_4]] | sibling | 0.33 |
| [[p04_tool_embedding_batch]] | downstream | 0.33 |
| [[p06_schema_embedding]] | downstream | 0.32 |
| [[bld_config_embedding_config]] | downstream | 0.30 |
| [[p01_kc_rag_chunking_strategies]] | related | 0.29 |
| [[bld_instruction_embedding_config]] | downstream | 0.29 |
| [[p10_lr_embedding_config_builder]] | downstream | 0.28 |
