---
pillar: P01
llm_function: INJECT
purpose: Standards and patterns for permission production
sources: [NIST RBAC, OWASP Access Control, ABAC, CEX Laws]
---

# Domain Knowledge: permission

## Foundational Concepts
Permissions control WHO can do WHAT on WHICH resource.
Three access levels: read (view), write (modify), execute (run).
Core principle: deny overrides allow (explicit deny always wins).
In CEX: declarative access rules applied to agents, artifacts, and resources.

## Industry Patterns
| Source | What it defines | CEX alignment |
|--------|----------------|---------------|
| NIST RBAC | Role-Based Access Control standard | Roles, hierarchy, inheritance |
| OWASP Access Control | Broken access control prevention | Deny-by-default, least privilege |
| ABAC | Attribute-Based Access Control | Conditional access based on context |
| AWS IAM | Identity and access management | Allow/deny lists, policy precedence |
| POSIX Permissions | Unix file permissions (rwx) | read/write/execute model |

## Key Principles
- Deny overrides allow (explicit deny always wins)
- Least privilege: grant minimum access needed
- Roles define groups; permissions apply to roles (not individuals)
- Inheritance flows top-down (orchestrator > researcher > viewer)
- Every access event should be auditable
- Temporary elevation (escalation) needs approver and time limit

## CEX-Specific Extensions
| Field | Justification | Closest equivalent |
|-------|--------------|-------------------|
| scope | What the permission controls | IAM: Resource ARN |
| roles | Who holds this permission | IAM: Principal |
| read/write/execute | Access levels | POSIX: rwx |
| deny_list | Explicit denials | IAM: Deny policy |

## Boundary vs Nearby Types
| Type | What it does | NOT this |
|------|-------------|----------|
| guardrail (P11) | Prevents DAMAGE (safety boundary) | Does NOT control access |
| law (P08) | Defines OPERATIONAL rules (inviolable) | Does NOT grant/deny access |
| feature_flag (P09) | Toggles FEATURES on/off | Does NOT define who can access |
| runtime_rule (P09) | Defines TIMEOUTS and retries | Does NOT define permissions |
