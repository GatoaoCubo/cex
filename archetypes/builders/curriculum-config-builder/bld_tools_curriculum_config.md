---
kind: tools
id: bld_tools_curriculum_config
pillar: P04
llm_function: CALL
purpose: Tools available for curriculum_config production
quality: null
title: "Curriculum Config Builder - Tools ISO"
version: "1.0.0"
author: n03_builder
tags: [curriculum_config, builder, tools]
tldr: "Tool registry for curriculum config builder: CEX pipeline tools (compile, score, retrieve), file system ops (Read/Write/Edit/Glob/Grep), and domain-specific automation for training data ordering, difficulty scheduling, and adaptive pacing configuration."
domain: "training curriculum"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_curriculum_config
---

# Tools: curriculum-config-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile artifact to YAML | Phase 3 | ACTIVE |
| cex_score.py | Score artifact quality | Phase 3 | ACTIVE |
| cex_retriever.py | Find similar configs | Phase 1 | ACTIVE |
| cex_doctor.py | Health check | Phase 3 | ACTIVE |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P07_evals/_schema.yaml | Field definitions |
| Bengio 2009 | arxiv.org/abs/0904.3541 | Original curriculum learning paper |
| DoReMi | arxiv.org/abs/2305.10429 | Optimized data mixing for LLM pretraining |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Permitted |
| DENIED | (none) | -- |

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
| Domain | curriculum config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
