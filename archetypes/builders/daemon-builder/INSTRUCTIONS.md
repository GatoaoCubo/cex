---
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for daemon
pattern: 3-phase pipeline (research -> compose -> validate)
---

# Instructions: How to Produce a daemon

## Phase 1: RESEARCH
1. Identify the background task and why it must be persistent (not one-shot)
2. Determine schedule: continuous, cron expression, or fixed interval
3. Determine restart_policy: always, on_failure, or never
4. Define signal handling: at minimum SIGTERM graceful shutdown behavior
5. Identify resource limits: memory ceiling, CPU shares, max file descriptors
6. Determine health_check strategy: endpoint, heartbeat file, or process check
7. Check for existing daemon artifacts via brain_query [IF MCP] (avoid duplicates)
8. Confirm name slug for id: snake_case, lowercase, no hyphens

## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill {{vars}} following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set restart_policy to one of: always, on_failure, never
5. Write schedule as concrete value (cron, interval, or "continuous")
6. Write ## Overview: 1-2 sentences on what, why background, who depends
7. Write ## Lifecycle: schedule, startup, restart behavior, shutdown procedure
8. Write ## Signal Handling: table with SIGTERM, SIGINT, SIGHUP, custom
9. Write ## Monitoring: health check, metrics, alerting, log rotation
10. Verify body <= 1024 bytes
11. Verify id matches `^p04_daemon_[a-z][a-z0-9_]+$`

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm schedule is concrete (not vague like "periodically")
4. Confirm quality == null
5. Confirm body has all 4 required sections
6. Confirm signal_handling includes at least SIGTERM
7. Confirm body <= 1024 bytes
8. Score SOFT gates against QUALITY_GATES.md
9. Revise if score < 8.0 before outputting
