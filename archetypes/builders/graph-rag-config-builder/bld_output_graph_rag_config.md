---
kind: output_template
id: bld_output_template_graph_rag_config
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for graph_rag_config production
quality: 8.8
title: "Output Template Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, output_template]
tldr: "Template with vars for graph_rag_config production"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_output_template_reranker_config
  - bld_examples_workflow_node
  - bld_output_template_playground_config
  - bld_examples_graph_rag_config
  - graph-rag-config-builder
  - kc_graph_rag_config
  - bld_schema_graph_rag_config
  - bld_architecture_knowledge_graph
  - p03_sp_graph_rag_config_builder
  - bld_output_template_sdk_example
---

```yaml
---
id: p01_grc_{{id}}.yaml <!-- ^p01_grc_[a-z][a-z0-9_]+.yaml$ -->
name: {{name}} <!-- Configuration name (e.g., "knowledge_graph") -->
description: {{description}} <!-- Brief purpose of this config -->
quality: {{quality}} <!-- MUST be: null -->
version: {{version}} <!-- Semantic version (e.g., "1.0.0") -->
parameters:
  max_depth: {{max_depth}} <!-- Maximum traversal depth for graph -->
  llm_model: {{llm_model}} <!-- Model ID for RAG processing -->
data_sources:
  - {{source1}} <!-- Example: "internal_db" -->
  - {{source2}} <!-- Example: "external_api" -->
model_config:
  type: {{model_type}} <!-- "graph_rag" or "hybrid" -->
  temperature: {{temperature}} <!-- Float between 0-1 -->
```

| Parameter       | Example Value   | Description                     |
|-----------------|------------------|---------------------------------|
| max_depth       | 3                | Maximum graph traversal depth   |
| llm_model       | "llama3:8b"      | Model identifier for RAG        |
| temperature     | 0.7              | Creativity control (0-1)        |

```python
# Example data source config
data_sources = [
    {
        "type": "database",
        "connection": "postgresql://user:pass@host:port/db",
        "tables": ["entities", "relationships"]
    }
]
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_reranker_config]] | sibling | 0.37 |
| [[bld_examples_workflow_node]] | downstream | 0.26 |
| [[bld_output_template_playground_config]] | sibling | 0.24 |
| [[bld_examples_graph_rag_config]] | downstream | 0.23 |
| [[graph-rag-config-builder]] | upstream | 0.22 |
| [[kc_graph_rag_config]] | upstream | 0.22 |
| [[bld_schema_graph_rag_config]] | downstream | 0.20 |
| [[bld_architecture_knowledge_graph]] | downstream | 0.19 |
| [[p03_sp_graph_rag_config_builder]] | upstream | 0.19 |
| [[bld_output_template_sdk_example]] | sibling | 0.19 |
