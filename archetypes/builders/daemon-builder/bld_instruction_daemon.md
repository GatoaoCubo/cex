---
kind: instruction
id: bld_instruction_daemon
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for daemon
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.2
title: "Instruction Daemon"
version: "1.0.0"
author: n03_builder
tags: [daemon, builder, examples]
tldr: "Golden and anti-examples for daemon construction, demonstrating ideal structure and common pitfalls."
domain: "daemon construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a daemon
## Phase 1: RESEARCH
1. Identify what runs persistently in the background and why it cannot be a one-shot process
2. Determine schedule: continuous loop, cron expression (e.g., `0 * * * *`), or fixed interval (e.g., `30s`)
3. Define restart policy: always, on-failure, or never — with the justification for the choice
4. Map signal handling: at minimum SIGTERM (graceful shutdown) and SIGINT; add SIGHUP (config reload) if applicable
5. Specify resource limits: memory ceiling, CPU shares, and max open file descriptors
6. Define health check mechanism: HTTP endpoint, heartbeat file, or process liveness check with interval and timeout
7. Check for existing daemon artifacts to avoid duplicates
8. Confirm name slug for id: snake_case, lowercase, no hyphens
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Write Lifecycle section: startup sequence, restart conditions, and graceful shutdown procedure
5. Write Schedule section: concrete cron expression, interval value, or the word "continuous" — never vague
6. Write Signal Handling section: table with each signal (SIGTERM, SIGINT, SIGHUP, costm) and its handler behavior
7. Write Health Check section: mechanism type, check interval, timeout, and expected healthy response
8. Write Resource Limits section: memory ceiling, CPU shares, max file descriptors
9. Write Monitoring section: metrics to expose, alerting thresholds, log rotation policy
10. Write PID Management section: PID file location and stale PID handling procedure
11. Verify body <= 1024 bytes
12. Verify id matches `^p04_dm_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p04_dm_`
4. Confirm kind == daemon
5. Confirm restart policy is defined (always, on-failure, or never)
6. Confirm signal handling specifies at least SIGTERM behavior
7. Confirm health check is present with interval and expected response
8. Confirm schedule is concrete (not vague like "periodically")
9. HARD gates: frontmatter valid, id pattern matches, restart policy defined, signal handling specified, health check present
10. SOFT gates: graceful shutdown documented, score against QUALITY_GATES.md
11. Cross-check: persistent background process (not a one-shot cli_tool)? Not event-triggered (hook)? Not invocable on demand (skill)? Graceful shutdown path documented?
12. Revise if score < 8.0 before outputting

## ISO Loading

```yaml
loader: cex_skill_loader
injection_point: F3_compose
priority: high
```

```bash
python _tools/cex_skill_loader.py --verify daemon
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | daemon construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
