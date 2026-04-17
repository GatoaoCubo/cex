---
```yaml
updated: "2026-04-07"
domain: "knowledge management"
title: "Railway Networking"
version: "1.0.0"
author: n04_knowledge
created: "2026-04-07"
density_score: 0.97
tldr: "Defines the artifact specification for railway networking, with structural rules, validation gates, and integration points."
quality: 9.0
tags: [artifact, builder, examples]
---
id: p01_kc_railway_networking
kind: knowledge_card
pillar: P01
title: "Railway Networking — CORS Origins, Internal URLs, TCP Proxy, Rate Limiting, Custom Domains"
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: knowledge-card-builder
domain: infrastructure
subdomain: railway-networking
quality: 9.0
tags: [railway, networking, cors, domains, proxy, rate-limit, tcp]
tldr: "Railway platform networking features: CORS regex origins *.domain.com, private URLs service.railway.internal, TCP proxy for databases, Redis rate limiting patterns, PORT auto-binding"
when_to_use: "Configuring Railway networking, CORS policies, service discovery, rate limiting, custom domains, or TCP-based services"
keywords: [railway, cors, origins, internal, private, tcp, proxy, rate-limit, domains, networking]
long_tails:
  - "How to configure CORS regex patterns for Railway app origins including wildcards and subdomain matching"
  - "Railway internal private URL patterns for service-to-service communication and database connections"  
  - "TCP proxy configuration for Redis, PostgreSQL, and custom TCP services on Railway platform"
axioms:
  - "NEVER hardcode Railway URLs — use service.railway.internal for private communication between services"
  - "ALWAYS use regex CORS origins .*\\.domain\\.com instead of wildcards for security"
  - "IF TCP service THEN expose via Railway TCP proxy with health checks on designated port"
linked_artifacts:
  primary: null  
  related: [p01_kc_railway_platform_deep, p01_kc_uvicorn_production]
feeds_kinds:
  - env_config        # PORT, CORS_ORIGINS environment variables
  - rate_limit_config # Railway Redis-based rate limiting configs
  - path_config       # Custom domain routing and URL patterns
density_score: 0.91
data_source: "Railway official docs, platform testing, production deployment patterns"
---
```

# Railway Networking Features

## Quick Reference

**CORS Origins Configuration**
```bash
# Environment variables for CORS
CORS_ORIGINS="https://app.domain.com,https://*.domain.com"
CORS_ORIGIN_REGEX="https://.*\\.domain\\.com"
ALLOW_CREDENTIALS=true
CORS_METHODS="GET,POST,PUT,DELETE,OPTIONS"
```

**Internal Private URLs**
1. Service discovery: `servicename.railway.internal`  
2. Database: `postgres.railway.internal:5432`
3. Redis: `redis.railway.internal:6379`
4. Port auto-binding: `$PORT` (Railway-provided)

## Key Concepts

| Feature | Pattern | Port | Use Case |
|---------|---------|------|----------|
| HTTP Service | `app.railway.internal` | `$PORT` | Web app internal communication |
| PostgreSQL | `postgres.railway.internal` | `5432` | Database connections |
| Redis | `redis.railway.internal` | `6379` | Caching, sessions, queues |
| TCP Proxy | `tcp.railway.app:12345` | Custom | WebSocket, game servers, RPC |
| Custom Domain | `api.domain.com` | `443/80` | Public API endpoints |

**CORS Regex Origins Patterns**
```javascript
// Secure patterns - match specific subdomains
const corsPatterns = [
  /^https:\/\/.*\.domain\.com$/,           // *.domain.com
  /^https:\/\/app-.*\.domain\.com$/,       // app-*.domain.com  
  /^https:\/\/(www|app|api)\.domain\.com$/ // specific subdomains
];

// Railway environment variable
CORS_ORIGIN_REGEX="^https:\\/\\/.*\\.domain\\.com$"
```

**PORT Auto-Configuration**
```javascript
// Railway provides $PORT automatically
const port = process.env.PORT || 3000;
app.listen(port, '0.0.0.0', () => {
  console.log(`Server running on port ${port}`);
});
```

**Internal Service Discovery**
```bash
# Service-to-service communication
API_BASE_URL="https://api.railway.internal"
DATABASE_URL="postgresql://user:pass@postgres.railway.internal:5432/db"
REDIS_URL="redis://redis.railway.internal:6379"

# External custom domain
PUBLIC_URL="https://api.domain.com"
```

## Patterns

**Multi-Service Private Network**
```
Frontend (public) → API (internal) → Database (internal)
├── frontend.up.railway.app (public)
├── api.railway.internal (private)
└── postgres.railway.internal (private)
```

**CORS Configuration Hierarchy**
```yaml
# 1. Specific domains (highest security)
CORS_ORIGINS: "https://app.domain.com,https://admin.domain.com"

# 2. Regex patterns (flexible, secure)  
CORS_ORIGIN_REGEX: "^https://.*\\.domain\\.com$"

# 3. Development wildcard (lowest security)
CORS_ORIGINS: "*"  # Only for development
```

**TCP Proxy Setup**
```toml
# railway.toml
[build]
builder = "nixpacks"

[deploy]
startCommand = "node server.js"
restartPolicyType = "always"

# TCP service configuration
[[deploy.tcpProxies]]
applicationPort = 8080
externalPort = 12345
```

**Rate Limiting with Redis**
```javascript
// Railway Redis-based rate limiting
const redis = require('redis');
const client = redis.createClient({
  url: process.env.REDIS_URL // railway.internal:6379
});

// Rate limit pattern: 100 requests per minute per IP
const rateLimit = async (ip, limit = 100, window = 60) => {
  const key = `rate:${ip}`;
  const current = await client.incr(key);
  if (current === 1) await client.expire(key, window);
  return current <= limit;
};
```

## Golden Rules

**Private Communication Security**
1. Use `.railway.internal` domains for service-to-service communication
2. Never expose internal services via public URLs
3. Database connections MUST use private Railway URLs
4. Enable authentication between internal services

**CORS Origin Best Practices**  
1. Use regex patterns instead of wildcards for production
2. Match protocol (https://) and exact domain patterns
3. Test CORS preflight OPTIONS requests during deployment
4. Set `credentials: true` only when necessary

**PORT Binding Standards**
1. Bind to `0.0.0.0:$PORT` for Railway compatibility  
2. Use `$PORT` environment variable, fallback to default
3. Health check endpoint on same port as main application
4. TCP services expose single port via Railway proxy

**Custom Domain Configuration**
1. CNAME record points to `servicename.up.railway.app`
2. SSL certificates auto-generated via Let's Encrypt
3. Domain verification via DNS TXT record
4. Multiple domains per service supported

## Comparativo 

| Platform | CORS Config | Internal URLs | TCP Proxy | Rate Limiting |
|----------|-------------|---------------|-----------|---------------|
| **Railway** | Regex origins | `.railway.internal` | Built-in TCP proxy | Redis-based |
| Heroku | App-level CORS | Private spaces | Add-on required | Redis add-on |
| Render | Environment vars | Private network | Not supported | Third-party |
| Fly.io | App config | `.internal` domains | TCP/UDP proxy | Built-in |

## References

1. [Railway Networking Guide](https://docs.railway.app/reference/networking)
2. [CORS Configuration](https://docs.railway.app/develop/variables#cors-configuration)
3. [TCP Proxy Documentation](https://docs.railway.app/reference/tcp-proxy)
4. [Custom Domains Setup](https://docs.railway.app/deploy/custom-domains)
5. [Internal Service Discovery](https://docs.railway.app/reference/networking#private-networking)
6. [Rate Limiting Patterns](https://docs.railway.app/guides/rate-limiting)