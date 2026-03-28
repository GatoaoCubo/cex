# CEX Crew Runner -- Builder Execution
**Builder**: `runtime-rule-builder`
**Function**: CONSTRAIN
**Intent**: reconstroi env-config-builder com quality 9.5
**Quality Target**: >= 9.5
**Timestamp**: 2026-03-28T13:43:18.501809

## Intent Context
- **Verb**: reconstroi
- **Object**: env-config-builder
- **Domain**: generic
- **Multi-object**: False

## Builder Context (ISO Files)
### bld_manifest_runtime_rule.md
---
id: runtime-rule-builder
kind: type_builder
pillar: P09
parent: null
domain: runtime_rule
llm_function: GOVERN
version: 1.0.0
created: "2026-03-26"
updated: "2026-03-26"
author: builder
tags: [kind-builder, runtime-rule, P09, config, timeout, retry, limit]
---

# runtime-rule-builder
## Identity
Especialista em construir runtime_rule artifacts — regras de comportamento runtime do
sistema. Domina timeout configuration, retry strategies (fixed, exponential, jitter),
rate limiting (token bucket, sliding window), concurrency limits, circuit breaker patterns,
e a boundary entre runtime_rule (parametros tecnicos) e lifecycle_rule (P11, ciclo de vida)
ou law (P08, regras inviolaveis). Produz runtime_rule artifacts com frontmatter completo
e rule specification documentada.
## Capabilities
- Definir regras de timeout com granularidade por operacao
- Especificar retry strategies: fixed, exponential backoff, jitter
- Documentar rate limits: requests/sec, tokens/min, concurrent connections
- Definir circuit breaker thresholds e recovery behavior
- Validar artifact contra quality gates (8 HARD + 11 SOFT)
- Distinguir runtime_rule de lifecycle_rule, law, guardrail, env_config, feature_flag
## Routing
keywords: [timeout, retry, rate_limit, concurrency, circuit_breaker, backoff, throttle, limit, max_retries, cooldown]
triggers: "define timeout rules", "create retry strategy", "set rate limits", "configure circuit breaker"
## Crew Role
In a crew, I handle RUNTIME BEHAVIOR SPECIFICATION.
I answer: "what timeouts, retries, and limits govern this operation at runtime?"
I do NOT handle: lifecycle_rule (P11, artifact lifecycle), law (P08, inviolable rules),
guardrail (P11, safety boundaries), env_config (generic variables), feature_flag (on/off toggle).

### bld_instruction_runtime_rule.md
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

### bld_knowledge_card_runtime_rule.md
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

### bld_quality_gate_runtime_rule.md
---
id: p11_qg_runtime_rule
kind: quality_gate
pillar: P11
title: "Gate: Runtime Rule"
version: "1.0.0"
created: "2026-03-27"
updated: "2026-03-27"
author: builder
domain: runtime_rule
quality: null
density_score: 0.85
tags:
  - quality-gate
  - runtime-rule
  - p11
  - reliability
  - behavior
tldr: "Quality gate for runtime behavior specs: verifies rule type, numeric parameters with units, scope declaration, and recovery behavior."
---

## Definition
A runtime rule artifact specifies how a single operation behaves under load, failure, or resource pressure. It declares a rule type (timeout, retry, rate_limit, or circuit_breaker), the numeric parameters that govern the rule with explicit units, and the scope of operations the rule applies to. Every rule must define what happens when its threshold is breached — silent failure is not acceptable.
Scope: files with `kind: runtime_rule`. Does not apply to lifecycle rules (P09 sub-kind) or feature flags (P14), which govern activation rather than execution behavior.
## HARD Gates
Failure on any single gate means REJECT regardless of soft score.
| ID  | Predicate | How to test |
|-----|-----------|-------------|
| H01 | Frontmatter parses as valid YAML | `yaml.safe_load(frontmatter)` raises no error |
| H02 | `id` matches namespace `p09_rr_*` | `id.startswith("p09_rr_")` is true |
| H03 | `id` equals filename stem | `Path(file).stem == id` |
| H04 | `kind` equals literal `runtime_rule` | string equality check |
| H05 | `quality` is null at authoring time | `quality is None` |
| H06 | All required frontmatter fields present and non-empty | id, kind, pillar, title, version, created, updated, author, domain, tags, tldr, rule_type, scope all present |
| H07 | `rule_type` is one of: timeout, retry, rate_limit, circuit_breaker | enum membership check |
| H08 | All numeric parameter values include explicit units (ms, s, req/s, count, percent) | scan parameter table; every numeric value row has a unit column that is non-empty |
| H09 | `scope` field declares what operation or component this rule governs | `scope` field is non-empty string |
## SOFT Scoring
Score each dimension 0 (absent or fails) to 1 (present and passes). Weights are 0.5 or 1.0.
| #  | Dimension | Weight |
|----|-----------|--------|
| 1  | `density_score` field present and >= 0.80 | 1.0 |
| 2  | Retry strategy specified as fixed, exponential, or jitter (not just "retry") | 1.0 |
| 3  | Timeout values have units and are grounded in observed latency data or documented assumptions | 1.0 |
| 4  | Rate limit has a time window defined (per second, per minute, per hour) | 1.0 |
| 5  | Circuit breaker has a recovery behavior defined (half-open probe interval, reset condition) | 1.0 |
| 6  | Tags list includes `runtime-rule` | 0.5 |
| 7  | Default parameter values documented for each numeric field | 1.0 |
| 8  | Edge cases for parameter boundaries described (what happens at zero, at max) | 0.5 |
| 9  | Monitoring hooks or observable signals identified (metric name, alert condition) | 0.5 |
| 10 | Rule is compatible with the declared runtime environment | 0.5 |
| 11 | `tldr` is <= 160 characters | 0.5 |
**Formula**: `final_score = (sum of score_i * weight_i) / (sum of weight_i) * 10`
Weight total: 8.5. Each dimension contributes proportionally. Score range: 0.0 to 10.0.
## Actions
| Tier | Threshold | Action |
|------|-----------|--------|
| GOLDEN | >= 9.5 | Publish to pool as golden; use as reference for reliability engineering |
| PUBLISH | >= 8.0 | Publish to pool; mark production-ready |
| REVIEW | >= 7.0 | Return to author with scored dimension feedback; one revision cycle allowed |
| REJECT | < 7.0 | Block from pool; full rewrite required before re-evaluation |
## Bypass
| Field | Value |
|-------|-------|
| condition | Rule governs a third-party dependency whose latency profile is not yet characterized |
| approver | Domain lead must approve in writing before bypass takes effect |
| audit_log | Record in `records/pool/audits/bypasses.md` with date, approver, and reason |

### bld_schema_runtime_rule.md
---
kind: schema
id: bld_schema_runtime_rule
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for runtime_rule
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: runtime_rule
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_rr_{rule_slug}) | YES | - | Namespace compliance |
| kind | literal "runtime_rule" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| rule_name | string | YES | - | Human-readable rule name |
| rule_type | enum: timeout, retry, rate_limit, circuit_breaker, concurrency | YES | - | Primary rule category |
| scope | string | YES | - | What component/operation this applies to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "runtime_rule" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this rule governs |
| fallback | string | REC | - | Behavior when rule triggers |
| severity | enum: critical, high, medium, low | REC | medium | Impact if rule is misconfigured |
## ID Pattern
Regex: `^p09_rr_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Rule Specification` — concrete parameters: values with units, thresholds, limits
2. `## Trigger Behavior` — what happens when rule activates (timeout reached, retries exhausted, rate exceeded)
3. `## Tuning Guide` — how to adjust parameters, safe ranges, what metrics to watch
## Constraints
- max_bytes: 3072 (body only)
- naming: p09_rr_{rule_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- All numeric values MUST include units (ms, s, min, req/s, etc.)
- quality: null always
- NEVER use vague terms ("fast", "many") — always concrete numbers

### bld_examples_runtime_rule.md
---
kind: examples
id: bld_examples_runtime_rule
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of runtime_rule artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: runtime-rule-builder
## Golden Example
INPUT: "Define retry rules for the API client connecting to external payment provider"
OUTPUT:
```yaml
id: p09_rr_payment_api_retry
kind: runtime_rule
pillar: P09
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
rule_name: "payment_api_retry"
rule_type: retry
scope: "payment_connector"
quality: null
tags: [runtime_rule, retry, payment, P09, api, resilience]
tldr: "Payment API retry: exponential backoff 500ms base, 3 max, jitter, 5s total budget"
description: "Retry strategy for external payment API calls with exponential backoff and jitter"
fallback: "Return payment_unavailable error after 3 retries exhausted"
severity: critical
```
## Rule Specification
| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| max_retries | 3 | count | After 3 failures, stop retrying |
| base_delay | 500 | ms | Initial wait before first retry |
| strategy | exponential_jitter | - | base * 2^attempt + random(0, 250ms) |
| max_delay | 4000 | ms | Cap on any single retry delay |
| total_budget | 5000 | ms | Max total time for all retries |
| retryable_codes | [408, 429, 500, 502, 503] | HTTP | Only retry on transient errors |
## Trigger Behavior
When max_retries exhausted: return `payment_unavailable` error to caller.
When rate-limited (429): respect Retry-After header if present, else use backoff.
When total_budget exceeded: abort remaining retries, return timeout error.
Log every retry attempt with: attempt number, wait duration, error code.
## Tuning Guide
- base_delay: increase to 1000ms if payment provider has strict rate limits
- max_retries: do not exceed 5 (risk of duplicate payments)
- Monitor: retry_count metric, success_after_retry_rate, total_budget_exceeded_count
- Safe range: base_delay 200-2000ms, max_retries 1-5, total_budget 3000-15000ms
WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_rr_ pattern (H02 pass)
- kind: runtime_rule (H04 pass)
- 19 required+recommended fields present (H06 pass)
- body has all 3 sections: Rule Specification, Trigger Behavior, Tuning Guide (H07 pass)
- rule_type: retry (valid enum) (H08 pass)
- All values have units (ms, count, HTTP) (H09 pass)
- No vague terms — all concrete numbers (S05 pass)
- tldr: 75 chars <= 160 (S01 pass)
- tags: 6 items, includes "runtime_rule" (S02 pass)
## Anti-Example
INPUT: "Create retry rules"
BAD OUTPUT:
```yaml
id: retry-rules
kind: rule
pillar: runtime
rule_name: Retry
rule_type: general
timeout: fast
retries: some
quality: 8.5
tags: [retry]
```
Retry when things fail. Wait a bit between retries.
FAILURES:
1. id: "retry-rules" uses hyphens, no `p09_rr_` prefix -> H02 FAIL
2. kind: "rule" not "runtime_rule" -> H04 FAIL
3. pillar: "runtime" not "P09" -> H06 FAIL
4. rule_type: "general" not in enum [timeout, retry, rate_limit, circuit_breaker, concurrency] -> H08 FAIL
5. quality: 8.5 (not null) -> H05 FAIL
6. timeout: "fast" — vague, no numeric value with units -> H09 FAIL
7. retries: "some" — vague, no numeric value -> H09 FAIL
8. Missing fields: version, created, updated, author, scope, tldr -> H06 FAIL
9. tags: only 1 item, missing "runtime_rule" -> S02 FAIL
10. Body missing ## Rule Specification, ## Trigger Behavior, ## Tuning Guide -> H07 FAIL
11. No fallback behavior defined -> S06 FAIL
12. "Wait a bit" is vague — no concrete delay values -> S05 FAIL

### bld_config_runtime_rule.md
---
kind: config
id: bld_config_runtime_rule
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: runtime_rule Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_rr_{rule_slug}.yaml` | `p09_rr_payment_api_retry.yaml` |
| Builder directory | kebab-case | `runtime-rule-builder/` |
| Frontmatter fields | snake_case | `rule_name`, `rule_type` |
| Rule slug | snake_case, lowercase, no hyphens | `payment_api_retry`, `brain_query_timeout` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P09_config/examples/p09_rr_{rule_slug}.yaml`
- Compiled: `cex/P09_config/compiled/p09_rr_{rule_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total (frontmatter + body): ~4500 bytes
- Density: >= 0.80 (no filler)
## Rule Type Reference
| Type | Core parameters | Typical scope |
|------|----------------|---------------|
| timeout | duration (ms/s), connect_timeout, read_timeout | API calls, DB queries |
| retry | max_retries, base_delay, strategy, max_delay, total_budget | Network calls, transient failures |
| rate_limit | requests_per_second, burst_size, window, algorithm | API endpoints, external services |
| circuit_breaker | failure_threshold, recovery_timeout, half_open_requests | Service dependencies |
| concurrency | max_parallel, queue_size, rejection_policy | Worker pools, batch processing |
## Unit Conventions
| Unit | Abbreviation | When to use |
|------|-------------|-------------|
| milliseconds | ms | Timeouts < 10s, retry delays |
| seconds | s | Timeouts >= 10s, recovery windows |
| minutes | min | Long recovery, measurement windows |
| requests/second | req/s | Rate limits |
| count | count | Retries, thresholds, queue sizes |

### bld_output_template_runtime_rule.md
---
kind: output_template
id: bld_output_template_runtime_rule
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a runtime_rule artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: runtime_rule
```yaml
id: p09_rr_{{rule_slug}}
kind: runtime_rule
pillar: P09
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
rule_name: "{{human_readable_rule_name}}"
rule_type: {{timeout|retry|rate_limit|circuit_breaker|concurrency}}
scope: "{{component_or_operation}}"
quality: null
tags: [runtime_rule, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_rule_governs_max_200ch}}"
fallback: "{{behavior_when_rule_triggers}}"
severity: {{critical|high|medium|low}}
```
## Rule Specification
{{concrete_parameters_with_units}}
| Parameter | Value | Unit | Notes |
|-----------|-------|------|-------|
| {{param_1}} | {{value_1}} | {{unit_1}} | {{notes_1}} |
| {{param_2}} | {{value_2}} | {{unit_2}} | {{notes_2}} |
## Trigger Behavior
{{what_happens_when_rule_activates}}
{{fallback_behavior_details}}
## Tuning Guide
{{how_to_adjust_and_safe_ranges}}
{{metrics_to_monitor}}
## References
- {{reference_1}}

### bld_architecture_runtime_rule.md
---
kind: architecture
id: bld_architecture_runtime_rule
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of runtime_rule — inventory, dependencies, and architectural position
---

# Architecture: runtime_rule in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, scope, rule_type, etc.) | runtime-rule-builder | active |
| timeout_config | Per-operation timeout values with granularity levels | author | active |
| retry_strategy | Retry approach (fixed, exponential backoff, jitter) with max attempts | author | active |
| rate_limits | Requests per second, tokens per minute, concurrent connection caps | author | active |
| circuit_breaker | Failure threshold, open duration, and recovery behavior | author | active |
| concurrency_limits | Maximum parallel operations and queue overflow behavior | author | active |
## Dependency Graph
```
agent          --governed_by-->  runtime_rule  --enforced_by-->  runtime_engine
boot_config    --configures-->   runtime_rule  --signals-->      limit_breach
runtime_rule   --depends-->      env_config
```
| From | To | Type | Data |
|------|----|------|------|
| runtime_rule | agent (P02) | dependency | agent operations bounded by runtime parameters |
| runtime_rule | runtime_engine | consumes | engine enforces timeouts, retries, and limits |
| boot_config (P02) | runtime_rule | data_flow | boot configuration may override default values |
| env_config (P09) | runtime_rule | dependency | environment variables provide runtime-specific values |
| runtime_rule | limit_breach (P12) | signals | emitted when a limit, timeout, or circuit is triggered |
| law (P08) | runtime_rule | dependency | laws may mandate specific runtime constraints |
## Boundary Table
| runtime_rule IS | runtime_rule IS NOT |
|-----------------|---------------------|
| A technical runtime parameter (timeout, retry, rate limit) | An artifact lifecycle state machine (lifecycle_rule P11) |
| Scoped to specific operations or services | An inviolable operational mandate (law P08) |
| Configures circuit breaker and concurrency limits | A safety restriction on agent behavior (guardrail P11) |
| Enforced by the runtime engine automatically | A generic environment variable (env_config P09) |
| Overridable via boot_config or environment | A feature on/off toggle (feature_flag P09) |
| Prevents cascade failures through backpressure | A quality scoring check (quality_gate P11) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Configuration | frontmatter, env_config, boot_config | Supply rule identity and environment overrides |
| Timing | timeout_config, retry_strategy | Define when operations stop and how they retry |
| Throughput | rate_limits, concurrency_limits | Cap request rates and parallel operations |
| Resilience | circuit_breaker | Prevent cascade failures with open/close circuits |
| Enforcement | runtime_engine, limit_breach | Apply rules and signal when limits are hit |


[... truncated at 30KB budget ...]

## Execution Instructions
1. You are executing builder `runtime-rule-builder` for pipeline function `CONSTRAIN`.
2. Follow the builder's ISO instructions precisely.
3. Generate the complete output artifact.
4. Quality target: >= 9.5 (no filler, no repetition, no platitudes).
5. At the end, self-assess with: `quality: X.X`
