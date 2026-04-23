---
id: "p07_se_{{SCOPE_SLUG}}"
kind: smoke_eval
pillar: P07
version: 1.0.0
title: Template - Smoke Eval
tags: [template, smoke, eval, sanity, quick]
tldr: Fast sanity check (<30s) that catches obvious regressions. Syntax, import, basic function, output format.
quality: 9.0
updated: "2026-04-07"
domain: "evaluation and testing"
author: n03_builder
created: "2026-04-07"
density_score: 0.95
related:
  - smoke-eval-builder
  - bld_config_smoke_eval
  - bld_memory_smoke_eval
  - bld_architecture_smoke_eval
  - p03_sp_smoke_eval_builder
  - p01_kc_smoke_eval
  - bld_collaboration_smoke_eval
  - bld_output_template_smoke_eval
  - p01_kc_git_hooks_ci
  - bld_knowledge_card_smoke_eval
---

# Smoke Eval: [NAME]

## Purpose
[WHAT this smoke_eval does]
## Checks
| Check | What | Pass | Time |
|-------|------|------|------|
| syntax | .py files compile | 0 errors | <2s |
| import | Main module loads | No ImportError | <5s |
| function | Core fn returns | Non-null | <10s |
| format | Output matches schema | Valid | <5s |
## Execution
```bash
python -m pytest tests/ -m smoke --timeout=30 --fail-fast
```
## When to Run
1. Before every commit (pre-commit)
2. First CI step
3. After dependency update
4. After config change
## Quality Gate
1. [ ] Total < 30s
2. [ ] No external deps (DB, API)
3. [ ] Catches syntax + import + format
4. [ ] fail_fast=true

## Artifact Properties

| Property | Value |
|----------|-------|
| Kind | `smoke_eval` |
| Pillar | P07 |
| Domain | evaluation and testing |
| Pipeline | 8F (F1-F8) |
| Scorer | `cex_score.py` |
| Compiler | `cex_compile.py` |
| Retriever | `cex_retriever.py` |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[smoke-eval-builder]] | related | 0.33 |
| [[bld_config_smoke_eval]] | downstream | 0.31 |
| [[bld_memory_smoke_eval]] | downstream | 0.29 |
| [[bld_architecture_smoke_eval]] | downstream | 0.29 |
| [[p03_sp_smoke_eval_builder]] | upstream | 0.29 |
| [[p01_kc_smoke_eval]] | related | 0.28 |
| [[bld_collaboration_smoke_eval]] | related | 0.27 |
| [[bld_output_template_smoke_eval]] | upstream | 0.26 |
| [[p01_kc_git_hooks_ci]] | upstream | 0.25 |
| [[bld_knowledge_card_smoke_eval]] | related | 0.24 |
