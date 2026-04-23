---
kind: config
id: bld_config_synthetic_data_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits for synthetic_data_config
quality: null
title: "Synthetic Data Config Builder - Config ISO"
version: "1.0.0"
author: n03_builder
tags: [synthetic_data_config, builder, config]
tldr: "Production config for synthetic data config: naming, paths, and constraints."
domain: "synthetic data generation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_schema_synthetic_data_config
---

# Config: synthetic_data_config Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | p01_sdc_{config_slug}.md | p01_sdc_self_instruct_qa.md |
| Builder directory | kebab-case | synthetic-data-config-builder/ |
| Frontmatter fields | snake_case | generation_method, source_model |

## File Paths

1. Output: P01_knowledge/examples/p01_sdc_{slug}.md
2. Compiled: P01_knowledge/compiled/p01_sdc_{slug}.yaml

## Size Limits

1. Body: max 2048 bytes
2. Density: >= 0.85

## Generation Method Enum

| Method | Use Case | Complexity |
|--------|----------|------------|
| self_instruct | General instruction generation | Low |
| evol_instruct | Progressive complexity | Medium |
| backtranslation | Paraphrase augmentation | Low |
| seed_expand | Seed-based expansion | Medium |
