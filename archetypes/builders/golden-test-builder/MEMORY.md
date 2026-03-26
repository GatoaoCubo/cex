---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: golden-test-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. quality_threshold below 9.5 (H07 rejects < 9.5)
3. Truncated golden_output with "..." (must be complete artifact)
4. Rationale without gate IDs ("it's good" instead of "H01-H10 pass")
5. Producer self-approving as reviewer (separate roles required)
6. Confusing golden_test with few_shot_example (P01 teaches; P07 evaluates)
7. Using hyphens in id slug (must be underscores: p07_gt_kc_caching)

## Golden Candidate Sources
| Source | Where | Quality indicator |
|--------|-------|-------------------|
| Pool artifacts | pool/ | quality >= 9.5 in metadata |
| Builder examples | archetypes/builders/*/EXAMPLES.md | Golden section |
| Manual curation | Domain experts | Reviewer stamp |

## Production Counter
| Metric | Value |
|--------|-------|
| Tests produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | finding 9.5+ candidates; complete output length |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a golden_test, update:
- New common mistake (if encountered)
- New golden candidate source (if discovered)
- Production counter increment
