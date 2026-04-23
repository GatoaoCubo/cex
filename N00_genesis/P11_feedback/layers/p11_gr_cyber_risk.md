---
id: p11_gr_cyber_risk
kind: guardrail
pillar: P11
title: "Guardrail: Cybersecurity Risk Assessment"
version: 1.0.0
quality: 9.1
severity: high
enforcement: block
tags: [guardrail, security, cyber, risk, owasp]
tldr: "Safety guardrail for detecting and preventing cybersecurity risks in generated code and configurations. Covers OWASP Top 10, injection, and secret exposure."
domain: "feedback"
author: n03_builder
created: "2026-04-12"
updated: "2026-04-12"
density_score: 0.93
related:
  - p11_qg_security
  - p11_gr_{{SCOPE_SLUG}}
  - p12_wf_auto_security
  - p03_brand_config_extractor
  - p03_brand_book_generator
  - bld_quality_gate_supabase_data_layer
  - bld_sp_quality_gate_software_project
  - kc_env_config
  - n06_output_brand_book
  - p01_kc_secret_config
---

# Cybersecurity Risk Guardrail

## Scope
Applies to all generated code (.py, .ps1, .sh, .js, .ts) and
configuration files (.yaml, .json, .env, .toml) produced by any nucleus.

## OWASP Top 10 Checks

| Risk | Check | Action on Detect |
|------|-------|-----------------|
| A01 Broken Access Control | Hardcoded roles, missing auth checks | BLOCK |
| A02 Cryptographic Failures | Weak hashing, plaintext secrets | BLOCK |
| A03 Injection | SQL concat, shell interpolation, eval() | BLOCK |
| A04 Insecure Design | Missing input validation at boundaries | WARN |
| A05 Security Misconfiguration | Debug mode in prod, default creds | BLOCK |
| A06 Vulnerable Components | Known CVE in dependencies | WARN |
| A07 Auth Failures | Weak password rules, missing MFA hooks | WARN |
| A08 Data Integrity | Unsigned updates, untrusted deserialization | BLOCK |
| A09 Logging Failures | Secrets in logs, missing audit trail | WARN |
| A10 SSRF | Unvalidated URL construction | BLOCK |

## Secret Exposure Rules

NEVER include in generated code or committed files:
- API keys, tokens, passwords (use env vars or secret_config)
- Private keys or certificates
- Database connection strings with credentials
- OAuth client secrets

## Code Generation Rules

1. Parameterize all SQL queries (no string concatenation)
2. Sanitize all user input before rendering (HTML escape, etc.)
3. Use subprocess with list args, never shell=True with user input
4. Validate file paths to prevent directory traversal
5. Set appropriate CORS, CSP, and security headers
6. Use HTTPS for all external API calls

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_security]] | related | 0.28 |
| [[p11_gr_{{SCOPE_SLUG}}]] | sibling | 0.26 |
| [[p12_wf_auto_security]] | downstream | 0.24 |
| [[p03_brand_config_extractor]] | upstream | 0.24 |
| [[p03_brand_book_generator]] | upstream | 0.23 |
| [[bld_quality_gate_supabase_data_layer]] | upstream | 0.23 |
| [[bld_sp_quality_gate_software_project]] | upstream | 0.21 |
| [[kc_env_config]] | upstream | 0.20 |
| [[n06_output_brand_book]] | upstream | 0.20 |
| [[p01_kc_secret_config]] | upstream | 0.18 |
