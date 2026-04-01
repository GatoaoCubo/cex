---
id: p01_kc_env_config
kind: knowledge_card
type: kind
pillar: P09
title: "Env Config — Deep Knowledge for env_config"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: env_config
quality: 9.0
tags: [env_config, P09, GOVERN, kind-kc]
tldr: "env_config is the versioned YAML spec of environment variables for a bounded scope — separating required from optional, documenting defaults, and pointing to secret_config rather than inlining credentials."
when_to_use: "Building, reviewing, or reasoning about env_config artifacts"
keywords: [environment_variables, configuration, system_config]
feeds_kinds: [env_config]
density_score: null
---

# Env Config

## Spec
```yaml
kind: env_config
pillar: P09
llm_function: GOVERN
max_bytes: 4096
naming: p09_env_{{scope}}.yaml
core: true
```

## What It Is
An env_config is the authoritative YAML spec of environment variables for a bounded scope — documenting required vars (system fails without them), optional vars (defaults available), and pointers to secret_config for credentials. It is NOT a boot_config (P02, per-provider startup), NOT a feature_flag (P09, binary on/off with rollout), NOT a path_config (P09, filesystem paths).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Environment variables | `LANGCHAIN_API_KEY`, `LANGCHAIN_TRACING_V2` |
| LlamaIndex | `Settings` + env vars | `OPENAI_API_KEY`, `LLAMA_INDEX_CACHE_DIR` |
| CrewAI | Env vars + LLM config | `OPENAI_API_KEY`, `SERPER_API_KEY` for tool access |
| DSPy | `dspy.configure()` + env | `OPENAI_API_KEY`, LM configuration via env |
| Haystack | YAML config + env | API keys in env; component config in YAML pipeline |
| OpenAI | Platform env vars | `OPENAI_API_KEY`, `OPENAI_ORG_ID` |
| Anthropic | Env vars + beta headers | `ANTHROPIC_API_KEY`, model names, budget env flags |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| scope | string | required | system/agent_node/service — tighter = clearer ownership |
| required | list[EnvVar] | required | System fails without these — zero defaults allowed |
| optional | list[EnvVar] | [] | System degrades gracefully — always document default |
| secret_refs | list[str] | [] | Names pointing to secret_config, never actual values |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Prefix scoping | All vars prefixed by service | `organization_*`, `RAILWAY_*`, `ANTHROPIC_*` |
| Secret separation | API keys as pointer, not value | `ANTHROPIC_API_KEY` → `p09_secret.md` |
| Feature toggle | Boolean env vars enable features | `FIRECRAWL_ENABLED=true`, `organization_RLM_PROBING=true` |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Inline secrets | API key values committed to YAML/git | Always use `secret_refs` pointer to secret_config |
| Undocumented defaults | Optional vars without defaults cause silent degradation | Document every optional var's default value |
| God env config | 50+ vars in one config with mixed scopes | Split by service scope; one file per agent_node/service |

## Integration Graph
```
secret_config, feature_flag --> [env_config] --> boot_config, runtime_rule
                                      |
                                 path_config, permission, agent_card
```

## Decision Tree
- IF var controls feature on/off with rollout THEN feature_flag (not env_config)
- IF var is a credential, key, or token THEN secret_config (not env_config)
- IF var is a filesystem path THEN path_config (not env_config)
- DEFAULT: env_config for all other system configuration variables

## Quality Criteria
- GOOD: required/optional split, scope defined, no credentials inline, defaults documented
- GREAT: validation rules per var, deployment checklist linked, migration guide for renames
- FAIL: API keys inline, no scope, missing defaults, required vs optional not distinguished
