---
pillar: P01
llm_function: INJECT
purpose: Standards and domain knowledge for env_config production
sources: 12-factor app, dotenv conventions, secret management patterns
---

# Domain Knowledge: env_config

## Foundational Concept
An env_config artifact defines the VARIABLE CONTRACT for a system scope. It catalogs
every environment variable needed: name, type, whether required, default value,
sensitivity level, and validation rule. Env configs follow the 12-Factor App principle
(Factor III: Store config in the environment) — config that varies between deploys
lives in env vars, not in code.

## Industry Implementations

| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| 12-Factor App (Factor III) | Config in environment, not code | env_config separates config from artifacts |
| dotenv (.env files) | Local dev environment variables | env_config is the spec; .env is one implementation |
| Kubernetes ConfigMap/Secret | Namespaced config and secrets | env_config maps to ConfigMap (non-sensitive) + Secret (sensitive) |
| AWS SSM Parameter Store | Hierarchical config with encryption | env_config.sensitive vars map to SecureString params |

## Key Patterns
- Scope hierarchy: global > satellite > service (narrower scope wins)
- Override precedence: env var > config file > default value
- Sensitive vars: NEVER log, NEVER commit, ALWAYS mask in output
- Validation: every var should have a type and constraint (even if permissive)
- Naming: UPPER_SNAKE_CASE for env vars, optional prefix per scope (CEX_, SHAKA_, etc.)
- Required vs optional: required vars block startup if missing; optional use defaults

## Variable Types

| Type | Validation | Example |
|------|-----------|---------|
| string | regex or enum | DATABASE_URL, LOG_LEVEL |
| integer | min/max range | PORT, MAX_RETRIES |
| boolean | true/false only | DEBUG, FEATURE_ENABLED |
| url | URL format validation | API_BASE_URL, WEBHOOK_URL |
| secret | non-empty, masked | API_KEY, JWT_SECRET |

## Boundary vs Nearby Types

| Type | What it is | Why it is NOT env_config |
|------|------------|------------------------|
| boot_config | Per-provider startup config (model, temp, system_prompt) | Boot config is provider-specific; env is generic |
| feature_flag | On/off toggle with rollout | Feature flag is logic; env is data/config |
| path_config | Filesystem path definitions | Path config is paths only; env is all variables |
| permission | Access control rules | Permission is who can do what; env is system config |
| runtime_rule | Timeouts, retries, limits | Runtime rule is behavior; env is config values |

## References
- 12factor.net/config — Factor III: Config
- dotenv specification (github.com/motdotla/dotenv)
- OWASP Secret Management Cheat Sheet
