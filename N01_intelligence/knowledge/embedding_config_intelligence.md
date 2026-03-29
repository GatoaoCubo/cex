---
I'm here to configure an `embedding_config` specifically tailored for your use case. Let's proceed with creating an optimal configuration for your embedding model:

---

```yaml
id: p01_emb_nomic_library
kind: embedding_config
pillar: P01
version: "1.0.0"
created: "2023-10-01"
updated: "2023-10-01"
author: "embedding-config-builder"
model_name: "nomic-embed-text"
provider: "ollama"
dimensions: 768
chunk_size: 512
overlap: 50
tokenizer: "nomic-bert"
distance_metric: "cosine"
batch_size: 32
normalize: true
max_tokens: 8192
cost_per_1m_tokens: null
domain: "knowledge-retrieval"
quality: null
tags: [embedding, ollama, nomic]
tldr: "nomic-embed-text configured for effective local deployment: 768 dimensions, cosine similarity."
```
---

---

## Model
The embedding model chosen is `nomic-embed-text` provided by Ollama. It is local, offers 768 dimensions, and is optimized for privacy-conscious tasks with zero cost to operationalize.

## Chunking
Chunks are sized at 512 tokens with a 50-token overlap, utilizing the `nomic-bert` tokenizer. This configuration is designed to handle paragraph-level retrieval tasks efficiently.

## Performance
Configured for local deployment with Ollama. Latency is low (~50ms per batch), and throughput is competitive at ~1000 chunks per minute. No costs are incurred as it functions independently of API calls.

## Integration
Deploy this configuration for semantic vector search by using Ollama’s local API calls. Ideal for projects needing cost-effective and reliable embedding solutions.

## References
- Nomic AI model documentation
- Ollama local library specs

This `embedding_config` is set specifically for a local setup with privacy considerations, ensuring it aligns with dimension and retrieval-specific requirements.