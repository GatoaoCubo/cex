---
kind: memory
id: p10_mem_rbac_policy_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for rbac_policy construction
quality: 8.7
title: "Memory Rbac Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [rbac_policy, builder, memory]
tldr: "Learned patterns and pitfalls for rbac_policy construction"
domain: "rbac_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_rbac_policy
  - kc_rbac_policy
  - bld_knowledge_card_rbac_policy
  - p03_sp_rbac_policy_builder
  - rbac-policy-builder
  - p09_qg_rbac_policy
  - p10_lr_sandbox_config_builder
  - p03_ins_permission
  - bld_examples_rbac_policy
  - p03_sp_permission_builder
---

## Observation
Misaligned role hierarchies often cause unintended access overlaps, while overly broad resource scopes break tenant isolation. Policies frequently omit explicit tenant identifiers, leading to cross-tenant data exposure.

## Pattern
Granular role definitions paired with tenant-specific resource constraints ensure isolation. Hierarchical roles with inherited permissions reduce redundancy while maintaining clarity.

## Evidence
Reviewed policies using "tenant-abc-admin" roles with restricted resource paths demonstrated effective isolation. Overlapping roles in another artifact caused unauthorized access across tenants.

## Recommendations
- Enforce tenant-specific role names and resource scopes.
- Avoid wildcard resource patterns; use explicit path matching.
- Validate role inheritance to prevent accidental privilege escalation.
- Include tenant ID attributes in policy conditions for dynamic isolation.
- Audit policies for unused roles and redundant permissions quarterly.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_rbac_policy]] | upstream | 0.55 |
| [[kc_rbac_policy]] | upstream | 0.55 |
| [[bld_knowledge_card_rbac_policy]] | upstream | 0.54 |
| [[p03_sp_rbac_policy_builder]] | upstream | 0.53 |
| [[rbac-policy-builder]] | upstream | 0.52 |
| [[p09_qg_rbac_policy]] | downstream | 0.48 |
| [[p10_lr_sandbox_config_builder]] | related | 0.29 |
| [[p03_ins_permission]] | upstream | 0.27 |
| [[bld_examples_rbac_policy]] | upstream | 0.27 |
| [[p03_sp_permission_builder]] | upstream | 0.25 |
