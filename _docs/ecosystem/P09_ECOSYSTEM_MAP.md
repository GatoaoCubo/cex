# P09 Config — Ecosystem Map
> Generated: 2026-03-28 | Author: builder_agent

## 1. Frameworks Audited
| Framework | Domain | Key Concepts |
|-----------|--------|--------------|
| LiteLLM | LLM proxy/router | model_list, fallback chains, budgets, rate limits, API key vault, router config, retry policy, timeout config |
| RouteLLM | Model routing | routing_strategy, cost thresholds, model tiers, preference matrix, calibration data |
| OpenRouter | Multi-model API | model selection, pricing tiers, rate limits, provider preferences, fallback ordering |
| Portkey | AI gateway | virtual keys, configs (retry, cache, timeout), guardrails config, load balancing weights, provider routing |
| Helicone | Observability | API key proxy, property headers, cache config, rate limit policies, alert thresholds, logging config |
| LangFuse | LLM observability | project config, API keys, trace sampling, score definitions, prompt management, dataset config |
| Anthropic Rate Limits | API provider | tier system (1-4), RPM/TPM limits, daily token limits, rate limit headers, retry-after |
| OpenAI Tier System | API provider | usage tiers (free-5), RPM/TPM/RPD limits, model access gates, organization quotas |
| LaunchDarkly | Feature management | flags (boolean/multivariate/JSON), targeting rules, segments, rollout %, prerequisite flags, experiments |
| dotenv | Env management | .env files, variable interpolation, multi-environment (.env.local, .env.production), type coercion |
| 12-Factor App | App methodology | strict config/code separation, env vars only, no config files in code, backing service URLs as config |
| Kubernetes ConfigMaps | Container config | ConfigMap, Secret, mounted volumes, env injection, hot-reload via watch, namespace isolation |
| HashiCorp Vault | Secrets management | dynamic secrets, secret engines, policies, token auth, lease/renewal, encryption-as-a-service, audit log |

## 2. Industry Concepts Found
| Concept | Framework(s) | Description | Frequency |
|---------|-------------|-------------|:---------:|
| Environment Variable | dotenv, 12-Factor, K8s (env injection), Vault (env template), LiteLLM, Helicone, LangFuse | Key-value config injected at runtime, not in code | 7 |
| Secret / API Key | Vault (dynamic secrets), K8s (Secrets), Portkey (virtual keys), LiteLLM (API key vault), Helicone (proxy keys), LangFuse (API keys) | Sensitive credential with rotation, encryption, access audit | 6 |
| Rate Limit Config | Anthropic (tier RPM/TPM), OpenAI (tier RPM/TPM/RPD), LiteLLM (budgets), Portkey (rate limiting), Helicone (rate limit policies), OpenRouter (rate limits) | Throughput constraints per model/key/org with enforcement policy | 6 |
| Feature Flag | LaunchDarkly (flags), Portkey (config versions), K8s (feature gates), LiteLLM (feature toggles) | Boolean/multivariate toggle for gradual rollout and experimentation | 4 |
| Fallback / Retry Config | LiteLLM (fallback chains), Portkey (retry config), OpenRouter (fallback ordering), RouteLLM (fallback tiers) | Ordered list of alternatives when primary fails, with retry policy | 4 |
| Model Routing Config | LiteLLM (model_list + router), RouteLLM (routing_strategy), OpenRouter (model selection), Portkey (load balancing) | Rules for selecting which model handles a request based on cost/quality/latency | 4 |
| Path / Mount Config | K8s (volume mounts), Vault (mount paths), dotenv (file paths), 12-Factor (backing service URLs) | File system paths or URLs for locating resources | 4 |
| Permission / Access Policy | Vault (policies), K8s (RBAC), Anthropic (tier access), OpenAI (model access gates), LaunchDarkly (role targeting) | Who can access what, with granularity levels | 5 |
| Budget / Cost Limit | LiteLLM (max_budget), Portkey (spend alerts), Helicone (cost tracking), OpenRouter (credit limits) | Spending cap that triggers alerts or blocks requests | 4 |
| Observability Config | Helicone (logging config), LangFuse (trace sampling, score definitions), Portkey (analytics config) | What to log, trace, measure, and alert on | 3 |
| Cache Config | Portkey (cache config), Helicone (semantic cache), LiteLLM (cache type + TTL) | Caching strategy (exact/semantic), TTL, invalidation rules | 3 |
| Runtime Rule | LiteLLM (timeout, retry), Portkey (timeout, retry, cache), Anthropic (retry-after), K8s (resource limits) | Operational constraints: timeouts, retries, concurrency limits | 4 |

## 3. CEX Current vs Industry
| CEX Kind | Maps To | Coverage % | Gap |
|----------|---------|:----------:|-----|
| env_config | Environment Variable | 90% | Excellent match. CEX covers dotenv + 12-Factor patterns well. Minor gap: no multi-environment layering (.env.local overrides .env). |
| path_config | Path / Mount Config | 80% | Good match to K8s mounts and 12-Factor backing service URLs. Gap: industry treats paths as a subset of env_config (12-Factor says ALL config is env vars); CEX separates them, which is actually more organized. |
| permission | Permission / Access Policy | 75% | Matches Vault policies and K8s RBAC. Gap: industry permissions often include temporal rules (expire-after, time-window access) and audit logging. CEX is static read/write/execute. |
| feature_flag | Feature Flag | 70% | Matches LaunchDarkly core concept. Gap: industry flags support targeting rules (user segments, % rollout, prerequisites), multivariate values (not just on/off), and experiment linkage. CEX is simpler. |
| runtime_rule | Runtime Rule | 85% | Strong match to LiteLLM/Portkey timeout/retry configs. Well-scoped in CEX. Gap: industry adds circuit-breaker pattern (open/half-open/closed states). |

## 4. Proposed NEW Kinds (ONLY if 2+ frameworks use it)
| Kind | Justification | Frameworks | Priority |
|------|---------------|------------|:-------:|
| secret_config | Secrets are universally treated as distinct from general env vars. They require rotation, encryption at rest, access audit, and lease management. CEX currently puts API keys in env_config, but industry strongly separates them. Distinct from permission (who CAN access) — secret_config is WHAT is protected and HOW it rotates. | Vault (dynamic secrets), K8s (Secrets), Portkey (virtual keys), LiteLLM (API key vault), Helicone (proxy keys) | high |
| rate_limit_config | Rate limiting is a first-class concept in every LLM API (Anthropic tiers, OpenAI tiers) and every proxy (LiteLLM, Portkey, Helicone). Includes RPM, TPM, daily caps, budget limits, and tier escalation. Currently partially covered by runtime_rule, but rate limits have unique semantics: they're provider-imposed, tier-dependent, and budget-linked. | Anthropic, OpenAI, LiteLLM, Portkey, Helicone, OpenRouter | med |

## 5. Proposed REMOVALS/RENAMES
| Kind | Action | Reason |
|------|--------|--------|
| env_config | NARROW scope | After extracting secret_config, env_config should explicitly exclude secrets. Boundary update: "Non-sensitive configuration variables. For API keys and credentials, use secret_config." |
| runtime_rule | NARROW scope | After extracting rate_limit_config, runtime_rule should focus on timeouts, retries, concurrency. Boundary update: "Operational constraints excluding rate limits (see rate_limit_config)." |

## 6. KEEPS (validated)
| Kind | Frameworks That Match |
|------|----------------------|
| env_config | dotenv, 12-Factor App, K8s ConfigMaps, LiteLLM general config, LangFuse project config |
| path_config | K8s volume mounts, Vault mount paths, 12-Factor backing service URLs, dotenv file locations |
| permission | Vault policies, K8s RBAC, Anthropic tier access gates, OpenAI model access, LaunchDarkly role targeting |
| feature_flag | LaunchDarkly flags, Portkey config versions, K8s feature gates, LiteLLM feature toggles |
| runtime_rule | LiteLLM timeout/retry, Portkey retry config, Anthropic retry-after headers, K8s resource limits |

## 7. Summary
Current: 5 kinds → Proposed: 7 kinds (+secret_config, +rate_limit_config) | Coverage: ~80% → ~90%

Key insight: The LLM API ecosystem universally treats **secrets** and **rate limits** as first-class configuration concerns, separate from general env vars and runtime rules. Every LLM proxy (LiteLLM, Portkey, OpenRouter) and every provider (Anthropic, OpenAI) has dedicated rate limit semantics with tiers, budgets, and escalation paths. Similarly, Vault and K8s Secrets demonstrate that secrets management (rotation, encryption, audit) is fundamentally different from env var management. CEX's current kinds are solid but slightly under-differentiated in these two high-traffic areas.
