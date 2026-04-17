---
kind: quality_gate
id: p01_qg_dataset_card
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for dataset_card
quality: 8.9
title: "Quality Gate Dataset Card"
version: "1.0.0"
author: wave1_builder_gen
tags: [dataset_card, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for dataset_card"
domain: "dataset_card construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|--------|-----------|----------|-------|
| Doc Completeness | 100% | == | Metadata & Schema |

## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | YAML Syntax | Parse Error |
| H02 | ID Pattern | Regex Mismatch |
| H03 | Kind Match | Not 'dataset_card' |
| H04 | Schema Presence | Missing definition |
| H05 | License Field | Null or Empty |
| H06 | Version Format | Non-SemVer |
| H07 | Owner Identity | Unassigned |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|-----|-----------|--------|---------------|
| D01 | Metadata Depth | 0.15 | Field coverage % |
| D02 | Schema Clarity | 0.15 | Type accuracy |
| D03 | Lineage Trace | 0.10 | Upstream links |
| D04 | Usage Limits | 0.10 | Constraint detail |
| D05 | Privacy Flags | 0.15 | PII identification |
| D06 | Stat Summary | 0.10 | Distribution info |
| D07 | Style Consistency| 0.05 | Format adherence |
| D08 | Bias/Error Notes | 0.10 | Known issue depth |
| D09 | Interoperability | 0.10 | Format compatibility|

## Actions
| Score | Action |
|-------
