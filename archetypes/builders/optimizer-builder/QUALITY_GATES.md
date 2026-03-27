---
pillar: P11
llm_function: GOVERN
purpose: Quality gates for optimizer artifacts (recursive)
note: this file IS an instance of what the builder governs
---

# Quality Gates: optimizer

## HARD Gates
| Gate | Check |
|------|-------|
| H01 | YAML parses without error |
| H02 | id matches ^p11_opt_[a-z][a-z0-9_]+$ |
| H03 | id == filename stem |
| H04 | kind == optimizer |
| H05 | pillar == P11 |
| H06 | quality == null |
| H07 | target field is non-empty string |
| H08 | metric.direction in [minimize, maximize] |
| H09 | action.type in [tune, prune, scale, replace, restructure] |
| H10 | threshold.trigger, threshold.target, threshold.critical are numeric |
| H11 | frequency in [continuous, hourly, daily, weekly, monthly] |
| H12 | risk.level in [low, medium, high] |
| H13 | baseline.value is numeric |
| H14 | improvement.current and improvement.target are numeric |
| H15 | All 5 body sections present (Target Process, Metrics, Actions, Risk Assessment, Monitoring) |

## SOFT Gates
| Gate | Check | Weight |
|------|-------|--------|
| S01 | tldr < 160 chars | 1.0 |
| S02 | tags >= 3 items, includes "optimizer" | 0.5 |
| S03 | Secondary metrics table has >= 1 row | 1.0 |
| S04 | Actions table has >= 2 rows | 1.0 |
| S05 | Rollback procedure defined | 1.5 |
| S06 | Risk table has >= 2 rows | 1.0 |
| S07 | monitoring.alerts list has >= 2 entries | 1.0 |
| S08 | baseline.conditions non-empty | 0.5 |
| S09 | improvement.history is list (even if empty) | 0.5 |
| S10 | density >= 0.80 | 1.0 |

## Scoring
GOLDEN >= 9.5 | PUBLISH >= 8.0 | REVIEW >= 7.0 | REJECT < 7.0

## Threshold Validation (direction-aware)
| direction | Rule | Check |
|-----------|------|-------|
| minimize | trigger < target < critical | lower = better, critical = worst |
| maximize | trigger > target > critical | higher = better, critical = floor |
