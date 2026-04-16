---
kind: tools
id: bld_tools_experiment_tracker
pillar: P04
llm_function: CALL
purpose: Real CEX tools available for experiment_tracker production
quality: 9.0
title: "Tools Experiment Tracker"
version: "1.1.0"
author: n03_hybrid_review3
tags: [experiment_tracker, builder, tools]
tldr: "Real CEX tools (verified in _tools/) + industry tracking backends"
domain: "experiment_tracker construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.88
---

## Production Tools (real, present in `_tools/`)
| Tool | Purpose | When |
| :--- | :--- | :--- |
| cex_compile.py | Compile .md -> .yaml artifact | After F6 save |
| cex_score.py | Peer-review scoring (5D) | F7 GOVERN |
| cex_retriever.py | Find similar experiment_tracker artifacts | F3 INJECT |
| cex_doctor.py | Builder health check | Pre-dispatch |
| cex_feedback.py | Quality trend tracking | Post-F8 |
| cex_quality_monitor.py | Regression detection across runs | Weekly |
| signal_writer.py | Signal n05/n07 on completion | F8 |
| cex_hooks.py | Pre-commit validation | F8 |

## Validation Tools
| Tool | Purpose | When |
| :--- | :--- | :--- |
| cex_sanitize.py | ASCII enforcement | Pre-commit |
| cex_doctor.py | ISO structural check | After edit |
| cex_wave_validator.py | Wave-level audit | Mission consolidation |

## External Tracking Backends (integrate, do not fabricate)
- **MLflow** (`mlflow.org`): REST API `/api/2.0/mlflow/runs/*`, Tracking URI, Model Registry
- **Weights & Biases** (`wandb.ai`): Python SDK `wandb.init()`, `wandb.log()`, sweep agents
- **Neptune.ai** (`neptune.ai`): `neptune.init_run()`, namespaces, series
- **Comet ML** (`comet.com`): `Experiment()`, offline/online modes
- **TensorBoard** (`tensorflow.org/tensorboard`): `SummaryWriter`, event files
- **DVC** (`dvc.org`): `dvc exp run`, `params.yaml`, `metrics.json`, `dvc.yaml`

## Anti-Patterns
- Do NOT fabricate tools (`cex_logger.py`, `cex_verify.py`, `cex_audit.py`, `cex_tester.py` do not exist).
- When logging frameworks are needed, emit integration code that calls the real backend SDK (mlflow/wandb/neptune), not a made-up CEX wrapper.
