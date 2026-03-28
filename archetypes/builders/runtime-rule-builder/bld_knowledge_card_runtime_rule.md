---
kind: knowledge_card
id: bld_knowledge_card_runtime_rule
pillar: P09
llm_function: INJECT
purpose: Domain knowledge for runtime_rule production — atomic searchable facts
sources: runtime-rule-builder MANIFEST.md + SCHEMA.md
---

# Domain Knowledge: runtime_rule

## Executive Summary

A runtime_rule specifies concrete numeric parameters governing system behavior at execution time — timeouts, retry strategies, rate limits, circuit breakers, and concurrency limits. It is a technical configuration artifact, not a policy declaration. Every numeric value requires units (ms, s, req/s). It differs from lifecycle_rule (P11, artifact state transitions), law (P08, inviolable axioms), guardrail (P11, safety boundary), env_config (variable values), and feature_flag (on/off toggle).

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P09 (config) |
| ID pattern | `^p09_rr_[a-z][a-z0-9_]+$` |
| Required frontmatter fields | 13 (includes `rule_name`, `rule_type`, `scope`) |
| Recommended fields | 3 (description, fallback, severity) |
| `rule_type` enum | timeout / retry / rate_limit / circuit_breaker / concurrency |
| `severity` enum | critical / high / medium (default) / low |
| Max body | 3072 bytes |
| Body sections | 3 (Rule Specification, Trigger Behavior, Tuning Guide) |
| Naming | `p09_rr_{rule_slug}.yaml` |

## Patterns

| Pattern | Rule |
|---------|------|
| Units required | Every numeric value MUST include units: ms, s, min, req/s, tokens/min, connections |
| Retry strategies | `fixed` (constant interval) / `exponential` (base * 2^attempt) / `exponential_jitter` (adds random spread; best practice for distributed systems) |
| Rate limit algorithms | `token_bucket` (burst-tolerant) / `sliding_window` (strict, no burst) |
| Circuit breaker states | CLOSED (normal) → OPEN (blocking, failure threshold exceeded) → HALF_OPEN (probe recovery) |
| `fallback` field | Specifies concrete behavior on trigger: "return cached response", "reject with HTTP 429", "enqueue for retry" |
| `scope` field | Names the specific component or operation — not system-wide unless explicitly stated |
| Tuning Guide section | Must include safe parameter ranges + metric signals indicating misconfiguration |

## Anti-Patterns

| Anti-Pattern | Why it fails |
|-------------|-------------|
| Vague values ("fast", "a few retries", "low rate") | Schema rejects non-numeric; unenforceable at runtime |
| Numeric values without units | Ambiguous — ms vs s vs min differs by orders of magnitude |
| runtime_rule for lifecycle transitions | Wrong kind — use lifecycle_rule (P11) |
| runtime_rule for inviolable axioms | Wrong kind — use law (P08) |
| runtime_rule for safety boundaries | Wrong kind — use guardrail (P11) |
| No `fallback` specified | Undefined system behavior when rule triggers |
| Circuit breaker with no HALF_OPEN policy | Circuit stays open permanently; no recovery path |
| `quality` non-null | Self-scoring forbidden; always `null` |

## Application

1. Identify the operation and select `rule_type`: timeout / retry / rate_limit / circuit_breaker / concurrency
2. Write frontmatter: 13 required fields — `rule_name` (human label), `scope` (specific component), `quality: null`
3. Add recommended fields: `severity` (impact if misconfigured), `fallback` (what triggers), `description` (<= 200 chars)
4. Write `## Rule Specification` — all parameters with concrete values and units:
   - Timeout: `timeout_ms: 30000`, `timeout_action: reject`
   - Retry: `max_retries: 3`, `backoff_base_ms: 1000`, `strategy: exponential_jitter`
   - Rate limit: `requests_per_sec: 10`, `algorithm: token_bucket`, `burst_limit: 20`
   - Circuit breaker: `failure_threshold: 5`, `open_duration_ms: 60000`, `probe_interval_ms: 10000`
5. Write `## Trigger Behavior` — what happens when rule fires; not just what the rule is
6. Write `## Tuning Guide` — safe ranges, metric signals, how to adjust per load profile
7. Verify body <= 3072 bytes; all numeric values have units; `id` equals filename stem

## References

- runtime-rule-builder MANIFEST.md v1.0.0
- runtime_rule SCHEMA.md (no version declared)
- Boundary: runtime_rule (operational params, P09) vs lifecycle_rule (P11, state transitions) vs law (P08, inviolable) vs guardrail (P11, safety) vs env_config (P09, variable values) vs feature_flag (P09, on/off toggle)
