---
id: ex_env_config_default
kind: env_config
pillar: P09
title: Default Environment Config
tags: [config, env, default]
references:
  - tpl_env_config
---

# Default Environment Config

> Skeleton: env_config kind

| Variable | Default | Description |
|----------|---------|------------|
| CEX_MODEL | claude-sonnet | LLM for main tasks |
| CEX_MICRO | claude-haiku | LLM for decompose |
| CEX_QUALITY | 8.0 | Minimum quality bar |

## Links

- Template: [[tpl_env_config]]
