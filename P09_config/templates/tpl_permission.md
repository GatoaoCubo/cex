---
id: "p09_perm_{{SCOPE_SLUG}}"
kind: permission
pillar: P09
version: 1.0.0
title: Template - Permission
tags: [template, permission, access, rbac, security]
tldr: Access control for agents and nuclei. Who can read, write, execute per resource type.
quality: null
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
