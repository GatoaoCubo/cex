---
id: "p09_perm_{{SCOPE_SLUG}}"
kind: permission
pillar: P09
version: 1.0.0
title: Template - Permission
tags: [template, permission, access, rbac, security]
tldr: Access control for agents and nuclei. Who can read, write, execute per resource type.
quality: 9.0
updated: "2026-04-07"
domain: "configuration management"
author: n03_builder
created: "2026-04-07"
density_score: 0.97
related:
  - permission-builder
  - bld_architecture_permission
  - bld_collaboration_permission
  - bld_output_template_permission
  - bld_tools_permission
  - bld_config_permission
  - p11_qg_permission
  - p01_kc_permission
  - bld_memory_permission
  - bld_schema_permission
---

# Permission: [NAME]

## Purpose
[WHAT this permission does]
## Permission Matrix
| Resource | N01 | N02 | N03 | N04 | N05 | N06 | N07 |
|----------|-----|-----|-----|-----|-----|-----|-----|
| Builders | R | R | RW | R | R | R | R |
| KCs | RW | R | R | RW | R | R | R |
| Config | R | R | R | R | RW | R | RW |
| Deploy | -- | -- | R | -- | RWX | -- | RW |
## Levels
| Level | Meaning |
|-------|---------|
| R | Read/view |
| W | Create/modify |
| X | Run/deploy |
| A | Approve/sign-off |
## Escalation
- **Higher access**: Request from N07
- **Emergency**: N07 grants temp RWX (1h)
- **Audit**: All changes logged
## Quality Gate
- [ ] Every nucleus has explicit permissions
- [ ] Least privilege enforced
- [ ] N07 coordinates but doesn't build
- [ ] Escalation path documented

## Cross-References

- **Pillar**: P09 (Config)
- **Kind**: `permission`
- **Artifact ID**: `p09_perm_{{SCOPE_SLUG}}`
- **Tags**: [template, permission, access, rbac, security]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P09 | Config domain |
| Kind `permission` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: permission
pillar: P09
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[permission-builder]] | related | 0.47 |
| [[bld_architecture_permission]] | upstream | 0.44 |
| [[bld_collaboration_permission]] | related | 0.42 |
| [[bld_output_template_permission]] | upstream | 0.37 |
| [[bld_tools_permission]] | upstream | 0.35 |
| [[bld_config_permission]] | related | 0.32 |
| [[p11_qg_permission]] | downstream | 0.32 |
| [[p01_kc_permission]] | related | 0.32 |
| [[bld_memory_permission]] | downstream | 0.32 |
| [[bld_schema_permission]] | upstream | 0.31 |
