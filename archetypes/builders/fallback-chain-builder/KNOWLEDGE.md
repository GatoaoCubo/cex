---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for fallback_chain production
sources: CEX taxonomy, circuit breaker pattern, resilience engineering, LLM provider docs
---

# Domain Knowledge: fallback_chain

## Foundational Concept
A fallback chain implements graceful degradation for LLM-powered systems. When the primary
model fails (timeout, error, rate limit) or produces below-threshold quality, the system
automatically falls back to the next model in the chain. This pattern derives from circuit
breaker design (Nygard 2007, "Release It!") adapted for multi-model LLM architectures where
models vary in capability, cost, and latency.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Circuit breaker (Nygard) | Fail-fast with recovery | circuit_breaker_threshold field |
| Netflix Hystrix | Cascading failure prevention | timeout_per_step + retry_count |
| LiteLLM fallbacks | Model-level retry with alternatives | Chain step table (model sequence) |
| AWS Route 53 health checks | DNS failover on health failure | quality_threshold triggers next step |

## Key Patterns
- Ordered degradation: steps go from most capable to least capable (opus->sonnet->haiku)
- Timeout gating: each step has max execution time before triggering next
- Quality gating: output below quality_threshold triggers next step even on success
- Circuit breaker: N consecutive failures trip the breaker, halting all attempts
- Cost awareness: each step has known cost; total chain cost has ceiling
- Retry before fallback: retry_count attempts per step before moving to next
- Final step alert: reaching last step triggers alert (system at minimum capability)
- Stateless per-request: chain state resets for each new request

## CEX-Specific Extensions

| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| quality_threshold | CEX scores output 0-10; threshold triggers fallback | No direct equivalent |
| steps_count | Integrity check: frontmatter matches body | No direct equivalent |
| cost_ceiling_usd | Budget control across all steps | AWS budget alerts |
| alert_on_final_fallback | Operational awareness when at minimum | PagerDuty severity escalation |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT fallback_chain |
|------|------------|----------------------------|
| chain (P03) | Prompt sequence (text A->B->C) | Sequences PROMPTS, not MODELS |
| workflow (P12) | Multi-step agent orchestration | Orchestrates AGENTS, not MODEL selection |
| router (P02) | Task-to-destination decision | Routes TASKS, not degrades MODELS |
| model_card (P02) | Single model specification | Describes ONE model, not a sequence |

## References
- Michael Nygard, "Release It!" (2007) — circuit breaker pattern
- LiteLLM docs — model fallback configuration
- CEX TAXONOMY_LAYERS.yaml — fallback_chain in runtime layer
- CEX SEED_BANK.yaml — P02_fallback_chain seeds
