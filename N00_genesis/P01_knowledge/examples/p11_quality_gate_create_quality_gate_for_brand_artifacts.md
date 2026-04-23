---
id: p11_qg_brand_artifacts
kind: quality_gate
pillar: P11
title: "Gate: Brand Artifacts"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "quality-gate-builder"
domain: "brand"
quality: 9.1
tags: [quality-gate, brand, p11, governance, identity]
tldr: "Pre-publish gate for brand artifacts: 8 HARD checks + 5-dimension weighted scoring >= 8.5 before pool merge"
density_score: 0.91
related:
  - p11_qg_creation_artifacts
  - p11_qg_marketing_artifacts
  - p11_qg_engineering_artifacts
  - p11_qg_orchestration_artifacts
  - p11_qg_intelligence_artifact
  - p11_qg_quality_gate
  - p03_sp_brand_nucleus
  - p11_qg_chunk_strategy
  - p03_brand_book_generator
  - p11_qg_response_format
---
## Definition

| Property | Value |
|----------|-------|
| Metric | brand_quality_score |
| Threshold | 8.5 |
| Operator | >= |
| Scope | All brand artifacts before pool merge or publication via N06 or any nucleus |

## HARD Gates

Failure on any single gate sets final score to 0 and blocks pool merge immediately.

| ID  | Criterion | Failure Action |
|-----|-----------|----------------|
| H01 | YAML frontmatter parses without syntax errors | block |
| H02 | `id` matches pattern `p{nn}_{kind}_{slug}` (no uppercase, no spaces) | block |
| H03 | `id` value equals filename stem exactly (case-sensitive) | block |
| H04 | `kind` field matches a literal registered in `kinds_meta.json` | block |
| H05 | `quality` field is null at authoring time (self-scoring forbidden) | block |
| H06 | All required frontmatter fields present and non-empty: id, kind, pillar, title, version, created, updated, author, domain, tags, tldr | block |
| H07 | No unresolved `{{BRAND_*}}` placeholder tokens remain in body or frontmatter | block |
| H08 | Brand config references (colors, voice, values) resolve to entries in `.cex/brand/brand_config.yaml` | block |

## SOFT Scoring

Score each dimension 0.0 (absent or fails) to 1.0 (fully present and passes). Partial credit allowed where noted.

| ID  | Dimension | Weight | Criteria | Scoring Method |
|-----|-----------|--------|----------|----------------|
| S01 | Structural validity | 20% | All schema-required sections present; body within max_bytes for the artifact kind | binary |
| S02 | Brand alignment | 25% | Voice, tone, and values demonstrably match `brand_config.yaml` identity fields; no generic filler language | graduated |
| S03 | Content density | 20% | `density_score` >= 0.85; no padding, no restated headings, each paragraph carries unique information | graduated |
| S04 | Voice consistency | 20% | Personality markers (formal/casual, technical/friendly) are consistent throughout; no tonal shifts between sections | graduated |
| S05 | Documentation completeness | 15% | `tldr` <= 160 chars; at least one concrete example or use case present; tags are domain-accurate | graduated |

**Scoring Formula**

```
brand_quality_score = (S01*0.20 + S02*0.25 + S03*0.20 + S04*0.20 + S05*0.15) * 10
```

Weight total: 1.00 (100%). Score range: 0.0–10.0.
HARD gate failure overrides formula: `final = hard_pass ? brand_quality_score : 0`.

## Actions

| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to brand pool as reference; flag for brand style guide inclusion |
| PUBLISH | >= 8.5 | Publish to brand pool; mark production-ready for N06 consumption |
| REVIEW | >= 7.0 | Return to author with per-dimension scores and specific revision notes; one revision cycle |
| REJECT | < 7.0 | Block from pool; full rewrite required; raise signal to N07 with failure summary |

## Bypass

| Field | Value |
|-------|-------|
| condition | Brand config is actively being revised (bootstrap or rebrand in progress) and artifact uses provisional values pending final brand decisions |
| approver | Brand owner or N07 orchestrator must approve in writing before bypass takes effect |
| audit_log | Record in `.cex/runtime/decisions/bypass_log.md` with: date, artifact id, approver, specific gates bypassed, and reason |
| expiry | 7 days from grant; artifact must reach full compliance or be removed from pool before expiry |

**Non-bypassable gates**: H01 (YAML parse) and H05 (quality null) can never be bypassed under any conditions.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_creation_artifacts]] | sibling | 0.68 |
| [[p11_qg_marketing_artifacts]] | sibling | 0.63 |
| [[p11_qg_engineering_artifacts]] | sibling | 0.59 |
| [[p11_qg_orchestration_artifacts]] | sibling | 0.54 |
| [[p11_qg_intelligence_artifact]] | sibling | 0.53 |
| [[p11_qg_quality_gate]] | sibling | 0.42 |
| [[p03_sp_brand_nucleus]] | upstream | 0.39 |
| [[p11_qg_chunk_strategy]] | sibling | 0.37 |
| [[p03_brand_book_generator]] | upstream | 0.37 |
| [[p11_qg_response_format]] | sibling | 0.35 |
