---
kind: knowledge_card
id: bld_knowledge_card_secret_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for secret_config production — credential and secret management specification
sources: HashiCorp Vault docs, Kubernetes Secrets, AWS Secrets Manager, SOPS, OWASP Secrets Management
---

# Domain Knowledge: secret_config
## Executive Summary
Secret configs are credential management specifications that define how sensitive values (API keys, tokens, passwords, certificates) are stored, encrypted, rotated, and retrieved. They are provider-specific specs — not generic env configs. A secret_config always declares a backend provider, a rotation policy, an encryption posture, and an access pattern. Secrets NEVER appear in plaintext in the spec.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (Config) |
| llm_function | GOVERN |
| Layer | runtime |
| Providers | vault, k8s, aws, portkey, 1password, sops |
| Access patterns | dynamic, static, injected, env |
| Rotation methods | automatic, manual, triggered |
| Encryption at-rest | AES-256-GCM, KMS, SOPS-age, envelope |
| Encryption in-transit | TLS 1.3, mTLS |
## Provider Patterns
| Provider | Auth Method | Retrieval | Rotation Support |
|----------|------------|-----------|-----------------|
| HashiCorp Vault | AppRole, K8s SA, JWT | Dynamic lease, KV v2 | Native auto-rotation |
| Kubernetes Secrets | SA token, RBAC | Volume mount, env inject | External via ESO |
| AWS Secrets Manager | IAM role, IRSA | SDK/API, Lambda layer | Native scheduled rotation |
| Portkey vault | API key, workspace token | SDK, gateway header | Manual + webhook |
| 1Password Connect | Service account token | SDK, CLI, operator | Manual + vault policy |
| SOPS | age key, KMS key | CLI decrypt, pre-commit | Key rotation via re-encrypt |
## Rotation Policy Patterns
- **Automatic**: provider rotates on schedule; agents get new value on next lease/fetch (Vault, AWS SM)
- **Manual**: operator rotates; agents notified via signal or restart (1Password, static K8s secrets)
- **Triggered**: rotation fires on breach detection, certificate expiry, or pipeline event
- **On-breach**: emergency rotation protocol — invalidate all leases, rotate immediately, audit trail required
| Pattern | Frequency | Risk Profile | Use Case |
|---------|-----------|-------------|----------|
| Automatic daily | 24h | Low | API keys, service tokens |
| Weekly | 7d | Medium | DB passwords |
| Monthly | 30d | Medium-high | Certificate renewal |
| On-breach | Immediate | Critical | Compromise response |
## Access Patterns
- **dynamic**: agent requests a short-lived lease from provider at runtime (Vault dynamic secrets, AWS STS)
- **static**: secret fetched once at deploy time and cached; rotated by re-deploy
- **injected**: sidecar or init container injects secret as file or env at pod start (K8s CSI driver, Vault Agent)
- **env**: secret injected as environment variable via platform (Railway, Heroku, Render env vars)
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Plaintext secrets in config | Credential leak; violates every security standard |
| No rotation policy | Stale credentials; breach window grows unbounded |
| Missing encryption at-rest | Data-at-rest exposure if storage is compromised |
| access_pattern unspecified | Agents cannot know how to retrieve at runtime |
| Reusing secrets across environments | Single breach compromises all environments |
| No audit_log | Impossible to detect unauthorized access |
| Hardcoded secret paths | Path changes break all consumers silently |
## Application
1. Choose provider based on runtime platform and team capability
2. Define rotation_policy: frequency + method matching risk profile
3. Declare encryption: at_rest algorithm + in_transit protocol
4. Set access_pattern matching provider capabilities and agent runtime
5. List secret_paths as placeholders (never real values)
6. Enable audit_log always
7. Define fallback provider for high-availability secrets
## References
- HashiCorp Vault: secrets engine, dynamic secrets, AppRole auth
- Kubernetes External Secrets Operator (ESO)
- AWS Secrets Manager rotation Lambda patterns
- SOPS: Secrets OPerationS — file-based encrypted secrets with age/KMS
- OWASP Secrets Management Cheat Sheet
