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
quality: 8.9
tags: [quality-gate, brand, identity, messaging, conversion]
tldr: "Pre-publish gate for brand artifacts: structural validation + 5-dimension brand quality scoring >= 8.5"
density_score: 0.92
---
## Definition
| Property | Value |
|----------|-------|
| Metric | brand_quality_score |
| Threshold | 8.5 |
| Operator | >= |
| Scope | All brand artifacts before pool merge or publication |

## HARD Gates
ALL must pass or artifact is rejected regardless of SOFT score.

| ID  | Criterion | Failure Action |
|-----|-----------|----------------|
| H01 | YAML frontmatter parses without syntax errors | block |
| H02 | ID follows pattern `p{pillar}_{kind}_{slug}` format | block |
| H03 | ID equals filename stem exactly | block |
| H04 | Kind field matches declared artifact type | block |
| H05 | Quality field is null at authoring time | block |
| H06 | All required frontmatter fields present and non-empty | block |
| H07 | Brand config references resolve to valid values | block |
| H08 | No placeholder values ({{var}}, TBD, TODO) in final output | block |
| H09 | Target audience specified and non-generic | block |
| H10 | Brand voice indicators present (tone, personality traits) | block |

## SOFT Scoring
Score each dimension 0.0-1.0. Final score = weighted average * 10.

| ID | Dimension | Weight | Scoring Method |
|----|-----------|--------|----------------|
| S01 | Brand Voice Consistency | 25% | Voice matches brand personality traits and tone guidelines |
| S02 | Visual Identity Compliance | 20% | Colors, fonts, logos follow brand style guide |
| S03 | Message Clarity | 20% | Core value proposition clear and compelling |
| S04 | Target Audience Alignment | 20% | Content resonates with specified customer segments |
| S05 | Conversion Optimization | 15% | Clear call-to-action and path to desired outcome |

**Scoring Formula**: `final_score = (S01*0.25 + S02*0.20 + S03*0.20 + S04*0.20 + S05*0.15) * 10`

## Actions
| Result | Threshold | Action |
|--------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as reference example; feature in brand showcase |
| PUBLISH | >= 8.5 | Approved for publication and external use |
| REVIEW | >= 7.0 | Return for brand alignment review; one revision cycle |
| REJECT | < 7.0 | Block from publication; requires complete brand redesign |

## Bypass
| Field | Value |
|-------|-------|
| Condition | Emergency brand crisis response or time-sensitive launch requirement |
| Approver | Brand Director or CMO written approval required |
| Audit Trail | Log in `.cex/runtime/audits/brand_bypasses.md` with timestamp, approver, reason, and review date |
| Expiry | 7 days maximum; must achieve full compliance before expiry or be withdrawn |
| Never Bypass | H01 (YAML parsing), H05 (quality null), H07 (brand config validity) |