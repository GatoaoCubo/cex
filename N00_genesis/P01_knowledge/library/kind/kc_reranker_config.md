---
id: kc_reranker_config
kind: knowledge_card
title: Reranker Configuration
version: 1.0.0
quality: 8.5
pillar: P01
density_score: 1.0
updated: "2026-04-15"
---

## Reranker Configuration Parameters

**Model Configuration**
- `model_name`: Name of the reranking model (e.g., `rerank-1.0`)
- `model_version`: Version of the model (e.g., `v2.1`)
- `model_params`: Additional parameters for model initialization

**Strategy Parameters**
- `strategy`: Reranking strategy (e.g., `confidence`, `diversity`, `relevance`)
- `threshold`: Minimum score threshold for item inclusion
- `max_items`: Maximum number of items to return
- `weighting`: Weight distribution across ranking criteria

**Example Configuration**
```yaml
model_name: rerank-1.0
model_version: v2.1
strategy: confidence
threshold: 0.75
max_items: 10
weighting:
  relevance: 0.6
  diversity: 0.3
  confidence: 0.1
```
