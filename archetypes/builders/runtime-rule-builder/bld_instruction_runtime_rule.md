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
quality: 9.1
tags: [instruction, runtime-rule, P09, timeout, retry, rate-limit, circuit-breaker]
idempotent: true
atomic: true
rollback: "Delete the produced rule file. No system behavior changes until the rule is applied to the runtime."
dependencies: []
logging: true
tldr: "Specify timeout, retry, rate limit, or circuit breaker parameters for a named operation with units, trigger behavior, and tuning guidance."
density_score: 0.93
llm_function: REASON
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
## Phases
### Phase 1: Research — Rule Specification
Identify the operation, classify the rule type, and determine apownte numeric values.
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
  RETURN "Route to invariant-builder — laws are non-technical behavioral rules."
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
