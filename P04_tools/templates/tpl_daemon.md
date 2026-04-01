---
id: "p04_daemon_{{NAME_SLUG}}"
kind: daemon
pillar: P04
version: 1.0.0
title: Template - Daemon
tags: [template, daemon, background, service, worker]
tldr: "Long-running background service: startup, shutdown, health check, signal handling, restart policy."
quality: 8.6
---

# Daemon: [NAME]

## Purpose
[WHAT this daemon does]
## Configuration
```yaml
name: "[DAEMON_NAME]"
type: [worker | watcher | scheduler | server]
health_interval_s: [30]
pid_file: "[/var/run/daemon.pid]"
```
## Lifecycle
| Phase | Action | Signal |
|-------|--------|--------|
| Start | Init resources, begin loop | -- |
| Health | Verify connectivity | -- |
| Reload | Re-read config | SIGHUP |
| Stop | Finish task, cleanup | SIGTERM |
| Kill | Immediate stop | SIGKILL |
## Restart Policy
- **Crash**: Auto-restart after 5s, max 3 retries
- **OOM**: Restart + increase memory
- **Unresponsive**: Kill after 60s no health
## Quality Gate
- [ ] PID file prevents duplicates
- [ ] Graceful SIGTERM handling
- [ ] Health check endpoint
- [ ] Max restart limit set
