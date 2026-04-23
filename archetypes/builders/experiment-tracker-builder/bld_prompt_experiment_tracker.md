---
kind: instruction
id: bld_instruction_experiment_tracker
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for experiment_tracker
quality: 9.0
title: "Instruction Experiment Tracker"
version: "1.1.0"
author: n03_hybrid_review3
tags: [experiment_tracker, builder, instruction]
tldr: "Step-by-step production process for experiment_tracker aligned with MLflow, W&B, Neptune schemas"
domain: "experiment_tracker construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.90
related:
  - p07_qg_experiment_tracker
  - bld_tools_experiment_tracker
  - bld_knowledge_card_experiment_tracker
  - bld_architecture_experiment_tracker
  - p07_qg_12_point_validation
  - p01_kc_experiment_driven_development
  - bld_instruction_playground_config
  - experiment-tracker-builder
  - p03_sp_experiment_config_builder
  - p03_sp_experiment_tracker_builder
---

## Phase 1: FRAME
1. Define experiment_id (UUID or monotonic), experiment_name, project/workspace, owner.
2. Identify research question and falsifiable hypothesis (if/then structure).
3. Enumerate hyperparameters to sweep vs. hold constant; pick search strategy (grid, random, bayes).
4. Select primary metric (single scalar to optimize) and secondary metrics (observability).
5. Bind dataset_ref (point to dataset_card id + version) and model_architecture_ref.

## Phase 2: INSTRUMENT
1. Declare metric schema: name, type (scalar/histogram/image), frequency (per-step/per-epoch), direction (min/max).
2. Declare artifacts: checkpoints, configs, logs, predictions. Size budget per run.
3. Capture environment: git SHA, python version, torch/jax version, GPU type, OS.
4. Set tags: phase (dev/staging/prod), team, tracker-backend (mlflow/wandb/neptune/comet/dvc).
5. Attach run to parent experiment; define sweep_id if parameter search.

## Phase 3: EXECUTE
1. Log params once at run start (immutable).
2. Log metrics continuously; flush at epoch boundaries to survive crashes.
3. Log artifacts at checkpoints and final state; version with content hash.
4. Emit STATUS transitions: QUEUED -> RUNNING -> FINISHED | FAILED | KILLED.
5. On failure: log stack trace to artifacts, preserve last-known-good checkpoint.

## Phase 4: GOVERN
1. Enforce reproducibility: seeds logged, dataset version pinned, env captured.
2. Validate metric schema stays stable across runs (schema drift prevention).
3. Link child runs to parent sweep; compute pareto-front for multi-metric sweeps.
4. Write frontmatter per bld_schema_experiment_tracker.md; populate body per bld_output_template_experiment_tracker.md.
5. Gate via bld_quality_gate_experiment_tracker.md; compile and commit.

## Reference Standards
- MLflow Tracking API (runs, experiments, metrics, params, artifacts)
- Weights & Biases (project, entity, run, sweep, artifacts)
- Neptune.ai (experiment, run, series, namespace)
- Comet ML (experiment key, workspace, logged assets)
- TensorBoard (scalar, histogram, image, graph, hparams)
- DVC (dvc.yaml stages, params.yaml, metrics.json)


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_qg_experiment_tracker]] | downstream | 0.26 |
| [[bld_tools_experiment_tracker]] | downstream | 0.25 |
| [[bld_knowledge_card_experiment_tracker]] | upstream | 0.24 |
| [[bld_architecture_experiment_tracker]] | downstream | 0.20 |
| [[p07_qg_12_point_validation]] | downstream | 0.17 |
| [[p01_kc_experiment_driven_development]] | upstream | 0.17 |
| [[bld_instruction_playground_config]] | sibling | 0.17 |
| [[experiment-tracker-builder]] | downstream | 0.17 |
| [[p03_sp_experiment_config_builder]] | related | 0.16 |
| [[p03_sp_experiment_tracker_builder]] | related | 0.16 |
