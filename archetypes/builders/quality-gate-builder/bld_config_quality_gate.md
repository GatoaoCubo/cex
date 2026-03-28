---
kind: config
id: bld_config_quality_gate
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for quality_gate production
pattern: CONFIG restricts SCHEMA, never contradicts
---

# Config: quality_gate Production Rules

## Naming
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact | p11_qg_{slug}.md | p11_qg_kc_publish.md |
| Builder dir | kebab-case | quality-gate-builder/ |
| Fields | snake_case | density_score |

Rule: id MUST equal filename stem.

## File Paths
- Output: cex/P11_feedback/examples/p11_qg_{slug}.md
- Compiled: cex/P11_feedback/compiled/p11_qg_{slug}.yaml

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes
- Density: >= 0.80
