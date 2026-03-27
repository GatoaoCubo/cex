---
pillar: P10
llm_function: INJECT
purpose: What the builder remembers between production sessions
pattern: stateless per invocation, but carries accumulated patterns
---

# Memory: env-config-builder

## Accumulated Patterns (update after each production)

### Common Mistakes (learned from production)
1. Using hyphens in id slug (must be underscores: p09_env_api_service not p09_env_api-service)
2. Setting quality to a number instead of null (H05 rejects any non-null value)
3. variables list not matching ## Variable Catalog names exactly (S03 drift)
4. Including actual secret values in artifact (H09 — NEVER include passwords, keys, tokens)
5. Confusing env_config with boot_config (env is generic, boot is per-provider)
6. Variable names in lowercase (must be UPPER_SNAKE_CASE by convention)
7. Missing validation rules for variables (each var needs type + constraint)
8. Not marking DATABASE_URL and API keys as sensitive (common oversight)
9. Vague scope like "system" instead of concrete "api_service" or "global"
10. Missing ## Sensitive Variables section even when no sensitive vars exist (section required, state "none")

### Scope Patterns
| Scope | Typical Vars | Sensitive Count |
|-------|-------------|-----------------|
| global | LOG_LEVEL, DEBUG, NODE_ENV | 0 |
| api_service | DATABASE_URL, PORT, JWT_SECRET | 2-3 |
| satellite | MODEL, API_KEY, MCP_CONFIG | 1-2 |
| worker | QUEUE_URL, CONCURRENCY, TIMEOUT | 0-1 |

### Production Counter
| Metric | Value |
|--------|-------|
| Artifacts produced | 0 (builder just created) |
| Avg quality | - |
| Common friction | secret leaks, variable naming, scope ambiguity |

## State Between Sessions
This builder is STATELESS per invocation. Memory is embedded in this file.
After producing an env_config, update:
- New common mistake (if encountered)
- New scope pattern (if discovered)
- Production counter increment
