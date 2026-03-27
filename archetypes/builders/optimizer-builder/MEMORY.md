---
pillar: P10
llm_function: INJECT
purpose: Patterns remembered between production sessions
---

# Memory: optimizer-builder

## Common Mistakes
1. Threshold ordering reversed for maximize direction — trigger must be > target > critical when maximizing
2. automated: true on risk=medium/high actions — auto-fire requires risk=low and instant rollback
3. baseline.conditions empty — "measured on 2026-03-20" is not enough; need load level + environment
4. improvement.current != baseline.value at creation — they must match on first artifact version
5. Subjective triggers ("when slow", "if degraded") — every trigger must be numeric
6. Missing rollback in Actions section — SOFT gate S05 weight 1.5, often causes score < 8.0
7. monitoring.alerts as general ("check latency") — must be specific threshold violations with time windows
8. frequency too low for fast-changing metrics — latency needs continuous, not daily
9. Conflating optimizer with bugloop — if the target is fixing a specific bug, use bugloop instead
10. cost.compute and cost.time as strings — must be floats

## Proven Optimizer Patterns
| Domain | metric | direction | frequency | action.type | automated |
|--------|--------|-----------|-----------|-------------|-----------|
| API latency | p99_latency_ms | minimize | continuous | tune | true |
| Pool quality | avg_pool_score | maximize | daily | prune | false |
| Embedding cost | tokens_per_kc | minimize | daily | tune | true |
| Pipeline throughput | kc_per_hour | maximize | hourly | scale | false |
| Memory usage | peak_memory_mb | minimize | continuous | prune | true |

## Threshold Ranges (proven)
| Domain | trigger | target | critical | direction |
|--------|---------|--------|----------|-----------|
| LLM latency (ms) | 3000 | 1500 | 8000 | minimize |
| Quality score | 7.5 | 8.5 | 6.0 | maximize |
| Error rate (%) | 2.0 | 0.5 | 10.0 | minimize |
| CPU usage (%) | 70 | 50 | 90 | minimize |

## Production Counter
| Metric | Value |
|--------|-------|
| Optimizers produced | 0 |
