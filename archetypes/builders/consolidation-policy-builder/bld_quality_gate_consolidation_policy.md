---
kind: quality_gate
id: p10_qg_consolidation_policy
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for consolidation_policy
quality: 9.0
title: "Quality Gate: consolidation_policy"
version: "2.0.0"
author: n06_commercial
tags: [consolidation_policy, builder, quality_gate]
tldr: "HARD gates enforce artifact structure (schema, ID, async flag, promotion rules). SOFT scoring weights domain accuracy, eviction completeness, commercial differentiation, and compliance."
domain: "LLM agent memory consolidation"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.90
---

## Definition

| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Required frontmatter fields | 100% | == | Artifact |
| consolidation_async | true | == | Artifact |
| Promotion Rules section present | true | == | Artifact |
| Eviction Rules section present | true | == | Artifact |

## HARD Gates

| ID | Check | Fail Condition |
|----|-------|---------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches `^p10_cp_[a-z][a-z0-9_]+$` | ID absent or does not match pattern |
| H03 | kind field equals `consolidation_policy` | kind field absent, wrong, or misspelled |
| H04 | `consolidation_async: true` in frontmatter | Field absent or set to false |
| H05 | Promotion Rules section present with table | Section absent or table empty |
| H06 | Eviction Rules section present with table | Section absent or table empty |
| H07 | No OS memory management content (GC, slab, heap, TLB, fragmentation) | OS terminology present |

## SOFT Scoring

| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|--------------|
| D1 | Domain accuracy | 0.25 | 1.0 = all content is LLM agent memory; 0.0 = OS/GC contamination |
| D2 | Promotion completeness | 0.20 | 1.0 = all tier transitions defined with conditions; 0.5 = partial; 0.0 = absent |
| D3 | Commercial differentiation | 0.20 | 1.0 = FREE/PRO/ENTERPRISE matrix with 5+ features; 0.5 = partial; 0.0 = absent |
| D4 | Eviction coverage | 0.20 | 1.0 = eviction defined per layer with trigger + action; 0.5 = partial; 0.0 = absent |
| D5 | Compliance coverage | 0.15 | 1.0 = retention_days + gdpr_erasure + audit_trail; 0.5 = partial; 0.0 = absent (enterprise penalized more) |

## Actions

| Score | Action |
|-------|--------|
| >= 9.5 | GOLDEN -- archive as gold standard example |
| >= 8.0 | PUBLISH -- merge to main |
| >= 7.0 | REVIEW -- surgical fix before merge |
| < 7.0 | REJECT -- rebuild required |

## Bypass

| Condition | Approver | Audit Trail |
|-----------|----------|------------|
| Emergency patching of agent memory incident | N07 + N06 | Incident report with justification |
| Free-tier artifact with no consolidation (correct behavior) | N06 | Tier=free annotation in frontmatter |
