---
kind: config
id: bld_config_daemon
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
---
# Config: daemon Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_daemon_{name_slug}.md` + `.yaml` | `p04_daemon_brain_rebuilder.md` |
| Builder directory | kebab-case | `daemon-builder/` |
| Frontmatter fields | snake_case | `restart_policy`, `health_check` |
| Name slug | snake_case, lowercase, no hyphens | `brain_rebuilder`, `log_rotator` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_daemon_{name_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_daemon_{name_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2500 bytes
- Density: >= 0.80 (no filler)
## Restart Policy Enum
| Value | When to use |
|-------|-------------|
| always | Critical services that must always be running |
| on_failure | Tasks that may complete normally (cron jobs) |
| never | One-shot scheduled tasks (consider cli_tool instead) |
## Schedule Formats
| Format | Example | When to use |
|--------|---------|-------------|
| cron | "0 */6 * * *" | Periodic tasks at specific times |
| interval | "every 30s" | Polling loops with fixed delay |
| continuous | "continuous" | Always-running watchers/consumers |
## Logging Enum
| Value | When to use |
|-------|-------------|
| structured | JSON logs with fields (default, recommended) |
| plaintext | Simple text logs (legacy or human-readable) |
| syslog | System log integration (traditional Unix daemons) |
