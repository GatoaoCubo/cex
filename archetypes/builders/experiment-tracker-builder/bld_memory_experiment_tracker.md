---
kind: learning_record
id: p10_lr_experiment_tracker_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for experiment_tracker construction
quality: 8.7
title: "Learning Record Experiment Tracker"
version: "1.0.0"
author: wave1_builder_gen
tags: [experiment_tracker, builder, learning_record]
tldr: "Learned patterns and pitfalls for experiment_tracker construction"
domain: "experiment_tracker construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p10_lr_tts_provider_builder
  - p03_sp_experiment_tracker_builder
  - bld_knowledge_card_experiment_tracker
  - kc_experiment_tracker
  - p10_lr_agent_computer_interface_builder
  - p10_lr_stt_provider_builder
  - p10_lr_builder-builder
  - experiment-tracker-builder
  - p10_lr_model_registry_builder
  - p01_kc_meta_factory
---

## Observation
Builders often struggle with managing the lifecycle of the tracker, leading to data loss during experiment crashes. There is also a common tendency to overlook the need for a unified, versioned schema, which prevents meaningful longitudinal comparisons.

## Pattern
Effective builders utilize a factory pattern to instantiate trackers with specific backends (e.g., local, MLflow, or WandB). Decoupling the data collection interface from the storage implementation ensures the system remains extensible and testable.

## Evidence
Reviewed tracker-builder implementations show that a provider-agnostic API is essential for supporting multiple logging backends.

## Recommendations
* Use a factory pattern to instantiate trackers based on configuration.
* Enforce a strict, versioned schema for all recorded metrics and parameters.
* Implement automatic environment snapshots (e.g., git commit, library versions).
* Decouple the logging interface from the specific storage backend.
* Provide a mechanism to reconstruct experiment state from logged metadata.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_tts_provider_builder]] | sibling | 0.21 |
| [[p03_sp_experiment_tracker_builder]] | upstream | 0.21 |
| [[bld_knowledge_card_experiment_tracker]] | upstream | 0.20 |
| [[kc_experiment_tracker]] | upstream | 0.19 |
| [[p10_lr_agent_computer_interface_builder]] | related | 0.19 |
| [[p10_lr_stt_provider_builder]] | sibling | 0.17 |
| [[p10_lr_builder-builder]] | sibling | 0.17 |
| [[experiment-tracker-builder]] | upstream | 0.16 |
| [[p10_lr_model_registry_builder]] | sibling | 0.15 |
| [[p01_kc_meta_factory]] | upstream | 0.15 |
