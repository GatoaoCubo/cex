---
kind: quality_gate
id: p05_qg_case_study
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for case_study
quality: 9.0
title: "Quality Gate Case Study"
version: "1.1.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for case_study artifacts"
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|--------|-----------|----------|-------|
| ID pattern | ^p05_cs_[a-z][a-z0-9_]+\\.md$ | matches | all case_study files |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML frontmatter valid | invalid YAML syntax |
| H02 | ID matches pattern ^p05_cs_[a-z][a-z0-9_]+\\.md$ | ID does not match pattern |
| H03 | kind field equals "case_study" | kind != "case_study" |
| H04 | Challenge section present (150+ words) | missing or < 100 words |
| H05 | Solution section present with named product features | missing or generic "our product" |
| H06 | Outcome section present with 3+ KPIs | fewer than 3 measurable KPIs |
| H07 | Pullquote present with champion name and title | anonymous or missing quote |
| H08 | ROI call-out present with headline metric and source | no ROI metric or unverified claim |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D1 | Narrative structure | 0.20 | Clear Challenge->Solution->Outcome arc with transitions = 1.0 |
| D2 | Metric specificity | 0.20 | Before/after comparison with % or absolute numbers = 1.0; vague = 0.0 |
| D3 | Pullquote quality | 0.15 | Direct, attributed, emotionally resonant = 1.0; generic = 0.5 |
| D4 | Data verification | 0.15 | Metrics approved by customer = 1.0; unverified = 0.0 |
| D5 | Clarity | 0.15 | Plain language, no jargon without context = 1.0 |
| D6 | Completeness | 0.15 | All 6 sections: Snapshot/Challenge/Solution/Outcome/ROI/Lessons = 1.0 |

## Actions
| Score | Action |
|-------|--------|
| >= 9.5 | Highlight as exemplar |
| >= 8.0 | Deploy to public repo |
| >= 7.0 | Request minor edits |
| < 7.0 | Discard, rework required |

## Bypass
| conditions | approver | audit trail |
|------------|----------|-------------|
| Strategic customer reference with legal deadline | CTO | Note in audit log with customer name and deadline |
