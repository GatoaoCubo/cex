---
kind: tools
id: bld_tools_retrieval_evaluator
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for retrieval_evaluator production
quality: null
title: "Retrieval Evaluator Builder - Tools ISO"
version: "1.0.0"
author: n03_builder
tags: [retrieval_evaluator, builder, tools]
tldr: "Tools available for retrieval evaluator production including scoring, validation, and retrieval."
domain: "retrieval evaluation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_retrieval_evaluator
  - bld_schema_retrieval_evaluator
---

# Tools: retrieval-evaluator-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile artifact to YAML | Phase 3 (post-produce) | ACTIVE |
| cex_score.py | Score artifact quality | Phase 3 (validation) | ACTIVE |
| cex_retriever.py | Find similar existing evaluators | Phase 1 (dedup check) | ACTIVE |
| cex_doctor.py | Health check on produced artifact | Phase 3 (validation) | ACTIVE |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions for retrieval_evaluator |
| CEX Examples | P07_evals/examples/ | Existing retrieval_evaluator artifacts |
| BEIR Benchmark | beir.ai | Standard retrieval benchmark datasets |
| MTEB Leaderboard | huggingface.co/spaces/mteb/leaderboard | Retrieval model rankings |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | -- |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## CEX Pipeline Tools

| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile .md artifact to .yaml | After Write (F8) |
| cex_score.py | Peer-review quality scoring | After production (F7) |
| cex_retriever.py | Discover similar artifacts by TF-IDF | During F3 INJECT |
| cex_doctor.py | Health check builder ISOs | Before dispatch |

## Properties

| Property | Value |
|----------|-------|
| Kind | `tools` |
| Pillar | P04 |
| Domain | retrieval evaluator construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
