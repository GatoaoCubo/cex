---
kind: knowledge_card
id: bld_knowledge_card_session_backend
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for session_backend production — agent session state persistence
sources: 12-Factor App (Factor VI), Redis persistence docs, SQLite WAL mode, PostgreSQL session management, OWASP session management cheat sheet
---

# Domain Knowledge: session_backend
## Executive Summary
Session backends define the persistence contract for agent session state — specifying which storage engine to use, how to connect, when sessions expire, and how data is serialized. Following the file-first principle (start simple, upgrade when needed), session backends provide a clear upgrade path from zero-dependency file storage to fully distributed postgres. They differ from compression configs (how to reduce state), memory configs (what to remember), and cache configs (ephemeral key-value).
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P10 (memory) |
| llm_function | INJECT |
| Frontmatter fields | 17+ |
| Quality gates | 10 HARD + 12 SOFT |
| Backend options | file, sqlite, redis, postgres |
| Default TTL | 72h (dev), 24h (prod) |
| Naming | p10_sb_{backend}.yaml |
## Patterns
- **Backend selection ladder**: choose based on requirements
| Backend | Concurrency | Distribution | Dependencies | Best for |
|---------|-------------|-------------|-------------|----------|
| file | Single-writer | Local only | None | Dev, prototyping, single-agent |
| sqlite | Multi-reader, single-writer (WAL) | Local only | stdlib sqlite3 | Multi-agent local, moderate scale |
| redis | Multi-reader, multi-writer | Distributed | redis-py + server | Production, TTL enforcement, pub/sub |
| postgres | Full ACID | Distributed | psycopg2 + server | Production, audit trail, complex queries |
- **Session scoping**: namespace isolation prevents data corruption
| Scope | Key format | Use case |
|-------|-----------|----------|
| per_nucleus | `{nucleus}:{session_id}` | Default — each nucleus has its own state |
| per_agent | `{agent}:{session_id}` | Shared state across nuclei for one agent |
| global | `global:{session_id}` | Cross-agent coordination (rare, justify explicitly) |
- **Serialization selection**: format affects readability, speed, and safety
| Format | Human-readable | Speed | Size | Schema evolution | Security |
|--------|---------------|-------|------|-----------------|----------|
| json | Yes | Slow | Large | Add fields with null defaults | Safe |
| msgpack | No | Fast | Small | Forward-compatible | Safe |
| protobuf | No | Fastest | Smallest | .proto versioning | Safe |
| pickle | No | Fast | Medium | Fragile | UNSAFE — never use |
| Source | Concept | Application |
|--------|---------|-------------|
| 12-Factor (VI) | Processes are stateless, share-nothing | State lives in backing service, not process memory |
| Redis | TTL on keys | Automatic session expiration without cleanup cron |
| SQLite WAL | Write-ahead logging | Concurrent reads with single writer |
| OWASP | Session management | Token-based session IDs, secure storage, TTL enforcement |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| In-memory without persistence | State lost on restart — agent forgets mid-conversation |
| Global namespace | Concurrent nuclei overwrite each other's sessions |
| No TTL | Storage grows unbounded — disk exhaustion in production |
| Pickle serialization | Arbitrary code execution on deserialization (CVE risk) |
| Embedded credentials | Connection passwords committed to git, exposed in logs |
| No compaction | Session files accumulate stale entries, slow to load |
| No max_sessions | Resource exhaustion when many conversations spawn simultaneously |
## Application
1. Assess scale: single-agent (file), multi-agent (sqlite), distributed (redis/postgres)
2. Select backend from ladder based on concurrency and distribution needs
3. Define TTL: 72h dev, 24h prod (adjust based on session length)
4. Choose serialization: json (dev, readability), msgpack (prod, speed)
5. Set scoping: per_nucleus default, per_agent for shared state
6. Configure encryption: none (dev), basic (staging), full (prod with PII)
7. Document upgrade path to next tier
8. Reference credentials via env vars, never embed
## References
- 12factor.net/processes: Factor VI — Stateless processes
- Redis persistence: RDB vs AOF for session durability
- SQLite WAL mode: concurrent read access documentation
- OWASP: Session Management Cheat Sheet
