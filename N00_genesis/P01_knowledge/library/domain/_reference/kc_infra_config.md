---
id: p01_kc_infra_config
kind: knowledge_card
type: domain
pillar: P01
title: "Infrastructure Configuration — Paths, Permissions, Feature Flags, Runtime Rules, Secrets, Rate Limits"
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: infra_config
origin: manual
quality: 9.1
tags: [infrastructure, config, permissions, feature-flags, runtime, secrets, rate-limits, rbac]
tldr: "Infrastructure configuration covers path management, RBAC permissions, feature toggles, runtime constraints, secret management, and API rate limiting"
when_to_use: "Managing environment configs, access control, feature rollouts, secret rotation, or API tier enforcement"
keywords: [path, permission, feature-flag, runtime-rule, secret, rate-limit, config, rbac, vault]
long_tails:
  - "How to map environment variables and path configs to CEX path_config kind"
  - "Which patterns govern RBAC permissions and feature flag evaluation in agent systems"
axioms:
  - "Configuration is code — all infra config must be version-controlled, never hardcoded in runtime"
  - "Secrets never appear in source — use vault references or environment injection exclusively"
linked_artifacts:
  primary: null
  related: [p01_kc_orchestration_runtime, p01_kc_governance_patterns]
feeds_kinds:
  - path_config        # File paths, directory structures, mount points, working directories
  - permission         # RBAC roles, ACLs, scope fences, capability grants
  - feature_flag       # Boolean/percentage toggles, A/B flags, gradual rollouts
  - runtime_rule       # Constraints, timeouts, retry policies, concurrency limits
  - secret_config      # Vault references, env injection, rotation policies, key management
  - rate_limit_config  # API tiers, token budgets, request quotas, throttling rules
density_score: 0.88
related:
  - feature-flag-builder
  - p01_kc_feature_flag
  - bld_collaboration_secret_config
  - bld_collaboration_runtime_rule
  - bld_collaboration_feature_flag
  - secret-config-builder
  - runtime-rule-builder
  - bld_knowledge_card_feature_flag
  - bld_architecture_path_config
  - kc_env_config
---

# Infrastructure Configuration

## Quick Reference
```yaml
topic: Infra Config (paths, permissions, flags, rules, secrets, rate limits)
scope: Environment management, access control, feature toggles, runtime constraints, secrets, API limits
source: manual (cross-framework patterns)
criticality: high
```

## Key Concepts

| Concept | Domain | CEX Kind | Role |
|---------|--------|----------|------|
| Path Registry | Environment | path_config | Centralized file/dir path management with validation |
| RBAC Matrix | Access Control | permission | Role-based access with scope fences per agent/agent_group |
| Feature Toggle | Rollout | feature_flag | Boolean/percentage flags for gradual feature release |
| Runtime Constraint | Execution | runtime_rule | Timeouts, retry limits, concurrency caps, circuit breakers |
| Secret Reference | Security | secret_config | Vault URIs, env var injection, rotation schedules |
| Rate Limit Tier | API Management | rate_limit_config | Per-endpoint/per-user quotas with burst allowance |

## Patterns

| Trigger | Action |
|---------|--------|
| New environment setup | Define `path_config` entries for all required dirs, validate existence at boot |
| Add agent capability | Create `permission` entry with role, scope fence, and allowed tools list |
| Gradual feature rollout | Create `feature_flag` with percentage ramp: 0% -> 5% -> 25% -> 100% |
| Protect against runaway | Define `runtime_rule` with timeout, max_retries, and circuit breaker threshold |
| Rotate secret | Update `secret_config` rotation_policy, trigger re-injection without restart |
| Enforce API budget | Set `rate_limit_config` with requests/minute, token budget, and burst window |

## Anti-Patterns

- Hardcoding paths instead of using path_config registry (breaks across environments)
- Embedding secrets in source code or config files (use vault references only)
- Binary feature flags without gradual rollout capability (risky big-bang releases)
- Missing rate limits on LLM API calls (unbounded cost exposure)
- Runtime rules without circuit breakers (cascading failures)

## CEX Mapping

```text
[path_config -> permission] -> [feature_flag -> runtime_rule] -> [secret_config -> rate_limit_config]
  Environment setup         ->   Behavior control            ->   Security & cost boundaries
```

## References

- related: p01_kc_orchestration_runtime, p01_kc_governance_patterns
- patterns: 12-factor app, Vault, LaunchDarkly, Envoy rate limiting

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[feature-flag-builder]] | downstream | 0.37 |
| [[p01_kc_feature_flag]] | sibling | 0.32 |
| [[bld_collaboration_secret_config]] | downstream | 0.32 |
| [[bld_collaboration_runtime_rule]] | downstream | 0.30 |
| [[bld_collaboration_feature_flag]] | downstream | 0.30 |
| [[secret-config-builder]] | downstream | 0.29 |
| [[runtime-rule-builder]] | downstream | 0.27 |
| [[bld_knowledge_card_feature_flag]] | sibling | 0.25 |
| [[bld_architecture_path_config]] | downstream | 0.25 |
| [[kc_env_config]] | sibling | 0.25 |
