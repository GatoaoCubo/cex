---
id: ex_dag_content_factory
kind: dag
pillar: P12
title: "Example DAG: Content Factory"
version: 1.0.0
created: 2026-04-16
updated: 2026-04-16
author: n02_marketing
domain: content_factory_pipeline
quality: 8.7
brand_placeholders:
  - BRAND_VOICE
  - BRAND_AUDIENCE
  - BRAND_CONTENT_THEMES
tags: [dag, content-factory, orchestration, n02]
tldr: "Directed graph for parallelizable content operations across research, copy, media, QA, and publishing."
density_score: 0.91
related:
  - p11_qg_dag
  - bld_examples_dag
  - p10_lr_dag_builder
  - p12_dag_builder_8f
  - bld_knowledge_card_dag
  - workflow-node-builder
  - bld_instruction_dag
  - p01_kc_social_publisher
  - p11_qg_memory_scope
  - p11_qg_retriever_config
---

# Node Graph

```yaml
nodes:
  - intake_brief
  - select_angle
  - draft_copy
  - draft_media
  - validate_copy
  - validate_html
  - schedule_publish
  - publish
  - capture_feedback
edges:
  - intake_brief -> select_angle
  - select_angle -> draft_copy
  - select_angle -> draft_media
  - draft_copy -> validate_copy
  - draft_media -> validate_html
  - validate_copy -> schedule_publish
  - validate_html -> schedule_publish
  - schedule_publish -> publish
  - publish -> capture_feedback
```

## Routing Notes

- `select_angle` chooses the strongest audience/content-theme fit.
- `draft_copy` and `draft_media` can run in parallel.
- Publishing is blocked until both validation branches pass.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_dag]] | upstream | 0.26 |
| [[bld_examples_dag]] | upstream | 0.23 |
| [[p10_lr_dag_builder]] | upstream | 0.21 |
| [[p12_dag_builder_8f]] | sibling | 0.19 |
| [[bld_knowledge_card_dag]] | upstream | 0.18 |
| [[workflow-node-builder]] | related | 0.17 |
| [[bld_instruction_dag]] | upstream | 0.17 |
| [[p01_kc_social_publisher]] | upstream | 0.17 |
| [[p11_qg_memory_scope]] | upstream | 0.16 |
| [[p11_qg_retriever_config]] | upstream | 0.16 |
