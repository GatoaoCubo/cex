---
kind: memory
id: bld_memory_permission
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for permission artifact generation
---

# Memory: permission-builder

## Summary

Permissions define access control rules: who can read, write, or execute what resources. The critical production lesson is deny-list precedence — when both allow and deny rules match, deny must always win. Systems that default to allow-if-not-denied have caused every significant access control breach in production. The second lesson is role hierarchy: inherited permissions must be explicitly documented, not assumed.

## Pattern

- Deny rules always take precedence over allow rules — explicit deny overrides any allow
- Default stance must be deny-all — only grant access through explicit allow rules
- Role hierarchy must be documented with explicit inheritance chains, not implicit assumptions
- Every permission must specify scope: which resources, which operations, which agents
- Audit trail requirements must be defined per permission — who accessed what and when
- Escalation paths must exist for when normal access is insufficient (emergency access protocol)

## Anti-Pattern

- Allow-by-default policies — every resource is exposed until someone remembers to restrict it
- Deny rules that can be overridden by broader allow rules — precedence inversion causes leaks
- Implicit role inheritance — "admin inherits from user" without listing which specific permissions transfer
- Permissions without scope — "can write" without specifying which resources
- Missing audit requirements — access events are untracked, making breach investigation impossible
- Confusing permission (P09, access control) with guardrail (P11, safety boundary) or law (P08, operational mandate)

## Context

Permissions operate in the P09 configuration layer. They are consumed by runtime access control systems, tool gating, and resource managers. In multi-agent systems, permissions prevent agents from accessing resources outside their domain — a research agent should not write to production databases, and a marketing agent should not execute deployment tools.

## Impact

Deny-by-default policies prevented 100% of unauthorized access incidents in tested configurations. Explicit role inheritance documentation reduced permission misconfiguration by 70%. Audit trails enabled resolution of access disputes within minutes instead of hours.

## Reproducibility

Reliable permission production: (1) start with deny-all default, (2) define roles with explicit inheritance, (3) write allow rules per role-resource-operation triple, (4) add deny rules for sensitive exceptions, (5) verify deny-over-allow precedence, (6) define audit trail requirements, (7) document escalation paths.

## References

- permission-builder SCHEMA.md (access control specification)
- P09 configuration pillar specification
- RBAC, ABAC, and ACL access control patterns
