---
kind: knowledge_card
id: bld_knowledge_card_permission
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for permission production — atomic searchable facts
sources: permission-builder MANIFEST.md + SCHEMA.md, NIST RBAC, OWASP Access Control, POSIX
---

# Domain Knowledge: permission
## Executive Summary
Permissions are declarativand access control rules defining WHO can do WHAT (read/write/execute) on WHICH resource. Each permission declares a scope, roles with hierarchical inheritance, operations per role, and a deny-by-default baseline. They differ from guardrails (which prevent safety damage), laws (which mandate operational rules), feature flags (which toggle features), and runtime rules (which control system behavior) by governing access to specific resources through role-based allow/deny lists.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P09 (configuration) |
| Kind | `permission` (exact literal) |
| ID pattern | `p09_perm_{slug}` |
| Required frontmatter | 14 fields |
| Quality gates | 8 HARD + 12 SOFT |
| Max body | 3072 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Access levels | read, write, execute |
| Default access | deny (safe baseline) |
| Min roles | 1 |
## Patterns
| Pattern | Application |
|---------|-------------|
| Deny-by-default | Default access is "deny"; explicit allow grants access |
| Deny overrides allow | When conflict exists, deny always wins |
| Least privilege | Grant minimum access needed for the role |
| Role hierarchy | Inheritance flows top-down (admin > editor > viewer) |
| Explicit operations | Declare read, write, execute per role (allow/deny/conditional) |
| Audit trail | Log every access event with timestamp and actor |
| Escalation path | Temporary elevation needs approver + time limit |
| Time restrictions | Optional time-window or expiry constraints on grants |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| No scope field | Permission without scope = permission on everything |
| Missing default_access | Implicit allow is dangerous; must be explicit "deny" |
| Operations not declared per role | Missing operations imply allow — a dangerous default |
| No role hierarchy | Flat roles cause permission duplication and inconsistency |
| Permanent escalation without expiry | Elevated access must be time-bounded |
| No audit trail | Cannot detect or investigate unauthorized access |
| Allow-by-default | Violates least privilege; any new resource is open |
## Application
1. Define `scope`: which resource or resource class is governed
2. Set `default_access: deny` (justify if "allow")
3. Define `roles` list with hierarchy and inheritance rules
4. Declare `operations` (read/write/execute) per role: allow, deny, or conditional
5. Set `allow_deny_precedence`: confirm deny overrides allow
6. Define `audit_trail`: logged events and retention period
7. Define `escalation_path`: approver role and max duration
8. Validate: 8 HARD + 12 SOFT gates, body <= 3072 bytes
## References
- permission-builder SCHEMA.md v1.0.0
- NIST RBAC (Role-Based Access Control)
- OWASP Access Control Cheat Sheet
- POSIX file permissions (rwx model)
- AWS IAM policy evaluation logic
