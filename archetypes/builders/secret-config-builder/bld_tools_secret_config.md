---
kind: tools
id: bld_tools_secret_config
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for secret_config production
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
