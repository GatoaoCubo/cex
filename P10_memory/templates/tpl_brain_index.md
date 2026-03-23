---
# TEMPLATE: Brain Index (P10 Memory)
# Valide contra P10_memory/_schema.yaml (types.brain_index)
# Max 3072 bytes

id: p10_bi_{{INDEX_SLUG}}
type: brain_index
lp: P10
title: "Brain Index: {{INDEX_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Brain Index: {{INDEX_NAME}}

## Index Config
```yaml
engine: {{bm25|faiss|hybrid}}
namespace: {{NAMESPACE}}
refresh: {{REFRESH_POLICY}}
```

## Retrieval Policy
- Query shape: {{EXPECTED_QUERY_PATTERN}}
- Ranking signal: {{PRIMARY_RANKING_SIGNAL}}
- Reindex when: {{REINDEX_TRIGGER}}
