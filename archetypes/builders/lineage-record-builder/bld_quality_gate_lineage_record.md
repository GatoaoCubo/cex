---
id: bld_quality_gate_lineage_record
kind: quality_gate
pillar: P07
title: "Gate: lineage_record"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: lineage_record
quality: 7.0
tags: [quality_gate, lineage_record, P01]
llm_function: GOVERN
tldr: "Validates lineage records for completeness of provenance chain using PROV-O."
density_score: null
---

## Definition
A lineage_record must be complete enough to reconstruct the derivation path of a knowledge artifact without relying on memory or implicit context.

## HARD Gates
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML valid |
| H02 | ID matches namespace | `^p01_lr_[a-z][a-z0-9_]+$` |
| H03 | Kind matches literal | `kind` is exactly `lineage_record` |
| H04 | Quality is null | `quality: null` |
| H05 | target_artifact set | Non-empty |
| H06 | sources_count >= 1 | At least 1 source entity |
| H07 | Timestamps present | At least 1 ISO 8601 timestamp on entities |
| H08 | Agent identified | At least 1 agent in agents list |

## SOFT Scoring
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| PROV-O relations explicit | 1.0 | Derivation Relations section uses PROV-O vocabulary |
| All activities have agents | 1.0 | No activity without agent assignment |
| sources_count matches list | 0.5 | frontmatter count = actual list length |
| activities_count matches list | 0.5 | frontmatter count = actual list length |
| Derivation type set | 0.5 | derivation_type is one of the 4 PROV-O types |

Sum of weights: 3.5. `soft_score = sum / 3.5 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |
