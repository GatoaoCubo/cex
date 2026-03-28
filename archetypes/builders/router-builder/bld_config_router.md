---
kind: config
id: bld_config_router
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
---

# Config: router Production Rules

## Naming Convention

| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p02_router_{slug}.md` | `p02_router_satellite_task.md` |
| Builder directory | kebab-case | `router-builder/` |
| Frontmatter fields | snake_case | `routes_count`, `fallback_route` |
| Router slug | snake_case, lowercase | `satellite_task`, `api_gateway` |

Rule: id MUST equal filename stem.

## File Paths
- Output: `cex/P02_model/examples/p02_router_{slug}.md`
- Compiled: `cex/P02_model/compiled/p02_router_{slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Total (frontmatter + body): ~5500 bytes
- Density: >= 0.80

## Load Balance Enum

| Value | When to use |
|-------|-------------|
| priority | Routes have clear priority ordering (default) |
| weighted | Traffic should be distributed by weight percentage |
| round_robin | Equal distribution across equivalent destinations |
| none | Single best match only, no distribution |

## Confidence Threshold Guidelines

| Range | Meaning | Use case |
|-------|---------|----------|
| 0.9-1.0 | Very high confidence required | Critical/admin routes |
| 0.7-0.9 | Standard confidence | Most production routes |
| 0.5-0.7 | Loose matching | Exploratory or catch-all routes |
| < 0.5 | Not recommended | Too many false positives |

## Route Table Requirements
- Minimum 2 routes per router (1-route routers are dispatch_rules)
- Each pattern must be unique across the table
- Priority range: 1-100 (higher = preferred)
- Confidence_min per route can override global confidence_threshold
