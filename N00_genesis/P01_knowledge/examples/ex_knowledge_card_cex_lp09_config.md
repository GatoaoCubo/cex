---
id: p01_kc_cex_lp09_config
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP09 Config — Operational Control Panel for LLM Systems"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, lp09, config, env-config, feature-flag, permission, runtime-rule]
tldr: "P09 defines 5 types of operational configuration: env_config, path_config, permission, feature_flag, runtime_rule"
when_to_use: "Understand how LLM systems separate configuration from identity and architecture"
keywords: [config, env-config, path-config, permission, feature-flag, runtime-rule]
long_tails:
  - "How to configure environment variables for LLM agents"
  - "What is the difference between config P09 and boot_config P02 in CEX"
axioms:
  - "ALWAYS separate config (P09) from identity (P02)"
  - "NEVER hardcode values that belong in env_config"
linked_artifacts:
  primary: p01_kc_cex_lp08_architecture
  related: [p01_kc_cex_lp10_memory]
density_score: 1.0
data_source: "https://12factor.net/config"
related:
  - p01_kc_lp09_config
  - bld_architecture_env_config
  - env-config-builder
  - path-config-builder
  - bld_architecture_runtime_rule
  - bld_architecture_path_config
  - bld_examples_kind
  - runtime-rule-builder
  - bld_architecture_sso_config
  - bld_architecture_playground_config
---

## Quick Reference

topic: P09 Config | scope: operational settings | criticality: high
types: 5 | function: GOVERN | layer: runtime + governance

## Key Concepts

- P09 is the operational control panel of the system
- env_config stores environment variables (API keys, URLs)
- path_config defines filesystem paths per scope
- permission controls read/write/execute access per resource
- feature_flag enables/disables features with rollout
- runtime_rule defines timeouts, retries and technical limits
- P09 transforms architecture (P08) into concrete operation
- Config is NOT identity: P02 defines WHO, P09 defines HOW
- boot_config (P02) is per-provider; env_config (P09) is global
- permission (P09) controls access; guardrail (P11) is safety
- runtime_rule (P09) is technical; law (P08) is inviolable
- feature_flag uses JSON; remaining types use YAML
- env_config max 4096 bytes; feature_flag max 1536 bytes
- P09 configures P04 (which tools are enabled)
- P09 configures P02 (which model, temperature, tokens)
- Dominant function: GOVERN (operational governance)
- Analogy: altimeter in feet vs meters changes everything

## Phases

1. Survey all required environment variables
2. Create env_config with values per scope (dev/staging/prod)
3. Define path_config with absolute paths per environment
4. Map permissions per resource and role (read/write/exec)
5. Isolate experimental features with feature_flags
6. Document runtime_rules (timeouts, retries, rate limits)

## Golden Rules

- ALWAYS externalize config (never inline in code)
- NEVER confuse env_config with boot_config (P02)
- ALWAYS validate config at initialization (fail fast)
- NEVER place secrets in feature_flags (use env_config)
- ALWAYS have safe defaults when config is absent

## Comparativo

| Tipo | Layer | Format | Max Bytes | Exemplo |
|------|-------|--------|-----------|---------|
| env_config | runtime | yaml | 4096 | API keys, URLs, secrets |
| path_config | runtime | yaml | 3072 | Dirs de agents, pool, output |
| permission | governance | yaml | 3072 | Agent_group write access |
| feature_flag | runtime | json | 1536 | Enable firecrawl enrichment |
| runtime_rule | runtime | yaml | 3072 | Timeout 30s, max 3 retries |

## Flow

```
[P09: Config Layer]
         |
    +----+----+----+----+
    |    |    |    |    |
  env  path perm  ff  rule
    |    |    |    |    |
    v    v    v    v    v
  [GOVERN]  [GOVERN]  [GOVERN]
    |          |        |
    v          v        v
 variables  access   limits
    |          |        |
    +-----+----+--------+
          |
          v
   [P04 tools enabled]
          |
          v
   [P02 model configured]
```

## References

- source: https://12factor.net/config
- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_lp08_architecture
- related: p01_kc_cex_lp10_memory


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_lp09_config]] | sibling | 0.41 |
| [[bld_architecture_env_config]] | downstream | 0.38 |
| [[env-config-builder]] | downstream | 0.35 |
| [[path-config-builder]] | downstream | 0.30 |
| [[bld_architecture_runtime_rule]] | downstream | 0.27 |
| [[bld_architecture_path_config]] | downstream | 0.26 |
| [[bld_examples_kind]] | downstream | 0.25 |
| [[runtime-rule-builder]] | downstream | 0.25 |
| [[bld_architecture_sso_config]] | downstream | 0.25 |
| [[bld_architecture_playground_config]] | downstream | 0.25 |
