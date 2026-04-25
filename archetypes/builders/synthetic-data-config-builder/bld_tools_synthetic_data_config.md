---
kind: tools
id: bld_tools_synthetic_data_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for synthetic_data_config production
quality: null
title: "Synthetic Data Config Builder - Tools ISO"
version: "1.0.0"
author: n03_builder
tags: [synthetic_data_config, builder, tools]
tldr: "Tool registry for synthetic data config builder: CEX pipeline tools (compile, score, retrieve), file system ops (Read/Write/Edit/Glob/Grep), and domain-specific automation for synthetic training data generation pipeline configuration."
domain: "synthetic data generation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_synthetic_data_config
  - bld_schema_synthetic_data_config
---

# Tools: synthetic-data-config-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_compile.py | Compile artifact to YAML | Phase 3 (post-produce) | ACTIVE |
| cex_score.py | Score artifact quality | Phase 3 (validation) | ACTIVE |
| cex_retriever.py | Find similar existing configs | Phase 1 (dedup check) | ACTIVE |
| cex_doctor.py | Health check on produced artifact | Phase 3 | ACTIVE |

## Data Sources

| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P01_knowledge/_schema.yaml | Field definitions |
| Self-Instruct paper | arxiv.org/abs/2212.10560 | Method reference |
| Evol-Instruct paper | arxiv.org/abs/2304.12244 | Complexity evolution method |

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
| Domain | synthetic data config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
