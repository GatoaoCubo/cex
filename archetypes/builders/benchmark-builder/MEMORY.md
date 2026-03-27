---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: benchmark-builder

## Common Mistakes
1. Setting quality to a number instead of null (H06 rejects any value)
2. Using string for baseline/target ("fast") instead of numeric (850)
3. Iterations < 10 (minimum for any statistical meaning)
4. Warmup = 0 (always need >= 1 to avoid cold-start contamination)
5. Missing direction field (ambiguous: is 850ms good or bad?)
6. Percentiles without p95 (p50 alone hides tail latency)
7. Missing environment (benchmark is not reproducible without it)
8. Using averages in body text instead of percentiles

## Common Benchmark Patterns
| Metric | Unit | Direction | Typical baseline | Domain |
|--------|------|-----------|-----------------|--------|
| TTFT | ms | lower_is_better | 200-2000 | llm_inference |
| TPS | tokens/s | higher_is_better | 30-150 | llm_inference |
| Cost/1M input | USD | lower_is_better | 0.25-15.00 | llm_cost |
| Cost/1M output | USD | lower_is_better | 1.00-75.00 | llm_cost |
| Req/s | req/s | higher_is_better | 10-1000 | api_throughput |
| Build time | s | lower_is_better | 5-300 | ci_cd |

## Production Counter
| Metric | Value |
|--------|-------|
| Benchmarks produced | 0 (builder just created) |
| Avg quality | — |
| Common friction | baseline measurement; environment documentation |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing a benchmark, update:
- New common mistake (if encountered)
- New benchmark pattern (if discovered)
- Production counter increment
