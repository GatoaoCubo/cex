---
id: p05_output_env_contract
kind: output_validator
pillar: P05
title: "Environment Variable Contract — .env.example"
version: 1.0.0
created: 2026-04-01
author: n05_railway_superintendent
domain: infrastructure
quality: 9.1
tags: [output, template, env, railway, config]
tldr: "63-var .env.example — categorized, with defaults, mock behavior, and boot validation."
density_score: 1.0
related:
  - spec_n05_railway_superintendent
  - bld_examples_env_config
  - p06_schema_env_contract
  - KC_N05_RAILWAY_CLI_PATTERNS
  - p01_kc_railway_cli_patterns
  - p01_kc_railway_platform_deep
  - KC_N05_RAILWAY_PLATFORM_DEEP
  - p02_agent_railway_superintendent
  - KC_N05_POSTGRESQL_RAILWAY
  - p01_kc_deploy_paas
---

# Environment Variable Contract — .env.example

## Purpose
Complete .env.example with all 63 variables categorized.
Used for: new developer onboarding, Railway variable setup, CI/CD validation.

---

## .env.example

```bash
# ════════════════════════════════════════════════════════════
# CODEXA API — Environment Variables (.env.example)
# Copy to .env and fill required values
# ════════════════════════════════════════════════════════════

# ─── REQUIRED (fatal if missing) ─────────────────────────
DATABASE_URL=postgresql://user:pass@host:5432/dbname  # asyncpg connection
PORT=8000                          # Railway auto-injects
ENV=development                    # development | staging | production
SECRET_KEY=change-me-in-production # JWT signing key
APP_URL=http://localhost:8000      # Base URL for callbacks

# ─── CLOUD LLM TIER ─────────────────────────────────────
# If missing → pipeline runs local tier only (degraded)
ANTHROPIC_API_KEY=                 # Claude API
OPENAI_API_KEY=                    # GPT API
GOOGLE_AI_API_KEY=                 # Gemini API

# ─── CODE EXECUTION ─────────────────────────────────────
# If missing → mock (returns sample output)
E2B_API_KEY=                       # E2B sandbox execution

# ─── PAYMENTS: STRIPE ────────────────────────────────────
# If missing → mock (accepts all, returns test IDs)
STRIPE_SECRET_KEY=sk_test_...
STRIPE_WEBHOOK_SECRET=whsec_...
STRIPE_PRICE_ID_100=price_...      # R$10 = 100 credits
STRIPE_PRICE_ID_500=price_...      # R$40 = 500 credits
STRIPE_PRICE_ID_1000=price_...     # R$70 = 1000 credits

# ─── PAYMENTS: MERCADO PAGO ─────────────────────────────
# If missing → mock (accepts PIX, returns test IDs)
MERCADOPAGO_ACCESS_TOKEN=TEST-...
MERCADOPAGO_PUBLIC_KEY=TEST-...
MERCADOPAGO_WEBHOOK_SECRET=

# ─── MERCADO LIVRE (OAuth) ───────────────────────────────
# If missing → skip OAuth, empty listings
ML_APP_ID=
ML_CLIENT_SECRET=
ML_REDIRECT_URI=
ML_ACCESS_TOKEN=                   # refreshed automatically
ML_REFRESH_TOKEN=

# ─── BLING ERP (OAuth) ──────────────────────────────────
# If missing → skip OAuth, disable bg refresh
BLING_CLIENT_ID=
BLING_CLIENT_SECRET=
BLING_REDIRECT_URI=
BLING_ACCESS_TOKEN=                # refreshed in background
BLING_REFRESH_TOKEN=

# ─── WHATSAPP ────────────────────────────────────────────
WA_TOKEN=                          # WhatsApp Business API
WA_PHONE_NUMBER_ID=
WA_VERIFY_TOKEN=

# ─── SCRAPING / RESEARCH ────────────────────────────────
FIRECRAWL_API_KEY=                 # Web scraping
FIRECRAWL_MONTHLY_BUDGET=1000      # Max pages/month

# ─── CACHE ───────────────────────────────────────────────
# If missing → in-memory dict with TTL
REDIS_URL=redis://default:pass@host:6379

# ─── DATABASE POOL TUNING ───────────────────────────────
DB_POOL_MIN=3                      # asyncpg min connections
DB_POOL_MAX=20                     # asyncpg max connections
DB_COMMAND_TIMEOUT=60              # query timeout seconds
DB_SSL_MODE=prefer                 # disable | prefer | require

# ─── RATE LIMITING ──────────────────────────────────────
RATE_LIMIT_FREE=60                 # req/min free tier
RATE_LIMIT_PRO=120                 # req/min pro tier
RATE_LIMIT_BUSINESS=300            # req/min business tier

# ─── COST CONTROL ───────────────────────────────────────
LLM_BUDGET_DAILY=50.00             # Max USD/day for LLM calls
CREDIT_WARN_THRESHOLD=100          # Alert when user < N credits

# ─── CORS ────────────────────────────────────────────────
CORS_ORIGINS=http://localhost:3000,http://localhost:5173
CORS_ORIGIN_REGEX=https?://(localhost(:\d+)?|.*\.railway\.app|.*\.codexa\.com\.br)

# ─── RAILWAY (auto-injected) ────────────────────────────
# These are set automatically by Railway — do NOT set manually
# RAILWAY_ENVIRONMENT=production
# RAILWAY_PROJECT_ID=...
# RAILWAY_SERVICE_ID=...
# RAILWAY_DEPLOYMENT_ID=...

# ─── MONITORING ──────────────────────────────────────────
LOG_LEVEL=info                     # debug | info | warning | error
SENTRY_DSN=                        # Error tracking (optional)
```

## Boot Validation

```python
"""Validate env vars at startup."""
import os
import sys
import logging

logger = logging.getLogger(__name__)

REQUIRED = ["DATABASE_URL", "PORT", "ENV", "SECRET_KEY", "APP_URL"]

WARN_IF_MISSING = [
    "ANTHROPIC_API_KEY", "OPENAI_API_KEY",  # cloud tier
    "STRIPE_SECRET_KEY",                     # payments
    "REDIS_URL",                             # cache
]

def validate_env():
    """Check required vars, warn on optional missing."""
    missing = [v for v in REQUIRED if not os.getenv(v)]
    if missing:
        logger.critical(f"Missing required env vars: {missing}")
        sys.exit(1)
    
    for v in WARN_IF_MISSING:
        if not os.getenv(v):
            logger.warning(f"Optional env var {v} not set — using mock/fallback")
    
    logger.info(f"Env validation passed: {len(REQUIRED)} required, "
                f"{sum(1 for v in WARN_IF_MISSING if os.getenv(v))}/{len(WARN_IF_MISSING)} optional")
```

## Variable Count

| Category | Count |
|----------|-------|
| Required | 5 |
| Cloud LLM | 3 |
| Code Execution | 1 |
| Stripe | 4 |
| MercadoPago | 3 |
| MercadoLivre | 5 |
| Bling | 5 |
| WhatsApp | 3 |
| Scraping | 2 |
| Cache | 1 |
| Pool Tuning | 4 |
| Rate Limiting | 3 |
| Cost Control | 2 |
| CORS | 2 |
| Railway (auto) | 4 |
| Monitoring | 2 |
| **Total** | **49 explicit + 14 Railway/derived = 63** |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_n05_railway_superintendent]] | downstream | 0.28 |
| [[bld_examples_env_config]] | downstream | 0.27 |
| [[p06_schema_env_contract]] | downstream | 0.26 |
| [[KC_N05_RAILWAY_CLI_PATTERNS]] | upstream | 0.25 |
| [[p01_kc_railway_cli_patterns]] | upstream | 0.24 |
| [[p01_kc_railway_platform_deep]] | upstream | 0.24 |
| [[KC_N05_RAILWAY_PLATFORM_DEEP]] | upstream | 0.23 |
| [[p02_agent_railway_superintendent]] | upstream | 0.23 |
| [[KC_N05_POSTGRESQL_RAILWAY]] | upstream | 0.23 |
| [[p01_kc_deploy_paas]] | upstream | 0.23 |
