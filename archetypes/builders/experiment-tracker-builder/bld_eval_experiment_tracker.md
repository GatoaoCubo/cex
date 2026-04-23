---
kind: quality_gate
id: p07_qg_experiment_tracker
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for experiment_tracker
quality: 9.0
title: "Quality Gate Experiment Tracker"
version: "1.1.0"
author: n03_hybrid_review3
tags: [experiment_tracker, builder, quality_gate]
tldr: "HARD gates (H01-H07) + SOFT scoring (D1-D9, weights=1.00) for experiment_tracker artifacts"
domain: "experiment_tracker construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.90
related:
  - bld_examples_experiment_tracker
  - p11_qg_experiment_config
  - bld_instruction_experiment_tracker
  - p11_qg_kind_builder
  - p03_sp_experiment_tracker_builder
  - p11_qg_function_def
  - p02_qg_training_method
  - p07_qg_eval_framework
  - bld_knowledge_card_quality_gate
  - p06_vs_frontmatter
---

## Quality Gate

## Scope
Validates that an experiment_tracker artifact can be reliably ingested by MLflow/W&B/Neptune-class backends and supports longitudinal comparison across runs.

## HARD Gates (all must pass; any fail -> reject)
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML Frontmatter Parse | Invalid YAML, missing `---` delimiters |
| H02 | ID Pattern | Regex mismatch: `^p07_et_[a-z0-9_]+\.md$` |
| H03 | Kind Match | `kind:` != `experiment_tracker` |
| H04 | Required Fields | Missing id, kind, pillar, title, version, metric_primary, hypothesis |
| H05 | Pillar Correctness | `pillar:` != `P07` |
| H06 | Version Format | Non-SemVer (not `MAJOR.MINOR.PATCH`) |
| H07 | Metric Schema | `metric_primary` missing type or direction (min/max) |

## SOFT Scoring (weighted sum; target >= 8.5)
| ID | Dimension | Weight | Scoring Guide |
|----|-----------|--------|---------------|
| D1 | Hypothesis Clarity | 0.12 | Falsifiable if/then structure present |
| D2 | Param Completeness | 0.12 | All tuned hyperparameters enumerated with types |
| D3 | Metric Schema Rigor | 0.15 | Primary + secondaries with type+direction+frequency |
| D4 | Reproducibility | 0.15 | git SHA, seeds, env, deps all logged |
| D5 | Dataset Lineage | 0.10 | dataset_ref points to versioned dataset_card |
| D6 | Artifact Policy | 0.08 | Checkpoint/logs/config declared with size budget |
| D7 | Status Machine | 0.08 | QUEUED/RUNNING/FINISHED/FAILED transitions defined |
| D8 | Cross-Backend Compat | 0.10 | Fields map cleanly to MLflow AND W&B AND Neptune |
| D9 | Observability | 0.10 | Logging frequency + flush policy specified |

Sum = 1.00

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | Accept, auto-publish |
| 8.5-8.9 | Accept with minor annotations |
| 7.0-8.4 | Return for surgical revision |
| < 7.0 | Rebuild via 8F pipeline |

## Anti-Patterns (auto-fail)
- Hardcoded run_id collisions (breaks longitudinal comparison)
- Metrics logged without direction (optimizer can't compare runs)
- Missing env capture (reproducibility void)
- Mutable params (changing params after run start)

## Examples

## Golden Example
---
kind: experiment_tracker
metadata:
  project_name: "transformer-layer-scaling"
  experiment_group: "width-vs-depth-study"
  total_runs: 3
runs:
  - run_id: "run_alpha"
    timestamp: "2023-11-01T08:00:00Z"
    configuration:
      layers: 6
      hidden_dim: 512
      heads: 8
    results:
      perplexity: 12.4
      training_loss: 0.85
      throughput_tokens_sec: 1200
  - run_id: "run_beta"
    timestamp: "2023-11-01T14:30:00Z"
    configuration:
      layers: 12
      hidden_dim: 512
      heads: 8
    results:
      perplexity: 10.2
      training_loss: 0.72
      throughput_tokens_sec: 850
  - run_id: "run_gamma"
    timestamp: "2023-11-02T09:15:00Z"
    configuration:
      layers: 12
      hidden_dim: 768
      heads: 12
    results:
      perplexity: 9.8
      training_loss: 0.68
      throughput_tokens_sec: 600
---

## Anti-Example 1: Single experiment configuration
---
kind: experiment_config
parameters:
  learning_rate: 0.0001
  batch_size: 32
  optimizer: "adamw"
---
## Why it fails
This is an `experiment_config`. It only contains the settings for a single execution. An `experiment_tracker` must contain a collection of multiple runs to allow for comparison and historical tracking.

## Anti-Example 2: Evaluation benchmark
---
kind: benchmark_suite
dataset: "GLUE_benchmark"
model_version: "v2.1-final"
evaluation_metrics:
  mnli_accuracy: 0.88
  sst2_accuracy: 0.92
  cola_score: 0.65
---
## Why it fails
This is a `benchmark`. It focuses on the static evaluation of a specific model version against a fixed dataset. An `experiment_tracker` should focus on the iterative process of changing parameters and observing the resulting changes in performance across different attempts.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
