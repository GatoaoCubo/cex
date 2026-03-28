---
kind: knowledge_card
id: bld_knowledge_card_env_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for env_config production — environment variable specification
sources: 12-Factor App (Factor III), dotenv conventions, Kubernetes ConfigMap/Secret, OWASP
---

# Domain Knowledge: env_config
## Executive Summary
Env configs define the variable contract for a system scope — every environment variable needed with its name, type, default, sensitivity level, and validation rule. Following 12-Factor App principle III (store config in environment, not code), env configs separate deployment-varying configuration from artifacts. They differ from boot configs (provider-specific), feature flags (on/off logic), and permissions (access control).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (config) |
| llm_function | GOVERN |
| Frontmatter fields | 15+ |
| Quality gates | 8 HARD + 11 SOFT |
| Override precedence | env var > config file > default |
| Scope hierarchy | global > satellite > service |
| Naming | UPPER_SNAKE_CASE, optional prefix per scope |
## Patterns
- **Variable type system**: every variable has an explicit type with validation
| Type | Validation | Example |
|------|-----------|---------|
| string | regex or enum | LOG_LEVEL, DATABASE_URL |
| integer | min/max range | PORT, MAX_RETRIES |
| boolean | true/false only | DEBUG, FEATURE_ENABLED |
| url | URL format check | API_BASE_URL, WEBHOOK_URL |
| secret | non-empty, masked | API_KEY, JWT_SECRET |
- **Scope hierarchy**: narrower scope wins — service config overrides satellite, satellite overrides global
- **Sensitivity handling**: sensitive vars (secrets, keys) NEVER logged, NEVER committed, ALWAYS masked in output
- **Required vs optional**: required vars block startup if missing; optional vars use defaults
- **Naming convention**: UPPER_SNAKE_CASE with optional prefix (CEX_, researcher_) for scope clarity
| Source | Concept | Application |
|--------|---------|-------------|
| 12-Factor (III) | Config in environment | Separate config from code |
| dotenv | Local dev variables | .env as implementation of spec |
| K8s ConfigMap/Secret | Namespaced config | Non-sensitive vs sensitive split |
| AWS SSM | Hierarchical encrypted config | SecureString for sensitive vars |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Secrets in code/config files | Committed to git; exposed in logs |
| No validation rules | Invalid values cause runtime errors |
| Missing defaults for optional vars | Startup fails unnecessarily |
| No scope prefix | Variable collisions between services |
| Logging sensitive vars | Secrets appear in plaintext in logs |
| No type declaration | String "true" treated as truthy in some languages, not others |
## Application
1. Catalog variables: name, type, required/optional, default, description
2. Classify sensitivity: public (ConfigMap) vs sensitive (Secret)
3. Define validation: regex, range, enum per variable
4. Set scope: global, satellite, or service with appropriate prefix
5. Document precedence: env var > config file > default
6. Validate: required vars have no defaults; secrets are marked sensitive
## References
- 12factor.net/config: Factor III — Config in environment
- dotenv: local development variable convention
- OWASP: Secret Management Cheat Sheet
- Kubernetes: ConfigMap and Secret best practices
