---
id: bld_quality_gate_canary_config
kind: quality_gate
pillar: P07
title: "Gate: canary_config"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: canary_config
quality: null
tags: [quality_gate, canary_config, P09]
llm_function: GOVERN
tldr: "Validates canary configs for gradual rollout, rollback triggers, and analysis configuration."
density_score: null
---

## Definition
A canary_config must ensure gradual traffic exposure with defined automatic rollback. Any config that jumps directly to 100% or lacks rollback triggers is not a canary -- it is a direct deploy.

## HARD Gates
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML valid |
| H02 | ID matches namespace | `^p09_cc_[a-z][a-z0-9_]+$` |
| H03 | Kind matches literal | `kind` is exactly `canary_config` |
| H04 | Quality is null | `quality: null` |
| H05 | canary_version and stable_version set | Both non-empty, different values |
| H06 | stages_count matches list | frontmatter count = actual stages |
| H07 | rollback_trigger_metric set | Non-empty rollback metric |
| H08 | Last stage is 100% | Traffic progression completes at 100% |
| H09 | First stage < 50% | Gradual start required |

## SOFT Scoring
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Analysis interval per stage | 1.0 | analysis_interval_minutes present on each stage |
| Provider specified | 0.5 | provider is one of known values |
| Rollback threshold is numeric | 0.5 | threshold is float, not null |
| Pause duration per stage | 0.5 | pause_duration_minutes present on each non-final stage |

Sum of weights: 2.5. `soft_score = sum / 2.5 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |
