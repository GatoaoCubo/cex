---
id: p01_kc_quality_gates
kind: knowledge_card
type: domain
pillar: P01
title: "Quality Gates — Automated Pass/Fail Checkpoints"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: operations
quality: 9.0
tags: [quality-gate, validation, checkpoint, cicd, governance]
tldr: "Automated checkpoints that block progression if quality criteria aren't met. Compile gate, doctor gate, test gate, review gate."
when_to_use: "Implementing quality enforcement in artifact production or deployment pipelines"
keywords: [quality-gate, checkpoint, governance, pass-fail, blocking]
density_score: 0.92
updated: "2026-04-07"
related:
  - bld_schema_quickstart_guide
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_search_strategy
  - bld_schema_usage_report
  - bld_schema_playground_config
  - bld_schema_quality_gate
  - bld_schema_contributor_guide
  - bld_schema_pitch_deck
  - bld_schema_action_paradigm
---

# Quality Gates

## The Pattern
```
PRODUCE → GATE 1 (schema) → GATE 2 (tests) → GATE 3 (review) → SHIP
              ↓ fail              ↓ fail            ↓ fail
            FIX + RETRY        FIX + RETRY       FIX + RETRY
```

## CEX Quality Gates

| Gate | What | Tool | Blocking? |
|------|------|------|-----------|
| Frontmatter | Required fields present | `cex_compile.py` | Yes |
| Schema | YAML structure valid | `cex_compile.py` | Yes |
| Doctor | Builder specs complete | `cex_doctor.py` | Yes (for builders) |
| Tests | pytest passes | `pytest` | Yes (for tools) |
| Density | Content density >= 0.85 | Frontmatter field | Warn |
| Quality score | Peer-review >= 8.0 | `cex_score.py` | Yes (for publish) |
| Brand audit | Brand consistency >= 0.85 | `brand_audit.py` | Yes (for N06) |

## Anti-Pattern: Self-Scoring
Never let the producing LLM score its own output. Always peer-review.
CEX rule: `quality: null` on creation → peer scores later.

## Key Principles

- Domain-specific knowledge must be verifiable and traceable
- Artifacts reference this card via `tags` matching
- Updates trigger re-scoring of dependent artifacts
- Card freshness tracked via `created`/`updated` timestamps
- Cross-references validated by `cex_compile.py`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_quickstart_guide]] | downstream | 0.36 |
| [[bld_schema_integration_guide]] | downstream | 0.35 |
| [[bld_schema_reranker_config]] | downstream | 0.35 |
| [[bld_schema_search_strategy]] | downstream | 0.34 |
| [[bld_schema_usage_report]] | downstream | 0.34 |
| [[bld_schema_playground_config]] | downstream | 0.34 |
| [[bld_schema_quality_gate]] | downstream | 0.33 |
| [[bld_schema_contributor_guide]] | downstream | 0.33 |
| [[bld_schema_pitch_deck]] | downstream | 0.33 |
| [[bld_schema_action_paradigm]] | downstream | 0.32 |
