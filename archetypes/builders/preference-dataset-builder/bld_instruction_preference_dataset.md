---
kind: instruction
id: bld_instruction_preference_dataset
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for preference_dataset
pattern: 3-phase pipeline (define -> compose -> validate)
quality: 7.1
title: "Instruction Preference Dataset"
version: "1.0.0"
author: n03_builder
tags: [preference_dataset, builder, instruction]
tldr: "3-phase process: define scope and annotation schema, compose pairs with metadata, validate quality gates."
domain: "preference dataset construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Instructions: How to Produce a preference_dataset

## Phase 1: DEFINE
1. Identify the training objective: RLHF reward modeling, DPO, constitutional AI, or custom preference signal
2. Declare domain and task_type (e.g., instruction-following, coding, summarization, safety)
3. Determine annotation method: human raters, model-assisted labeling, constitutional criteria
4. Set quality thresholds: minimum agreement_rate (>= 0.8 recommended), min_rater_count (>= 2)
5. Define preference_signal: what makes "chosen" better than "rejected" (helpfulness, safety, accuracy)
6. Determine dataset scope: total_pairs target, language, source_distribution
7. Set train/eval/test split (default: 80/10/10)
8. Check for existing preference_dataset artifacts with overlapping domain to avoid duplication

## Phase 2: COMPOSE
1. Read SCHEMA.md -- source of truth for all fields
2. Read OUTPUT_TEMPLATE.md -- fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null -- never self-score)
4. Write pairs section: array of {prompt, chosen, rejected, metadata} triplets
5. Declare annotation_method with rater_count, agreement_rate, confidence
6. Write quality_filters section: threshold values and exclusion criteria
7. Declare split_ratios and total_pairs count
8. Write Overview: 2 sentences on objective and scope
9. Write Annotation Protocol: criteria defining chosen vs rejected
10. Write Quality Filters: automated and human checks applied
11. Verify body <= 4096 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `^p11_pd_[a-z][a-z0-9_]+$`
4. Confirm kind == preference_dataset
5. Confirm pairs array has >= 1 example (schema validation)
6. Confirm agreement_rate >= 0.0 and <= 1.0
7. Confirm preference_signal is declared (not empty)
8. HARD gates: frontmatter valid, id pattern matches, pairs present, signal declared
9. SOFT gates: score against QUALITY_GATES.md -- target >= 8.0
10. Cross-check kind boundaries: no expected outputs without alternatives (eval_dataset or golden_test)? No reward model weights (model artifact, not dataset)?
11. Revise if score < 8.0 -- most common fix: add annotation_method detail or quality filter criteria
