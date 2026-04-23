---
kind: instruction
id: bld_prompt_distillation_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for distillation_config
quality: null
title: "Distillation Config Builder - Prompt ISO"
version: "1.0.0"
author: n03_builder
tags: [distillation_config, builder, instruction]
tldr: "Production instructions for distillation config artifacts."
domain: "model distillation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_distillation_config
  - bld_schema_distillation_config
---

# Instructions: How to Produce a distillation_config

## Phase 1: RESEARCH

1. Identify the teacher model (architecture, parameter count, performance)
2. Define the compression target (parameter reduction ratio, latency budget)
3. Select student architecture (subset of teacher or different architecture)
4. Determine distillation method: logit matching, feature distillation, or progressive
5. Identify training data source: labeled, unlabeled, or synthetic
6. Check existing distillation_config artifacts to avoid duplication

## Phase 2: COMPOSE

1. Read SCHEMA -- source of truth for all fields
2. Fill all frontmatter fields; set quality: null
3. Write Teacher section: model ID, parameter count, performance baseline
4. Write Student section: architecture, target parameter count
5. Write Training section: temperature, alpha, learning rate, epochs
6. Write Loss section: KD loss weight, task loss weight, composition formula
7. Write Evaluation section: checkpoints, quality thresholds, regression criteria

## Phase 3: VALIDATE

1. Check HARD gates: YAML parses, id matches, kind correct
2. Verify teacher and student models specified
3. Verify temperature > 1 for knowledge transfer
4. Verify loss composition adds to 1.0
5. Cross-check: this is DISTILLATION CONFIG, not training config or model architecture
6. If score < 8.0: revise before outputting
