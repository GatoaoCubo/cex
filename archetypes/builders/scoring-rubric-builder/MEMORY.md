---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: scoring-rubric-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Weights not summing to exactly 100% (H07, most common: rounding error)
3. Fewer than 3 dimensions (H08, minimum for meaningful evaluation)
4. Overlapping dimensions (e.g., "quality" and "completeness" both checking fields)
5. Subjective criteria ("good enough", "appropriate") instead of measurable
6. Missing automation_status or invalid enum value (H09)
7. Omitting one of the 4 tiers (H10, all must be present)
8. Using hyphens in id slug (must be underscores: p07_sr_5d_kc)

## Proven Rubric Patterns
| Framework | Dimensions | Domain | Weights |
|-----------|-----------|--------|---------|
| 5D | Density, Completeness, Actionability, Boundary, References | knowledge_card | 25/25/20/15/15 |
| HARD/SOFT | Binary gates + weighted numeric | quality_gate | varies |
| 12LP | One per pillar (P01-P12) | cross-pillar | equal ~8% each |

## Production Counter
| Metric | Value |
|--------|-------|
| Rubrics produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | weight balancing; concrete criteria wording |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a scoring_rubric, update:
- New common mistake (if encountered)
- New proven rubric pattern (if discovered)
- Production counter increment
