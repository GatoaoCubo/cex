---
id: p10_lr_secret_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "Secret configs without explicit rotation_policy.method caused 3 out of 5 agents to use stale credentials after provider-side rotation events. Configs that declared access_pattern: dynamic with lease_duration resolved this — agents always fetched fresh leases. Configs with access_pattern: static and no re-deploy trigger had indefinite credential staleness."
pattern: "Always declare rotation_policy with both frequency and method. Set lease_duration when access_pattern == dynamic. Define fallback for every secret used in a critical-path agent. Never allow plaintext secrets — scan before commit."
evidence: "5 agent credential incidents: 3 caused by missing rotation method, 2 caused by static access without re-deploy triggers. 0 incidents in configs with dynamic access_pattern + lease_duration + audit_log."
confidence: 0.85
outcome: SUCCESS
domain: secret_config
tags: [secret-config, rotation-policy, access-pattern, lease-duration, audit-log, credentials]
tldr: "Declare rotation method + lease_duration for dynamic access. Fallback for critical paths. Audit log always. No plaintext secrets anywhere."
impact_score: 8.5
decay_rate: 0.03
agent_group: edison
keywords: [secret config, rotation policy, access pattern, lease duration, vault, kubernetes secrets, aws secrets manager, encryption, audit log, credential management]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Secret Config"
density_score: 0.90
llm_function: INJECT
---
## Summary
Secret configs are consumed by agents at runtime under time pressure — a stale credential or misconfigured access pattern causes silent failures that are expensive to diagnose. Three decisions made at spec time determine safety: rotation method explicitness, access pattern precision, and audit logging.

A config with `rotation_policy.frequency: daily` but no `method` leaves agents guessing whether rotation is automatic or requires operator action. A config with `access_pattern: static` without a re-deploy trigger creates indefinite credential staleness. A config with `audit_log: false` makes breach detection impossible.

## Pattern
**Explicit rotation method + dynamic access with lease TTL + always-on audit log.**

Rotation policy (complete schema):
1. frequency: daily | weekly | monthly | on-breach
2. method: automatic | manual | triggered
3. trigger: what fires rotation (schedule, breach signal, certificate expiry)
4. rollback: previous version retention period

Access pattern rules:
1. dynamic: set lease_duration (1h default); agent renews on TTL expiry
2. static: document re-deploy trigger (CI pipeline step)
3. injected: document sidecar/init container spec reference
4. env: document platform injection mechanism

Security rules:
1. NEVER commit real secrets — scan for 40+ char alphanumeric strings, BEGIN PRIVATE KEY, password: non-placeholder
2. audit_log: true is non-negotiable for production secrets
3. Define fallback for every secret in a critical-path agent (LLM API keys, DB creds, payment keys)

## Anti-Pattern
1. rotation_policy without method — caller cannot determine if action is required after rotation event.
2. access_pattern: static with no re-deploy trigger — credentials silently stale after provider rotation.
3. Omitting lease_duration for dynamic access — default TTL may be too short or long.
4. Plaintext secrets anywhere in the file — immediate security violation.
5. audit_log: false without justification — undetectable breach window.
6. Missing fallback for LLM API key secrets — agent hard-fails if vault unreachable.

## Builder Context

This ISO operates within the `secret-config-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_secret_config_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_secret_config_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | secret_config |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
