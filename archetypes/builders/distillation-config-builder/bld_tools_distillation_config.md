---
kind: tools
id: bld_tools_distillation_config
pillar: P04
llm_function: CALL
purpose: Tools available for distillation_config production
quality: null
title: "Distillation Config Builder - Tools ISO"
version: "1.0.0"
author: n03_builder
tags: [distillation_config, builder, tools]
tldr: "Tools available for distillation config production."
domain: "model distillation"
created: "2026-04-23"
updated: "2026-04-23"
density_score: 0.85
related:
  - bld_model_distillation_config
---

# Tools: distillation-config-builder

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
| CEX Schema | P02_model/_schema.yaml | Field definitions |
| Hinton 2015 | arxiv.org/abs/1503.02531 | Original KD paper |
| DistilBERT | arxiv.org/abs/1910.01108 | BERT distillation reference |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Permitted |
| DENIED | (none) | -- |
