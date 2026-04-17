---
id: p06_td_quality_score
kind: type_def
pillar: P06
description: "Type definition for the 5-dimension quality score used across organization"
version: 1.0.0
created: 2026-03-24
author: builder_agent
quality: 9.0
tags: [type-def, quality, scoring, validation]
updated: "2026-04-07"
domain: "schema"
title: "Type Def Quality Score"
density_score: 0.92
tldr: "Defines type def for type def quality score, with validation gates and integration points."
---

# Type: quality_score

## Definition
```yaml
quality_score:
  type: object
  properties:
    overall:
      type: number
      minimum: 0.0
      maximum: 10.0
    dimensions:
      type: object
      properties:
        syntax: {type: number, min: 0, max: 10}
        structure: {type: number, min: 0, max: 10}
        size: {type: number, min: 0, max: 10}
        lint: {type: number, min: 0, max: 10}
        completeness: {type: number, min: 0, max: 10}
    weights:
      syntax: 3.0
      structure: 2.0
      size: 1.5
      lint: 2.0
      completeness: 1.5
  required: [overall, dimensions]
```

## Thresholds
| Score | Tier | Action |
|-------|------|--------|
| >= 9.0 | PASS | Commit allowed |
| 7.0-8.9 | WARN | Commit with warning |
| < 7.0 | FAIL | Commit blocked, rollback recommended |

## Usage
Used by: quality_gate.py (pre-commit hook), signal_writer (completion), pool promotion.
Source: `records/core/python/quality_gate.py`

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Properties

| Property | Value |
|----------|-------|
| Kind | `type_def` |
| Pillar | P06 |
| Domain |  |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
