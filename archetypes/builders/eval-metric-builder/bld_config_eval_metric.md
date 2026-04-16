---
kind: config
id: bld_config_eval_metric
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for eval_metric production
quality: 8.6
title: "Config Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, config]
tldr: "Naming, paths, limits for eval_metric production"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Naming Convention
Pattern: `p07_em_<metric_name>`
Examples:
- p07_em_accuracy
- p07_em_f1_score

## Paths
Artifacts: `/mnt/artifacts/p07/em/<metric_name>/`
Checksum: `/mnt/checksums/p07/em/<metric_name>.sha256`
Note: Use POSIX-compliant paths only

## Limits
max_bytes: 4096
max_turns: 100
effort_level: 3

## Hooks
pre_build: null
post_build: null
on_error: null
on_quality_fail: null
