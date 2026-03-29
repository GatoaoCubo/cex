---
id: p02_boot_codex_edison_eng
kind: boot_config
pillar: P02
version: "1.0.0"
created: "2023-10-18"
updated: "2023-10-18"
author: "EDISON"
provider: "codex"
identity:
  name: "Engineering Nucleus Agent"
  role: "Infrastructure setup and configuration management"
  satellite: "agnostic"
constraints:
  max_tokens: 8192
  context_window: 16384
  timeout_seconds: 180
  max_retries: 3
  temperature: 0.5
tools: [infra_setup, config_manager, code_deploy]
model: "codex-engine-v1"
temperature: 0.5
flags: [--strict-config, --no-external-network]
mcp_config:
  infra_control: stdio
permissions:
  read: [records/configs/]
  write: [deploy/setup/]
  execute: [shell, git]
system_prompt_ref: "p03_sp_infrastructure_agent"
domain: "engineering"
quality: null
tags: [boot-config, infrastructure, codex, P02]
tldr: "Codex boot config for engineering nucleus agent with infra_control MCP and context limits"
density_score: 0.85
---

## Provider Overview
Codex runtime for infrastructure setup and configuration management agents. Supports CLI tools, secure MCP interactions, and moderate context window requirements.

## Identity Block
Name: Engineering Nucleus Agent  
Role: Infrastructure setup and configuration management  
Satellite: agnostic

## Constraints
| Parameter       | Value  | Rationale                                               |
|-----------------|--------|---------------------------------------------------------|
| max_tokens      | 8192   | Sufficient for comprehensive infrastructure tasks       |
| context_window  | 16384  | Allows medium-sized context for processing configurations |
| timeout_seconds | 180    | Aligns with typical setup command durations             |
| max_retries     | 3      | Ensures idempotency in setup scripts                    |

## Tools Configuration
| Tool            | Type | Purpose                                    |
|-----------------|------|--------------------------------------------|
| infra_setup     | cli  | Initialize infrastructure settings         |
| config_manager  | cli  | Manage configuration files and settings    |
| code_deploy     | cli  | Deploy software across managed environments|

## Flags
| Flag                   | Purpose                                      |
|------------------------|----------------------------------------------|
| --strict-config        | Enforces strict validation of configuration files |
| --no-external-network  | Prevents access to unauthorized external networks|

## References
- Provider docs: https://docs.codex.com/procedures/engineering/deployment
- Related config: p02_boot_codex_infra_manager