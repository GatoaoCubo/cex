---
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for permission production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: permission Production Rules

## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p09_perm_{scope_slug}.md | p09_perm_pool_access.md |
| Builder dir | kebab-case | permission-builder/ |
| Fields | snake_case | deny_list, allow_list |

Rule: id MUST equal filename stem.

## File Paths
- Output: cex/P09_config/examples/p09_perm_{scope_slug}.md
- Compiled: cex/P09_config/compiled/p09_perm_{scope_slug}.yaml

## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Density: >= 0.80

## Access Level Matrix
| Level | Meaning | Enum values |
|-------|---------|------------|
| read | View resource content | allow, deny, conditional |
| write | Modify resource content | allow, deny, conditional |
| execute | Run resource as action | allow, deny, conditional |

## Precedence Rule
deny_list ALWAYS overrides allow_list (no exceptions).
