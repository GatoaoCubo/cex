---

```yaml
id: p01_emb_shaka_v1
kind: embedding_config
pillar: P01
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "embedding-config-builder"
model_name: "bert_base_multilingual_cased"
provider: "huggingface"
dimensions: 768
chunk_size: 512
overlap: 50
tokenizer: "BERT"
distance_metric: "cosine"
batch_size: 32
normalize: true
max_tokens: 512
cost_per_1m_tokens: null
domain: "research-intelligence"
quality: null
tags: [embedding, huggingface, bert]
tldr: "BERT base multilingual model for Shaka — 768d, 512-token chunks, cosine similarity, local processing"
```

---

## Model
The BERT base multilingual cased model is selected for its robust performance across multiple languages. Provided by Hugging Face, it outputs 768-dimensional vectors, making it a balanced choice for semantic representation in multilingual contexts.

## Chunking
This configuration uses a chunk size of 512 tokens with a 50-token overlap to maintain context continuity. The tokenizer aligns with BERT's architecture, ensuring that chunking does not exceed the model's token context window.

## Performance
- Latency: Dependent on local processing capabilities, generally low when batch processed
- Throughput: High processing rate due to local computation
- Cost: Zero for local use, making it ideal for ongoing research activities
- Quality: Established high performance in semantic understanding tasks

## Integration
To use this configuration in a RAG pipeline, input text is first tokenized using the BERT tokenizer, then chunked into 512-token segments with specified overlap. The cosine distance metric ensures effective semantic similarity measurement during retrieval.

## References
- BERT model card on Hugging Face
- Research papers on multilingual semantic search using BERT-based models