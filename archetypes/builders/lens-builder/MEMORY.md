---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: lens-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Setting quality to a number instead of null (H05 rejects any value)
2. Using hyphens in id slug (must be underscores: p02_lens_cost_efficiency, not p02_lens_cost-efficiency)
3. Making applies_to a string instead of list (must be list[string])
4. Writing abstract filters ("quality aspects") instead of concrete attributes ("pricing", "latency")
5. Omitting Limitations section (every perspective has blind spots)
6. Drifting into agent territory — adding execution logic or tool references
7. Mixing lens with scoring rubric — lens filters, rubric scores
8. Empty applies_to list (must have at least 1 kind)

### Lens Patterns

| Pattern | When to use | Focus style |
|---------|-------------|------------|
| Cost lens | Budget/ROI decisions | Pricing, efficiency ratios |
| Quality lens | Output evaluation | Accuracy, density, completeness |
| Speed lens | Latency-sensitive routing | Throughput, response time |
| Security lens | Compliance/safety review | Vulnerabilities, permissions |
| Domain lens | Specialized analysis | Industry-specific attributes |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | abstract vs concrete filters, boundary with scoring_rubric |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a lens, update:
- New common mistake (if encountered)
- New lens pattern (if discovered)
- Production counter increment
