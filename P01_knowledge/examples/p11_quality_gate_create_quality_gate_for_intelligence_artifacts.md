---
id: p11_qg_intelligence_artifacts
kind: quality_gate
pillar: P11
title: "Gate: Intelligence Artifacts"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "quality-gate-builder"
domain: "intelligence"
quality: 8.9
tags: [quality-gate, intelligence, research, analysis, n01]
tldr: "Quality gate for intelligence artifacts: research depth, source verification, factual accuracy with 8.0+ threshold"
density_score: 0.87
---
## Definition

| Property | Value |
|----------|-------|
| Metric | intelligence_quality_score |
| Threshold | 8.0 |
| Operator | >= |
| Scope | All intelligence artifacts (research briefs, competitor analysis, trend reports, market intelligence) before publication |

## HARD Gates

Failure on any single gate results in immediate rejection regardless of soft score.

| ID  | Criterion | Failure Action |
|-----|-----------|---------------|
| H01 | YAML frontmatter parses without error | block |
| H02 | ID matches pattern `{pillar}_{kind}_{slug}` | block |
| H03 | ID equals filename stem | block |
| H04 | Kind field equals declared artifact type | block |
| H05 | Quality field is null at authoring time | block |
| H06 | All required frontmatter fields present | block |
| H07 | Research methodology section present with >= 2 sources | block |
| H08 | Executive summary present and <= 500 words | block |
| H09 | Key findings section with >= 3 numbered insights | block |
| H10 | Source attribution for all factual claims | block |

## SOFT Scoring

Each dimension scored 0.0-1.0, multiplied by weight. Formula: `final_score = sum(dimension_score * weight) * 10`

| ID  | Dimension | Weight | Scoring Method |
|-----|-----------|--------|----------------|
| S01 | Research depth | 25% | Graduated: shallow (0.0), adequate (0.5), comprehensive (0.8), exhaustive (1.0) |
| S02 | Source quality | 20% | Binary per source: credible (1.0) or questionable (0.0), averaged across all sources |
| S03 | Factual accuracy | 25% | Graduated: verifiable claims rate (0-100% = 0.0-1.0 score) |
| S04 | Actionability | 15% | Binary: concrete recommendations present (1.0) or vague conclusions only (0.0) |
| S05 | Completeness | 15% | Graduated: addresses stated scope fully (1.0), partially (0.6), minimally (0.2) |

**Weight total**: 100%. **Score range**: 0.0-10.0.

## Actions

| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to intelligence pool; flag as reference-quality research |
| PUBLISH | >= 8.0 | Publish to pool; suitable for decision-making use |
| REVIEW | >= 7.0 | Return to analyst with scored feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; requires substantial rework of research methodology |

## Bypass

| Field | Value |
|-------|-------|
| Condition | Time-sensitive intelligence with verified high-impact findings scoring 7.5-7.9 |
| Approver | N01 nucleus lead or intelligence pillar owner |
| Audit log | Record in `.cex/runtime/audits/intelligence_bypasses.log` with timestamp, approver, rationale |
| Expiry | 72 hours from bypass grant; must achieve full compliance within timeframe |

**Note**: H01, H05, and H10 (source attribution) gates cannot be bypassed under any circumstances.