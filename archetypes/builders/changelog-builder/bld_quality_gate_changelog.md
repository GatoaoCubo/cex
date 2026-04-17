---
kind: quality_gate
id: p01_qg_changelog
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for changelog
quality: 9.0
title: "Quality Gate Changelog"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [changelog, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for changelog artifacts"
domain: "changelog construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|--------|-----------|----------|-------|
| ID pattern | ^p01_ch_[a-z][a-z0-9_]+\\.md$ | matches | all changelog files |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | invalid YAML syntax |
| H02 | ID matches pattern ^p01_ch_[a-z][a-z0-9_]+\\.md$ | ID does not match pattern |
| H03 | kind field equals "changelog" | kind != "changelog" |
| H04 | version field present and SemVer X.Y.Z | missing or non-SemVer version |
| H05 | At least one of: Added/Changed/Fixed/Removed/Deprecated/Security section present | no change sections found |
| H06 | MAJOR version bump includes Migration section | MAJOR bump without migration guide |
| H07 | No fabricated issue IDs (issue refs must be integers or alphanumeric) | fictional issue ID format |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Section completeness | 0.20 | All 6 Keep a Changelog sections present = 1.0; fewer = proportional |
| D2 | Entry precision | 0.20 | Entries are specific and actionable = 1.0; vague = 0.0 |
| D3 | SemVer alignment | 0.15 | Version bump type matches changes = 1.0; mismatch = 0.0 |
| D4 | Breaking change clarity | 0.15 | BREAKING: prefix + migration steps = 1.0; unlabeled = 0.0 |
| D5 | Traceability | 0.15 | Issue/PR IDs linked = 1.0; no references = 0.0 |
| D6 | Imperative language | 0.15 | "Add X", "Fix Y" = 1.0; passive/nominal = 0.5 |

## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | Auto-publish |
| >= 8.0 | Publish |
| >= 7.0 | Require review |
| < 7.0 | Block release |

## Bypass
| conditions | approver | audit trail |
|------------|----------|-------------|
| Urgent hotfix with breaking customer impact | CTO | Audit log entry with timestamp and justification |
