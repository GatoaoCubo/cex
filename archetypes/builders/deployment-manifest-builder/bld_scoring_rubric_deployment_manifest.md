---
id: bld_scoring_rubric_deployment_manifest
kind: knowledge_card
pillar: P07
title: "Scoring Rubric: deployment_manifest"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: deployment_manifest
quality: null
tags: [scoring_rubric, deployment_manifest, P09]
llm_function: GOVERN
tldr: "5-dimension scoring rubric for deployment_manifest artifacts."
density_score: null
---

# Scoring Rubric: deployment_manifest

## 5-Dimension Scoring (D1-D5)

| Dimension | Weight | Score 10 Criteria | Score 5 Criteria | Score 0 Criteria |
|-----------|--------|-------------------|------------------|-----------------|
| D1 Completeness | 0.25 | All sections present + artifacts_count matches | Missing 1 section or minor count mismatch | Missing multiple sections |
| D2 Safety | 0.30 | No inline secrets, all versions pinned, rollback_to set | One safety issue (e.g. missing checksum) | Inline secrets OR "latest" tag OR no rollback |
| D3 Precision | 0.20 | Full env target (namespace+region+cluster), health check, auto_rollback flag | Partial env target (missing 1 field) | Env target incomplete or absent |
| D4 Density | 0.15 | No redundant prose; tables used for structured data; <= 4096 bytes | Moderate prose inflation | Narrative-heavy; data tables missing |
| D5 Compliance | 0.10 | ID pattern matches, kind literal correct, frontmatter parses | Minor naming issue | HARD gate failure |

## Composite Score
`score = (D1*0.25 + D2*0.30 + D3*0.20 + D4*0.15 + D5*0.10) * 10`

## Thresholds
| Score | Status |
|-------|--------|
| >= 9.0 | PUBLISH |
| 7.0-8.9 | REVIEW |
| < 7.0 | REJECT |

## D2 Safety is the Critical Dimension
A deployment_manifest with inline secrets or unpinned versions is an immediate REJECT regardless of other scores. Safety gates H04 and H07 are non-negotiable.
