---
id: p06_val_quality_score
kind: validator
pillar: P06
title: "Validator: Quality Score Field"
version: 1.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.0
tags: [validator, quality, score, schema]
tldr: "Validation rules for quality_score field: range 0.0-10.0, tier classification, pool eligibility gates"
max_bytes: 1024
density_score: 0.89
source: organization-core/records/framework/docs/LAWS_v3_PRACTICAL.md + CLAUDE.md quality tiers
linked_artifacts:
  schema: p06_is_quality_audit
  gate: p11_qg_cex_quality
---

# Validator: Quality Score Field

## Field Definition

```yaml
quality_score:
  type: float
  required: true
  range: [0.0, 10.0]
  precision: 1  # max 1 decimal place (7.0, 8.5, 9.2 — not 7.23)
  default: null  # must be set explicitly, no default
```

## Tier Classification

| Score | Tier | Label | Action |
|-------|------|-------|--------|
| >= 9.5 | T1 | Master / Golden | Promote to Pool as Golden |
| 8.0 - 9.4 | T2 | Skilled | Add to Pool + remember() |
| 7.0 - 7.9 | T3 | Learning | Experimental — do not pool |
| < 7.0 | T4 | Rejected | Redo or discard |

## Validation Rules

```yaml
rules:
  - id: QS-001
    name: range_check
    condition: "0.0 <= quality_score <= 10.0"
    on_fail: reject
    message: "quality_score must be between 0.0 and 10.0"

  - id: QS-002
    name: precision_check
    condition: "round(quality_score, 1) == quality_score"
    on_fail: warn
    message: "quality_score should have at most 1 decimal place"

  - id: QS-003
    name: pool_gate
    condition: "quality_score >= 8.0 OR skip_pool=true"
    on_fail: block_pool_write
    message: "Score < 8.0 cannot be written to shared pool"

  - id: QS-004
    name: golden_gate
    condition: "quality_score >= 9.5 OR skip_golden=true"
    on_fail: block_golden_promote
    message: "Score < 9.5 cannot be promoted as Golden artifact"
```

## Valid Examples

```yaml
quality: 9.5   # valid — T1 Master
quality: 8.0   # valid — T2 minimum pool threshold
quality: 7.3   # valid — T3 experimental
```

## Invalid Examples

```yaml
quality: 10.5  # FAILS QS-001 — out of range
quality: 8.25  # FAILS QS-002 (warn) — too precise, should be 8.3
quality: null  # FAILS — required field
quality: "high" # FAILS — must be float, not string
```
