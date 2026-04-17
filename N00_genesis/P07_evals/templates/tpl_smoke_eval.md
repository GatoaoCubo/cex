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
