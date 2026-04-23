---
kind: architecture
id: bld_architecture_permission
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of permission — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Permission"
version: "1.0.0"
author: n03_builder
tags: [permission, builder, examples]
tldr: "Golden and anti-examples for permission construction, demonstrating ideal structure and common pitfalls."
domain: "permission construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Architecture: permission in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata header (id, kind, pillar, domain, scope, roles, etc.) | permission-builder | active |
| access_rules | Read/write/execute controls with allow_list and deny_list | author | active |
| role_definitions | Named roles with capabilities and inheritance hierarchy | author | active |
| scope_binding | What resources, artifacts, or paths this permission governs | author | active |
| precedence_rules | Resolution order when allow and deny rules conflict | author | active |
| audit_trail | Logging requirements for access attempts and escalations | author | active |
| escalation_path | Who to contact and what process to follow for access elevation | author | active |
## Dependency Graph
```
agent          --governed_by-->  permission  --enforced_by-->  validator
permission     --consumed_by-->  path_config  --signals-->     access_violation
guardrail      --depends-->      permission
```
| From | To | Type | Data |
|------|----|------|------|
| permission | agent (P02) | dependency | agents must comply with access controls |
| permission | validator (P06) | consumes | validators enforce permission rules at runtime |
| permission | path_config (P09) | data_flow | paths restricted by permission scope |
| guardrail (P11) | permission | dependency | safety guardrails may reference permission rules |
| permission | access_violation (P12) | signals | emitted when unauthorized access is attempted |
| law (P08) | permission | dependency | laws may mandate specific access controls |
## Boundary Table
| permission IS | permission IS NOT |
|---------------|-------------------|
| A read/write/executand access control with roles and scope | A safety boundary on agent behavior (guardrail P11) |
| Enforced via allow_list and deny_list with precedence | An inviolable operational mandate (law P08) |
| Role-based with inheritance hierarchy | A pass/fail quality check (quality_gate P11) |
| Includes audit trail and escalation path | A runtime timeout or retry parameter (runtime_rule P09) |
| Scoped to specific resources, artifacts, or paths | A feature on/off toggle (feature_flag P09) |
| Governs who can access what and how | A naming convention for resources (naming_rule P05) |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | role_definitions, escalation_path | Define who has access and elevation procedures |
| Policy | frontmatter, access_rules, precedence_rules | Specify what access is allowed or denied |
| Scope | scope_binding, path_config | Define which resources are governed |
| Enforcement | validator, access_violation | Check access and report violations |
| Audit | audit_trail | Log access attempts for compliance |
