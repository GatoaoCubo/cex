---
kind: schema
id: bld_schema_director
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for agent_card
pattern: TEMPLATE derives from this. CONFIG restricts this.
---

# Schema: agent_card
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p08_ac_{name}) | YES | - | Namespace compliance |
| kind | literal "agent_card" | YES | - | Type integrity |
| pillar | literal "P08" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Versionamento |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| name | string | YES | - | Satellite name (uppercase) |
| role | string | YES | - | Primary function description |
| model | string | YES | - | LLM model used (opus, sonnet, haiku) |
| mcps | list[string] | YES | - | MCP servers available |
| domain_area | string | YES | - | Domain this satellite covers |
| boot_sequence | list[string] | REC | [] | Ordered boot steps |
| constraints | list[string] | REC | [] | Operational limitations |
| dispatch_keywords | list[string] | REC | [] | Keywords that route tasks here |
| tools | list[string] | REC | [] | Tools available to this satellite |
| dependencies | list[string] | REC | [] | Other satellites/services required |
| scaling | object or null | REC | null | Scaling rules (max_concurrent, timeout) |
| monitoring | object or null | REC | null | Health check and alerting config |
| runtime | string | REC | "claude" | Runtime engine (claude, codex) |
| mcp_config_file | string or null | REC | null | Path to .mcp-{sat}.json |
| flags | list[string] | REC | [] | CLI flags for spawn |
| domain | string | YES | - | Domain this artifact belongs to |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "satellite" |
| tldr | string <= 160ch | YES | - | Dense summary |
## Complex Objects
```yaml
scaling:
  max_concurrent: integer    # max parallel instances
  timeout_minutes: integer   # max execution time
  memory_limit_mb: integer   # RAM ceiling
monitoring:
  health_check: string       # command or URL
  signal_on_complete: boolean # emit signal when done
  alert_on_failure: boolean  # notify on error
```
## ID Pattern
Regex: `^p08_ac_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Role` — what the satellite does and its primary function
2. `## Model & MCPs` — LLM model details and MCP server specs
3. `## Boot Sequence` — ordered initialization steps
4. `## Dispatch` — keywords and routing rules
5. `## Constraints` — operational limits and prohibitions
6. `## Dependencies` — external services and sibling satellites
7. `## Scaling & Monitoring` — concurrency, timeouts, health checks
## Constraints
- max_bytes: 4096 (body only)
- naming: p08_ac_{name_lower}.yaml
- machine_format: yaml
- id == filename stem
- name MUST be non-empty (uppercase convention)
- role MUST describe primary function
- model MUST be a valid LLM identifier
- mcps MUST list available MCP servers (empty list if none)
- quality: null always
