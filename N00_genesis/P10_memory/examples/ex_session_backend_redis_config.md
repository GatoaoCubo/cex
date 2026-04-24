---
id: p10_sb_redis
kind: session_backend
8f: F5_call
pillar: P10
title: "Example — Redis Session Backend"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
backend: redis
connection_string: "redis://localhost:6379/0"
ttl_hours: 24
max_sessions: 100
serialization: json
encryption: false
domain: session_backend
quality: 9.1
tags: [session-backend, redis, persistence, state, memory]
tldr: "Redis session backend — localhost:6379, JSON serialization, 24h TTL, 100 max sessions, namespace-per-nucleus isolation."
when_to_use: "Multi-process agent sessions requiring shared state and fast read/write with automatic expiry"
keywords: [session, redis, persistence, state, ttl, multi-process]
density_score: null
related:
  - p01_kc_session_backend
  - bld_knowledge_card_session_backend
  - bld_examples_session_backend
  - p03_sp_session_backend_builder
  - session-backend-builder
  - bld_collaboration_session_backend
  - bld_architecture_session_backend
  - bld_instruction_session_backend
  - bld_config_session_backend
  - p10_lr_session_backend_builder
---

# Session Backend: Redis

## Configuration
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| backend | redis | Sub-ms read/write, built-in TTL, pub/sub for signals |
| connection | redis://localhost:6379/0 | Standard local instance |
| serialization | json | Human-readable, debuggable, no security risk (vs pickle) |
| ttl_hours | 24 | Auto-cleanup prevents unbounded growth |
| max_sessions | 100 | Cap prevents resource exhaustion |
| encryption | false | Local dev; enable for production |

## Namespace Strategy
| Key Pattern | Content | TTL |
|-------------|---------|-----|
| `cex:session:{nucleus}:{session_id}` | Conversation state | 24h |
| `cex:memory:{nucleus}:{kind}` | Builder memory observations | 168h (7d) |
| `cex:signal:{mission}:{nucleus}` | Completion signals | 1h |
| `cex:lock:{resource}` | Distributed locks | 300s |

## Operations
```python
import redis, json

r = redis.Redis.from_url("redis://localhost:6379/0")

# Save session state
state = {"turns": [...], "context": {...}, "decisions": {...}}
r.setex(f"cex:session:n03:{sid}", 86400, json.dumps(state))

# Load session state
raw = r.get(f"cex:session:n03:{sid}")
state = json.loads(raw) if raw else {}

# Signal completion
r.setex(f"cex:signal:MISSION:n03", 3600, "complete")

# Check all nucleus signals
signals = {k.decode(): r.get(k).decode()
           for k in r.scan_iter("cex:signal:MISSION:*")}
```

## Upgrade Path
| Backend | Concurrency | Persistence | Latency | Complexity |
|---------|------------|-------------|---------|-----------|
| file | single | yes (git) | ~5ms | zero deps |
| sqlite | single-write | yes | ~1ms | one file |
| **redis** | **multi-process** | **optional** | **<1ms** | **server** |
| postgres | multi-process | yes (ACID) | ~2ms | full DB |

## Performance
| Metric | Value |
|--------|-------|
| GET latency | ~0.1ms |
| SET latency | ~0.1ms |
| Memory per session (~5KB) | ~500 KB for 100 sessions |
| Max throughput | ~100K ops/sec |

## Boundary
session_backend IS: storage config for agent session state with connection, TTL, and serialization rules.
session_backend IS NOT: a compression config (how to compact), a memory type (what to remember), or a trace config (what to log).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_session_backend]] | related | 0.56 |
| [[bld_knowledge_card_session_backend]] | upstream | 0.43 |
| [[bld_examples_session_backend]] | upstream | 0.42 |
| [[p03_sp_session_backend_builder]] | upstream | 0.42 |
| [[session-backend-builder]] | upstream | 0.41 |
| [[bld_collaboration_session_backend]] | downstream | 0.40 |
| [[bld_architecture_session_backend]] | upstream | 0.39 |
| [[bld_instruction_session_backend]] | upstream | 0.38 |
| [[bld_config_session_backend]] | upstream | 0.36 |
| [[p10_lr_session_backend_builder]] | related | 0.34 |
