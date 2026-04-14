---
kind: collaboration
id: bld_collaboration_model_registry
pillar: P12
llm_function: COLLABORATE
purpose: How model_registry-builder works in crews with other builders
quality: null
title: "Collaboration Model Registry"
version: "1.0.0"
author: wave1_builder_gen
tags: [model_registry, builder, collaboration]
tldr: "How model_registry-builder works in crews with other builders"
domain: "model_registry construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role
Central orchestrator for aggregating, versioning, and indexing model
artifacts, metadata, and lineage into a unified, searchable catalog.

## Receives From
| Builder | What | Format |
| :--- | :--- | :--- |
| checkpoint_builder | Model weights & artifacts | .bin, .safetensors |
| model_card_builder | Model performance metrics | .json, .yaml |
| data_lineage_builder | Dataset & feature references | .manifest, .parquet |

## Produces For
| Builder | What | Format |
| :--- | :--- | :--- |
| deployment_engine | Model lookup & deployment URI | REST API, URI |
| monitoring_agent | Model version & drift targets | JSON, Prometheus |
| audit_service | Provenance & compliance logs | Structured Logs |

## Boundary
Does not generate weights (checkpoint_builder).
Does not define single model specs (model_card_builder).
Does not manage live inference (deployment_engine).
