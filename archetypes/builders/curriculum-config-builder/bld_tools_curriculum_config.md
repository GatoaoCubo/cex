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
tldr: "Tools available for curriculum config production."
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
