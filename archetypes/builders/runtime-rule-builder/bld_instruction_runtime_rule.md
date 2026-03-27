---
id: p03_ins_runtime_rule
kind: instruction
pillar: P09
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Runtime Rule Builder Instructions
target: "runtime-rule-builder agent"
phases_count: 4
prerequisites:
  - "The operation or component that needs runtime governance is identified"
  - "Rule type is known or determinable: timeout, retry, rate_limit, circuit_breaker, or concurrency"
  - "Numeric values (durations, counts, rates) are known or researchable for the target domain"
validation_method: checklist
domain: runtime_rule
quality: null
tags: [instruction, runtime-rule, P09, timeout, retry, rate-limit, circuit-breaker]
idempotent: true
atomic: true
rollback: "Delete the produced rule file. No system behavior changes until the rule is applied to the runtime."
dependencies: []
logging: true
tldr: "Specify timeout, retry, rate limit, or circuit breaker parameters for a named operation with units, trigger behavior, and tuning guidance."
density_score: 0.93
---

## Context

A **runtime_rule** specifies the operational parameters that govern how a system component behaves under load, failure, or resource pressure. Rules are technical, numeric, and scoped to a specific component or operation. They are not behavioral policies (law), safety constraints (guardrail), or lifecycle rules — they are configuration-level specifications for engineers and runtime systems to implement.

**Inputs**

| Field | Type | Description |
|---|---|---|
| `operation` | string | The specific component or endpoint this rule governs (e.g. `llm_api_call`, `crawl_job`, `embedding_pipeline`) |
| `rule_type` | enum | `timeout` \| `retry` \| `rate_limit` \| `circuit_breaker` \| `concurrency` |
| `scope` | string | Which layer this applies to: `per_request`, `per_user`, `per_service`, `global` |
| `domain` | string | The subject domain (e.g. `llm_inference`, `data_ingestion`, `api_gateway`) |

**Output**

A single `.md` file with YAML frontmatter (all required fields) + 3 mandatory body sections: Rule Specification, Trigger Behavior, Tuning Guide. Body must be <= 3072 bytes. All numeric values must include units.

**Boundary rules**
- runtime_rule = technical parameters for timeouts, retries, limits, breakers (this builder)
- lifecycle_rule = when to promote, retire, or deprecate an artifact (different builder)
- law = inviolable behavioral rules that must never be overridden (different builder)
- guardrail = safety boundaries for agent behavior (different builder)
- env_config = environment-specific variables (different builder)
- feature_flag = on/off toggle for feature availability (different builder)

---

## Phases

### Phase 1: Research — Rule Specification

Identify the operation, classify the rule type, and determine appropriate numeric values.

```
Identify the operation:
  name: specific component, endpoint, or pipeline step (not vague like "the system")
  layer: which architectural layer (e.g. HTTP client, LLM SDK, database driver)
  failure mode: what goes wrong without this rule (hung requests, cascading failures, overload)

Classify rule_type:
  timeout:         maximum time allowed for an operation to complete
  retry:           how many times and at what intervals to retry a failed operation
  rate_limit:      maximum request or token throughput per time window
  circuit_breaker: threshold at which to stop calling a failing service temporarily
  concurrency:     maximum number of simultaneous in-flight operations

Research numeric values:
  timeout:        LLM APIs typically 30-120s; DB queries 5-30s; HTTP calls 10-30s
  retry:          2-5 attempts; exponential backoff starting 1s, max 60s
  rate_limit:     match provider limits; express in req/s, req/min, tokens/min
  circuit_breaker: 50% error rate over 10 requests; recovery window 30-60s
  concurrency:    1-10 for expensive ops; 10-100 for lightweight ops

RULE: Every numeric value MUST have a unit (ms, s, min, req/s, tokens/min, connections)
RULE: No vague terms — replace "fast", "many", "some", "reasonable" with exact numbers

Generate rule_slug: snake_case, lowercase (e.g. llm_api_call_timeout, crawl_job_retry)
Check brain_query [IF MCP] for existing runtime_rule for the same operation.
Assess severity: what is the blast radius if this rule is misconfigured?
```

Deliverable: rule type, operation, scope, numeric values with units, and severity assessment.

### Phase 2: Classify — Boundary Check

Confirm the artifact belongs to `runtime_rule` and not a sibling kind.

```
IF the rule is about when to retire or promote an artifact through its lifecycle:
  RETURN "Route to lifecycle-rule-builder."
IF the rule is an inviolable behavioral constraint that must never be overridden:
  RETURN "Route to law-builder — laws are non-technical behavioral rules."
IF the rule defines a safety boundary for agent behavior:
  RETURN "Route to guardrail-builder."
IF the value is an environment variable (API key, base URL, flag):
  RETURN "Route to env-config-builder."
IF the value is a boolean feature toggle:
  RETURN "Route to feature-flag-builder."
IF the rule governs timeout, retry, rate limit, circuit breaker, or concurrency
  AND applies to a named operation at runtime:
  PROCEED as runtime_rule
```

Deliverable: confirmed `kind: runtime_rule` with one-line justification.

### Phase 3: Compose — Build the Rule Artifact

Assemble frontmatter and all 3 required body sections following SCHEMA.md and OUTPUT_TEMPLATE.md.

```
ID generation:
  id = "p09_rr_" + rule_slug
  must match: ^p09_rr_[a-z][a-z0-9_]+$

Frontmatter (all required fields from SCHEMA.md):
  id, kind (= runtime_rule), pillar (= P09), title, version,
  created, updated, author, rule_type, operation, scope,
  domain, quality (= null), tags

Body sections (in this order):

  ## Rule Specification
  Parameter table with exact values and units:
    | Parameter         | Value       | Unit  | Notes           |
    | {param_name}      | {number}    | {ms}  | {context note}  |
  ALL values must be concrete numbers, not ranges.
  For retry: include strategy (fixed | exponential | jitter), max_attempts, base_interval, max_interval.
  For rate_limit: include window_type (sliding | token_bucket), rate, burst_allowance.
  For circuit_breaker: include error_threshold (%), sample_size, open_duration, half_open_probes.
  For timeout: include per-phase timeouts if operation has multiple phases.
  For concurrency: include queue behavior (reject | queue | backpressure) when limit exceeded.

  ## Trigger Behavior
  What happens when this rule activates:
    - Immediate action (e.g. abort request, return error, open circuit)
    - Error type / exception raised
    - Log level and required log fields
    - Downstream notification (e.g. alert, metric increment)
  State the fallback behavior explicitly (what the caller receives).

  ## Tuning Guide
  How to adjust this rule safely:
    - Safe range for each parameter (min / max)
    - Metrics to observe when tuning (latency p95, error rate, queue depth)
    - Warning signs of misconfiguration (e.g. circuit always open, retries always exhausted)
    - Dependencies: which other rules or configurations interact with this one

Body size check: must be <= 3072 bytes.
```

Deliverable: complete `.md` file with frontmatter + 3 body sections, body <= 3072 bytes.

### Phase 4: Validate — Gate Check

Run all quality gates before delivering.

```
HARD gates (all must pass — fix before delivering):
  H01: YAML frontmatter parses without errors
  H02: id matches ^p09_rr_[a-z][a-z0-9_]+$
  H03: kind == "runtime_rule"
  H04: rule_type is one of: timeout, retry, rate_limit, circuit_breaker, concurrency
  H05: all numeric values in Rule Specification have units (ms, s, req/s, etc.)
  H06: quality == null
  H07: body contains all 3 required sections
  H08: body <= 3072 bytes

SOFT gates (target >= 6/11):
  S01: operation is specific (not "the system" or "API calls" generically)
  S02: scope is one of: per_request, per_user, per_service, global
  S03: no vague terms in Rule Specification (no "fast", "many", "some", "reasonable")
  S04: Trigger Behavior specifies the exact error type or return value on activation
  S05: Trigger Behavior specifies log level and required log fields
  S06: Tuning Guide provides safe range (min/max) for at least the primary parameter
  S07: Tuning Guide identifies at least one observable metric for validation
  S08: retry rule specifies strategy type (fixed, exponential, or jitter)
  S09: circuit_breaker rule specifies both open and half-open behavior
  S10: severity assessment is present (blast radius if misconfigured)
  S11: tags include rule_type and domain

IF any HARD gate fails: fix the violation and re-check that gate.
IF soft_score < 6: add "Known gaps" note listing which soft gates failed.
Set quality: null — never self-score.
```

---

## Output Contract

```
---
id: p09_rr_{{rule_slug}}
kind: runtime_rule
pillar: P09
title: "{{title}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{author}}"
rule_type: {{timeout|retry|rate_limit|circuit_breaker|concurrency}}
operation: {{specific_operation_name}}
scope: {{per_request|per_user|per_service|global}}
domain: {{domain}}
quality: null
tags: [runtime-rule, {{rule_type}}, {{domain}}]
---

## Rule Specification

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| {{parameter_name}} | {{number}} | {{unit}} | {{context}} |

## Trigger Behavior

Activation condition: {{when_rule_fires}}
Immediate action: {{what_happens_at_activation}}
Error returned: {{error_type_or_response}}
Log level: {{debug|info|warn|error}}
Log fields: {{required_fields}}
Fallback: {{what_caller_receives}}

## Tuning Guide

Safe range: {{parameter}} = {{min}} to {{max}} {{unit}}
Observe: {{metric_name}} ({{what_to_watch_for}})
Warning signs: {{misconfiguration_symptoms}}
Dependencies: {{other_rules_or_configs_that_interact}}
```

---

## Validation

- [ ] All 8 HARD gates pass (H01-H08)
- [ ] Soft score >= 6/11 or "Known gaps" block present
- [ ] Every numeric value in Rule Specification has a unit — no bare numbers
- [ ] No vague terms anywhere in the body (replaced with exact numbers)
- [ ] `rule_type` matches the actual content of Rule Specification
- [ ] Trigger Behavior specifies what the caller receives on activation
- [ ] `quality: null` — never self-scored
- [ ] Body <= 3072 bytes

---

## Metacognition

**Does**
- Specify exact timeout, retry, rate limit, circuit breaker, or concurrency parameters for a named operation
- Require all numeric values to carry units (no bare numbers)
- Define what happens when the rule triggers (error type, log fields, fallback)
- Provide tuning guidance with safe ranges and observable metrics

**Does NOT**
- Define inviolable behavioral constraints (law-builder)
- Set safety boundaries for agent behavior (guardrail-builder)
- Manage artifact lifecycle phases (lifecycle-rule-builder)
- Store environment variables or feature flags (env-config-builder, feature-flag-builder)
- Implement the rule in code (runtime rules are specifications for engineers)

**Chaining**
- Upstream: architecture or incident analysis identifies the operation needing governance
- Downstream: runtime rule is consumed by infrastructure configuration, SDK wrappers, or service mesh policies
- Common set: timeout + retry + circuit_breaker rules for the same operation form a resilience triple
