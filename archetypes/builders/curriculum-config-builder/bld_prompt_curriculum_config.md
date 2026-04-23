---
kind: instruction
id: bld_prompt_curriculum_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for curriculum_config
quality: null
title: "Curriculum Config Builder - Prompt ISO"
version: "1.0.0"
author: n03_builder
tags: [curriculum_config, builder, instruction]
tldr: "Production instructions for curriculum config artifacts."
domain: "training curriculum"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_curriculum_config
  - bld_schema_curriculum_config
---

# Instructions: How to Produce a curriculum_config

## Phase 1: RESEARCH

1. Identify the training task: pretraining, fine-tuning, multi-task, domain adaptation
2. Catalog available data sources with size and domain
3. Define difficulty metric: perplexity, length, complexity score, annotation confidence
4. Select curriculum strategy: easy-to-hard, self-paced, competence-based, data mixing
5. Determine annealing schedule if applicable
6. Check existing curriculum_config artifacts to avoid duplication

## Phase 2: COMPOSE

1. Read SCHEMA -- source of truth for all fields
2. Fill all frontmatter fields; set quality: null
3. Write Strategy section: selected approach with rationale
4. Write Data Sources section: sources, sizes, mixing ratios
5. Write Difficulty section: metric definition and progression schedule
6. Write Schedule section: warmup, phases, annealing
7. Write Checkpoints section: evaluation points and competence gates

## Phase 3: VALIDATE

1. Check HARD gates: YAML parses, id matches, kind correct
2. Verify strategy specified with rationale
3. Verify difficulty metric defined
4. Verify data sources listed with mixing ratios
5. Cross-check: this is CURRICULUM CONFIG, not data generation or model architecture
