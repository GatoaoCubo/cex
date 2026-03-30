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
