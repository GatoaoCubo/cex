---
id: p12_mission_n03_shokunin
kind: dag
pillar: P12
title: "Mission: N03 Shokunin Wave — The Craftsman Refines His Tools"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n07_orchestrator
pipeline: meta_improvement
domain: orchestration
quality: null
tags: [mission, shokunin, n03, self-improvement, testing, refactoring, ci-cd]
tldr: "Meta-mission: N03 applies its own software engineering knowledge to refine its own tools. pyproject.toml, 80+ tests, shared library (DRY), error hierarchy, CI/CD, type hints, lint, 8F pipeline refactoring."
node_count: 23
edge_count: 5
estimated_duration: "6-8h"
density_score: 0.94
---

# Mission: N03 Shokunin Wave (職人)

## The Paradox

N03 teaches 12 software engineering practices.
N03 violates all 12 in its own code.
The Shokunin Wave resolves this paradox.

## The Gap

```
TODAY:  N03 builds perfect .md artifacts (avg 8.9)
        N03's own Python code: 0 tests, 0 lint, 0 types, 0 CI
        12,500 lines of untested, unlinted, untyped code

AFTER:  N03's tools follow the same standards as its artifacts
        80+ tests, 60% coverage, 0 lint errors, CI/CD
        The builder's tools are as refined as what it builds
```

## Phase DAG

```
S1 (foundation)
├── pyproject.toml
├── cex_shared.py (DRY)
├── cex_errors.py (hierarchy)
└── refactor 3 core tools
         │
S2 (tests) ─────────────────┐
├── conftest.py              │
└── 10 test files (80+ tests)│
         │                   │
S3 (quality) ◄──────────────┘
├── ruff lint + fix
├── type hints (5 tools)
└── error handling (specific types)
         │
S4 (ci/cd)
├── .github/workflows/ci.yml
└── .github/workflows/quality.yml
         │
S5 (meta)
├── 8F runner refactor (13→5 responsibilities)
├── structured logging (build_id)
├── retry with backoff
└── 3 KCs (shokunin, shared_lib, errors)
```

## Key Metrics

| Metric | Before | After |
|--------|--------|-------|
| Tests | 0 | ≥80 |
| Coverage | 0% | ≥40% |
| Lint errors | Unknown | 0 |
| Typed functions | 9/200 (4%) | 120/200 (60%) |
| Duplicated code | 6x strip_fm, 6x builder_load | 1x each |
| Error classes | 0 | 7 |
| CI workflows | 0 | 2 |
| 8F runner lines | 1386 | ≤1000 |
| pyproject.toml | Missing | Complete |

## Outputs
- Python: pyproject.toml, cex_shared.py, cex_errors.py, 10 test files, conftest.py, 2 CI workflows, 3 refactored tools
- CEX: 3 knowledge cards (shokunin, shared_lib, errors)

## Status
- [ ] S1: Foundation (pyproject.toml + shared lib + errors + refactor)
- [ ] S2: Tests (conftest + 10 test files, 80+ tests)
- [ ] S3: Quality (lint + type hints + error handling)
- [ ] S4: CI/CD (2 GitHub Actions workflows)
- [ ] S5: Meta (8F refactor + logging + 3 KCs)
