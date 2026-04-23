---
kind: collaboration
id: bld_collaboration_model_registry
pillar: P12
llm_function: COLLABORATE
purpose: How model_registry-builder works in crews with other builders
quality: 8.9
title: "Collaboration Model Registry"
version: "1.0.0"
author: wave1_builder_gen
tags: [model_registry, builder, collaboration]
tldr: "How model_registry-builder works in crews with other builders"
domain: "model_registry construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - model-registry-builder
  - bld_knowledge_card_model_registry
  - bld_architecture_model_registry
  - bld_instruction_model_registry
  - p03_sp_model_registry_builder
  - kc_model_registry
  - p11_qg_model_registry
  - bld_collaboration_model_card
  - model-card-builder
  - p10_lr_model_registry_builder
---

## Crew Role
Central orchestrator for aggregating, versioning, and indexing model
artifacts, metadata, and lineage into a unified, searchable catalog.

## Receives From

| Nucleus | What | Format |
| :--- | :--- | :--- |
| N01 Research | Training run reports, benchmark results, dataset lineage refs | knowledge_card, .yaml |
| N03 Build | New model artifact entries (weights URI, config, tokenizer) | model_registry draft, .yaml |
| N04 Knowledge | Domain taxonomy updates, embedding model provenance | knowledge_card, chunk_strategy |
| N05 Operations | Evaluation outputs, CI test results, deployment configs | eval_metric, env_config |

## Produces For

| Nucleus | What | Format |
| :--- | :--- | :--- |
| N05 Operations | Registry lookup for deployment: model URI + stage + version | model_registry entry |
| N04 Knowledge | Embedding model provenance for RAG pipelines | model_registry reference |
| N07 Orchestrator | Registry status reports for mission gates | knowledge_card |

## Boundary
Does not generate raw model weights (checkpoint kind -- N03 scope).
Does not define qualitative model specs (model_card kind -- N04 scope).
Does not manage live inference endpoints (deploy config -- N05 scope).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[model-registry-builder]] | upstream | 0.41 |
| [[bld_knowledge_card_model_registry]] | upstream | 0.35 |
| [[bld_architecture_model_registry]] | upstream | 0.35 |
| [[bld_instruction_model_registry]] | upstream | 0.35 |
| [[p03_sp_model_registry_builder]] | upstream | 0.34 |
| [[kc_model_registry]] | upstream | 0.30 |
| [[p11_qg_model_registry]] | upstream | 0.27 |
| [[bld_collaboration_model_card]] | sibling | 0.25 |
| [[model-card-builder]] | upstream | 0.25 |
| [[p10_lr_model_registry_builder]] | upstream | 0.25 |
