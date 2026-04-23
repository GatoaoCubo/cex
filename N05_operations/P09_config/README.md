# P09 Config — N05 Operations

> Gating Wrath · configuration for deploy, CI/CD, runtime

## Scope in N05
Runtime settings for operations: deploy targets, CI secrets,
environment vars, feature flags for release toggles, rate limits
on deploy operations. Wrath drives "break what must break" — so
configs here enforce strict gates (fail-closed by default).

## Kinds that live here
- `env_config` — env vars per environment (dev/staging/prod)
- `secret_config` — deploy keys, DB credentials (gitignored)
- `feature_flag` — release toggles with kill-switch semantics
- `rate_limit_config` — throttles on deploy/rollback operations

## Related
- `tools/` — CI/CD scripts and deploy tools this config governs
- `quality/` — gates that read these flags
