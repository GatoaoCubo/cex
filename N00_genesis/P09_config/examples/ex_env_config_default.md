---
id: ex_env_config_default
kind: env_config
pillar: P09
title: Default Environment Config
environment: default
tags: [config, env, default, variables]
references:
  - tpl_env_config
tldr: "Complete CEX environment configuration: model selection, API keys, quality thresholds, feature flags, and runtime settings."
quality: 9.1
---

# Default Environment Config

## Core Model Settings

| Variable | Default | Type | Description |
|----------|---------|------|-------------|
| `CEX_MODEL` | `claude-sonnet` | string | Primary LLM for artifact production |
| `CEX_MICRO` | `claude-haiku` | string | LLM for intent parsing, decomposition |
| `CEX_REASONING` | `claude-opus` | string | LLM for F4 REASON (complex planning) |
| `CEX_TEMPERATURE` | `0.7` | float | Default temperature (0.0-1.0) |
| `CEX_MAX_TOKENS` | `4096` | int | Max output tokens per LLM call |

## Quality & Validation

| Variable | Default | Type | Description |
|----------|---------|------|-------------|
| `CEX_QUALITY` | `8.0` | float | Minimum quality bar for artifact promotion |
| `CEX_MAX_RETRIES` | `2` | int | F7 GOVERN retry limit before saving as draft |
| `CEX_DENSITY_TARGET` | `0.85` | float | Minimum body density score |
| `CEX_MAX_BODY_BYTES` | `5120` | int | Default max body size (overridden by schema) |

## API Keys (secrets — use vault in production)

| Variable | Default | Type | Description |
|----------|---------|------|-------------|
| `ANTHROPIC_API_KEY` | — | secret | Claude API authentication |
| `GOOGLE_AI_KEY` | — | secret | Gemini API for N01/N04 nuclei |
| `OPENAI_API_KEY` | — | secret | OpenAI API for N05 (Codex) |

## Runtime Settings

| Variable | Default | Type | Description |
|----------|---------|------|-------------|
| `CEX_ROOT` | auto-detected | path | Repository root (resolved from `_tools/` parent) |
| `CEX_LOG_LEVEL` | `INFO` | enum | Logging: DEBUG, INFO, WARN, ERROR |
| `CEX_COMPILE_ON_SAVE` | `true` | bool | Auto-compile .md → .yaml after save |
| `CEX_AUTO_COMMIT` | `true` | bool | Auto git-commit after F8 COLLABORATE |
| `CEX_SIGNAL_ON_COMPLETE` | `true` | bool | Write signal to `.cex/runtime/signals/` |

## Feature Flags

| Variable | Default | Type | Description |
|----------|---------|------|-------------|
| `CEX_ENABLE_F4` | `true` | bool | Enable F4 REASON (LLM planning) |
| `CEX_ENABLE_F5` | `true` | bool | Enable F5 CALL (tool scan) |
| `CEX_ENABLE_LEARNING_RECORDS` | `true` | bool | Write build outcomes to `.cex/learning_records/` |
| `CEX_ENABLE_MEMORY_APPEND` | `true` | bool | Append to builder `bld_memory` after builds |

## Override Hierarchy

```
Defaults (this file)
  ↓ overridden by
.env file (CEX_ROOT/.env)
  ↓ overridden by
Environment variables (export CEX_MODEL=opus)
  ↓ overridden by
CLI flags (--kind, --execute, --verbose)
```

## Environment Profiles

| Profile | CEX_MODEL | CEX_MICRO | CEX_QUALITY | Use Case |
|---------|-----------|-----------|-------------|----------|
| `default` | sonnet | haiku | 8.0 | Standard development |
| `quality` | opus | sonnet | 9.0 | Production artifacts |
| `speed` | haiku | haiku | 7.0 | Rapid prototyping |
| `offline` | ollama/llama3 | ollama/llama3 | 7.0 | No API access |

## Validation Rules

- `CEX_MODEL` must be one of: `claude-opus`, `claude-sonnet`, `claude-haiku`, `ollama/*`
- `CEX_QUALITY` must be in range [0.0, 10.0]
- `CEX_TEMPERATURE` must be in range [0.0, 1.0]
- `CEX_MAX_TOKENS` must be positive integer, max 8192
- Secret variables (`*_API_KEY`) must not appear in git-tracked files
