---
kind: quality_gate
id: p05_qg_code_of_conduct
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for code_of_conduct
quality: 9.0
title: "Quality Gate Code of Conduct"
version: "1.0.0"
author: n04_knowledge
tags: [code_of_conduct, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for code_of_conduct"
domain: "code_of_conduct construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Definition
| Metric | Threshold | Operator | Scope |
|--------|-----------|----------|-------|
| Enforcement ladder completeness | 4 levels | equals | All CoC artifacts |
| Reporting channel present | 1 contact | minimum | All CoC artifacts |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | Invalid YAML syntax or missing required fields |
| H02 | ID matches pattern ^p05_coc_[a-z][a-z0-9_]+.md$ | ID format mismatch |
| H03 | kind field matches "code_of_conduct" | Kind field incorrect or missing |
| H04 | contact_email field present and non-empty | Missing or empty reporting channel |
| H05 | Enforcement ladder has all 4 levels | Missing Correction, Warning, Temp Ban, or Perm Ban |
| H06 | Our Pledge section present | Missing pledge commitment statement |
| H07 | Attribution to Contributor Covenant present | Missing source attribution |
| H08 | Scope section covers online spaces | No scope definition |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Pledge quality (inclusive, specific commitment) | 0.25 | 1.0 (specific + inclusive) to 0.0 (vague or missing) |
| D02 | Standards completeness (positive + negative behaviors) | 0.25 | 1.0 (5+ each) to 0.0 (<3 total) |
| D03 | Enforcement ladder clarity (4 tiers with consequences) | 0.25 | 1.0 (all 4 tiers with consequences) to 0.0 (<2 tiers) |
| D04 | Reporting channel usability (email + SLA + confidentiality) | 0.15 | 1.0 (all 3 elements) to 0.0 (email only) |
| D05 | Attribution and version accuracy | 0.10 | 1.0 (correct version + URL) to 0.0 (missing) |

## Actions
| Score | Action |
|-------|--------|
| GOLDEN (>=9.5) | Auto-publish; no review required |
| PUBLISH (>=8.0) | Publish after maintainer approval |
| REVIEW (>=7.0) | Flag for community review |
| REJECT (<7.0) | Reject; request revision against H gates |

## Bypass
| Conditions | Approver | Audit Trail |
|------------|----------|-------------|
| Emergency conduct incident | Lead Maintainer | GitHub issue + approval comment |
