---
id: "p07_se_{{SCOPE_SLUG}}"
kind: smoke_eval
pillar: P07
version: 1.0.0
title: Template - Smoke Eval
tags: [template, smoke, eval, sanity, quick]
tldr: Fast sanity check (<30s) that catches obvious regressions. Syntax, import, basic function, output format.
quality: 8.6
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
- Before every commit (pre-commit)
- First CI step
- After dependency update
- After config change
## Quality Gate
- [ ] Total < 30s
- [ ] No external deps (DB, API)
- [ ] Catches syntax + import + format
- [ ] fail_fast=true
