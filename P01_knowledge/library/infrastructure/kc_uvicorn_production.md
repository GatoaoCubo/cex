---
```yaml
updated: "2026-04-07"
domain: "knowledge management"
title: "Uvicorn Production"
version: "1.0.0"
author: n04_knowledge
created: "2026-04-07"
density_score: 0.94
tldr: "Defines the artifact specification for uvicorn production, with structural rules, validation gates, and integration points."
quality: 9.0
tags: [artifact, builder, examples]
---
id: p01_kc_uvicorn_production
kind: knowledge_card
type: domain
pillar: P01
title: "Uvicorn Production — Workers, Host Config, Environment Variables, Proxy Headers, Graceful Shutdown"
version: 1.0.0
created: 2026-04-01
updated: 2026-04-01
author: builder_agent
domain: infrastructure
origin: manual
quality: 9.0
tags: [uvicorn, production, workers, asgi, fastapi, deployment, proxy, environment]
tldr: "Production uvicorn configuration with optimal worker counts, host binding, environment integration, proxy header handling, and graceful shutdown patterns"
when_to_use: "Deploying FastAPI/ASGI apps to production with proper scaling, load balancing, and reliability patterns"
keywords: [uvicorn, workers, host, port, proxy-headers, lifespan, graceful-shutdown, asgi, production]
long_tails:
  - "How to calculate optimal uvicorn worker count based on CPU cores for production deployment"
  - "Which proxy headers to trust and configure in uvicorn for proper client IP and protocol detection"
axioms:
  - "Workers = 2*CPU+1 balances throughput with memory efficiency for I/O-bound ASGI applications"
  - "Always bind to 0.0.0.0 in containers, never localhost — enables external access through orchestration"
linked_artifacts:
  primary: null
  related: [p01_kc_deploy_paas, p01_kc_docker_patterns]
feeds_kinds:
  - env_config        # Environment variable injection and PORT configuration
  - runtime_rule      # Worker limits, timeout constraints, restart policies
  - path_config       # Static file paths, mount points, working directories
density_score: 0.89
---

# Uvicorn Production Configuration

## Quick Reference
```bash
# Production command pattern
uvicorn app:main --host 0.0.0.0 --port $PORT --workers $(($(nproc)*2+1)) \
  --proxy-headers --lifespan on --access-log --timeout-keep-alive 65

# Environment variables
export PORT=8000
export WEB_CONCURRENCY=4  # Override worker calculation if needed
export UVICORN_HOST=0.0.0.0
export UVICORN_PORT=$PORT
```

## Key Concepts

| Concept | Production Value | Why | Impact |
|---------|-----------------|-----|---------|
| Worker Count | `2*CPU+1` | Optimal for I/O-bound ASGI apps | Balances throughput vs memory usage |
| Host Binding | `0.0.0.0` | Container/orchestration compatibility | Enables external traffic routing |
| PORT Environment | `$PORT` or `${PORT:-8000}` | Platform-agnostic deployment | Works across PaaS providers |
| Proxy Headers | `--proxy-headers` | Trust X-Forwarded headers | Correct client IP/protocol detection |
| Lifespan Events | `--lifespan on` | Startup/shutdown hooks | Database connections, cache warmup |
| Keep-Alive Timeout | `65s` | Slightly longer than load balancer | Prevents premature connection drops |

## Patterns

| Scenario | Configuration | Reasoning |
|----------|---------------|-----------|
| Railway/Render Deploy | `uvicorn app:main --host 0.0.0.0 --port $PORT --workers 2` | Respect platform PORT, minimal workers for small instances |
| Docker Container | `--host 0.0.0.0 --port 8000 --workers $(($(nproc)*2+1))` | Container networking + CPU-based scaling |
| Behind Nginx/ALB | `--proxy-headers --timeout-keep-alive 65` | Trust forwarded headers, align timeouts |
| FastAPI + DB | `--lifespan on` for startup/shutdown | Proper connection pool lifecycle |
| High Traffic | `--workers 8 --worker-class uvicorn.workers.UvicornWorker` | Max workers with proper worker class |
| Development Preview | `--host 127.0.0.1 --port 8000 --reload` | Local binding with auto-reload |

## Golden Rules

1. **Worker Formula**: Use `workers = 2*CPU+1` as starting point, tune based on memory/performance metrics
2. **Host Binding**: Always `0.0.0.0` in production containers, never `localhost` or `127.0.0.1`
3. **Environment PORT**: Use `$PORT` variable for platform compatibility (Railway, Heroku, Render, etc.)
4. **Proxy Integration**: Enable `--proxy-headers` behind load balancers to preserve client IP/protocol
5. **Graceful Shutdown**: Enable `--lifespan on` for proper startup/shutdown sequence with database connections
6. **Timeout Alignment**: Set `--timeout-keep-alive 65` to be slightly longer than upstream load balancer timeout (usually 60s)

## Anti-Patterns

- Hard-coding port instead of using `$PORT` environment variable (breaks platform deployment)
- Using `localhost` binding in containers (blocks external traffic)
- Single worker in production (no fault tolerance, poor CPU utilization)
- Ignoring proxy headers behind load balancers (incorrect client IP logging)
- Missing lifespan events with database connections (connection leaks, startup delays)
```