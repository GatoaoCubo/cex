---
kind: instruction
id: bld_prompt_retrieval_evaluator
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for retrieval_evaluator
pattern: 3-phase pipeline (research -> compose -> validate)
quality: null
title: "Retrieval Evaluator Builder - Prompt ISO"
version: "1.0.0"
author: n03_builder
tags: [retrieval_evaluator, builder, instruction]
tldr: "Step-by-step instructions for producing retrieval evaluator artifacts via research, compose, validate phases."
domain: "retrieval evaluation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.88
related:
  - bld_model_retrieval_evaluator
  - bld_schema_retrieval_evaluator
  - bld_output_retrieval_evaluator
---

# Instructions: How to Produce a retrieval_evaluator

## Phase 1: RESEARCH

1. Identify the retrieval system under evaluation: dense retrieval, sparse (BM25), hybrid, or RAG
2. Determine the use case: question answering, document search, recommendation, or fact verification
3. Select primary metrics matching the use case: NDCG@k for ranked results, MRR for single-answer tasks, MAP for full-list evaluation
4. Define relevance judgment scale: binary (relevant/not) or graded (0-3)
5. Identify baseline system for comparison (BM25 is the standard baseline)
6. Check existing retrieval_evaluator artifacts to avoid duplication

## Phase 2: COMPOSE

1. Read SCHEMA -- source of truth for all fields
2. Read OUTPUT TEMPLATE -- fill the template following schema constraints
3. Fill all frontmatter fields; set quality: null -- never self-score
4. Write Metrics section: primary and secondary metrics with formulas
5. Write Query Set section: minimum size, construction methodology, domain coverage
6. Write Judgment section: relevance scale, annotator agreement threshold
7. Write Baseline section: reference system, expected score ranges
8. Write Thresholds section: pass/fail criteria, regression detection rules

## Phase 3: VALIDATE

1. Check all HARD gates: YAML parses, id matches pattern, kind is retrieval_evaluator
2. Verify at least 2 metrics defined with formulas
3. Verify query set requirements specified (minimum size, domain)
4. Verify baseline defined with expected score range
5. Verify thresholds set for pass/fail/regression
6. Cross-check: this is EVALUATION methodology, not retrieval logic or index config
7. If score < 8.0: revise before outputting
