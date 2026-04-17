---
id: p01_kc_secret_config
kind: knowledge_card
type: kind
pillar: P09
title: "Secret Config — Deep Knowledge for secret_config"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: commercial_agent
domain: secret_config
quality: 9.1
tags: [secret_config, P09, GOVERN, kind-kc]
tldr: "secret_config documents the existence, storage location, and rotation schedule of credentials — never their values — providing a pointer registry that env_config references via secret_refs."
when_to_use: "Building, reviewing, or reasoning about secret_config artifacts"
keywords: [secrets_management, credentials, rotation_schedule]
feeds_kinds: [secret_config]
density_score: null
---

# Secret Config

## Spec
```yaml
kind: secret_config
pillar: P09
llm_function: GOVERN
max_bytes: 1024
naming: p09_secret.md
core: true
```

## What It Is
A secret_config documents the existence, storage backend, env var name, and rotation schedule of credentials — never their actual values. It serves as a pointer registry: env_config uses `secret_refs` to point here, and runtime reads from environment or vault. It is NOT an env_config (which stores non-sensitive configuration values).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|-------------------|---------------|-------|
| LangChain | Environment variable pattern | `LANGCHAIN_API_KEY` via env only — never in code |
| LlamaIndex | `Settings.llm` init kwargs | API key from env, not hardcoded in Settings |
| CrewAI | `LLM(api_key=os.environ[...])` | LiteLLM reads from env; supports rotation |
| DSPy | `dspy.LM(api_key=os.environ[...])` | Env-based key injection pattern |
| Haystack | `Secret` class | `haystack.utils.Secret` wraps env-based secrets |
| OpenAI | `OPENAI_API_KEY` env var | Official: env var only, never in code |
| Anthropic | `ANTHROPIC_API_KEY` env var | Official: env var; never hardcode in source |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|-----------|------|---------|----------|
| secret_id | string | required | Unique identifier — used in secret_refs from env_config |
| env_var | string | required | Env var name that holds the value at runtime |
| rotation_days | int | 90 | Lower = more secure; higher = less operational overhead |
| storage | enum | env | env/vault/railway — determines how value is injected |

## Patterns
| Pattern | When to Use | Example |
|---------|-------------|---------|
| Env-only secrets | All credentials via env vars, never in files | `ANTHROPIC_API_KEY` set in shell/Railway env |
| Railway injection | Secrets injected by Railway at deploy time | `storage: railway` — no local .env needed |
| Rotation schedule | Document expected rotation cadence | `rotation_days: 90` — calendar reminder + script |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Hardcoded secret values | API keys in YAML/code committed to git = permanent breach | Detected by secrets-scan; rotate immediately if found |
| Secret value in env_config | env_config is committed; secrets must never be there | Use `secret_refs` in env_config pointing to secret_config |
| No rotation schedule | Long-lived credentials expand breach window | Always set `rotation_days`; automate reminder |

## Integration Graph
```
env_config, permission --> [secret_config] --> rate_limit_config, agent_card
                                  |
                             law, runtime_rule, path_config
```

## Decision Tree
- IF value is a credential, token, API key, or private cert THEN secret_config
- IF stored in Railway environment THEN `storage: railway`
- IF stored locally THEN env var only — no .env file committed to git
- DEFAULT: env-based, `rotation_days: 90`, value never in any file

## Quality Criteria
- GOOD: env_var, storage, rotation_days all present; no actual values in file
- GREAT: rotation procedure documented, breach response plan linked, auto-scan configured
- FAIL: actual credential value in file, no rotation_days, storage undefined
