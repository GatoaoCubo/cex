---
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for optimizer
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: optimizer

## Frontmatter Fields
| Field | Type | Required | Default |
|-------|------|----------|---------|
| id | string (p11_opt_{slug}) | YES | — |
| kind | literal "optimizer" | YES | — |
| pillar | literal "P11" | YES | — |
| version | semver string | YES | "1.0.0" |
| created | date YYYY-MM-DD | YES | — |
| updated | date YYYY-MM-DD | YES | — |
| author | string | YES | — |
| domain | string (process domain being optimized) | YES | — |
| quality | null | YES | null |
| tags | list[string], len >= 3, includes "optimizer" | YES | — |
| tldr | string < 160ch | YES | — |
| density_score | float 0.80-1.00 | REC | — |

## Type-Specific Fields
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| target | string | YES | what process is being optimized |
| metric | object | YES | {name: string, unit: string, direction: enum[minimize,maximize]} |
| action | object | YES | {type: enum[tune,prune,scale,replace,restructure], description: string, automated: boolean} |
| threshold | object | YES | {trigger: float, target: float, critical: float} |
| frequency | string enum | YES | continuous / hourly / daily / weekly / monthly |
| baseline | object | YES | {value: float, measured_at: date, conditions: string} |
| improvement | object | YES | {current: float, target: float, history: list} |
| cost | object | YES | {compute: float, time: float, risk: string} |
| risk | object | YES | {level: enum[low,medium,high], mitigation: string} |
| monitoring | object | YES | {dashboard: string, alerts: list, reporting: string} |

## Body Structure (required sections)
1. ## Target Process — scope, boundaries, what is being optimized
2. ## Metrics — primary metric, secondary metrics, thresholds
3. ## Actions — triggers, strategies, automation level
4. ## Risk Assessment — cost, side effects, rollback plan
5. ## Monitoring — dashboards, alerts, reporting cadence

## Constraints
- max_bytes: 4096 (body only)
- naming: p11_opt_{target_slug}.md
- id == filename stem
- threshold.trigger < threshold.target < threshold.critical (direction: minimize) OR reversed (maximize)
- improvement.history is list of {date, value} entries
- quality: null always
- metric.direction determines threshold ordering
