---
id: p03_ins_permission
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-03-27
updated: 2026-03-27
author: instruction-builder
title: Permission Builder Instructions
target: permission-builder agent
phases_count: 3
prerequisites:
  - The resource, agent, or artifact requiring access control is named
  - At least one role that needs access is identified (e.g., "admin", "read-only user", "service account")
  - The operations requiring control are known (read, write, execute, or a subset)
validation_method: checklist
domain: permission
quality: null
tags:
  - instruction
  - permission
  - access-control
  - P09
idempotent: true
atomic: false
rollback: "Delete the produced permission artifact file; no system state changes occur"
dependencies: []
logging: true
tldr: "Research scope and roles, compose read/write/execute rules with allow/deny lists and audit trail, validate precedence and gates, write permission artifact."
density_score: 0.84
---

## Context

The permission-builder receives a **resource or artifact description** and produces a `permission` artifact encoding the access control rules for that scope — who can read, write, and execute it, under what conditions, and how access is inherited.

**Input variables**:
- `{{scope}}` — the resource, artifact, or agent being protected (e.g., `artifact_store`, `signal_writer`, `admin_dashboard`)
- `{{roles}}` — list of roles that interact with the scope (e.g., `[admin, editor, viewer, service_account]`)
- `{{operations}}` — the operations requiring control: any combination of `read`, `write`, `execute`
- `{{access_model}}` — optional: `RBAC` (role-based), `ABAC` (attribute-based), or `ACL` (access control list). Default: `RBAC`
- `{{conditions}}` — optional: contextual conditions under which access applies (e.g., "only during business hours", "only from internal network")

**Output**: a single `permission` artifact at `p09_perm_{{scope_slug}}.md` with read/write/execute rules, role hierarchy, allow_list, deny_list, audit config, and escalation path.

**Boundaries**: handles access control rules only. Does NOT define safety constraints that limit what a system CAN do regardless of permission (use guardrail-builder), operational laws that are inviolable (use law-builder), or quality thresholds (use quality_gate-builder).

---

## Phases

### Phase 1: RESEARCH

**Goal**: Identify the full access landscape — scope, roles, access patterns, and existing rules — before writing.

1. Identify the `{{scope}}`: confirm it is a concrete resource, artifact, or agent. A scope that is too broad ("the whole system") must be split into multiple permission artifacts.
2. Find existing permissions for the same scope: search `P09_config/examples/` or use brain_query [IF MCP]: `permission {{scope}}`. If found, determine whether an update or merge is needed.
3. Enumerate all roles from `{{roles}}`. For each role, determine:
   - What operations they need: `read`, `write`, `execute`
   - Whether access is unconditional or conditional (see `{{conditions}}`)
   - Whether this role inherits from a parent role (role hierarchy)
4. Identify the access model from `{{access_model}}`:
   - `RBAC`: permissions attached to roles, roles assigned to principals
   - `ABAC`: permissions evaluated against resource/subject attributes at runtime
   - `ACL`: explicit list of principals with their allowed operations per resource
5. Determine deny precedence rule: deny_list entries ALWAYS override allow_list entries. Document this explicitly.
6. Identify what must be logged for audit: at minimum, log all `write` and `execute` operations with principal identity, timestamp, and resource identifier.
7. Identify the escalation path: how does a principal request elevated access that they do not currently hold?

**Exit**: all roles mapped to operations, access model confirmed, deny precedence rule documented, audit log requirements identified, escalation path known.

---

### Phase 2: COMPOSE

**Goal**: Produce all artifact fields and body sections following SCHEMA.md and OUTPUT_TEMPLATE.md.

8. Read SCHEMA.md — source of truth for all required fields (17 required + 4 recommended).
9. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints exactly.
10. Generate `scope_slug` in snake_case. Set `id = p09_perm_{{scope_slug}}` matching `^p09_perm_[a-z][a-z0-9_]+$`.
11. Fill frontmatter: all 17 required + 4 recommended fields. Set `quality: null` — never self-score.
12. Set `scope` to the concrete resource or artifact being protected.
13. Define **read rules**: who can view the scope and under what conditions. For conditional access, state the condition explicitly.
14. Define **write rules**: who can modify the scope and under what conditions. Write access implies read access unless explicitly denied.
15. Define **execute rules**: who can run or invoke the scope and under what conditions. Only include if `execute` is in `{{operations}}`.
16. Define the **role hierarchy**: list each role and its parent role (if any). A child role inherits all permissions of its parent unless explicitly overridden.
17. Write **allow_list**: explicit role-operation pairs that are permitted. Format: `role: [operation_1, operation_2]`.
18. Write **deny_list**: explicit role-operation pairs that are forbidden. Format: `role: [operation_1]`. Deny overrides allow — document this precedence.
19. Write **audit** section: what gets logged (operation, principal, timestamp, resource ID), where logs are sent, retention period.
20. Write **escalation** section: how to request elevated access — process (ticket, approval chain), approver role, time limit for temporary elevation.

**Exit**: read/write/execute rules defined for all roles in `{{roles}}`, deny_list precedence documented, audit section complete.

---

### Phase 3: VALIDATE

**Goal**: Verify all quality gates and precedence rules before writing the final artifact.

21. Check QUALITY_GATES.md — verify HARD gates: id format, kind, pillar, quality==null, scope present.
22. Verify deny_list overrides allow_list (precedence correct) — this must be stated explicitly in the artifact body.
23. Verify read/write/execute sections are each defined (even if empty for inapplicable operations).
24. Verify roles in allow_list and deny_list are all present in the role hierarchy.
25. Verify no circular inheritance in role hierarchy.
26. Score SOFT gates: read/write/execute defined, roles concrete (not "someone" or "users"), audit section present and specific.
27. If score < 8.0: revise in same pass before outputting. Do not output a failing artifact.
28. Write the final artifact using the Output Contract template below.

---

## Output Contract

```
---
id: p09_perm_{{scope_slug}}
kind: permission
pillar: P09
domain: {{scope}}
version: 1.0.0
created: {{date}}
author: permission-builder
scope: {{scope_description}}
access_model: {{RBAC|ABAC|ACL}}
roles: [{{role_1}}, {{role_2}}]
operations: [{{read|write|execute}}]
quality: null
tags: [permission, {{scope_slug}}, access-control]
---

## Scope

**Resource**: {{scope_description}}
**Access model**: {{RBAC|ABAC|ACL}}
**Deny precedence**: deny_list overrides allow_list unconditionally.

## Read Rules

| Role | Allowed | Condition |
|------|---------|-----------|
| {{role}} | {{true|false}} | {{condition or "none"}} |

## Write Rules

| Role | Allowed | Condition |
|------|---------|-----------|
| {{role}} | {{true|false}} | {{condition or "none"}} |

## Execute Rules

| Role | Allowed | Condition |
|------|---------|-----------|
| {{role}} | {{true|false}} | {{condition or "none"}} |

## Role Hierarchy

| Role | Parent | Inherits |
|------|--------|---------|
| {{role}} | {{parent_role or "none"}} | {{inherited_operations}} |

## Allow List

```yaml
{{role_1}}: [read, write]
{{role_2}}: [read]
```

## Deny List

```yaml
{{role_3}}: [write, execute]
```

## Audit

- **Log on**: all write and execute operations
- **Fields**: principal, operation, resource_id, timestamp, outcome
- **Destination**: {{log_destination}}
- **Retention**: {{retention_period}}

## Escalation

- **Process**: {{ticket_system_or_approval_chain}}
- **Approver**: {{approver_role}}
- **Temporary elevation limit**: {{time_limit}}
```

---

## Validation

| # | Gate | Type |
|---|------|------|
| 1 | `id` matches `^p09_perm_[a-z][a-z0-9_]+$` | HARD |
| 2 | `kind = permission` exactly | HARD |
| 3 | `pillar = P09` | HARD |
| 4 | `quality: null` is set | HARD |
| 5 | `scope` field is present and non-empty | HARD |
| 6 | deny_list overrides allow_list — precedence stated explicitly in body | HARD |
| 7 | Roles in allow_list and deny_list are all present in role hierarchy | HARD |
| 8 | No circular inheritance in role hierarchy | HARD |
| 9 | Read, write, and execute sections each defined (even if empty) | SOFT |
| 10 | Roles are concrete named entities, not generic ("users", "someone") | SOFT |
| 11 | Audit section specifies log fields and destination | SOFT |
| 12 | Escalation section specifies approver role and time limit | SOFT |

---

## Metacognition

**Does**:
- Encodes who can read, write, and execute a named resource with explicit role hierarchy
- Documents allow/deny with correct precedence (deny overrides allow)
- Specifies audit logging and escalation path as part of the access contract

**Does NOT**:
- Define safety constraints that limit system behavior regardless of permission (use guardrail-builder)
- Encode inviolable operational rules (use law-builder)
- Define quality thresholds or scoring (use quality_gate-builder)
- Control filesystem path access specifically (use path-config-builder for paths, permission-builder for access)

**Chaining**: output feeds authorization middleware (allow/deny evaluation), audit log routers (log fields), access request workflows (escalation path). Input from system design doc, security requirements, role catalog.
