---
id: p10_lr_secret_config_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
observation: "Secret configs without explicit rotation_policy.method caused 3 out of 5 agents to use stale credentials after provider-side rotation events. Configs that declared access_pattern: dynamic with lease_duration resolved this — agents always fetched fresh leases. Configs with access_pattern: static and no re-deploy trigger had indefinite credential staleness."
pattern: "Always declare rotation_policy with both frequency and method. Set lease_duration when access_pattern == dynamic. Define fallback for every secret used in a critical-path agent. Never allow plaintext secrets — scan before commit."
evidence: "5 agent credential incidents reviewed: 3 caused by missing rotation method, 2 caused by static access without re-deploy triggers. 0 incidents in configs with dynamic access_pattern + lease_duration + audit_log."
confidence: 0.85
outcome: SUCCESS
domain: secret_config
tags: [secret-config, rotation-policy, access-pattern, lease-duration, audit-log, credentials]
tldr: "Declare rotation method + lease_duration for dynamic access. Fallback for critical paths. Audit log always. No plaintext secrets anywhere."
impact_score: 8.5
decay_rate: 0.03
satellite: edison
keywords: [secret config, rotation policy, access pattern, lease duration, vault, kubernetes secrets, aws secrets manager, encryption, audit log, credential management]
---

## Summary
Secret configs are consumed by agents at runtime under time pressure — a stale credential or misconfigured access pattern causes silent failures that are expensive to diagnose. The difference between a secret_config that composes safely with agents and one that does not comes down to three decisions made at spec time: rotation method explicitness, access pattern precision, and audit logging.
A config that declares `rotation_policy.frequency: daily` without `method` leaves agents guessing whether rotation is automatic or requires operator action. A config with `access_pattern: static` without a re-deploy trigger creates indefinite credential staleness after provider-side rotation. A config with `audit_log: false` makes breach detection impossible.
## Pattern
**Explicit rotation method + dynamic access with lease TTL + always-on audit log.**
Rotation policy schema (complete):
- frequency: daily | weekly | monthly | on-breach
- method: automatic (provider-managed) | manual (operator action) | triggered (event-driven)
- trigger: what fires rotation (schedule, breach signal, certificate expiry)
- rollback: how to recover if rotation fails (previous version retention period)
Access pattern rules:
- dynamic: set lease_duration (1h default); agent renews on TTL expiry
- static: document re-deploy trigger (CI pipeline step, Ansible task)
- injected: document sidecar/init container spec reference
- env: document platform injection mechanism (Railway env, K8s ConfigMap ref)
Security rules:
- NEVER commit real secrets — scan with grep for 40+ char alphanumeric strings, BEGIN PRIVATE KEY, password: non-placeholder
- audit_log: true is non-negotiable for production secrets
- fallback: define for every secret in a critical-path agent (LLM API keys, DB creds, payment keys)
Body budget (1024 bytes max): Overview (100) + Provider (300) + Rotation Policy (250) + Access Pattern (300) = ~950.
## Anti-Pattern
- rotation_policy without method — caller cannot determine if action is required after rotation event.
- access_pattern: static with no re-deploy trigger — credentials silently stale after provider rotation.
- Omitting lease_duration for dynamic access — agent holds a default TTL that may be too short or too long for the task.
- Plaintext secrets anywhere in the file — immediate security violation regardless of other quality scores.
- audit_log: false without justification — undetectable breach window.
- Missing fallback for LLM API key secrets — agent hard-fails if vault is unreachable during task execution.
- Confusing secret_config with env_config: a secret_config governs SENSITIVE credentials with rotation; env_config handles non-sensitive vars like feature names, URLs, and timeouts.
## Context
The 1024-byte body limit for secret_config is tight given the four required sections. Write the rotation_policy and access_pattern fields in frontmatter first (forces scope decision), then allocate body bytes. Provider section is typically the largest — limit to auth method + paths only. Access Pattern section is load-bearing for agent implementers — include the exact retrieval steps, not just the pattern name.
