---
id: p11_qg_creation_artifacts
kind: quality_gate
8f: F7_govern
pillar: P11
title: "Gate: Creation Artifacts"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: quality-gate-builder
domain: creation
quality: 9.1
tags: [quality-gate, creation, pipeline, governance, p11]
tldr: "Pre-pool gate for creation artifacts: 8 HARD checks + 5-dimension scoring >= 8.0"
density_score: 0.91
related:
  - p11_qg_marketing_artifacts
  - p11_qg_engineering_artifacts
  - p11_qg_orchestration_artifacts
  - p11_qg_brand_artifacts
  - p11_qg_intelligence_artifact
  - p11_qg_quality_gate
  - bld_knowledge_card_quality_gate
  - p11_qg_chunk_strategy
  - p11_qg_response_format
  - p11_qg_constraint_spec
---
## Definition

| Property | Value |
|----------|-------|
| Metric | creation_quality_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All artifacts produced through CEX 8F creation pipeline before pool merge |

## HARD Gates

Failure on any single gate sets final score to 0 and blocks pool merge immediately.

| ID | Criterion | Failure Action |
|----|-----------|----------------|
| H01 | Frontmatter block parses as valid YAML without errors | block |
| H02 | `id` matches the required namespace pattern for the artifact kind (e.g. `p{nn}_{kind}_*`) | block |
| H03 | `id` value equals the filename stem exactly (case-sensitive) | block |
| H04 | `kind` field matches the literal artifact type registered in `kinds_meta.json` | block |
| H05 | `quality` field is null at authoring time (self-scoring forbidden) | block |
| H06 | All schema-required frontmatter fields present and non-empty: id, kind, pillar, title, version, created, updated, author, tags, tldr | block |
| H07 | Body content is present and >= 200 bytes (empty or stub artifacts rejected) | block |
| H08 | `pillar` value matches the pillar registered for the artifact kind in `kinds_meta.json` | block |

## SOFT Scoring

Score each dimension 0.0 (absent/fails) to 1.0 (fully present/passes). Apply weight. Sum weighted scores and normalize to 0–10.

| ID | Dimension | Weight | Scoring Method | Criteria |
|----|-----------|--------|----------------|----------|
| S01 | Structural completeness | 25% | binary | All required body sections present per kind schema; no placeholder text remaining |
| S02 | Content density | 25% | graduated | `density_score` field >= 0.85 = 1.0; 0.80–0.84 = 0.7; 0.75–0.79 = 0.4; < 0.75 = 0 |
| S03 | Actionability | 20% | graduated | >= 2 concrete examples, commands, or decision tables = 1.0; 1 present = 0.5; none = 0 |
| S04 | Domain specificity | 15% | binary | Content is specific to the declared domain; no generic filler that could apply to any kind |
| S05 | Reference integrity | 15% | binary | All internal references (kind IDs, pillar numbers, builder IDs) resolve against `kinds_meta.json` |

**Formula:**
```
final_score = hard_pass
  ? (S01*0.25 + S02*0.25 + S03*0.20 + S04*0.15 + S05*0.15) * 10
  : 0
```
Weight sum: 1.00. Score range: 0.0–10.0.

## Actions

| Tier | Threshold | Consequence |
|------|-----------|-------------|
| GOLDEN | >= 9.5 | Merge to pool as golden reference; flag for use in F3 INJECT examples |
| PUBLISH | >= 8.0 | Merge to pool; mark production-ready; compile YAML |
| REVIEW | 7.0–7.9 | Return to author with per-dimension score breakdown; one revision cycle; re-gate required |
| REJECT | < 7.0 | Block from pool; full rewrite required; do not archive partial draft |

## Bypass

| Field | Value |
|-------|-------|
| condition | Artifact is an experimental draft for an unstable kind schema under active design iteration |
| approver | N07 Orchestrator or Pillar owner must approve in writing before bypass takes effect |
| audit_log | Record in `.cex/runtime/decisions/bypasses.md` — include date, approver ID, artifact path, reason, and expiry date |
| expiry | 14 calendar days from bypass grant; artifact must reach PUBLISH tier before expiry or be removed from active use |

**Non-bypassable gates:** H01 (YAML parse failure = artifact is broken) and H05 (self-scoring is a schema violation). These two gates have no override path under any condition.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_marketing_artifacts]] | sibling | 0.59 |
| [[p11_qg_engineering_artifacts]] | sibling | 0.59 |
| [[p11_qg_orchestration_artifacts]] | sibling | 0.58 |
| [[p11_qg_brand_artifacts]] | sibling | 0.56 |
| [[p11_qg_intelligence_artifact]] | sibling | 0.55 |
| [[p11_qg_quality_gate]] | sibling | 0.45 |
| [[bld_knowledge_card_quality_gate]] | related | 0.37 |
| [[p11_qg_chunk_strategy]] | sibling | 0.37 |
| [[p11_qg_response_format]] | sibling | 0.36 |
| [[p11_qg_constraint_spec]] | sibling | 0.34 |
