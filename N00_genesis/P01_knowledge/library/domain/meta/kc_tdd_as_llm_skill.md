---
id: p01_kc_tdd_as_llm_skill
kind: knowledge_card
type: domain
pillar: P01
title: "TDD as LLM Skill — Test-Driven Development for Agents"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: meta
quality: 9.1
tags: [tdd, testing, llm, skill, red-green-refactor]
tldr: "LLMs can follow TDD: write test first (red), generate code to pass (green), refactor. Tests as specification. Especially effective for tool development."
when_to_use: "Teaching LLM agents to write reliable code via test-first approach"
keywords: [tdd, test-first, red-green-refactor, specification-by-test]
density_score: 0.92
updated: "2026-04-07"
---

# TDD as LLM Skill

## The Pattern
```
RED:    Write test that defines expected behavior → test fails
GREEN:  Write minimum code to pass test → test passes
REFACTOR: Improve code quality → test still passes
```

## Why TDD Works for LLMs
1. **Specification**: Test IS the spec — no ambiguity
2. **Validation**: Immediate feedback on correctness
3. **Scope**: Test constrains what to build (prevents over-engineering)
4. **Confidence**: Refactoring is safe when tests pass
5. **Self-healing**: Failed test + error message = auto-fix prompt

## LLM TDD Workflow
```
1. Human describes desired behavior
2. LLM writes pytest test
3. LLM runs test (fails — expected)
4. LLM writes implementation
5. LLM runs test (passes)
6. LLM refactors if needed
7. LLM runs test (still passes)
```

## CEX TDD Examples
- `test_brand_tools.py` (33 tests) → `brand_*.py` tools
- `test_brand_pipeline_e2e.py` (13 tests) → pipeline integration
- `test_bootstrap.py` (8 tests) → `cex_bootstrap.py`
- Tests written BEFORE or ALONGSIDE tools, never after

## Anti-Pattern: Test-After
Writing code first, tests later. LLM writes code that "feels right" but has subtle bugs. Tests would have caught them. Always test first.

## Quality Criteria

| Dimension | Requirement | Weight |
|-----------|------------|--------|
| Factual accuracy | Verifiable claims only | 0.25 |
| Atomicity | One concept per card | 0.20 |
| Actionability | Reader knows next steps | 0.20 |
| Density | No filler sentences | 0.20 |
| Searchability | Tags enable retrieval | 0.15 |
