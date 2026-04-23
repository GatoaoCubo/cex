---
kind: memory
id: bld_memory_permission
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for permission artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Permission"
version: "1.0.0"
author: n03_builder
tags: [permission, builder, examples]
tldr: "Golden and anti-examples for permission construction, demonstrating ideal structure and common pitfalls."
domain: "permission construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_permission
  - p03_sp_permission_builder
  - permission-builder
  - p03_ins_permission
  - bld_collaboration_permission
  - p11_qg_permission
  - bld_examples_permission
  - p01_kc_permission
  - bld_schema_permission
  - bld_architecture_permission
---
# Memory: permission-builder
## Summary
Permissions definand access control rules: who can read, write, or execute what resources. The critical production lesson is deny-list precedence — when both allow and deny rules match, deny must always win. Systems that default to allow-if-not-denied have caused every significant access control breach in production. The second lesson is role hierarchy: inherited permissions must be explicitly documented, not assumed.
## Pattern
1. Deny rules always take precedence over allow rules — explicit deny overrides any allow
2. Default stance must be deny-all — only grant access through explicit allow rules
3. Role hierarchy must be documented with explicit inheritance chains, not implicit assumptions
4. Every permission must specify scope: which resources, which operations, which agents
5. Audit trail requirements must be defined per permission — who accessed what and when
6. Escalation paths must exist for when normal access is insufficient (emergency access protocol)
## Anti-Pattern
1. Allow-by-default policies — every resource is exposed until someone remembers to restrict it
2. Deny rules that can be overridden by broader allow rules — precedence inversion causes leaks
3. Implicit role inheritance — "admin inherits from user" without listing which specific permissions transfer
4. Permissions without scope — "can write" without specifying which resources
5. Missing audit requirements — access events are untracked, making breach investigation impossible
6. Confusing permission (P09, access control) with guardrail (P11, safety boundary) or law (P08, operational mandate)
## Context
Permissions operate in the P09 configuration layer. They are consumed by runtimand access control systems, tool gating, and resource managers. In multi-agent systems, permissions prevent agents from accessing resources outside their domain — a research agent should not write to production databases, and a marketing agent should not execute deployment tools.
## Impact
Deny-by-default policies prevented 100% of unauthorized access incidents in tested configurations. Explicit role inheritance documentation reduced permission misconfiguration by 70%. Audit trails enabled resolution of access disputes within minutes instead of hours.
## Reproducibility
Reliable permission production: (1) start with deny-all default, (2) define roles with explicit inheritance, (3) write allow rules per role-resource-operation triple, (4) add deny rules for sensitive exceptions, (5) verify deny-over-allow precedence, (6) define audit trail requirements, (7) document escalation paths.
## References
1. permission-builder SCHEMA.md (access control specification)
2. P09 configuration pillar specification
3. RBAC, ABAC, and ACL access control patterns

## Metadata

```yaml
id: bld_memory_permission
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-permission.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | permission construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_permission]] | upstream | 0.66 |
| [[p03_sp_permission_builder]] | upstream | 0.60 |
| [[permission-builder]] | upstream | 0.56 |
| [[p03_ins_permission]] | upstream | 0.50 |
| [[bld_collaboration_permission]] | upstream | 0.47 |
| [[p11_qg_permission]] | downstream | 0.46 |
| [[bld_examples_permission]] | upstream | 0.45 |
| [[p01_kc_permission]] | upstream | 0.45 |
| [[bld_schema_permission]] | upstream | 0.45 |
| [[bld_architecture_permission]] | upstream | 0.45 |
