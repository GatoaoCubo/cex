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
---
## Summary
Secret configs are consumed by agents at runtime under time pressure — a stale credential or misconfigured access pattern causes silent failures that are expensive to diagnose. Three decisions made at spec time determine safety: rotation method explicitness, access pattern precision, and audit logging.

A config with `rotation_policy.frequency: daily` but no `method` leaves agents guessing whether rotation is automatic or requires operator action. A config with `access_pattern: static` without a re-deploy trigger creates indefinite credential staleness. A config with `audit_log: false` makes breach detection impossible.

## Pattern
**Explicit rotation method + dynamic access with lease TTL + always-on audit log.**

Rotation policy (complete schema):
- frequency: daily | weekly | monthly | on-breach
- method: automatic | manual | triggered
- trigger: what fires rotation (schedule, breach signal, certificate expiry)
- rollback: previous version retention period

Access pattern rules:
- dynamic: set lease_duration (1h default); agent renews on TTL expiry
- static: document re-deploy trigger (CI pipeline step)
- injected: document sidecar/init container spec reference
- env: document platform injection mechanism

Security rules:
- NEVER commit real secrets — scan for 40+ char alphanumeric strings, BEGIN PRIVATE KEY, password: non-placeholder
- audit_log: true is non-negotiable for production secrets
- Define fallback for every secret in a critical-path agent (LLM API keys, DB creds, payment keys)

## Anti-Pattern
- rotation_policy without method — caller cannot determine if action is required after rotation event.
- access_pattern: static with no re-deploy trigger — credentials silently stale after provider rotation.
- Omitting lease_duration for dynamic access — default TTL may be too short or long.
- Plaintext secrets anywhere in the file — immediate security violation.
- audit_log: false without justification — undetectable breach window.
- Missing fallback for LLM API key secrets — agent hard-fails if vault unreachable.
