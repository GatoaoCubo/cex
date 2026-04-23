---
kind: output_template
id: bld_output_template_reranker_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for reranker_config production
quality: 8.8
title: "Output Template Reranker Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [reranker_config, builder, output_template]
tldr: "Template with vars for reranker_config production"
domain: "reranker_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_graph_rag_config
  - bld_output_template_playground_config
  - kc_reranker_config
  - bld_schema_reranker_config
  - bld_examples_workflow_node
  - embedding_config_intelligence
  - kc_model_registry
  - bld_schema_graph_rag_config
  - bld_examples_workflow_primitive
  - bld_examples_tts_provider
---

```yaml
---
id: p01_rr_{{name}}.yaml  # Use lowercase letters, numbers, underscores (e.g., p01_rr_my_reranker)
name: {{name}}            # Human-readable name (e.g., "My Reranker")
description: {{description}}  # Purpose of this configuration (e.g., "Rank documents by relevance")
version: {{version}}      # Semantic version (e.g., "1.0.0")
quality: null             # Must remain null
schema: {{schema_version}}  # Schema version (e.g., "v1")
---
```

```yaml
# Example Reranker Configuration
parameters:
  model: {{model}}        # ML model name (e.g., "bert-base-uncased")
  threshold: {{threshold}}  # Scoring cutoff (e.g., 0.7)
  max_depth: {{max_depth}}  # Search depth limit (e.g., 5)
```

<!-- Table: Parameter Definitions -->
| Field       | Type   | Description                          | Example       |
|-------------|--------|--------------------------------------|---------------|
| `model`     | string | ML model identifier                  | "bert-base"   |
| `threshold` | float  | Minimum score for inclusion        | 0.7           |
| `max_depth` | int    | Maximum recursion depth            | 5             |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_graph_rag_config]] | sibling | 0.28 |
| [[bld_output_template_playground_config]] | sibling | 0.26 |
| [[kc_reranker_config]] | upstream | 0.23 |
| [[bld_schema_reranker_config]] | downstream | 0.22 |
| [[bld_examples_workflow_node]] | downstream | 0.22 |
| [[embedding_config_intelligence]] | upstream | 0.21 |
| [[kc_model_registry]] | upstream | 0.20 |
| [[bld_schema_graph_rag_config]] | downstream | 0.20 |
| [[bld_examples_workflow_primitive]] | downstream | 0.20 |
| [[bld_examples_tts_provider]] | downstream | 0.20 |
