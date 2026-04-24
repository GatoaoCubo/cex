---
id: p08_law_shokunin
kind: invariant
8f: F1_constrain
pillar: P08
title: "Invariant 13: Shokunin — Quality Excellence"
version: 3.0.0
created: 2026-03-22
updated: 2026-03-22
author: knowledge_agent
quality: 9.1
tags: [law, shokunin, quality, excellence, golden]
tldr: "LAW 13: Every output must pass the Shokunin test — 'Would I be proud of this?' Hesitation = iterate. Quality floor 8.0, Golden >= 9.5"
max_bytes: 1024
density_score: 0.93
source: organization-core/records/framework/docs/LAWS_v3_PRACTICAL.md (LAW 13)
linked_artifacts:
  gate: p11_qg_cex_quality
  rubric: p07_sr_5d_scoring
related:
  - p11_qg_shokunin_pool
  - p10_ax_shokunin_quality
  - bld_examples_invariant
  - p07_sr_5d_scoring
  - p01_kc_invariant
  - p10_rs_edison
  - p03_sp_golden_test_builder
  - p11_qg_law
  - p03_ins_law
  - p06_val_quality_score
---

# Invariant 13: Shokunin — Quality Excellence

## Statement

> Every organization output must pass the Shokunin test: "Eu tenho orgulho disso?" (Would I be proud of this?). Any hesitation means iterate — never ship doubt.

## Implementation

| Trigger | Implementation | Auto |
|---------|---------------|------|
| Any output generation | `ultrathink_orchestrator.py` quality check | ULTRATHINK mode |
| Pre-pool write | 5D scoring (D1-D5), score >= 8.0 required | Always |
| Golden promotion | score >= 9.5, all dims >= 9.0 | Always |

## Quality Tiers

| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | Masterwork / Golden | Pool as golden artifact |
| 8.0 - 9.4 | Skilled | Pool + remember() |
| 7.0 - 7.9 | Learning | Experimental only |
| < 7.0 | Rejected | Redo from scratch |

## Inviolable Rules

1. **Never ship < 7.0** — discard and rebuild
2. **Never pool < 8.0** — experimental artifacts stay local
3. **Golden requires 9.5** — not 9.4, not "close enough"
4. **Hesitation = iteration** — if unsure, the score is not ready
5. **Partial is better than fake** — score 8.0 partial > fake 9.5 complete

## Layer

```
LAYER 3: QUALITY SYSTEM
LAW 13 (Shokunin) ← LAW 12 (Confidence Tiers)
       │
LAW 4 (Pool) — artifacts must pass LAW 13 before entering pool
```

## Violation Pattern

```
WRONG: "I'll ship this 6.5 and note it's a draft"
RIGHT: Rebuild until >= 7.0, then decide on pooling

WRONG: "It's basically 9.5, close enough for golden"
RIGHT: Measure with 5D rubric. If < 9.5, it's T2 skilled — pool but not golden.
```

## Origin

"Shokunin" (Japanese: 職人) = artisan who pursues mastery not as goal but as daily practice. Applied in organization: every output reflects the system's character. Mediocre output = mediocre system.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_shokunin_pool]] | downstream | 0.40 |
| [[p10_ax_shokunin_quality]] | downstream | 0.33 |
| [[bld_examples_invariant]] | related | 0.25 |
| [[p07_sr_5d_scoring]] | upstream | 0.25 |
| [[p01_kc_invariant]] | related | 0.22 |
| [[p10_rs_edison]] | downstream | 0.22 |
| [[p03_sp_golden_test_builder]] | upstream | 0.21 |
| [[p11_qg_law]] | downstream | 0.20 |
| [[p03_ins_law]] | upstream | 0.20 |
| [[p06_val_quality_score]] | upstream | 0.20 |
