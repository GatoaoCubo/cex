---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for runtime_rule production
sources: Michael Nygard Release It!, resilience patterns, rate limiting algorithms
---

# Domain Knowledge: runtime_rule

## Foundational Concept
A runtime_rule artifact defines OPERATIONAL BEHAVIOR PARAMETERS for system components at
runtime. It specifies concrete numeric values for timeouts, retry strategies, rate limits,
concurrency limits, and circuit breaker thresholds. Runtime rules follow resilience patterns
from Michael Nygard's "Release It!" (2007, 2018): timeouts prevent hung connections, retries
recover from transient failures, circuit breakers prevent cascade failures, and rate limits
protect shared resources.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| Nygard "Release It!" (2007) | Stability patterns: timeout, retry, circuit breaker, bulkhead | Core rule types in runtime_rule |
| AWS retry guidelines | Exponential backoff with jitter, max retries | retry_strategy fields |
| Stripe rate limiting | Token bucket + sliding window per endpoint | rate_limit rule type |
| Netflix Hystrix/Resilience4j | Circuit breaker with half-open recovery | circuit_breaker rule type |

## Key Patterns
- Timeout: ALWAYS set explicit timeout; no operation should wait forever
- Retry: exponential backoff (base * 2^attempt) with jitter prevents thundering herd
- Rate limit: token bucket for burst-friendly; sliding window for strict enforcement
- Circuit breaker: closed (normal) -> open (failing) -> half-open (testing recovery)
- Concurrency: limit parallel operations to prevent resource exhaustion
- Fallback: every rule MUST define what happens when the rule triggers (timeout, retry exhaust, rate exceed)

## Retry Strategies

| Strategy | Formula | Use when |
|----------|---------|----------|
| fixed | wait = interval | Simple, predictable delays |
| exponential | wait = base * 2^attempt | Network/API calls, prevents thundering herd |
| exponential_jitter | wait = base * 2^attempt + random(0, base) | Best practice for distributed systems |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT runtime_rule |
|------|------------|---------------------------|
| lifecycle_rule (P11) | Artifact lifecycle management (archive, promote, deprecate) | Lifecycle is metadata state; runtime_rule is operational behavior |
| law (P08) | Inviolable system law (never changed at runtime) | Law is permanent; runtime_rule is configurable |
| guardrail (P11) | Safety boundary (prevent harm) | Guardrail is safety constraint; runtime_rule is operational parameter |
| env_config (P09) | System environment variables | env_config is variable values; runtime_rule is behavior |
| feature_flag (P09) | On/off toggle with rollout | Feature flag is logic; runtime_rule is numeric parameter |
| permission (P09) | Access control (read/write/execute) | Permission is authorization; runtime_rule is rate/limit |
| path_config (P09) | Filesystem path definitions | path_config is location; runtime_rule is behavior |

## References
- Michael Nygard: Release It! (2007, 2018) — Stability Patterns
- AWS Architecture Blog: Exponential Backoff and Jitter
- Stripe Engineering: Rate Limiters
- Martin Fowler: Circuit Breaker pattern
