---
kind: knowledge_card
id: bld_knowledge_card_secret_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for secret_config production — credential and secret management specification
sources: HashiCorp Vault docs, Kubernetes Secrets, AWS Secrets Manager, SOPS, OWASP Secrets Management
quality: 9.1
title: "Knowledge Card Secret Config"
version: "1.0.0"
author: n03_builder
tags: [secret_config, builder, examples]
tldr: "Golden and anti-examples for secret config construction, demonstrating ideal structure and common pitfalls."
domain: "secret config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Domain Knowledge: secret_config
## Executive Summary
Secret configs are credential management specifications that define how sensitive values (API keys, tokens, passwords, certificates) are stored, encrypted, rotated, and retrieved. They are provider-specific specs — not generic env configs. A secret_config always declares a backend provider, a rotation policy, an encryption posture, and an access pattern. Secrets NEVER appear in plaintext in the spec.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (Config) |
| llm_function | GOVERN |
| Providers | vault, k8s, aws, portkey, 1password, sops |
| Access patterns | dynamic, static, injected, env |
| Rotation methods | automatic, manual, triggered |
| Encryption at-rest | AES-256-GCM, KMS, SOPS-age |
| Encryption in-transit | TLS 1.3, mTLS |
## Provider Patterns
| Provider | Auth Method | Retrieval | Rotation |
|----------|------------|-----------|----------|
| HashiCorp Vault | AppRole, K8s SA, JWT | Dynamic lease, KV v2 | Native auto-rotation |
| Kubernetes Secrets | SA token, RBAC | Volume mount, env inject | External via ESO |
| AWS Secrets Manager | IAM role, IRSA | SDK/API, Lambda layer | Native scheduled rotation |
| Portkey vault | API key, workspace token | SDK, gateway header | Manual + webhook |
| 1Password Connect | Service account token | SDK, CLI, operator | Manual + vault policy |
| SOPS | age key, KMS key | CLI decrypt, pre-commit | Key rotation via re-encrypt |
## Rotation Policy Patterns
| Pattern | Frequency | Use Case |
|---------|-----------|----------|
| Automatic daily | 24h | API keys, service tokens |
| Weekly | 7d | DB passwords |
| Monthly | 30d | Certificate renewal |
| On-breach | Immediate | Compromise response |
## Access Patterns
- **dynamic**: agent requests short-lived lease at runtime (Vault dynamic secrets, AWS STS)
- **static**: secret fetched once at deploy time; rotated by re-deploy
- **injected**: sidecar/init container injects secret as file or env at pod start
- **env**: secret injected as environment variable via platform (Railway, Heroku)
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Plaintext secrets in config | Credential leak; violates every security standard |
| No rotation policy | Stale credentials; breach window grows unbounded |
| access_pattern unspecified | Agents cannot know how to retrieve at runtime |
| Reusing secrets across environments | Single breach compromises all environments |
| No audit_log | Impossible to detect unauthorized access |
## Application
1. Choose provider based on runtime platform and team capability
2. Define rotation_policy: frequency + method matching risk profile
3. Declare encryption: at_rest algorithm + in_transit protocol
4. Set access_pattern matching provider capabilities and agent runtime
5. List secret_paths as placeholders (never real values)
6. Enable audit_log always
7. Define fallback provider for high-availability secrets
## References
- HashiCorp Vault dynamic secrets | Kubernetes External Secrets Operator (ESO) | AWS Secrets Manager rotation | SOPS age/KMS | OWASP Secrets Management Cheat Sheet
