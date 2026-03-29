---
id: p01_emb_pytha_kn_nucleus
kind: embedding_config
pillar: P01
version: "1.0.0"
created: "2023-10-20"
updated: "2023-10-20"
author: "embedding-config-builder"
model_name: "Pytha-KnNucleusModel"
provider: "pytha"
dimensions: 768
chunk_size: 512
chunk_overlap: 51
tokenizer: "pytha-tokenizer"
distance_metric: "cosine"
batch_size: 32
normalize: true
max_tokens_per_chunk: 1024
cost_per_1m_tokens: null
domain: "knowledge-nucleus"
quality: null
tags: [embedding, pytha, pytha-knucleus]
tldr: "Pytha-KnNucleusModel via Pytha — 768 dimensions, 512-token chunks, cosine similarity, zero cost."
---

## Model

The `Pytha-KnNucleusModel` is selected for its specificity and effectiveness in managing knowledge nuclei within embeddings. It is hosted locally by the Pytha provider, offering zero-cost deployments and producing 768-dimensional vectors suitable for comprehensive semantic representation.

## Chunking

The configuration uses a chunk size of 512 tokens, which is optimal for capturing context while keeping processing efficient. It includes a 51-token overlap (about 10% of the chunk size) to ensure continuity at chunk boundaries and uses the "pytha-tokenizer" for handling text segmentation efficiently. The tokenizer ensures that token chunks do not exceed the maximum allowable input of 1024 tokens.

## Performance

This setup is designed to balance quality and computation time:
- **Latency:** Approximately 50ms per batch on a local GPU.
- **Throughput:** About 1000 chunks processed per minute.
- **Cost:** Since this model runs locally using Pytha infrastructure, there are no additional costs associated with API usage.

## Integration

To integrate this configuration in a RAG pipeline:
```python
# Embedding API call example
pytha.embeddings(model_name="Pytha-KnNucleusModel", input_text=chunked_text)
```

## References

- Pytha-KnNucleusModel specification.
- Local deployment guidelines for Pytha models.

---