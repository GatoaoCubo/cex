---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: pattern-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p08_pat_my_pattern not p08_pat_my-pattern)
3. Writing benefits-only consequences — must include at least 1 cost/drawback
4. Problem describing a one-off fix instead of recurring situation
5. Name too long (>5 words) or too vague (1 word)
6. Solution as abstract advice ("be efficient") instead of concrete steps
7. Confusing pattern with law — ask "is this a recommendation or a mandate?"
8. Confusing pattern with workflow — ask "does this describe or execute?"

### Architecture Pattern Catalog

| Domain | Common patterns | Key boundary |
|--------|----------------|-------------|
| Orchestration | Batching, signal monitoring, wave execution | vs workflow (P12) |
| Resilience | Retry, circuit breaker, fallback chain | vs runtime_rule (P09) |
| Knowledge | Distillation, hydration, pool promotion | vs instruction (P03) |
| Identity | Fractal boot, mental model derivation | vs satellite_spec (P08) |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | forces identification, consequences balance |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a pattern, update:
- New common mistake (if encountered)
- New catalog entry (if new domain)
- Production counter increment
