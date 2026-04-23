---
kind: config
id: bld_config_distillation_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions and operational constraints for distillation_config
quality: null
title: "Distillation Config Builder - Config ISO"
version: "1.0.0"
author: n03_builder
tags: [distillation_config, builder, config]
tldr: "Production config for distillation config: naming, paths, and constraints."
domain: "model distillation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_schema_distillation_config
---

# Config: distillation_config Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | p02_dc_{config_slug}.md | p02_dc_gpt4_to_llama3.md |
| Builder directory | kebab-case | distillation-config-builder/ |
| Frontmatter fields | snake_case | teacher_model, compression_ratio |

## File Paths

1. Output: P02_model/examples/p02_dc_{slug}.md
2. Compiled: P02_model/compiled/p02_dc_{slug}.yaml

## Size Limits

1. Body: max 2048 bytes
2. Density: >= 0.85

## Standard Temperature Ranges

| Temperature | Effect | Use Case |
|------------|--------|----------|
| 1.0 | No softening (hard targets only) | Not recommended for KD |
| 2-5 | Mild softening | Small teacher-student gap |
| 5-10 | Moderate softening | Standard distillation |
| 10-20 | Heavy softening | Large capacity gap |
