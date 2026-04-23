---
kind: tools
id: bld_tools_secret_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for secret_config production
quality: 9.0
title: "Tools Secret Config"
version: "1.0.0"
author: n03_builder
tags: [secret_config, builder, examples]
tldr: "Golden and anti-examples for secret config construction, demonstrating ideal structure and common pitfalls."
domain: "secret config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_function_def
  - bld_tools_search_tool
  - bld_tools_path_config
  - bld_tools_retriever_config
  - bld_tools_runtime_rule
  - bld_tools_memory_scope
  - bld_tools_cli_tool
  - bld_tools_feature_flag
  - bld_tools_response_format
  - bld_tools_input_schema
---

# Tools: secret-config-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing secret_config artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
| secrets_scan.py | Scan output for plaintext secrets before write | Phase 3 (safety gate) | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P09_config/_schema.yaml | Field definitions, secret_config kind |
| CEX Examples | P09_config/examples/ | Real secret_config artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P09_secret_config |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
## Provider Reference
| Provider | Docs Reference | Key Concepts |
|----------|---------------|-------------|
| HashiCorp Vault | developer.hashicorp.com/vault | AppRole, dynamic secrets, KV v2, lease TTL |
| Kubernetes Secrets | kubernetes.io/docs/concepts/configuration/secret | RBAC, CSI driver, ESO, sealed secrets |
| AWS Secrets Manager | docs.aws.amazon.com/secretsmanager | IAM IRSA, rotation Lambda, ARN paths |
| Portkey | portkey.ai/docs | Virtual keys, vault, gateway config |
| 1Password Connect | developer.1password.com/docs/connect | Service account, item references, operator |
| SOPS | github.com/getsops/sops | age encryption, KMS integration, .sops.yaml |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern matches p09_sec_, provider
is valid enum, rotation_policy has frequency+method, encryption has at_rest+in_transit,
access_pattern is valid enum, body <= 1024 bytes, quality == null, NO plaintext secrets.
## Safety Tools
Run a manual grep for patterns that indicate real secrets before committing:
- Tokens: 40+ character alphanumeric strings
- Keys: BEGIN PRIVATE KEY, BEGIN RSA PRIVATE KEY
- Passwords: password: followed by a non-placeholder value
Replace any found values with `<PLACEHOLDER>` or `${ENV_VAR_NAME}` notation.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_function_def]] | sibling | 0.54 |
| [[bld_tools_search_tool]] | sibling | 0.51 |
| [[bld_tools_path_config]] | sibling | 0.50 |
| [[bld_tools_retriever_config]] | sibling | 0.50 |
| [[bld_tools_runtime_rule]] | sibling | 0.49 |
| [[bld_tools_memory_scope]] | sibling | 0.48 |
| [[bld_tools_cli_tool]] | sibling | 0.48 |
| [[bld_tools_feature_flag]] | sibling | 0.48 |
| [[bld_tools_response_format]] | sibling | 0.48 |
| [[bld_tools_input_schema]] | sibling | 0.47 |
