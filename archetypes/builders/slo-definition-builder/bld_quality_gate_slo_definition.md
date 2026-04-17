---
id: bld_quality_gate_slo_definition
kind: quality_gate
pillar: P07
title: "Gate: slo_definition"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: slo_definition
quality: null
tags: [quality_gate, slo_definition, P09]
llm_function: GOVERN
tldr: "Validates SLO definitions for measurability, error budget math, and alerting completeness."
density_score: null
---

## Definition
An slo_definition must be measurable, mathematically correct, and actionable. This gate ensures the SLO can be implemented in a monitoring system without ambiguity.

## HARD Gates
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter valid |
| H02 | ID matches namespace | `^p09_slo_[a-z][a-z0-9_]+$` |
| H03 | Kind matches literal | `kind` is exactly `slo_definition` |
| H04 | Quality is null | `quality: null` |
| H05 | target_percent in range | 50.0 <= target_percent < 100.0 |
| H06 | error_budget_minutes present | Non-zero, computed from target and window |
| H07 | error_budget_policy set | One of: block_deploy, alert_only, auto_rollback |
| H08 | owner specified | Non-empty owner field |

## SOFT Scoring
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| SLI metric query explicit | 1.0 | Metric formula or query present |
| Both burn rate thresholds defined | 1.0 | 1h fast + 6h slow alerts both present |
| Error budget math verified | 1.0 | error_budget_minutes matches formula |
| Denominator documented | 0.5 | What "total" means for this SLI |
| Tags include slo_definition | 0.5 | tags contains "slo_definition" |

Sum of weights: 4.0. `soft_score = sum / 4.0 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |
