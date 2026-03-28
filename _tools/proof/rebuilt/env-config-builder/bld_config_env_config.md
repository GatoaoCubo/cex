---
kind: config
id: bld_config_env_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: env_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_env_{scope_slug}.yaml` | `p09_env_api_service.yaml` |
| Builder directory | kebab-case | `env-config-builder/` |
| Frontmatter fields | snake_case | `sensitive_count`, `override` |
| Scope slug | snake_case, lowercase, no hyphens | `api_service`, `global`, `shaka` |
| Variable names | UPPER_SNAKE_CASE | `DATABASE_URL`, `API_PORT` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P09_config/examples/p09_env_{scope_slug}.yaml`
- Compiled: `cex/P09_config/compiled/p09_env_{scope_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80 (no filler)
## Environment Enum
| Value | When to use |
|-------|-------------|
| development | Local dev only variables |
| staging | Pre-production environment |
| production | Production environment |
| all | Variables needed in all environments (default) |
## Scope Conventions
| Scope | Prefix | Example |
|-------|--------|---------|
| global | CEX_ | CEX_LOG_LEVEL, CEX_DEBUG |
| satellite | {DOMAIN}_ | RESEARCHER_API_KEY, BUILDER_MODEL |
| service | {SERVICE}_ | API_PORT, API_CORS_ORIGINS |
