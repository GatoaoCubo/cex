---
id: p01_kc_railway_platform_deep
kind: knowledge_card
pillar: P01
domain: infrastructure
quality: 9.1
density_score: 0.88
name: Railway Platform Deep
description: Railway PaaS deployment platform with 4-service topology, railway.toml configuration, and service orchestration
tags: [railway, paas, deployment, nixpacks, docker, microservices]
updated: "2026-04-07"
title: "Railway Platform Deep"
version: "1.0.0"
author: n04_knowledge
created: "2026-04-07"
related:
  - KC_N05_RAILWAY_CLI_PATTERNS
  - p08_ac_railway_superintendent
  - p01_kc_deploy_paas
  - KC_N05_RAILWAY_PLATFORM_DEEP
  - p01_kc_railway_cli_patterns
  - p02_agent_railway_superintendent
  - p03_sp_railway_superintendent
  - p05_output_railway_toml
  - p12_dr_railway_superintendent
  - KC_N05_POSTGRESQL_RAILWAY
---

# Railway Platform Deep

## Quick Reference

**Railway CLI**: Deploy applications with zero-config using Nixpacks builder
- `railway login` → authenticate with GitHub/Google
- `railway init` → link project to service
- `railway up` → deploy current directory
- `railway link` → connect local to existing service
- `railway logs` → stream deployment logs
- `railway shell` → access service shell
- `railway variables set KEY=value` → manage environment variables

**4-Service Topology**: api (backend) → frontend (web) → dashboard (admin) → gateway (proxy/load balancer)

## Key Concepts

**Railway.toml Configuration**
```toml
[build]
builder = "nixpacks"  # or "dockerfile"
buildCommand = "npm run build"

[deploy]
startCommand = "npm start"
healthcheckPath = "/health"
healthcheckTimeout = 300
restartPolicyType = "on_failure"
restartPolicyMaxRetries = 10
```

**Service Variables vs Shared Variables**
- Service variables: scoped to single service, accessed via `$VARIABLE_NAME`
- Shared variables: accessible across all services in project
- Railway provides: `$PORT`, `$RAILWAY_ENVIRONMENT_NAME`, `$RAILWAY_PROJECT_NAME`
- Database services auto-generate: `DATABASE_URL`, `REDIS_URL`

**Nixpacks Builder Intelligence**
- Auto-detects: Node.js (package.json), Python (requirements.txt), Go (go.mod), Rust (Cargo.toml)
- Installs dependencies: `npm install`, `pip install -r requirements.txt`, `go mod download`
- Build optimization: caches layers, parallel builds, multi-stage optimization
- Custom nixpacks.toml overrides: providers, buildCommand, staticDir

**Custom Domains & SSL**
- Connect domain: `railway domain add example.com`
- CNAME record: `servicename.railway.app`
- Free SSL certificates via Let's Encrypt
- Multiple domains per service supported
- Wildcard domains: `*.example.com`

**Deploy Logs & Monitoring**
- Build logs: Nixpacks detection, dependency installation, build commands
- Runtime logs: application stdout/stderr, crash reports, health checks
- Metrics dashboard: CPU, memory, network, request count
- Alerts: deployment failures, service crashes, resource limits

## Patterns

**Multi-Service Architecture Pattern**
```
Gateway Service (port 80/443)
├── API Service (internal port 8000)
├── Frontend Service (internal port 3000)
└── Dashboard Service (internal port 3001)
```
- Gateway routes traffic via internal Railway networking
- Services communicate via private networking: `api.railway.internal`
- Environment-specific URLs: `api-production.up.railway.app`

**Environment Promotion Pattern**
```
Development → Staging → Production
├── Separate Railway environments
├── Variable inheritance: shared → environment → service
└── Database forking for testing
```
- `railway environment create staging`
- Copy variables: `railway variables copy --from development`
- Promote deployment: `railway redeploy --environment production`

**Database Integration Pattern**
```yaml
# Add PostgreSQL service
railway add postgresql

# Auto-generated variables:
DATABASE_URL=postgresql://user:pass@host:port/db
PGHOST, PGPORT, PGUSER, PGPASSWORD, PGDATABASE
```
- Connection pooling via railway-provided URLs
- Automatic backups and point-in-time recovery
- Database migration on deployment hook

## Golden Rules

**Never Hardcode Service URLs**
- Use Railway-provided internal networking: `api.railway.internal:8000`
- Environment variables for external integrations: `$API_BASE_URL`
- Service discovery via DNS: avoid IP addresses
- Port binding: always use `process.env.PORT || 3000`

**Configuration Over Convention for Complex Apps**
- Simple apps: rely on Nixpacks auto-detection
- Complex builds: explicit railway.toml with buildCommand, startCommand
- Multi-stage deployments: dockerfile with COPY --from patterns
- Static sites: set staticDir in nixpacks.toml

**Health Checks Prevent Cascading Failures**
- Implement `/health` endpoint returning 200 OK
- Include dependency checks: database connectivity, external APIs
- Set appropriate healthcheckTimeout (default 300s)
- Use graceful shutdown handlers for SIGTERM
- Monitor via railway logs during deployment

## References

- [Railway Documentation](https://docs.railway.app/)
- [Nixpacks Documentation](https://nixpacks.com/docs)
- [Railway CLI Reference](https://docs.railway.app/reference/cli-api)
- [Service Networking Guide](https://docs.railway.app/reference/networking)
- [Environment Variables](https://docs.railway.app/develop/variables)
- [Custom Domains Setup](https://docs.railway.app/deploy/custom-domains)

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_railway_platform_deep`
- **Tags**: [railway, paas, deployment, nixpacks, docker, microservices]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[KC_N05_RAILWAY_CLI_PATTERNS]] | sibling | 0.68 |
| [[p08_ac_railway_superintendent]] | downstream | 0.63 |
| [[p01_kc_deploy_paas]] | sibling | 0.62 |
| [[KC_N05_RAILWAY_PLATFORM_DEEP]] | sibling | 0.62 |
| [[p01_kc_railway_cli_patterns]] | sibling | 0.61 |
| [[p02_agent_railway_superintendent]] | downstream | 0.60 |
| [[p03_sp_railway_superintendent]] | downstream | 0.57 |
| [[p05_output_railway_toml]] | downstream | 0.56 |
| [[p12_dr_railway_superintendent]] | downstream | 0.52 |
| [[KC_N05_POSTGRESQL_RAILWAY]] | sibling | 0.49 |
