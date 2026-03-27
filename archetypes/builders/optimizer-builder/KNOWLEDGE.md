---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for optimizer production
---

# Domain Knowledge: optimizer

## Foundational Concepts
Optimizers encode the feedback loop: measure metric -> compare to threshold -> fire action.
Origin: control theory (PID controllers), reinforcement learning (reward signals), DevOps
(SLO-driven automation). In CEX: process-level continuous improvement artifacts.

## CEX Optimizer Pattern
metric.direction determines ALL threshold semantics:
- minimize: lower is better (latency, error rate, cost). trigger=when to act, target=goal, critical=alarm.
- maximize: higher is better (throughput, score, coverage). trigger=when to act, target=goal, critical=floor alarm.

## Action Type Decision Table
| Type | When to use | Example |
|------|-------------|---------|
| tune | Adjust parameters within current system | Lower batch size when memory > 80% |
| prune | Remove low-value elements | Drop embeddings below similarity 0.3 |
| scale | Add or remove capacity | Add replicas when p99 latency > 500ms |
| replace | Swap component with better alternative | Switch model when accuracy < 0.85 |
| restructure | Redesign process flow | Reorder pipeline stages when bottleneck detected |

## Automation Decision
- automated: true — system fires action without approval. Use when: risk=low, rollback is instant, action is reversible.
- automated: false — system alerts, human approves. Use when: risk=medium/high, action is irreversible, first deployment.

## Baseline Best Practices
- Measure baseline under NORMAL load (not peak, not idle)
- Document conditions: date, load level, environment, config version
- baseline.value is the starting point for improvement.history

## Threshold Design Patterns
| Pattern | trigger | target | critical |
|---------|---------|--------|----------|
| Conservative | 70% of danger | 50% of danger | 90% of danger |
| Aggressive | 50% of danger | 30% of danger | 80% of danger |
| SLO-aligned | SLO budget burn 10% | SLO target | SLO hard limit |

## Industry References
| Pattern | Source | CEX alignment |
|---------|--------|---------------|
| SLO Error Budget | Google SRE Book | threshold.critical = SLO violation |
| PID Controller | Control Theory | trigger->action->measure loop |
| DORA Four Keys | Google DevOps | deployment frequency, lead time, MTTR, CFR |
| Auto-scaling policies | AWS/GCP | scale action with cooldown |

## Optimizer vs Siblings (P11)
| Type | Loop | Granularity | Trigger |
|------|------|------------|---------|
| optimizer | continuous metric>action | process-level | numeric threshold |
| bugloop | detect>fix>verify | artifact-level | failure signal |
| quality_gate | single pass/fail check | artifact-level | publish event |
| guardrail | block on violation | system-level | safety boundary |
| lifecycle_rule | freshness>archive>promote | artifact-level | age/staleness |
