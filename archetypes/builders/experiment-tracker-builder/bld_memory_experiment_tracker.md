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
