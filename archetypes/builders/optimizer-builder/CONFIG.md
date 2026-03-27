---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for optimizer production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: optimizer Production Rules

## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p11_opt_{target_slug}.md | p11_opt_kc_latency.md |
| Builder dir | kebab-case | optimizer-builder/ |
| Fields | snake_case | density_score, measured_at |
| Slug chars | [a-z][a-z0-9_]+ | no hyphens, no uppercase |

Rule: id MUST equal filename stem.
Rule: target_slug derived from target field — spaces to underscores, lowercase.

## File Paths
- Output: cex/P11_feedback/examples/p11_opt_{target_slug}.md
- Compiled: cex/P11_feedback/compiled/p11_opt_{target_slug}.yaml

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80

## Threshold Ordering Rules
| metric.direction | Ordering |
|-----------------|----------|
| minimize | trigger < target < critical |
| maximize | trigger > target > critical |

## Frequency Enum (valid values only)
continuous, hourly, daily, weekly, monthly

## Action Type Enum (valid values only)
tune, prune, scale, replace, restructure

## Risk Level Enum (valid values only)
low, medium, high

## Improvement History
- list of {date: YYYY-MM-DD, value: float}
- minimum 0 entries at creation
- append on each optimization cycle

## Automated Flag
- true: system executes action without human approval
- false: system flags, human approves before execution
