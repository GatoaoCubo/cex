---
kind: collaboration
id: bld_collaboration_experiment_tracker
pillar: P12
llm_function: COLLABORATE
purpose: How experiment_tracker-builder works in crews with other builders
quality: 8.9
title: "Collaboration Experiment Tracker"
version: "1.0.0"
author: wave1_builder_gen
tags: [experiment_tracker, builder, collaboration]
tldr: "How experiment_tracker-builder works in crews with other builders"
domain: "experiment_tracker construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role
Architects the centralized system for logging, storing, and
visualizing performance metrics, hyperparameters, and artifacts
across all active experiment runs to enable longitudinal analysis.

## Receives From
| Builder | What | Format |
| :--- | :--- | :--- |
| experiment_runner | Live metrics & logs | JSON/Stream |
| experiment_config | Run metadata & tags | YAML/Dict |
| data_pipeline | Dataset version IDs | String/Hash |

## Produces For
| Builder | What | Format |
| :--- | :--- | :--- |
| experiment_analyzer | Aggregated trend data | Parquet/CSV |
| experiment_reporter | Visual plots & summaries | PNG/HTML |
| experiment_config | Run execution IDs | UUID/String |

## Boundary
- Does NOT define single-run hyperparameters (handled by experiment_config).
- Does NOT execute evaluation suites or test logic (handled by benchmark).
- Does NOT manage raw data ingestion or cleaning (handled by data_pipeline).
