---
id: kc_sandbox_config
kind: knowledge_card
8f: F3_inject
title: Sandbox Configuration
version: 1.0.0
quality: 8.6
pillar: P01
density_score: 1.0
related:
  - kc_playground_config
  - sandbox-config-builder
  - p03_sp_sandbox_config_builder
  - p03_sp_code_executor_builder
  - bld_collaboration_sandbox_config
  - p01_kc_code_executor
  - playground-config-builder
  - bld_knowledge_card_code_executor
  - bld_collaboration_code_executor
  - code-executor-builder
---

# Sandbox Configuration

Configures isolated code execution environments for secure testing. Key parameters:

## Environment Isolation
- `runtime`: Specify execution environment (e.g., `python3`, `node`)
- `sandboxed`: Boolean to enable/disable isolation
- `networking`: Control network access (none/readonly/readwrite)

## Resource Limits
- `cpu`: CPU allocation percentage (0-100)
- `memory`: Memory limit in MB
- `timeout`: Maximum execution time in seconds

## Security Settings
- `allowed_modules`: Whitelist of permitted modules/packages
- `safe_mode`: Enable strict security restrictions
- `audit_log`: Enable execution activity logging

## Logging
- `log_level`: Set logging verbosity (debug/info/warning/error)
- `output_format`: Specify output format (text/json)
- `max_log_size`: Maximum log file size in MB

Configuration ensures safe execution while maintaining performance and security boundaries.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_playground_config]] | sibling | 0.33 |
| [[sandbox-config-builder]] | downstream | 0.33 |
| [[p03_sp_sandbox_config_builder]] | downstream | 0.31 |
| [[p03_sp_code_executor_builder]] | downstream | 0.30 |
| [[bld_collaboration_sandbox_config]] | downstream | 0.29 |
| [[p01_kc_code_executor]] | sibling | 0.24 |
| [[playground-config-builder]] | downstream | 0.23 |
| [[bld_knowledge_card_code_executor]] | sibling | 0.23 |
| [[bld_collaboration_code_executor]] | downstream | 0.22 |
| [[code-executor-builder]] | downstream | 0.21 |
