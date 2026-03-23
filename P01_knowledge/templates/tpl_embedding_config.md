---
# TEMPLATE: Embedding Config (P01 Knowledge)
# Valide contra P01_knowledge/_schema.yaml (types.embedding_config)
# Max 512 bytes

id: p01_emb_{{MODEL_SLUG}}
type: embedding_config
lp: P01
model_name: {{EMBEDDING_MODEL_NAME}}
dimensions: {{DIMENSIONS_INT}}
chunk_size: {{CHUNK_SIZE_INT}}
---

# Embedding Config: {{EMBEDDING_MODEL_NAME}}

## Parameters
```yaml
model_name: {{EMBEDDING_MODEL_NAME}}
dimensions: {{DIMENSIONS_INT}}
chunk_size: {{CHUNK_SIZE_INT}}
overlap: {{OVERLAP_INT}}
distance_metric: {{cosine|dot|l2}}
```

## Notes
- Use when: {{WHEN_TO_USE}}
- Tradeoff: {{PRIMARY_TRADEOFF}}
