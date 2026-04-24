---
id: p01_kc_security_practices
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Security Practices — Scanning, Secrets, SAST, Container"
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: software-engineering
quality: 9.0
tags: [security, scanning, secrets, sast, container-security]
tldr: "5-layer security from codexa-core: dependency scanning (pip-audit+safety), secret detection (gitleaks), SAST (bandit+semgrep), container scanning (trivy), CodeQL analysis. Weekly cron + per-PR."
density_score: 0.90
related:
  - p01_kc_github_actions
  - p12_wf_auto_security
  - bld_sp_tools_software_project
  - p11_qg_security
  - p01_fse_meta_builder_recipe
  - p06_security_validation_schema
  - bld_sp_quality_gate_software_project
  - p04_output_github_actions
  - kc_env_config
  - p11_gr_cyber_risk
---

# Security Practices

## 5-Layer Security Pipeline

```
Layer 1: Dependency Scan    → pip-audit, safety (known CVEs in deps)
Layer 2: Secret Detection   → gitleaks (API keys, passwords in code)
Layer 3: SAST              → bandit, semgrep (code vulnerabilities)
Layer 4: Container Scan    → trivy (OS + library vulns in Docker image)
Layer 5: CodeQL            → GitHub semantic analysis (deep patterns)
```

## Layer 1: Dependency Scanning

```yaml
# In CI
- run: pip install pip-audit safety
- run: pip-audit --format=markdown --desc on
- run: safety check --output=text
```

```bash
# Local
pip-audit                     # Check installed packages
pip-audit -r requirements.txt # Check requirements file
safety check                  # PyUp safety DB
```

## Layer 2: Secret Detection

```yaml
# In CI (gitleaks scans full git history)
- uses: gitleaks/gitleaks-action@v2
  env:
    GITHUB_TOKEN: ${{ secrets.GITHUB_TOKEN }}
```

### What Gitleaks Detects

- API keys (AWS, GCP, Azure, Stripe, etc.)
- OAuth tokens
- Private keys (RSA, SSH, PGP)
- Database connection strings
- JWT secrets
- Generic high-entropy strings

### .gitleaks.toml (Custom Rules)

```toml
[allowlist]
paths = ["tests/fixtures/", "docs/examples/"]
```

## Layer 3: SAST (Static Application Security Testing)

### Bandit (Python-specific)

```bash
bandit -r src/ --severity-level medium -x "*/tests/*"
```

```toml
# pyproject.toml
[tool.bandit]
exclude_dirs = ["tests"]
skips = ["B101", "B311"]  # assert, random (OK in non-crypto)
```

### Semgrep (Multi-language)

```yaml
- uses: returntocorp/semgrep-action@v1
  with:
    config: >-
      p/python
      p/security-audit
      p/secrets
```

## Layer 4: Container Scanning

```yaml
# Build image, then scan
- run: docker build -t myapp:scan .
- uses: aquasecurity/trivy-action@master
  with:
    image-ref: 'myapp:scan'
    format: 'sarif'
    severity: 'CRITICAL,HIGH'
    ignore-unfixed: true
```

## Layer 5: CodeQL

```yaml
- uses: github/codeql-action/init@v3
  with:
    languages: python
    queries: +security-extended
- uses: github/codeql-action/autobuild@v3
- uses: github/codeql-action/analyze@v3
```

## Application Security Patterns

### API Key Handling

```python
# NEVER log raw keys
def _hash_key(key: str) -> str:
    return hashlib.sha256(key.encode()).hexdigest()[:12]

# Generate secure keys
def generate_api_key() -> str:
    return f"cxa_{secrets.token_urlsafe(32)}"

# Load from env, not code
_valid_keys = set(os.getenv("API_KEYS", "").split(","))
```

### Token Encryption

```python
# Encrypt sensitive tokens at rest (OAuth refresh tokens)
from cryptography.fernet import Fernet

key = Fernet.generate_key()
cipher = Fernet(key)
encrypted = cipher.encrypt(token.encode())
decrypted = cipher.decrypt(encrypted).decode()
```

### Rate Limiting (Tiered)

```python
TIER_LIMITS = {
    "free": 60,       # 60 req/min
    "pro": 120,       # 120 req/min
    "business": 300,  # 300 req/min
}
```

### Row-Level Security (RLS)

```sql
ALTER TABLE data ENABLE ROW LEVEL SECURITY;
CREATE POLICY tenant_isolation ON data
    FOR ALL USING (tenant_id = current_setting('app.current_tenant'));
```

## Security Checklist

```
[ ] Dependencies scanned (pip-audit, no critical CVEs)
[ ] No secrets in code (gitleaks clean)
[ ] No SQL injection (parameterized queries only)
[ ] No XSS (output encoding, CSP headers)
[ ] Auth on all non-public endpoints
[ ] Rate limiting enabled
[ ] CORS restricted to known origins
[ ] Sensitive data encrypted at rest
[ ] Non-root Docker user
[ ] HTTPS only in production
```

## Anti-Patterns

- ❌ Secrets in code or config files (use env vars)
- ❌ No dependency scanning (known CVEs in production)
- ❌ Running containers as root
- ❌ Logging raw API keys or tokens
- ❌ `SELECT *` with user-provided WHERE (SQL injection)
- ❌ Security checks only on schedule (also run on PRs)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_github_actions]] | sibling | 0.32 |
| [[p12_wf_auto_security]] | downstream | 0.31 |
| [[bld_sp_tools_software_project]] | downstream | 0.28 |
| [[p11_qg_security]] | downstream | 0.28 |
| [[p01_fse_meta_builder_recipe]] | related | 0.26 |
| [[p06_security_validation_schema]] | downstream | 0.26 |
| [[bld_sp_quality_gate_software_project]] | downstream | 0.25 |
| [[p04_output_github_actions]] | downstream | 0.21 |
| [[kc_env_config]] | sibling | 0.21 |
| [[p11_gr_cyber_risk]] | downstream | 0.21 |
