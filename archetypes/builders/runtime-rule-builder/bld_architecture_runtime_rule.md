---
kind: architecture
id: bld_architecture_runtime_rule
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of runtime_rule — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Runtime Rule"
version: "1.0.0"
author: n03_builder
tags: [runtime_rule, builder, examples]
tldr: "Golden and anti-examples for runtime rule construction, demonstrating ideal structure and common pitfalls."
domain: "runtime rule construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - runtime-rule-builder
  - p03_sp_runtime_rule_builder
  - p03_ins_runtime_rule
  - bld_knowledge_card_runtime_rule
  - bld_collaboration_runtime_rule
  - bld_output_template_runtime_rule
  - bld_memory_runtime_rule
  - bld_examples_runtime_rule
  - bld_architecture_invariant
  - p11_qg_runtime_rule
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[runtime-rule-builder]] | downstream | 0.53 |
| [[p03_sp_runtime_rule_builder]] | upstream | 0.44 |
| [[p03_ins_runtime_rule]] | downstream | 0.39 |
| [[bld_knowledge_card_runtime_rule]] | downstream | 0.35 |
| [[bld_collaboration_runtime_rule]] | downstream | 0.32 |
| [[bld_output_template_runtime_rule]] | upstream | 0.32 |
| [[bld_memory_runtime_rule]] | downstream | 0.31 |
| [[bld_examples_runtime_rule]] | upstream | 0.30 |
| [[bld_architecture_invariant]] | sibling | 0.29 |
| [[p11_qg_runtime_rule]] | downstream | 0.28 |
