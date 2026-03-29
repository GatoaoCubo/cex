---

```yaml
id: p01_emb_example_config
kind: embedding_config
pillar: P01
version: "1.0.0"
created: "2023-10-04"
updated: "2023-10-04"
author: "embedding-config-builder"
model_name: "bert_base_uncased"
provider: "huggingface"
dimensions: 768
chunk_size: 512
overlap: 51
tokenizer: "bert-base-uncased-tokenizer"
distance_metric: "cosine"
batch_size: 32
normalize: true
max_tokens: 512
cost_per_1m_tokens: null
domain: "knowledge-retrieval"
quality: null
tags: [embedding, huggingface, bert]
tldr: "BERT base uncased via Hugging Face—768d, 512-token chunks, cosine similarity, zero cost local."
```

---

## Model
BERT Base Uncased model, provided by Hugging Face, with 768 dimensions. It uses the BERT tokenizer and works well for a variety of NLP tasks including retrieval.

## Chunking
The text is divided into chunks of 512 tokens, with an overlap of 51 tokens to ensure continuity at the boundaries. The tokenizer used is "bert-base-uncased-tokenizer".

## Performance
The model operates locally, so the cost is zero. The batch size is set to 32 vectors per embedding operation. Normalization is set to true for accurate cosine similarity calculations.

## Integration
Leverage this configuration in an embedding layer of a retrieval-augmented generation pipeline. Process text through the "bert_base_uncased" embedding model to obtain normalized vectors suitable for cosine similarity-based retrieval.

## References
- Hugging Face BERT model card
- Embedding and retrieval best practices documentation